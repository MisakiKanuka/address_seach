import requests

responce = requests.get(url="http://hachimantai.spartacamp.jp/")

print(responce)

# 八幡平市大更の情報をrequestaモジュールを使って取得してね
responce = requests.get(url="http://zipcloud.ibsnet.co.jp/api/search?zipcode=0287111")

# 演習２
responce = requests.get(url="http://zipcloud.ibsnet.co.jp/api/search?zipcode=0200757")

print(responce.text)
{
    "message": null,
    "results": [
        {
            "address1": "岩手県",
            "address2": "八幡平市",
            "address3": "大更",
            "kana1": "ｲﾜﾃｹﾝ",
            "kana2": "ﾊﾁﾏﾝﾀｲｼ",
            "kana3": "ｵｵﾌﾞｹ",
            "prefcode": "3",
            "zipcode": "0287111"
        }
    ],
    "status": 200
}
