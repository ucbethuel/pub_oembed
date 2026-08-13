


from pub_oembed.social_media.linkedin import LinkedInOEmbed
from pub_oembed.social_media.x_twitter import XTwitterOEmbed


x_twitter = "https://x.com/ucbethuel/status/1998024020726329831"
x = "https://x.com/ucbethuel/status/1998024020726329831?s=20"
another = "https://twitter.com/ucbethuel/status/1998024020726329831"

x_twitter_oembed = XTwitterOEmbed(x)

linked = "https://www.linkedin.com/posts/ucbethuel_my-achievement-share-7483483328365584385-tt67/"

lin = LinkedInOEmbed(linked, run_fetch=True)

# print(x_twitter_oembed.fetch_data())

print(lin.json_data, lin.get_data_dict)

# another_oembed = XTwitterOEmbed()

# print(x_twitter_oembed.fetch_data(x_twitter))