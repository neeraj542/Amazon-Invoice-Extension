from flask import Flask, request, send_file
import io
import pandas as pd
import PyPDF2
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Function to extract data from PDF
def extract_data_from_pdf(pdf_bytes):
    reader = PyPDF2.PdfReader(io.BytesIO(pdf_bytes))
    num_pages = len(reader.pages)
    data = []

    for page_num in range(num_pages):
        text = reader.pages[page_num].extract_text()
        data.append(text)

    return data


# Function to create CSV
def create_csv(data):
    df = pd.DataFrame(data, columns=["Text"])
    csv_buffer = io.StringIO()
    df.to_csv(csv_buffer, index=False)
    csv_buffer.seek(0)
    return csv_buffer

@app.route('/')
def index():
    return 'Welcome to the PDF to CSV Converter!'

@app.route('/favicon.ico')
def favicon():
    return '', 404

@app.route('/process_pdf', methods=['POST', 'OPTIONS'])
def process_pdf():
    if request.method == 'OPTIONS':
        return '', 200  # Response to preflight request

    if 'file' not in request.files:
        return 'No file part', 400  # Error if no file is provided

    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400  # Error if no file is selected

    if file and file.filename.endswith('.pdf'):
        pdf_bytes = file.read()
        data = extract_data_from_pdf(pdf_bytes)
        csv_buffer = create_csv(data)

        # Send the CSV file as an attachment
        response = send_file(
            io.BytesIO(csv_buffer.getvalue().encode()),
            mimetype='text/csv'
        )
        response.headers['Content-Disposition'] = 'attachment; filename=invoice_data.csv'

        return response
    else:
        return 'Invalid file format', 400  # Error if the file format is not PDF


if __name__ == '__main__':
    app.run(port=5000)
