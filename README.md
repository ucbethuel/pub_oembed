# pub_oembed

A small Python package for fetching social media oEmbed payloads from supported platforms. It currently includes a reusable `SocialOEmbed` base class and an X/Twitter-specific implementation.

## Features

- Fetch oEmbed JSON from supported social platforms
- Standardized result mapping for X/Twitter, TikTok, and YouTube
- Simple HTTP wrapper using `requests`
- Example usage included in `src/pub_oembed/explore.py`

## Requirements

- Python 3.11+
- `requests`

## Installation

```bash
pip install requests
```

Then install or use the package directly from the repository path.

## Usage

```python
from pub_oembed.social_media.x_twitter import XTwitterOEmbed

tweet_url = "https://x.com/ucbethuel/status/1998024020726329831"
oembed = XTwitterOEmbed(tweet_url)
data = oembed.fetch_data()
print(data)
```

## Supported Platforms

- `x_twitter` (X / Twitter)
- `tiktok`
- `youtube`

> Note: `linkedin` is listed in supported platform names, but LinkedIn oEmbed support is not currently implemented in the package code.

## Package Layout

- `src/pub_oembed/__init__.py`
- `src/pub_oembed/main.py`
- `src/pub_oembed/explore.py`
- `src/pub_oembed/social_media/social_oembed.py`
- `src/pub_oembed/social_media/x_twitter.py`
- `src/pub_oembed/social_media/resolver.py`

## How It Works

The base class `SocialOEmbed`:
- stores `url` and response data
- makes a request to the platform endpoint with `format=json`
- maps returned JSON into a consistent data dictionary
- supports different field mappings depending on the platform type

The `XTwitterOEmbed` class inherits from `SocialOEmbed` and uses the X embed endpoint:
- `https://publish.x.com/oembed`

## Example

```python
from pub_oembed.social_media.x_twitter import XTwitterOEmbed

tweet_url = "https://x.com/ucbethuel/status/1998024020726329831"
x_twitter_oembed = XTwitterOEmbed(tweet_url)
print(x_twitter_oembed.fetch_data())
```

## Notes

- The current implementation is primarily demonstrated for X/Twitter.
- TikTok and YouTube payloads are mapped in the base class, but only X/Twitter has a dedicated subclass.
- Any platform-specific extension should inherit `SocialOEmbed` and define `PLATFORM_NAME` + `OEMBED_ENDPOINT`.
