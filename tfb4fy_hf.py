import tkinter as tk
from tkinter import scrolledtext
from llama_cpp import Llama

# Load the LLM model from a GGUF file
MODEL_PATH = "./Llama-3.2-1B-Instruct-Q5_K_M.gguf"  # Replace with the actual path
llm = Llama(model_path=MODEL_PATH)

def analyze_country():
    country = country_entry.get()
    prompt = (f"Provide a detailed economic and sociological analysis of {country}. "
              f"Include information about GDP, employment rates, inflation, key industries, "
              f"income inequality, education levels, and social welfare. Additionally, discuss "
              f"the country's demographic trends and any major socio-economic challenges.")
    response = llm(prompt, max_tokens=150)  # Increase max_tokens for longer response
    result_text.config(state=tk.NORMAL)
    result_text.delete('1.0', tk.END)
    result_text.insert(tk.INSERT, response['choices'][0]['text'])
    result_text.config(state=tk.DISABLED)

# GUI Setup
root = tk.Tk()
root.title("Country Analysis App")
root.geometry("800x650")

tk.Label(root, text="Enter Country Name:").pack()

country_entry = tk.Entry(root)
country_entry.pack()

analyze_button = tk.Button(root, text="Analyze", command=analyze_country)
analyze_button.pack()

result_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=15, width=50)
result_text.pack()
result_text.config(state=tk.DISABLED, height=400, width=750)

root.mainloop()
