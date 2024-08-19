document.getElementById('uploadForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const formData = new FormData();
    const fileInput = document.getElementById('photoInput');
    if (fileInput.files.length === 0) {
        alert('Please select a file to upload.');
        return;
    }
    formData.append('photo', fileInput.files[0]);
    
    try {
        const response = await fetch('/upload', {
            method: 'POST',
            body: formData
        });
        const result = await response.text();
        prediction = result
        
        window.location.href = '/predict';
        // console.log(prediction)
        // document.getElementById('message').innerText = result;
    } catch (error) {
        console.error('Error uploading file:', error);
        document.getElementById('message').innerText = 'Error uploading file.';
    }
});