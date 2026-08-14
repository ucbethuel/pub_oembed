from pub_oembed.social_media.social_oembed import SocialOEmbed, platform_embed_endpoints

class TikTokOEmbed(SocialOEmbed):
    """A class to handle oEmbed for TikTok URLs."""
    
    PLATFORM_NAME = "tiktok"
    OEMBED_ENDPOINT = platform_embed_endpoints[PLATFORM_NAME]
    
    def __init__(self, url = None, run_fetch = False):
        """Initialize the TikTokOEmbed instance"""
        super().__init__(url, run_fetch)