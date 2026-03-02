from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)

USERNAME = "Reaper3441"
PASSWORD = "password"

def load_news():
    path = os.path.join("data", "news.json")
    with open(path, encoding="utf-8") as f:
        return json.load(f)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == USERNAME and password == PASSWORD:
            return redirect(url_for("news"))

    return render_template("login.html")

@app.route("/news")
def news():
    news_list = load_news()
    return render_template("index.html", news_list=news_list)

@app.route("/news/<int:news_id>")
def news_detail(news_id):
    news_list = load_news()

    news_list = sorted(news_list, key=lambda x: x["id"])

    current_index = None
    for index, item in enumerate(news_list):
        if item["id"] == news_id:
            current_index = index
            break

    if current_index is None:
        return "Новость не найдена"

    item = news_list[current_index]

    prev_news = news_list[current_index - 1] if current_index > 0 else None
    next_news = news_list[current_index + 1] if current_index < len(news_list) - 1 else None

    return render_template(
        "news_detail.html",
        item=item,
        prev_news=prev_news,
        next_news=next_news
    )
if __name__ == "__main__":
    app.run(debug=True)
