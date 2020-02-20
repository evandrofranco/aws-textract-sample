import os
import boto3


def textract_file_to_s3():
    # Document
    profile = os.getenv("AWS_PROFILE")
    s3BucketName = os.getenv("S3_BUCKET")
    documentName = os.getenv("DOCUMENT_SAMPLE")

    # Amazon Textract client
    session = boto3.Session(profile_name=profile)
    textract = session.client('textract')

    # Call Amazon Textract
    response = textract.detect_document_text(
        Document={
            'S3Object': {
                'Bucket': s3BucketName,
                'Name': documentName
            }
        }
    )

    # Print detected text
    output = ""
    for item in response["Blocks"]:
        if item["BlockType"] == "LINE":
            output += item["Text"] + '\n'

    # S3 Client + Write Textract response to S3
    s3 = boto3.client('s3')
    s3.put_object(
        Body=output,
        Bucket=s3BucketName,
        Key='output/result_' + documentName.split(".", 1)[0]
    )


if __name__ == "__main__":
    textract_file_to_s3()
