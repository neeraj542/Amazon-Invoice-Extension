# Amazon Invoice Processor Extension

## Extension Setup

1. Navigate to `chrome://extensions/` in Chrome.
2. Enable "Developer mode".
3. Click "Load unpacked" and select the `extension` directory.

## Backend Setup

1. Navigate to the `backend` directory.
2. Create a virtual environment:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install required packages:

    ```sh
    pip install -r requirements.txt
    ```

4. Run the Flask server:

    ```sh
    flask run
    ```

## Usage

1. Click the extension icon in Chrome.
2. Select a PDF file and click "Process PDF".
3. The processed CSV file will be downloaded automatically.
