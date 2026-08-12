from typing import Literal

import requests

OEmbedKey = Literal[
    "url",
    "author_name",
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
    A class to handle oEmbed for X (formerly Twitter) URLs.
    """

    PLATFORM_NAME = ""
    OEMBED_ENDPOINT = ""

    def __init__(self, url: str = None, run_fetch: bool = False):
        """
        Initialize the SocialOEmbed instance.
        """
        self._data = {}
        self._json_data = {}
        
        self._url = self.format_url(url) if url else None
        
        if run_fetch and url:
            self.fetch_data()
    
    
    # Get Object Properties
    def get_url(self) -> str:
        return self._url
    def get_json_data(self) -> dict:
        return self._json_data
    def get_data_dict(self) -> dict:
        return self._data


    # Methods
    def fetch_data(self) -> dict:
        """
        Get the oEmbed JSON for the tweet URL.

        Returns:
            dict: The oEmbed JSON response.
        """
        url = self.get_url()
        
        try:
            response = requests.get(
                self.OEMBED_ENDPOINT, timeout=20, params={"url": url, "format": "json"}
            )
            self.json_data = response.json()
            return self.json_data
        except requests.RequestException as e:
            print(f"Error fetching oEmbed for {url}: {e}")
            return None

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

        if json_data is None or not json_data:
            raise ValueError("No data fetched. Please call fetch_data(url) first.")
        platform_name = self.PLATFORM_NAME if self.PLATFORM_NAME else "unknown"

        url = self.get_url()
        
        if platform_name == "x_twitter":
            self._data = {
                "url": url,
                "author_name": json_data.get("author_name"),
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
        elif platform_name == "tiktok":
            self._data = {
                "url": url,
                "author_name": json_data.get("author_name"),
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
        #             {
        #   "version": "1.0",
        #   "type": "video",
        #   "title": "Tag those who have this habit 😅😅 |W/ @Watchluxury.nig💎🇳🇬  @vina 🥰✨ ✨  @LUCY ❤️_SOM | #butseriouslywhosleepswiththeirmouthsopen #fyp #relatable #goviral #gozmoclee ",
        #   "author_url": "https://www.tiktok.com/@gozmoc.lee",
        #   "author_name": "gozmoc_lee",
        #   "width": "100%",
        #   "height": "100%",
        #   "html": "<blockquote class=\"tiktok-embed\" cite=\"https://www.tiktok.com/@gozmoc.lee/video/7670623762080861448\" data-video-id=\"7670623762080861448\" data-embed-from=\"oembed\" style=\"max-width:605px; min-width:325px;\"> <section> <a target=\"_blank\" title=\"@gozmoc.lee\" href=\"https://www.tiktok.com/@gozmoc.lee?refer=embed\">@gozmoc.lee</a> <p>Tag those who have this habit 😅😅 |W/ @Watchluxury.nig💎🇳🇬  @vina 🥰✨ ✨  @LUCY ❤️_SOM | <a title=\"butseriouslywhosleepswiththeirmouthsopen\" target=\"_blank\" href=\"https://www.tiktok.com/tag/butseriouslywhosleepswiththeirmouthsopen?refer=embed\">#butseriouslywhosleepswiththeirmouthsopen</a> <a title=\"fyp\" target=\"_blank\" href=\"https://www.tiktok.com/tag/fyp?refer=embed\">#fyp</a> <a title=\"relatable\" target=\"_blank\" href=\"https://www.tiktok.com/tag/relatable?refer=embed\">#relatable</a> <a title=\"goviral\" target=\"_blank\" href=\"https://www.tiktok.com/tag/goviral?refer=embed\">#goviral</a> <a title=\"gozmoclee\" target=\"_blank\" href=\"https://www.tiktok.com/tag/gozmoclee?refer=embed\">#gozmoclee</a> </p> <a target=\"_blank\" title=\"♬ original sound - gozmoc_lee\" href=\"https://www.tiktok.com/music/original-sound-7670623812765666069?refer=embed\">♬ original sound - gozmoc_lee</a> </section> </blockquote> <script async src=\"https://www.tiktok.com/embed.js\"></script>",
        #   "thumbnail_width": 576,
        #   "thumbnail_height": 1024,
        #   "thumbnail_url": "https://p16-common-sign.tiktokcdn.com/tos-alisg-p-0037/okLUkPe8hA9fDj4mAIFG5hoDWfxBW7wEDICVzI~tplv-tiktokx-origin.image?dr=14575&x-expires=1786636800&x-signature=w97VUQSdo3AEw7l0sfxboCCDIJI%3D&t=4d5b0474&ps=13740610&shp=81f88b70&shcp=43f4a2f9&idc=my2",
        #   "provider_url": "https://www.tiktok.com",
        #   "provider_name": "TikTok",
        #   "author_unique_id": "gozmoc.lee",
        #   "embed_product_id": "7670623762080861448",
        #   "embed_type": "video"
        # }
        elif platform_name == "youtube":
            self._data = {
                "url": url,
                "author_name": json_data.get("author_name"),
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
        #                 {
        #   "title": "Why VDM will be the first to be evicted in the Big brother house 🤣🤣Kennyblaq",
        #   "author_name": "Shortcut Comedian",
        #   "author_url": "https://www.youtube.com/@shortcutcomedian4942",
        #   "type": "video",
        #   "height": 113,
        #   "width": 200,
        #   "version": "1.0",
        #   "provider_name": "YouTube",
        #   "provider_url": "https://www.youtube.com/",
        #   "thumbnail_height": 360,
        #   "thumbnail_width": 480,
        #   "thumbnail_url": "https://i.ytimg.com/vi/wRTBDDUraH0/hqdefault.jpg",
        #   "html": "<iframe width="200" height="113" src="https://www.youtube.com/embed/wRTBDDUraH0?feature=oembed" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen title="Why VDM will be the first to be evicted in the Big brother house 🤣🤣Kennyblaq"></iframe>"
        # }

        # Will work on Linkedin later, as it requires a different approach to fetch oEmbed data.
        # elif platform_name == "linkedin":

        else:
            raise ValueError(f"Unsupported platform: {platform_name}")

        return self._data

    

    def format_url(self, url: str) -> str:
        """
        Format the URL to ensure it is in the correct format for oEmbed.

        Parameters:
            url (str): The original URL.
        """
        
        formatted_url = url.split("?")[0]
        
        
        return formatted_url



