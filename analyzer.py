"""
analyzer.py
Ollama connection + generation logic for the AI Email Analyzer.
"""

import requests
import hashlib
import time

OLLAMA_URL = "http://localhost:11434"
REQUEST_TIMEOUT = 60
MAX_BODY_CHARS = 8000


def check_ollama():
    try:
        response = requests.get(f"{OLLAMA_URL}/api/tags", timeout=3)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False


def get_models():
    try:
        response = requests.get(f"{OLLAMA_URL}/api/tags", timeout=5)
        response.raise_for_status()
        models = response.json().get("models", [])
        names = [m["name"] for m in models]
        return names if names else ["llama3.2:1b"]
    except (requests.exceptions.RequestException, KeyError, ValueError):
        return ["llama3.2:1b"]


def truncate(text, limit=MAX_BODY_CHARS):
    if len(text) <= limit:
        return text
    return text[:limit] + "\n\n...[truncated for length]..."


def generate_response(prompt, model, retries=2):
    payload = {"model": model, "prompt": prompt, "stream": False}
    last_err = None

    for attempt in range(retries + 1):
        try:
            response = requests.post(
                f"{OLLAMA_URL}/api/generate", json=payload, timeout=REQUEST_TIMEOUT
            )
            response.raise_for_status()
            return response.json().get("response", "").strip()
        except requests.exceptions.Timeout:
            last_err = "⏱️ The model took too long to respond."
        except requests.exceptions.ConnectionError:
            last_err = "🔴 Could not connect to Ollama. Is `ollama serve` running?"
        except requests.exceptions.RequestException as e:
            last_err = f"⚠️ Request error: {e}"
        except ValueError:
            last_err = "⚠️ Received an invalid response from Ollama."
        time.sleep(0.6 * (attempt + 1))

    return f"[Error] {last_err}"


_cache = {}


def cached_generate(prompt, model):
    key = hashlib.sha256(f"{model}::{prompt}".encode("utf-8")).hexdigest()
    if key in _cache:
        return _cache[key]
    result = generate_response(prompt, model)
    if not result.startswith("[Error]"):
        _cache[key] = result
    return result