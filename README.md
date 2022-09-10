# SRV-MGMT

To install the requirements run `python -m pip install -r requirements.txt`

To add emails to AWS SES

1. Create a csv file with column name `Emails`.
```csv
Emails
asd@gmail.com
asd1@gmail.com
asd2@gmail.com
...
```
2. Run `python add_emails_to_ses.py --csv_file_path <PATH-TO-CSV-FILE>`.
