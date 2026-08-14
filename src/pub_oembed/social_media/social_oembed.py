from typing import Literal
import requests
from urllib.parse import urlparse




OEmbedKey = Literal[
    "url",
    # "author_name",
    "author_url",
    "html",
    "width",
    "height",
    "type",
    "cache_age",
    "provider_name",
    "provider_url",
    "version",
]

platform_embed_endpoints = {
    "x_twitter": "https://publish.x.com/oembed",
    "tiktok": "https://www.tiktok.com/oembed",
    "youtube": "https://www.youtube.com/oembed",
    # "linkedin": "https://www.linkedin.com/oembed?", 
}


class SocialOEmbed:
    """
    A parent class to handle oEmbed.
    """

    PLATFORM_NAME = ""
    OEMBED_ENDPOINT = ""

    def __init__(self, url: str = None, run_fetch: bool = False):
        """
        Initialize the SocialOEmbed instance.
        """
        self._data = None
        self._json_data = None
        
        self._url = self.format_url(url) if url else None
        
        if run_fetch and url:
            self.fetch_data()
    
    
    # Get & Set Object Properties
    def get_url(self) -> str:
        return self._url
    def get_json_data(self) -> dict:
        return self._json_data
    def get_data_dict(self) -> dict:
        return self._data


    def set_data_dict(self, data: str) -> dict:
        self._data = data        
    def set_json_data(self, json_data: dict) -> dict:
        self._json_data = json_data


    # Methods
    def fetch_data(self) -> dict:
        """
        Get the oEmbed JSON for the URL.
        """
        url = self.get_url()

        if not url:
            raise ValueError("No URL provided.")

        try:
            if self._json_data:
                return self._json_data

            print(
                f"\n\nFetching oEmbed data for {url} "
                f"from {self.OEMBED_ENDPOINT}..."
            )

            response = requests.get(
                self.OEMBED_ENDPOINT,
                timeout=20,
                params={
                    "url": url,
                    "format": "json",
                },
            )

            response.raise_for_status()

            json_data = response.json()

            
            self.set_json_data(json_data)

            return json_data

        except requests.RequestException as e:
            print(f"Error fetching oEmbed for {url}: {e}")
            return 


    def get_data(self, key: OEmbedKey) -> dict:
        """
        Get the stored oEmbed data.

        Parameters:
        key: one of "url", "author_name", "author_url",
             "html", "width", "height", "type", ...

        Returns:
            dict: The stored oEmbed data.
        """
        data = self.get_data_dict()
        if data is None or not data:
            raise ValueError("No data fetched. Please call fetch_data(url) first.")

        return data.get(key, None)

    def data_map(self) -> dict:
        """
        Get the stored oEmbed data from quried json into structured format in self.data.

        Just for data key consistency and to avoid key errors when accessing data.

        Returns:
            dict: The stored oEmbed data.
        """
        json_data = self.get_json_data()
        data_dict = self.get_data_dict()
        if not data_dict:
            mapped_data = {
                key: json_data.get(key) for key in json_data.keys()
            }
            self.set_data_dict(mapped_data)
            return "success"
        else:
            self.set_data_dict(data_dict)
            return "already exist"
        

    def format_url(self, url: str) -> str:
        """
        Format the URL to ensure it is in the correct format for oEmbed.

        Parameters:
            url (str): The original URL.
        """
        try:
            if self.is_url(url):   
                formatted_url = url.split("?")[0]
                return formatted_url
        except ValueError:
            return False
        
    def is_url(self, url):
        try:
            result = urlparse(url)
            return result.scheme in ("http", "https") and bool(result.netloc)
        except ValueError:
            return False    
        
        # return formatted_url



