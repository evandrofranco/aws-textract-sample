# AWS Textract
Exemplo de Uso do Textract da AWS

## Pré-Requisitos
Criar Role na AWS com permissões:

    AmazonS3ReadOnlyAccess
    AmazonTextractFullAccess

Declarar as variáveis de ambiente abaixo:

        export AWS_PROFILE=<seu-profile-local>
        export S3_BUCKET=<seu-bucket-s3>
        export DOCUMENT_SAMPLE=<nome-da-imagem-que-sera-lida>

## Execução
Após declarar as variáveis de ambiente, executar o script:

    python textract.py

**Obs.: Neste exemplo, o conteúdo será exibido no output.**

## Excecução com Output no S3

Para gerar o output em um arquivo do S3, a permissão do S3 precisa ser alterada (Ex: AmazonS3FullAccess)

Após isto, executar:

    python textract_to_s3.py