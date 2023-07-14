var videoElement;
var intervalId;
var model;
var objectDetails;

// Load the Teachable Machine model
async function loadModel() {
    const URL = 'https://teachablemachine.withgoogle.com/models/cWCSdmY45'; // Replace with your model URL
    model = await tmImage.load(URL + '/model.json', URL + '/metadata.json');
}

// Load the object details
async function loadObjectDetails() {
    // Assuming the object details are stored in object-details.json
    const response = await fetch('object-details.json');
    objectDetails = await response.json();
}

// Classify objects in real-time
async function classifyObjects() {
    const resultElement = document.getElementById('classificationResult');
    const resultDetails = document.getElementById('classificationDetails');
    const prediction = await model.predict(videoElement);

    const topPrediction1 = prediction[0];
    const topPrediction2 = prediction[1];
    const topPrediction3 = prediction[2];

    nothing = topPrediction1.className
    nothingProb = topPrediction1.probability.toFixed(2) * 100

    human = topPrediction2.className
    humanProb = topPrediction2.probability.toFixed(2) * 100

    atomicHabits = topPrediction3.className
    atomicHabitsProb = topPrediction3.probability.toFixed(2) * 100

    // Display the top prediction result
    resultElement.innerText = `${nothing} - ${nothingProb}%\n
        ${human} - ${humanProb}%\n
        ${atomicHabits} - ${atomicHabitsProb}%`;

        

    classDetails = '';

    if (nothingProb > humanProb && nothingProb > atomicHabitsProb) classDetails = 'nothing'
    else if (humanProb > nothingProb && humanProb > atomicHabitsProb) classDetails = 'human'
    else classDetails = 'atomic habits'

    data = objectDetails[classDetails]

    if (classDetails == 'nothing'){
        resultDetails.innerHTML = `
                <h3>Details</h3>
                <p>Message: ${data['message']}</p>
            `;
    }
    else if (classDetails == 'human') {
        resultDetails.innerHTML = `
                <h3>Details</h3>
                <p>Scientific name: ${data['Scientific name']}</p>
                <p>Height: ${data['Height']}</p>
                <p>Eats: ${data['Eats']}</p>
                <p>Order: ${data['Order']}</p>
                <p>Family: ${data['Family']}</p>
                <p>Kingdom: ${data['Kingdom']}</p>
                <p>Details: ${data['Details']}</p>
            `;
    }
    else if (classDetails === 'atomic habits') {
        resultDetails.innerHTML = `
                <h3>Details</h3>
                <p>Title: ${data['title']}</p>
                <p>Author: ${data['author']}</p>
                <p>Publisher: ${data['publisher']}</p>
                <p>PublicationYear: ${data['publicationYear']}</p>
                <p>Summary: ${data['summary']}</p>
            `;
    }
}

// Start classifier process
async function startClassifier() {
    console.log("start --->")
    videoElement = document.getElementById('videoElement');

    // Check if webcam access is supported by the browser
    if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
        // Access the webcam
        navigator.mediaDevices.getUserMedia({ video: true })
            .then(function (stream) {
                // Set the video element source
                videoElement = document.getElementById('videoElement');
                videoElement.srcObject = stream;
            })
            .catch(function (error) {
                console.error('Error accessing the webcam:', error);
            });
    } else {
        console.error('Webcam access is not supported by this browser.');
    }

    await loadModel();
    await loadObjectDetails();
    intervalId = setInterval(classifyObjects, 1000);
}

// Stop classifier process
function stopClassifier() {
    console.log("stop <---")
    clearInterval(intervalId);
    videoElement.pause();
}