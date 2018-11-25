import requests


class AddressSearcher:

    def __init__(self):
        self.base_url = "http://zipcloud.ibsnet.co.jp/api/search"

    def search(self, postal_code):
        url = f"{self.base_url}?zipcode={postal_code}"

        responce = requests.get(url)

        responce_dict = responce.json()

        if responce_dict["results"] is None:
            return "該当するデータは見つかりませんでした。検索キーワードを変えて再検索してください。"

        都道府県 = responce_dict["results"][0]["address1"]
        市区町村 = responce_dict["results"][0]["address2"]
        町域 = responce_dict["results"][0]["address3"]

        return f"{都道府県}{市区町村}{町域}"
