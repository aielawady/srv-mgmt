import csv
import boto3
from botocore.exceptions import ClientError
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("--col_name", type=str, required=False, default="Email")
parser.add_argument("--csv_file_path", type=str, required=True)

args = parser.parse_args()

emails_col_name = args.col_name
csv_file_path = args.csv_file_path

with open(csv_file_path) as f:
    reader = csv.reader(f)
    header = next(reader)
    col = header.index(emails_col_name)
    emails = [x[col].lower() for x in reader]

client = boto3.client("ses")

added_emails = client.list_identities()["Identities"]

not_added_emails = list(set(emails) - set(added_emails))
for email in not_added_emails:
    try:
        response = client.verify_email_identity(EmailAddress=email)
    # Display an error if something goes wrong.
    except ClientError as e:
        print(e.response["Error"]["Message"])
    # Otherwise, show the request ID of the verification message.
    else:
        print(
            "Verification email sent to "
            + email
            + ". Request ID: "
            + response["ResponseMetadata"]["RequestId"]
        )
