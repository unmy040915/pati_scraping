import requests
from bs4 import BeautifulSoup
import os

MINREPO_URL = "https://min-repo.com/1691982/?kishu=%E3%83%95%E3%82%A1%E3%83%B3%E3%82%AD%E3%83%BC%E3%82%B8%E3%83%A3%E3%82%B0%E3%83%A9%E3%83%BC%EF%BC%92%EF%BC%AB%EF%BC%B4"

response = requests.get(MINREPO_URL)
web_content = response.text
soup = BeautifulSoup(web_content, "html.parser")

# "table_wrap"クラスを持つ要素をすべて取得
object_items = soup.find_all(class_="table_wrap")

directory_name = "items"
if not os.path.exists(directory_name):
    os.makedirs(directory_name)  # ディレクトリが存在しない場合に作成する

# 取得した要素をファイルに保存する
for index, item in enumerate(object_items, start=1):
    filename = os.path.join(directory_name, f"item_{index}.html")
    with open(filename, "w", encoding="utf-8") as file:
        file.write(str(item))

    print(f"保存しました: {filename}")

print("スクレイピングが完了しました。")
