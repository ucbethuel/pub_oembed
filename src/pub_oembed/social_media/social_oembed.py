from typing import Literal

import requests

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
        
        if json_data is None or not json_data:
            raise ValueError("No data fetched. Please call fetch_data(url) first.")
        platform_name = self.PLATFORM_NAME if self.PLATFORM_NAME else "unknown"

        url = self.get_url()
        
        if platform_name == "x_twitter":
            data_dict = {
                "url": url,
                # "author_name": json_data.get("author_name"),
                "author_url": json_data.get("author_url"),
                "html": json_data.get("html"),
                "width": json_data.get("width"),
                "height": json_data.get("height"),
                "type": json_data.get("type"),
                "cache_age": json_data.get("cache_age"),
                "provider_name": json_data.get("provider_name"),
                "provider_url": json_data.get("provider_url"),
                "version": json_data.get("version"),
            }
            self.set_data_dict(data_dict)
            return data_dict
        elif platform_name == "tiktok":
            data_dict = {
                "url": url,
                # "author_name": json_data.get("author_name"),
                "author_url": json_data.get("author_url"),
                "html": json_data.get("html"),
                "width": json_data.get("width"),
                "height": json_data.get("height"),
                "type": json_data.get("type") or json_data.get("embed_type"),
                # "cache_age": json_data.get("cache_age"),
                "provider_name": json_data.get("provider_name"),
                "provider_url": json_data.get("provider_url"),
                "version": json_data.get("version"),
            }
            self.set_data_dict(data_dict)
            return data_dict
        
        elif platform_name == "youtube":
            data_dict = {
                "url": url,
                # "author_name": json_data.get("author_name"),
                "author_url": json_data.get("author_url"),
                "html": json_data.get("html"),
                "width": json_data.get("width"),
                "height": json_data.get("height"),
                "type": json_data.get("type"),
                # "cache_age": json_data.get("cache_age"),
                "provider_name": json_data.get("provider_name"),
                "provider_url": json_data.get("provider_url"),
                # "version": json_data.get("version"),
            }
            self.set_data_dict(data_dict)
            return data_dict
        #
        elif platform_name == "linkedin":
            data_dict = {
                "url": url,
                # "author_name": json_data.get("author_name"),
                "author_url": json_data.get("author_url"),
                "html": json_data.get("html"),
                "width": json_data.get("width"),
                "height": json_data.get("height"),
                "type": json_data.get("type"),
                # "cache_age": json_data.get("cache_age"),
                "provider_name": json_data.get("provider_name"),
                "provider_url": json_data.get("provider_url"),
                # "version": json_data.get("version"),
            }
            self.set_data_dict(data_dict)
            return data_dict
        # Will work on Linkedin later, as it requires a different approach to fetch oEmbed data.
        # elif platform_name == "linkedin":

        else:
            raise ValueError(f"Unsupported platform: {platform_name}")

    

    def format_url(self, url: str) -> str:
        """
        Format the URL to ensure it is in the correct format for oEmbed.

        Parameters:
            url (str): The original URL.
        """
        
        formatted_url = url.split("?")[0]
        
        
        return formatted_url



