from pub_oembed.social_media.social_oembed import SocialOEmbed, platform_embed_endpoints
# Token url
# X - GET https://publish.x.com/oembed?url=<TWEET_URL>


class XTwitterOEmbed(SocialOEmbed):
    """
    A class to handle oEmbed for X (formerly Twitter) URLs.
    """
    PLATFORM_NAME = "x_twitter"
    OEMBED_ENDPOINT = platform_embed_endpoints[PLATFORM_NAME]

    def __init__(self, url: str = None, run_fetch: bool = False):
        """
        Initialize the XTwitterOEmbed instance.
        """
        super().__init__(url, run_fetch)

