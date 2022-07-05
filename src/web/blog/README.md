# Web/Blog

## 概要

デザインが壊滅的な作りかけのブログアプリケーション

## 問題を解くにあたって

- `app/flag.txt` を直接開いてフラグを取得する必要はないです

## ビルド

このファイル [README.md](README.md) が存在するディレクトリで以下のコマンドを実行して問題サーバをビルドする (dockerが必要)

```bash
$ docker image build -t myctf-problems/web/blog:latest .
```

## 起動

このファイル [README.md](README.md) が存在するディレクトリで以下のコマンドを実行して問題サーバを起動する (dockerが必要)

```bash
$ docker container run -p 5000:5000 --name myctf-problems/web/blog -it myctf-problems/web/blog:latest
```

http://localhost:5000/ から問題サーバにアクセスできる

## 想定解法

[solveディレクトリ](solve) を参照

