import unittest


class AddressSearcher:
    def search(self, postal_code):
        return "岩手県八幡平市大更"


class TestAddressSearcher(unittest.TestCase):
    def test_岩手県八幡平市大更の地名を郵便番号から取得できる(self):
        address_searcher = AddressSearcher()

        actual = address_searcher.search(postal_code="02807111")

        self.assertEqual("岩手県八幡平市大更", actual)


if __name__ == "__main__":
    unittest.main()