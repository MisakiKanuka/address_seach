import requests


class AddressSearcher:
    def search(self, postal_code):
        url = f"http://zipcloud.ibsnet.co.jp/api/search?zipcode={postal_code}"

        responce = requests.get(url)

        responce_dict = responce.json()

        都道府県 = responce_dict["results"][0]["address1"]
        市区町村 = responce_dict["results"][0]["address2"]
        町域 = responce_dict["results"][0]["address3"]

        return f"{都道府県}{市区町村}{町域}"
