document.getElementById("send-btn").addEventListener("click", function() {
  const userInput = document.getElementById("user-input").value;

  if (userInput.trim() === "") {
      return;
  }

  const userMessage = document.createElement("div");
  userMessage.classList.add("user");
  userMessage.innerHTML = userInput;
  document.getElementById("chat-box").appendChild(userMessage);


  document.getElementById("user-input").value = "";

  document.getElementById("chat-box").scrollTop = document.getElementById("chat-box").scrollHeight;

  fetch("/ask", {
      method: "POST",
      headers: {
          "Content-Type": "application/json",
      },
      body: JSON.stringify({ message: userInput }),
  })
  .then(response => response.json())
  .then(data => {
      const botMessage = document.createElement("div");
      botMessage.classList.add("bot");
      botMessage.innerHTML = data.response;
      document.getElementById("chat-box").appendChild(botMessage);

      document.getElementById("chat-box").scrollTop = document.getElementById("chat-box").scrollHeight;
  })
  .catch(error => {
      console.error("Error:", error);
  });
});
