function generateAnswer() {
    const question = document.getElementById("question").value;
    const answerBox = document.getElementById("answer");

    if (question.trim() === "") {
        answerBox.innerText = "Please enter a question";
        return;
    }

    // Placeholder response (later replaced by Django API)
    answerBox.innerText = "Processing your question...";

    setTimeout(() => {
        answerBox.innerText = "This is where the chatbot answer will appear.";
    }, 600);
}