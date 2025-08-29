const textInput = document.getElementById('textInput');
const analyzeBtn = document.getElementById('analyzeBtn');
const clearBtn = document.getElementById('clearBtn');
const loading = document.getElementById('loading');
const result = document.getElementById('result');
const resultText = document.getElementById('resultText');
const resultDetails = document.getElementById('resultDetails');
const examples = document.querySelectorAll('.example');


//clear button 
clearBtn.addEventListener('click', ()=>{
    textInput.value = '';
    result.style.display = 'none';
    textInput.focus();
})

//analyze button
analyzeBtn.addEventListener('click', analyzeText);


//analyze text function
async function analyzeText() {
    const text = textInput.value.trim().replace(/\s+/g, ' ');

    //loading display
    loading.style.display = 'block';
    result.style.display = 'none';
    analyzeBtn.disabled = true;

    //try{ //post request to server
        const response = await fetch('/analyze',{
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({text: text})
        });

        const data = await response.json(); //response from model
        console.log(data);
       

        displayResult(data); //display results
    
         loading.style.display = 'none';
         analyzeBtn.disabled = false;
}

function displayResult(data) { //displaying results
    const classification = data.classification;
    const explanation = data.explanation.replaceAll("Explanation:", "");
    let resultType, icon, display;

    if (classification == "Label: Safe "){
        resultType = "Safe";
        icon = "✅";
        display = "Safe - No phishing detected";
    }
    else if (classification == "Label: Phishing "){
        resultType = "Phishing";
        icon = "❌";
        display = "Not Safe - Phishing message detected";
    }
    else{
        resultType = "error";
        displayError(data.error);
    }

    // Update UI
        result.className = `result ${resultType}`;
        result.style.display = 'block';
            
        resultText.innerHTML = `${icon} <strong>${display}</strong>`;
        resultDetails.innerHTML = `
            <strong>Explanation:</strong>${explanation} <br>
            `;
            
}

function displayError(message) {
        result.className = 'result danger';
        result.style.display = 'block';
        resultText.innerHTML = `❌ <strong>Error:</strong> ${message}`;
        resultDetails.innerHTML = 'Please try again or check if the AI service is running.';
    }

    // auto-resize textarea
textInput.addEventListener('input', function() {
    this.style.height = 'auto';
    this.style.height = Math.min(this.scrollHeight, 300) + 'px';
});

// focus on load
window.addEventListener('load', () => {
        textInput.focus();
    });
