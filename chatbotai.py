
import requests

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL_NAME = "llama3.2:latest"

SYSTEM_PROMPT = """
You are CS Mentor AI, a Computer Science Engineering tutor.
Teach C, Python, Java, JavaScript, DSA, Operating Systems,
DBMS, Computer Networks, Software Engineering, Cryptography,
Cloud Computing, AI, and Web Development.

Explain concepts clearly with examples. Support exam preparation
for 2-mark, 5-mark, and 10-mark questions. Help with programming,
debugging, algorithms, and interview preparation.
Adapt your explanation to the student's level.
"""

def ask_mentor(message, mode="Learn Concept", history=None):
    if not isinstance(history, list):
        history = []

    messages = [{"role": "system", "content": SYSTEM_PROMPT}]

    for item in history[-10:]:
        if (
            isinstance(item, dict)
            and item.get("role") in ("user", "assistant")
            and isinstance(item.get("content"), str)
        ):
            messages.append({
                "role": item["role"],
                "content": item["content"]
            })

    messages.append({
        "role": "user",
        "content": f"Learning mode: {mode}\n\nQuestion: {message}"
    })

    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL_NAME,
                "messages": messages,
                "stream": False
            },
            timeout=180
        )
        response.raise_for_status()
        data = response.json()
        return data["message"]["content"]

    except requests.RequestException as error:
        return (
            "Could not connect to Ollama. Make sure Ollama is running "
            f"and the model {MODEL_NAME} is installed. Details: {error}"
        )
    except (ValueError, KeyError, TypeError):
        return "Ollama returned an unexpected response. Please try again."
