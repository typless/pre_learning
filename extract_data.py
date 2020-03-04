import os
import time

import requests

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_NAME = 'circleci1.pdf'
file_path = os.path.join(BASE_DIR, 'examples', 'files', FILE_NAME)

with open(file_path, 'rb') as invoice_file:
    files = {
        "file": (FILE_NAME, invoice_file.read(),),
    }


request_data = {
    "document_type_name": 'pre-learning-example',
    "customer": 'me'
}
start = time.time()
response = requests.post(
    f'https://developers.typless.com/api/document-types/extract-data/',
    files=files,
    data=request_data,
    headers={'Authorization': f'Token {os.getenv("API_KEY")}'}
)
fields = response.json()['extracted_fields']
supplier = [field for field in fields if field['name'] == 'supplier'][0]['values'][0]['value']
invoice_number = [field for field in fields if field['name'] == 'invoice_number'][0]['values'][0]['value']
issue_date = [field for field in fields if field['name'] == 'issue_date'][0]['values'][0]['value']
total_amount = [field for field in fields if field['name'] == 'total_amount'][0]['values'][0]['value']

data = f'Extracted data - supplier: {supplier}, invoice_number: {invoice_number}, issue_date: {issue_date}, total_amount: {total_amount}'

print(data)
