from address_seacher import AddressSearcher


def main():
    # ユーザーからの郵便番号を受け取る
    # 郵便番号を入力してください：
    # 郵便番号はpostal_code

    postal_code = input("郵便番号を入力してください:")

    # 郵便番号を使って地名を取ってくる
    address_searcher = AddressSearcher()

    location = address_searcher.search(postal_code)

    # 地名をprintする
    # "岩手県八幡平市大更"が出力される
    print(location)


if __name__ == "__main__":
    main()
