

// Function to send user message
function sendMessage() {
    let userInput = document.getElementById("user-input").value;
    if (userInput === "") return;

    // Display user message in chat box
    const chatBox = document.getElementById("chat-box");
    chatBox.innerHTML += `
        <div class="chat-message user-message">
            <img src="../static/images/user_logo.png" alt="User" class="user-logo">
            <span>${userInput}</span>
        </div>
    `;

    // Send user input to server (Python) and get the response
    fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: userInput })
    })
    .then(response => response.json())
    .then(data => {
        // Display bot response in chat box
        chatBox.innerHTML += `
            <div class="chat-message bot-message">
                <img src="../static/images/bot_logo.png" alt="Bot" class="bot-logo">
                <span>${data.reply}</span>
            </div>
        `;
        chatBox.scrollTop = chatBox.scrollHeight; // Scroll to bottom
    });

    document.getElementById("user-input").value = ""; // Clear input
}




