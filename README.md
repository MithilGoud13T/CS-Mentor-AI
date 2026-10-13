# CS Mentor AI 🤖

**Your Personal Computer Science Engineering Study Partner**

CS Mentor AI is a locally running AI-powered chatbot designed to help students understand Computer Science concepts, practice programming, and learn technical subjects through interactive conversations.

The application uses **Python, Flask, HTML, CSS, JavaScript, Ollama, and Llama 3.2** to provide a web-based chat interface connected to a local language model.

## ✨ Features

- 💬 **Interactive AI Chat** — Ask questions about Computer Science and receive AI-generated explanations.
- 🧠 **Computer Science Learning** — Learn programming, DBMS, Operating Systems, Computer Networks, DSA, and more.
- 🎯 **Learning Modes** — Select a learning mode from the web interface.
- 🖥️ **Local AI Inference** — Run the Llama 3.2 model locally through Ollama.
- 🌐 **Web-Based Interface** — Chat through a browser using HTML, CSS, and JavaScript.
- 🔒 **Local Model Processing** — Prompts are sent to your local Ollama service rather than a hosted AI API. This does not guarantee that every part of the application is offline or that no data is transmitted elsewhere.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Flask | Web server and API |
| HTML5 | Web page structure |
| CSS3 | User interface styling |
| JavaScript | Chat interactions and API requests |
| Ollama | Local AI model runtime |
| Llama 3.2 | Language model |
| Git and GitHub | Version control and source code hosting |

## 📁 Project Structure

```text
CS-Mentor-AI/
├── app.py                 # Flask application and API routes
├── chatbotai.py           # Ollama communication and AI responses
├── static/
│   ├── css/
│   │   └── style.css      # Interface styling
│   └── js/
│       └── app.js         # Chat functionality
├── templates/
│   └── index.html         # Chat interface
├── .gitignore             # Files excluded from Git
└── README.md              # Project documentation
```

## ⚙️ Prerequisites

Install the following before running the application:

1. **Python 3.10 or newer**
2. **Git**
3. **Ollama**
4. **Llama 3.2 model**

Download:
- Python: https://www.python.org/downloads/
- Git: https://git-scm.com/downloads
- Ollama: https://ollama.com/

## 🚀 Installation and Setup

### 1. Clone the repository

Open a terminal and run:

```bash
git clone https://github.com/MithilGoud13T/CS-Mentor-AI.git
cd CS-Mentor-AI
```

### 2. Create a virtual environment

On Windows:

```bash
python -m venv .venv
```

Activate it in Command Prompt:

```cmd
.venv\Scripts\activate
```

If you use PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install Python dependencies

Install Flask and Requests:

```bash
python -m pip install Flask requests
```

If a `requirements.txt` file is added to the project later, you can install dependencies with:

```bash
python -m pip install -r requirements.txt
```

### 4. Download the Llama 3.2 model

Make sure Ollama is installed and running. In your terminal, execute:

```bash
ollama pull llama3.2
```

Verify that the model is available:

```bash
ollama list
```

### 5. Start the application

From the project directory, run:

```bash
python app.py
```

Wait until Flask reports that the development server is running.

### 6. Open the chatbot

Open your browser and visit:

**http://127.0.0.1:5000**

You can now start asking Computer Science questions.

## 💡 Example Questions

Try asking:

- Explain Java in simple words.
- What is the OSI model?
- Explain normalization in DBMS with examples.
- What is a process in an Operating System?
- Explain arrays and linked lists.
- What are cryptographic hash functions?
- Give me Python programming practice problems.

## 🔧 Troubleshooting

### The chatbot does not respond

- Make sure the Flask application is running.
- Make sure Ollama is installed and running.
- Verify that the model exists using `ollama list`.
- Check the terminal for errors.
- Confirm that the model name and Ollama API endpoint in the application match your local setup.

### The model is not found

Run:

```bash
ollama pull llama3.2
```

### Flask or Requests is missing

Activate your virtual environment and run:

```bash
python -m pip install Flask requests
```

## 🔐 Privacy and Security

- Do not commit passwords, API keys, `.env` files, or other secrets.
- Keep `.venv/` and `__pycache__/` out of Git.
- The application uses a local Ollama model, but privacy also depends on the application's implementation and any other services it contacts.
- Flask's built-in development server is intended for development, not production deployment.

## 🗺️ Future Improvements

Potential enhancements include:

- Add more learning modes and customizable explanations.
- Improve chat history and conversation management.
- Add code examples and programming exercises.
- Add a requirements file and automated tests.
- Improve error handling and loading indicators.
- Deploy a hosted version with appropriate security controls.

## 👨‍💻 Author

**Mithil Goud**

GitHub: [@MithilGoud13T](https://github.com/MithilGoud13T)

## 📄 License

No license has been specified yet. If you want others to reuse, modify, or distribute this project, consider adding an appropriate open-source license.

---

*Built to make learning Computer Science more interactive and accessible.*
