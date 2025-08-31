import webview
import threading
import os

def run_agent():
    os.system("python my_agent.py")

if __name__ == "__main__":
    threading.Thread(target=run_agent).start()
    webview.create_window("Miniature-Agent", "http://127.0.0.1:7860")
    webview.start()
