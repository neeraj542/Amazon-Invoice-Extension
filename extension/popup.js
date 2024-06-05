document.getElementById('processBtn').addEventListener('click', function() {
    const fileInput = document.getElementById('fileInput');
    if (fileInput.files.length === 0) {
        alert('Please select a PDF file to process.');
        return;
    }

    const file = fileInput.files[0];
    const reader = new FileReader();

    reader.onload = function(e) {
        const arrayBuffer = e.target.result;

        // Send the file to the background script for processing
        chrome.runtime.sendMessage({ action: 'processPDF', file: arrayBuffer }, function(response) {
            document.getElementById('output').textContent = response.message;
        });
    };

    reader.readAsArrayBuffer(file);
});
