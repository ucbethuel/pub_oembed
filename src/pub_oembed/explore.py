


from pub_oembed.social_media.linkedin import LinkedInOEmbed
from pub_oembed.social_media.tiktok import TikTokOEmbed
from pub_oembed.social_media.x_twitter import XTwitterOEmbed


x_twitter = "https://x.com/ucbethuel/status/1998024020726329831"
x = "https://x.com/ucbethuel/status/1998024020726329831?s=20"
another = "https://twitter.com/ucbethuel/status/1998024020726329831"
tik = "https://www.tiktok.com/@techroastshow/video/7671301322448047374?"
x_twitter_oembed = XTwitterOEmbed(x)

linked = "https://www.linkedin.com/posts/ucbethuel_my-achievement-share-7483483328365584385-tt67/"

lin = LinkedInOEmbed(linked, run_fetch=True)
tiko = TikTokOEmbed(tik)
print(tiko.fetch_data())
print(tiko.get_json_data())
print(tiko.get_data_dict(), "Data Dict:-----")
print(tiko.data_map(), "After mapping\n\n")
print(tiko.get_data_dict(), "Data Dict:-----")

# another_oembed = XTwitterOEmbed()

# print(x_twitter_oembed.fetch_data(x_twitter))