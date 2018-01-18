import requests

API_URL = "https://api.coinhive.com"


class PyHiveClient(object):
    def __init__(self, secret_key):

        self._headers = {
            "User-Agent": "PyHive (https://github.com/WeebWare/PyHive)",
            "Content-Type": "application/json"
        }

        if len(secret_key) != 32:
            raise ValueError("Secret key must be 32 characters long")

        self.secret_key = secret_key

    def get(self, path, params={}):
        """
        A base method for requesting the API

        :param str path: The route you want to access
        :param dict params: The URL params you want to pass to CoinHive
        """
        params.update(secret=self.secret_key)
        return requests.get(PyHiveClient.build_url(path), params=params).json()

    def post(self, path, data={}):
        """
        A base method for POSTing to the API

        :param str path: The route you want to access
        :param dict data: The data you want to post to CoinHive
        """
        data.update(secret=self.secret_key)
        return requests.post(PyHiveClient.build_url(path), data=data).json()

    @staticmethod
    def build_url(route):
        """
        Build the URL from the base url provided for coinhive's API.

        :param str route: The route of the API you want to access
        :param dict params: The URL params that you want to pass to CoinHive
        """
        return API_URL + route


if __name__ == "__main__":
    pass
