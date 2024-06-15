import webbrowser
import random
import time

def search():
    queries = [
        "Python programming",
        "OpenAI GPT-4",
        "Machine Learning",
        "Random Search Query",
    ]

    for query in queries:
        webbrowser.open(f"https://www.google.com/search?q={query}")
        time.sleep(120)  

    print("All searches completed.")
