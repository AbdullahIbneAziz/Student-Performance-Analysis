document.addEventListener('DOMContentLoaded', function() {
    // Handle form submission
    const form = document.getElementById('predictionForm');
    form.addEventListener('submit', function(e) {
        e.preventDefault();
        
        // Show loading state
        const submitButton = form.querySelector('button[type="submit"]');
        const originalText = submitButton.textContent;
        submitButton.textContent = 'Predicting...';
        submitButton.disabled = true;

        // Get form data
        const formData = new FormData(form);
        
        // Send prediction request
        fetch('/predict', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                // Display prediction result
                const resultDiv = document.getElementById('result');
                const predictionText = document.getElementById('predictionText');
                
                // Format the prediction result
                const status = data.status;
                let statusClass = 'alert-info';
                
                // Set appropriate alert class based on status
                switch(status) {
                    case 'Dropout':
                        statusClass = 'alert-danger';
                        break;
                    case 'Graduate':
                    case 'Graduated':
                        statusClass = 'alert-success';
                        break;
                    case 'Enrolled':
                        statusClass = 'alert-warning';
                        break;
                }
                
                // Update the result display
                predictionText.textContent = `Predicted Status: ${status}`;
                resultDiv.querySelector('.alert').className = `alert ${statusClass}`;
                resultDiv.style.display = 'block';
            } else {
                throw new Error(data.error || 'Prediction failed');
            }
        })
        .catch(error => {
            alert('Error: ' + error.message);
        })
        .finally(() => {
            // Reset button state
            submitButton.textContent = originalText;
            submitButton.disabled = false;
        });
    });
}); 