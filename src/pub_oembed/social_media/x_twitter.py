from typing import Literal

import requests

from pub_oembed.social_media.helper_class import SocialOEmbed
# Token url
# X - GET https://publish.x.com/oembed?url=<TWEET_URL>

"""
{
  "url": "https://x.com/ucbethuel/status/1998024020726329831",
  "author_name": "Uchenna Bethel Orji",
  "author_url": "https://x.com/ucbethuel",
  "html": "<blockquote class=\"twitter-tweet\"><p lang=\"en\" dir=\"ltr\">So glad to be selected as <a href=\"https://x.com/cowrywise?ref_src=twsrc%5Etfw\">@cowrywise</a> ambassador, looking forward for an amazing growth with them especially financially, 😊.<a href=\"https://x.com/hashtag/cowrywise?src=hash&amp;ref_src=twsrc%5Etfw\">#cowrywise</a> <a href=\"https://x.com/hashtag/graduate?src=hash&amp;ref_src=twsrc%5Etfw\">#graduate</a> <a href=\"https://x.com/hashtag/Ambassadorprogram?src=hash&amp;ref_src=twsrc%5Etfw\">#Ambassadorprogram</a> <a href=\"https://x.com/hashtag/ucbethuel?src=hash&amp;ref_src=twsrc%5Etfw\">#ucbethuel</a></p>&mdash; Uchenna Bethel Orji (@ucbethuel) <a href=\"https://x.com/ucbethuel/status/1998024020726329831?ref_src=twsrc%5Etfw\">December 8, 2025</a></blockquote>\n<script async src=\"https://platform.x.com/widgets.js\" charset=\"utf-8\"></script>\n\n",
  "width": 550,
  "height": null,
  "type": "rich",
  "cache_age": "3153600000",
  "provider_name": "X",
  "provider_url": "https://x.com",
  "version": "1.0"
}
"""



class XTwitterOEmbed(SocialOEmbed):
    """
    A class to handle oEmbed for X (formerly Twitter) URLs.
    """
    PLATFORM_NAME = "x_twitter"
    OEMBED_ENDPOINT = "https://publish.x.com/oembed?"

    def __init__(self, url: str = None, run_fetch: bool = False):
        """
        Initialize the XTwitterOEmbed instance.
        """
        super().__init__(url, run_fetch)

