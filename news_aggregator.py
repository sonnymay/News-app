import os
from tkinter import ttk
import requests
from dotenv import load_dotenv
import tkinter as tk
import webbrowser

load_dotenv()

API_KEY = os.getenv("NEWS_API_KEY")
API_URL = "https://newsapi.org/v2/everything"

def get_news(keyword):
    params = {
        "q": keyword,
        "apiKey": API_KEY,
        "pageSize": 10,
        "language": "en",
        "sortBy": "publishedAt",
    }

    response = requests.get(API_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        return data["articles"]
    else:
        print("Error fetching news data.")
        return None

def open_url(event, url):
    webbrowser.open(url)

def display_news(articles):
    results_text.config(state='normal')
    results_text.delete(1.0, tk.END)
    
    for article in articles:
        title = article["title"]
        source = article["source"]["name"]
        published_at = article["publishedAt"][:10]
        url = article["url"]

        results_text.insert(tk.END, f"{title}\n", "title")
        results_text.insert(tk.END, f"Source: {source}\nPublished At: {published_at}\n", "info")
        results_text.insert(tk.END, f"{url}\n", "url")
        results_text.tag_bind("url", "<Button-1>", lambda event, url=url: open_url(event, url))
        results_text.insert(tk.END, "\n")

    results_text.config(state='disabled')

def on_search_click():
    keyword = keyword_entry.get()
    articles = get_news(keyword)
    if articles:
        display_news(articles)

root = tk.Tk()
root.title("News Aggregator")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

keyword_label = ttk.Label(frame, text="Enter a keyword to search for news articles:")
keyword_label.grid(row=0, column=0, sticky=tk.W)

keyword_entry = ttk.Entry(frame, width=40)
keyword_entry.grid(row=1, column=0, sticky=(tk.W, tk.E))

search_button = ttk.Button(frame, text="Search", command=on_search_click)
search_button.grid(row=1, column=1, sticky=tk.W)

results_text = tk.Text(root, wrap=tk.WORD, width=100, height=20)
results_text.tag_configure("title", font=("TkDefaultFont", 12, "bold"))
results_text.tag_configure("info", font=("TkDefaultFont", 10))
results_text.tag_configure("url", font=("TkDefaultFont", 10, "underline"), foreground="blue")
results_text.config(state='disabled')
results_text.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

root.mainloop()