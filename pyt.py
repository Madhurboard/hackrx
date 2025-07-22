from pyngrok import ngrok
import subprocess

# 1. Open a tunnel on port 8000
public_url = ngrok.connect(8000)
print(f"🌍 Public URL: {public_url}")

# 2. Start your FastAPI app with Uvicorn
subprocess.run(["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"])
