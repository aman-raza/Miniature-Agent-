import os, json, subprocess
from dotenv import load_dotenv
import gradio as gr

# -------------------
# Setup Environments
# -------------------
load_dotenv()
USE_OPENAI = bool(os.getenv("OPENAI_API_KEY"))

conversation = []

# -------------------
# Model Configuration
# -------------------
if USE_OPENAI:
    import openai
    openai.api_key = os.getenv("OPENAI_API_KEY")

    def query_llm(messages):
        resp = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        return resp.choices[0].message.content

else:
    from transformers import AutoTokenizer, pipeline
    import torch

    model_name = "codellama/CodeLlama-7b-hf"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    generator = pipeline(
        "text-generation",
        model=model_name,
        tokenizer=tokenizer,
        torch_dtype=torch.float16,
        device_map="auto",
    )

    def query_llm(messages):
        prompt = "\n".join([f"{m['role']}: {m['content']}" for m in messages])
        result = generator(prompt, max_new_tokens=200, do_sample=False)
        return result[0]["generated_text"]

# -------------------
# Tools
# -------------------
def read_file(path):
    try:
        with open(path, 'r') as f: return f.read()
    except Exception as e: return str(e)

def write_file(path, content):
    try:
        with open(path, 'w') as f: f.write(content)
        return f"File {path} updated."
    except Exception as e: return str(e)

def run_command(cmd):
    try:
        res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return res.stdout or res.stderr
    except Exception as e: return str(e)

TOOLS = {"read_file": read_file, "write_file": write_file, "run_cmd": run_command}

def process_tool_request(output):
    try:
        obj = json.loads(output)
    except:
        return None
    tool = obj.get("tool"); arg = obj.get("input", "")
    if tool in TOOLS:
        return TOOLS[tool](arg)
    return None

# -------------------
# Chat Logic
# -------------------
def agent_reply(user_msg, history):
    global conversation
    history = history or []
    conversation.append({"role": "user", "content": user_msg})

    response = query_llm(conversation)

    tool_output = process_tool_request(response)
    if tool_output:
        conversation.append({"role": "tool", "content": tool_output})
        response = query_llm(conversation)

    conversation.append({"role": "assistant", "content": response})
    history.append((user_msg, response))
    return history

# -------------------
# Web UI using gradio
# -------------------
with gr.Blocks() as demo:
    gr.Markdown("# 🤖 Miniature Agent")
    gr.Markdown("Ask me to write, explain, or run code. Type `exit` to stop.")
    chatbot = gr.Chatbot()
    msg = gr.Textbox(label="Your message")
    clear = gr.Button("Clear Chat")

    def user_submit(user_msg, chat_history):
        return "", agent_reply(user_msg, chat_history)

    msg.submit(user_submit, [msg, chatbot], [msg, chatbot])
    clear.click(lambda: None, None, chatbot, queue=False)

demo.launch()
