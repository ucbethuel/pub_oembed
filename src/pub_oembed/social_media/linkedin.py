import re
from typing import Optional

from pub_oembed.social_media.social_oembed import SocialOEmbed, logger


class LinkedInOEmbed(SocialOEmbed):
    """
    A class to handle oEmbed for LinkedIn URLs.
    """

    PLATFORM_NAME = "linkedin"
    # OEMBED_ENDPOINT = f"https://www.linkedin.com/embed/feed/update/urn:li:{post_type}:{post_id}?collapsed=1" #"https://www.linkedin.com/embed/feed/update/urn:li:share:{share_id}?format=oembed"

    def __init__(self, url: str = None, run_fetch: bool = False):
        """
        Initialize the LinkedInOEmbed instance.
        """
        super().__init__(url, run_fetch)

    # Custom Methods to build and generate linked in OEmbed URL and HTML snippet
    def get_linkedin_embed_url(self) -> Optional[str]:
        """Extract the LinkedIn embed src URL from a post link."""
        # Matches "...-share-1234567890123456789-..." style slugs
        url = self.get_url()

        match = re.search(r"-(activity|share|ugcPost)-(\d+)-", url)
        if not match:
            # Fallback: direct urn:li:type:id already in the URL
            match = re.search(r"urn:li:(activity|share|ugcPost):(\d+)", url)
        if not match:
            return None

        post_type, post_id = match.group(1), match.group(2)
        OEMBED_ENDPOINT = f"https://www.linkedin.com/embed/feed/update/urn:li:{post_type}:{post_id}"
        return OEMBED_ENDPOINT, post_type

    def build_linkedin_embed(
        self, height: int = 627, width: int = 504
    ) -> Optional[str]:
        """Build a full iframe embed snippet from a LinkedIn post URL."""

        src = self.get_linkedin_embed_url()[0]

        if not src:
            return None
        return (
            f'<iframe src="{src}" height="{height}" width="{width}" '
            f'frameborder="0" allowfullscreen title="Embedded post"></iframe>'
        )
    # Overwriting Superclass Method
    def fetch_data(self) -> dict:
        """
        Get the oEmbed JSON for the LinkedIn URL.
        """

        try:
            url = self.get_url()
            json_data = self.get_json_data()
            # print(f"\n\nFetching oEmbed data for {url} from LinkedIn...{json_data}")
            if json_data is None or not json_data:
                json_data = {
                    "url" : self.get_url(),
                    "author_url":  f"https://www.linkedin.com/in/{url.split('posts/')[1].split('_')[0]}/",
                    "html" : self.build_linkedin_embed(),
                    "height": 627,
                    "width": 504,
                    "type": self.get_linkedin_embed_url()[1],
                    "cache_age": "3153600000",
                    "provider": "LinkedIn",
                    "provider_url": "https://linkedin.com",
                }
                # print(json_data)  
                self.set_json_data(json_data)
                return json_data         
        except Exception as e:
            logger.error(f"Error fetching oEmbed for {url}: {e}")
            return 
    



