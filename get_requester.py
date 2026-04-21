import requests

class GetRequester:
    """
    A reusable class for sending GET requests to a remote API
    and retrieving JSON data.
    """

    def __init__(self, url):
        """
        Initialize the requester with the API endpoint URL.
        """
        self.url = url

    def get_response_body(self):
        """
        Send an HTTP GET request to the endpoint
        and return the raw response body.
        """
        response = requests.get(self.url)
        return response.text

    def load_json(self):
        """
        Convert the API response into JSON
        and return Python data structures.
        """
        response = requests.get(self.url)
        return response.json()