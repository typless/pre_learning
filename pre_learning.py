import os
import sqlite3

import requests

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# open connection
conn = sqlite3.connect(os.path.join(BASE_DIR, 'examples', 'examples.db'))
conn.row_factory = sqlite3.Row

cur = conn.cursor()
cur.execute("SELECT * FROM received_invoices")

# get all received invoices
rows = cur.fetchall()

for row in rows:
    with open(os.path.join(BASE_DIR, 'examples', 'files', row['file_path']), 'rb') as invoice_file:
        files = {
            "file": (row['file_path'].split('/')[-1], invoice_file.read(),),
        }
    request_data = {
        "document_type_name": 'pre-learning-example',
        "customer": 'me',
        "learning_fields": [
            {'name': 'supplier', 'value': row['supplier']},
            {'name': 'invoice_number', 'value': row['invoice_number']},
            {'name': 'issue_date', 'value': row['issue_date']},  # convert to YYYY-MM-DD string if your database has datetime type
            {'name': 'total_amount', 'value': '%.2f' % row['total_amount']},
        ]
    }
    if os.getenv('API_KEY') is None:
        raise Exception('YOU MUST SET API KEY!')

    response = requests.post(
        f'https://developers.typless.com/api/document-types/learn/',
        files=files,
        data=request_data,
        headers={'Authorization': f'Token {os.getenv("API_KEY")}'}
    )
    print(response.text)
