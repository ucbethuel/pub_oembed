from pub_oembed.social_media.linkedin import LinkedInOEmbed
from pub_oembed.social_media.social_oembed import SocialOEmbed
from pub_oembed.social_media.tiktok import TikTokOEmbed
from pub_oembed.social_media.youtube import YouTubeOEmbed
from pub_oembed.social_media.x_twitter import XTwitterOEmbed


# test instance of SocialOEmbed
def test_instance():
    social = SocialOEmbed()
    assert isinstance(social, SocialOEmbed)
# -------------------------------


# Inheritance checks
def test_linkedin_inheritance():
    assert issubclass(LinkedInOEmbed, SocialOEmbed)


def test_tiktok_inheritance():
    assert issubclass(TikTokOEmbed, SocialOEmbed)


def test_youtube_inheritance():
    assert issubclass(YouTubeOEmbed, SocialOEmbed)


# --------------------------------------------


