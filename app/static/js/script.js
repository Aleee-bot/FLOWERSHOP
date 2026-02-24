function generateAnswer() {
    console.log("generateAnswer function called");
    const question = document.getElementById("question").value;
    const answerBox = document.getElementById("answer");

    if (question.trim() === "") {
        answerBox.innerText = "Please enter a question.";
        return;
    }

    answerBox.innerText = "Processing your question...";

    fetch("/chat/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            message: question
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log("Server response:", data);
        answerBox.innerText = data.response;
    })
    .catch(error => {
        console.error("Error:", error);
        answerBox.innerText = "Something went wrong!";
    });
}