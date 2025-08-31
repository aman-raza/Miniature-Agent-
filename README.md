# 🤖 Miniature Agent

An **AI-powered coding assistant** that runs locally and helps you **write, edit, and run code** through a simple **chat interface**.  
Inspired by [ghuntley’s coding agent workshop](https://github.com/ghuntley/how-to-build-a-coding-agent) and enhanced with support for **OpenAI APIs** *or* **free local Hugging Face models** (e.g. [Code Llama](https://huggingface.co/codellama/CodeLlama-7b-hf)).

Built entirely in **Python** with a sleek **Gradio web UI**.

---

## ✨ Features
- 🧑‍💻 **Code Generation & Explanation** – ask the agent to write or explain code.  
- 📂 **File Tools** – read, edit, and update local files.  
- 🖥️ **Command Execution** – run shell commands (e.g. `pytest`).  
- 🔄 **Flexible Models**  
  - Use **OpenAI GPT-3.5/4** if you have an API key.  
  - Or run **CodeLlama locally** for free (no key required).  
- 🌐 **Web Interface** – intuitive chat UI powered by [Gradio](https://gradio.app).  
- ⚡ **One-Click Run** – just `python app.py` and start coding with your AI buddy.  

---

## 📦 Installation

### 1. Clone the repo
```bash
git clone https://github.com/aman-raza/Miniature-Agent-.git
cd Miniature-Agent-
```

## 2. Create a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate   # (Windows: venv\Scripts\activate)
```

## 3. Install Dependencies
```bash
pip install -r requirements.txt
```

## 4. 🔑 Configuration

- Using OpenAI (recommended for accuracy):

  - Create a .env file in the project root:

    ```env 
    OPENAI_API_KEY=sk-xxxx
    ```

  - The agent will automatically use GPT-3.5/4.

- Using Hugging Face local model (free):

  - No .env required.

  - The app will download CodeLlama 7B
   - on first run (~13GB).

  - GPU strongly recommended.

## 5. 🚀 Usage

- Start the app:

  ```bash
  python app.py
  ```

## 6. Gradio will launch at:

  ```bash
  http://127.0.0.1:7860
  ```
  Now you can chat with your coding agent in the browser

## 7. 🛠️ Example Interactions

- Writing Code
  ```python
  User: Write a Python function to check if a number is prime.
  Agent: 
  def is_prime(n):
      if n < 2: return False
      for i in range(2, int(n**0.5)+1):
          if n % i == 0: return False
      return True
  ```

- Running Test
  ```pgsql
  User: Run pytest on the current project.
  Agent: {"tool": "run_cmd", "input": "pytest --maxfail=1"}
  Agent: (shows test results)
  ```

- Editing Files
  ```vbnet
  User: Add a function reverse_string(s) to utils.py
  Agent: ✅ File utils.py updated.
  ```
- Project Structure
  ```bash
  coding-agent/
  │── my_agent.py            # main script (run this)
  │── requirements.txt  # dependencies
  │── .env              # API keys (optional, for OpenAI)
  │── README.md         # this file
  ```
## 8. (Optional) Create a desktop `.exe` app
  - Install pyinstaller and pywebview
    ```
    pip install pywebview
    pip install pyinstaller
    ```
  - Build `.exe`
    ```
    pyinstaller --noconfirm --onefile --windowed main.py
    ```
  - After building, you’ll find the .exe inside dist/main.exe. Double-click -> results in a true desktop app.
----
- ⚠️ Notes

  - Local models require significant RAM/GPU. If limited, prefer OpenAI API.
  - Always review code before executing – the agent can run shell commands.
 
- 📜 License
  - MIT License – feel free to fork, modify, and share.
 
- 🙌 Acknowledgements
  - [Geoffrey Huntley – How to Build a Coding Agent](https://ghuntley.com/agent/)
  - [Hugging Face – Code Llama](https://huggingface.co/codellama/CodeLlama-7b-hf)
  - [Gradio](https://gradio.app)
