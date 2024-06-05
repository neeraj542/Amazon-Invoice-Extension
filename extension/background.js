chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
    if (request.action === 'processPDF') {
        const arrayBuffer = request.file;

        processPDF(arrayBuffer).then(result => {
            sendResponse({ success: true, message: 'PDF processed successfully: ' + result });
        }).catch(error => {
            sendResponse({ success: false, message: 'Error processing PDF: ' + error });
        });

        return true;
    }
});

async function processPDF(arrayBuffer) {
    const formData = new FormData();
    formData.append('file', new Blob([arrayBuffer], { type: 'application/pdf' }));

    const response = await fetch('http://localhost:5000/process_pdf', {
        method: 'POST',
        body: formData,
    });

    if (!response.ok) {
        throw new Error('Network response was not ok');
    }

    const blob = await response.blob();
    const url = URL.createObjectURL(blob);
    chrome.downloads.download({
        url: url,
        filename: 'invoice_data.csv'
    });

    return 'invoice_data.csv';
}
