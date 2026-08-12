


from pub_oembed.social_media.x_twitter import XTwitterOEmbed


x_twitter = "https://x.com/ucbethuel/status/1998024020726329831"
x = "https://x.com/ucbethuel/status/1998024020726329831?s=20"
another = "https://twitter.com/ucbethuel/status/1998024020726329831"

x_twitter_oembed = XTwitterOEmbed(x)

print(x_twitter_oembed.fetch_data())

# another_oembed = XTwitterOEmbed()

# print(x_twitter_oembed.fetch_data(x_twitter))