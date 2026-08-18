from pub_oembed.social_media.social_oembed import SocialOEmbed
from pub_oembed.social_media.x_twitter import XTwitterOEmbed



# Test XTwitter Subclass
def test_x_tiwtter_inheritance():
    assert issubclass(XTwitterOEmbed, SocialOEmbed)

# -------------------------------------------------------

# Test instance of XTwitterOEmbed
def test_instance():
    x_twitter = XTwitterOEmbed()
    assert isinstance(x_twitter, XTwitterOEmbed)

# --------------------------------------------------

# Test methods
def test_json_request(mocker, x_obj,mock_fake_data_return):
    fake_response = mocker.Mock()
    
    fake_response.json.return_value = mock_fake_data_return

    fake_response.raise_for_status.return_value = None

    mocker.patch(
        "requests.get",
        return_value=fake_response,
    )

    data = x_obj.get_json_data()

    assert isinstance(data, dict)

def test_data_mapping(x_obj, mock_request):
    job_status = x_obj.data_map()
    # print(x_obj.get_json_data())
    
    assert job_status == "success"

def test_get_data(x_obj):
    assert x_obj.get_data("url") == "https://x.com/ucbethuel/status/1998024020726329831"
    assert x_obj.get_data("html") == "<blockquote class=\"twitter-tweet\"><p lang=\"en\" dir=\"ltr\">So glad to be selected as <a href=\"https://x.com/cowrywise?ref_src=twsrc%5Etfw\">@cowrywise</a> ambassador, looking forward for an amazing growth with them especially financially, 😊.<a href=\"https://x.com/hashtag/cowrywise?src=hash&amp;ref_src=twsrc%5Etfw\">#cowrywise</a> <a href=\"https://x.com/hashtag/graduate?src=hash&amp;ref_src=twsrc%5Etfw\">#graduate</a> <a href=\"https://x.com/hashtag/Ambassadorprogram?src=hash&amp;ref_src=twsrc%5Etfw\">#Ambassadorprogram</a> <a href=\"https://x.com/hashtag/ucbethuel?src=hash&amp;ref_src=twsrc%5Etfw\">#ucbethuel</a></p>&mdash; Uchenna Bethel Orji (@ucbethuel) <a href=\"https://x.com/ucbethuel/status/1998024020726329831?ref_src=twsrc%5Etfw\">December 8, 2025</a></blockquote>\n<script async src=\"https://platform.x.com/widgets.js\" charset=\"utf-8\"></script>\n\n"
    assert x_obj.get_data("author_url") == "https://x.com/ucbethuel"
    assert x_obj.get_data("width") == 550
    assert x_obj.get_data("height") == 200
    assert x_obj.get_data("version") == "1.0"

def test_url(x_obj):
    assert x_obj.is_url(x_obj.get_url())
    # assert