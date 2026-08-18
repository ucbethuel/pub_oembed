import pytest
from pub_oembed.social_media.x_twitter import XTwitterOEmbed

# X_Twitter Fixtures
# ------------------------------------------------
# Reusable variable

@pytest.fixture
def mock_fake_data_return():
    return {
  "url": "https://x.com/ucbethuel/status/1998024020726329831",
  "author_name": "Fake Author",
  "author_url": "https://x.com/ucbethuel",
  "html": "<blockquote class=\"twitter-tweet\"><p lang=\"en\" dir=\"ltr\">So glad to be selected as <a href=\"https://x.com/cowrywise?ref_src=twsrc%5Etfw\">@cowrywise</a> ambassador, looking forward for an amazing growth with them especially financially, 😊.<a href=\"https://x.com/hashtag/cowrywise?src=hash&amp;ref_src=twsrc%5Etfw\">#cowrywise</a> <a href=\"https://x.com/hashtag/graduate?src=hash&amp;ref_src=twsrc%5Etfw\">#graduate</a> <a href=\"https://x.com/hashtag/Ambassadorprogram?src=hash&amp;ref_src=twsrc%5Etfw\">#Ambassadorprogram</a> <a href=\"https://x.com/hashtag/ucbethuel?src=hash&amp;ref_src=twsrc%5Etfw\">#ucbethuel</a></p>&mdash; Uchenna Bethel Orji (@ucbethuel) <a href=\"https://x.com/ucbethuel/status/1998024020726329831?ref_src=twsrc%5Etfw\">December 8, 2025</a></blockquote>\n<script async src=\"https://platform.x.com/widgets.js\" charset=\"utf-8\"></script>\n\n",
  "width": 550,
  "height": 200,
  "type": "rich",
  "cache_age": "3153600000",
  "provider_name": "X",
  "provider_url": "https://x.com",
  "version": "1.0"
}
    
@pytest.fixture
def mock_request(mocker, mock_fake_data_return):
    fake_response = mocker.Mock()
    
    fake_response.json.return_value = mock_fake_data_return

    fake_response.raise_for_status.return_value = None

    return mocker.patch(
        "requests.get",
        return_value=fake_response,
    )

@pytest.fixture
def x_obj(mock_request):
    x_twitter = "https://x.com/ucbethuel/status/1998024020726329831"
    return XTwitterOEmbed(x_twitter, run_fetch=True)
# -----------------------------------------