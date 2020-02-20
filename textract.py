import os
import boto3


def textract_file():
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
    for item in response["Blocks"]:
        if item["BlockType"] == "LINE":
            print('\033[94m' + item["Text"] + '\033[0m')


if __name__ == "__main__":
    textract_file()
