function generateAnswer() {
    const questionInput = document.getElementById("question");
    const chatBox = document.getElementById("chatBox");

    const question = questionInput.value.trim();
    if (!question) return;
    chatBox.innerHTML += `
        <div class="chat user">
            <strong>You:</strong> ${question}
        </div>
    `;

    questionInput.value = "";

    const thinkingId = `thinking-${Date.now()}`;
    chatBox.innerHTML += `
        <div class="chat bot" id="${thinkingId}">
            <strong>Bot:</strong> Typing...
        </div>
    `;

    chatBox.scrollTop = chatBox.scrollHeight;

    fetch("/chat/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: question })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById(thinkingId).innerHTML = `
            <strong>Bot:</strong> ${data.response}
        `;
        chatBox.scrollTop = chatBox.scrollHeight;
    })
    .catch(() => {
        document.getElementById(thinkingId).innerHTML = `
            <strong>Bot:</strong> Sorry, something went wrong.
        `;
    });
}