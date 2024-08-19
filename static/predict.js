document.getElementById('ageConfirmationForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    // console.log(prediction)
    console.log('work')
    const formData = new FormData(e.target);
    
    try {
        const response = await fetch('/confirm_age', {
            method: 'POST',
            body: formData
        });
        if (response.ok) {
            window.location.href = '/music';
        } else {
            alert('Error submitting age confirmation.');
        }
    } catch (error) {
        console.error('Error submitting age confirmation:', error);
        alert('Error submitting age confirmation.');
    }
});
