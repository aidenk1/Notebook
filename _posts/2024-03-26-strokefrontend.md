---
toc: true
comments: true
layout: post
title: Stroke ML Frontend
description: 
type: hacks
courses: { compsci: {week: 27} }
---
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Stroke Prediction</title>
<style>
body {
  font-family: Arial, sans-serif;
  background-color: #000; /* Black background */
  color: #fff; /* White text color */
}

.container {
  width: 50%;
  margin: 20px auto;
  background-color: #333; /* Dark gray container background */
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
}

h2 {
  text-align: center;
}

form {
  margin-bottom: 20px;
}

label {
  display: block;
  margin-bottom: 5px;
}

input[type="text"],
input[type="number"],
select {
  width: calc(100% - 18px);
  padding: 8px;
  margin-bottom: 10px;
  border: 1px solid #555;
  border-radius: 4px;
  background-color: #444; /* Dark gray input background */
  color: #fff; /* White input text color */
}

select {
  appearance: none;
}

button {
  background-color: #4CAF50; /* Green submit button */
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  width: 100%;
}

button:hover {
  background-color: #45a049; /* Darker green on hover */
}

#result {
  font-size: 18px;
  text-align: center;
  margin-top: 20px;
}
</style>
</head>
<body>

<h2>Stroke Prediction</h2>

<div class="container">
  <form id="predictionForm">
    <label for="age">Age:</label>
    <input type="number" id="age" name="age" required>

    <label for="gender">Gender:</label>
    <select id="gender" name="gender" required>
        <option value="Male">Male</option>
        <option value="Female">Female</option>
    </select>

    <label for="hypertension">Hypertension (0 for No, 1 for Yes):</label>
    <input type="number" id="hypertension" name="hypertension" min="0" max="1" required>

    <label for="heartDisease">Heart Disease (0 for No, 1 for Yes):</label>
    <input type="number" id="heartDisease" name="heartDisease" min="0" max="1" required>

    <label for="everMarried">Ever Married:</label>
    <select id="everMarried" name="everMarried" required>
        <option value="Yes">Yes</option>
        <option value="No">No</option>
    </select>

    <label for="workType">Work Type:</label>
    <select id="workType" name="work_type" required> <!-- Adjusted name to match backend -->
        <option value="Private">Private</option>
        <option value="Self-employed">Self-employed</option>
        <option value="Other">Other</option>
    </select>

    <label for="residenceType">Residence Type:</label>
    <select id="residenceType" name="residenceType" required>
        <option value="Rural">Rural</option>
        <option value="Urban">Urban</option>
    </select>

    <label for="avgGlucoseLevel">Average Glucose Level:</label>
    <input type="number" id="avgGlucoseLevel" name="avgGlucoseLevel" step="0.01" required>

    <label for="bmi">BMI:</label>
    <input type="number" id="bmi" name="bmi" step="0.01" required>

    <button type="submit">Predict Stroke Probability</button>
</form>

  <div id="result"></div>
</div>
<script>
document.getElementById("predictionForm").addEventListener("submit", function(event) {
  event.preventDefault(); // Prevent form submission
  predictStroke(); // Call function to predict stroke probability
});
function predictStroke() {
  // Get input values from the form
  var formData = {
    age: parseInt(document.getElementById("age").value),
    gender: document.getElementById("gender").value,
    hypertension: document.getElementById("hypertension").value === "0" ? 0 : 1, // Adjusted to handle "0" input
    heart_disease: document.getElementById("heartDisease").value === "0" ? 0 : 1, // Adjusted to handle "0" input
    ever_married: document.getElementById("everMarried").value, // Adjusted key
    work_type: document.getElementById("workType").value,
    Residence_type: document.getElementById("residenceType").value, // Adjusted key
    avg_glucose_level: parseFloat(document.getElementById("avgGlucoseLevel").value), // Adjusted key
    bmi: parseFloat(document.getElementById("bmi").value)
  };
  
  const apiUrl = "http://127.0.0.1:8086/api/stroke/predict";

  fetch(apiUrl, {
    method: "POST",
    headers: {
      "Content-Type": "application/json" // Set Content-Type header to application/json
    },
    body: JSON.stringify(formData) // Serialize formData as JSON
  })
  .then(response => response.json())
  .then(data => {
    // Display stroke probability result
    document.getElementById("result").innerHTML = "Stroke Probability: " + (data.stroke_probability * 100).toFixed(2) + "%";
  })
  .catch(error => {
    console.error("Error:", error);
    document.getElementById("result").innerHTML = "An error occurred. Please try again.";
  });
}
</script>
</body>
</html>