import requests

responce = requests.get(url="http://hachimantai.spartacamp.jp/")

print(responce)

# 八幡平市大更の情報をrequestaモジュールを使って取得してね
responce = requests.get(url="http://zipcloud.ibsnet.co.jp/api/search?zipcode=0287111")

# 演習２
responce = requests.get(url="http://zipcloud.ibsnet.co.jp/api/search?zipcode=0200757")
