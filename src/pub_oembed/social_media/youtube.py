from pub_oembed.social_media.social_oembed import SocialOEmbed, platform_embed_endpoints

class YouTubeOEmbed(SocialOEmbed):
    PLATFORM_NAME = "youtube"
    OEMBED_ENDPOINT = platform_embed_endpoints[PLATFORM_NAME]
    
    def __init__(self, url = None, run_fetch = False):
        """ Initialize the YoutubeOEmbed instance"""
        super().__init__(url, run_fetch)
        