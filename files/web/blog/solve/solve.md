# Web/Blog 想定解法解説

まずソースコードを読む

app/app.py

```py:app/app.py
# ~ 略 ~

@app.route("/articles")
def articles_():
    path = request.args.get("title")
    if path:
        article = get_article(path)
        return render_template("article.html", article=article)

# ~ 略 ~

def get_article(path: str) -> dict:
    with open("./articles/"+path, encoding="utf-8") as f:
        body = f.read()
    return {"title": path, "body": body}

# ~ 略 ~

```

`/articles` にて GETにおいてtitleパラメータで指定したファイル名を `./articles/{ファイル名}` としてファイルを読み込んでいる

ディレクトリトラバーサル [Wikipedia](https://ja.wikipedia.org/wiki/ディレクトリトラバーサル) ができそうなのでやってみる

`flag.txt` は articles ディレクトリが存在するディレクトリにあるので `./articles/../flag.txt ` で取れそう

`http://localhost:5000/articles?title=../flag.txt` にアクセスすればフラグが表示される

