import glob
import os

from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)


@app.route("/")
def index_():
    articles = get_articles()
    return render_template("index.html", articles=articles)


@app.route("/articles")
def articles_():
    path = request.args.get("title")
    if path:
        article = get_article(path)
        return render_template("article.html", article=article)
    else:
        return redirect(url_for("index_"))


def get_articles() -> list:
    articles = []
    for article_path in get_article_paths():
        articles.append({"title": article_path, "path": article_path})
    return articles


def get_article_paths() -> dict:
    article_file_paths = [path.split("/")[-1]
                          for path in glob.glob("./articles/*")]
    return article_file_paths


def get_article(path: str) -> dict:
    if os.path.exists(f"./articles/{path}"):
        with open("./articles/"+path, encoding="utf-8") as f:
            body = f.read()
    else:
        body = f"The specified article '{path}' was not found."
        path = "Not Found"
    return {"title": path, "body": body}


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0", debug=True)
