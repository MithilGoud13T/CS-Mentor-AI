const chatForm = document.getElementById("chatForm");
const messageInput = document.getElementById("messageInput");
const messages = document.getElementById("messages");
const modeSelect = document.getElementById("mode");
const sendBtn = document.getElementById("sendBtn");
const clearBtn = document.getElementById("clearBtn");
const statusLabel = document.getElementById("status");

const history = [];

function addMessage(role, text) {
    const bubble = document.createElement("div");
    bubble.className = `message ${role}`;

    const heading = document.createElement("strong");
    heading.textContent = role === "user" ? "You" : "CS Mentor AI";

    const paragraph = document.createElement("p");
    paragraph.textContent = text;

    bubble.append(heading, paragraph);
    messages.appendChild(bubble);
    messages.scrollTop = messages.scrollHeight;
}

async function checkConnection() {
    try {
        const response = await fetch("/api/health");
        if (!response.ok) throw new Error("Backend unavailable");

        statusLabel.textContent = "App connected";
        statusLabel.style.color = "#86efac";
    } catch {
        statusLabel.textContent = "Connection unavailable";
        statusLabel.style.color = "#fca5a5";
    }
}

chatForm.addEventListener("submit", async (event) => {
    event.preventDefault();

    const message = messageInput.value.trim();
    if (!message) return;

    addMessage("user", message);
    messageInput.value = "";
    sendBtn.disabled = true;
    sendBtn.textContent = "Thinking...";

    try {
        const response = await fetch("/api/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                message: message,
                mode: modeSelect.value,
                history: history.slice(-10)
            })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || "The request failed.");
        }

        const answer = data.response || "No response was returned.";
        addMessage("assistant", answer);

        history.push(
            { role: "user", content: message },
            { role: "assistant", content: answer }
        );
    } catch (error) {
        addMessage(
            "assistant",
            `Sorry, something went wrong: ${error.message}`
        );
    } finally {
        sendBtn.disabled = false;
        sendBtn.textContent = "Send";
        messageInput.focus();
    }
});

clearBtn.addEventListener("click", () => {
    history.length = 0;
    messages.replaceChildren();

    addMessage(
        "assistant",
        "Chat cleared! Ask me a new Computer Science question."
    );
});

checkConnection();