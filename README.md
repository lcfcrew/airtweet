# AirTweet

AirTweet analyzes Twitter search results using the Microsoft Cognitive Services
Text Analysis APIs.

**Note:** Before you can use AirTweet, you must add the necessary Twitter API and
Azure subscription details to `airtweet.ini`.

## Requirements

* Python 3.5
* airtweet
* requests

## Use

All you need to do is instantiate the `AirTweet` class and pass a desired query
to its `analyze()` method:

```python
import airtweet
client = airtweet.AirTweet()
client.analyze('#merica', 3)

# {'722851321666265089': {'key_phrases': ['pants',
#                                         'merica',
#                                         'fishin line',
#                                         'button',
#                                         'string'],
#                         'language': {'iso_6391': 'en',
#                                      'name': 'English',
#                                      'score': 1.0},
#                         'sentiment': 0.6875251,
#                         'text': 'When a button falls off of your pants and you '
#                                 'have no string so you have to sew it back on '
#                                 'with fishin line...... #merica'},
# '722852349614555136': {'key_phrases': ['Las Americas Premium Outlets', 'Yelp'],
#                        'language': {'iso_6391': 'en',
#                                     'name': 'English',
#                                     'score': 1.0},
#                        'sentiment': 0.868752,
#                        'text': 'Ready to get my #shop on! #merica #outlets (@ '
#                                'Las Americas Premium Outlets) on #Yelp '
#                                'https://t.co/Ea2APV2Be5'},
# '722852868554825729': {'key_phrases': ['NotCoachella',
#                                        'Montgomery',
#                                        'Dodgers'],
#                        'language': {'iso_6391': 'en',
#                                     'name': 'English',
#                                     'score': 1.0},
#                        'sentiment': 0.7456422,
#                        'text': 'RT @Jill_Montgomery: #NotCoachella #Dodgers '
#                                '#merica 🌭⚾️🇺🇸 https://t.co/vOKcEXiXTh'},
# '722853016529870848': {'key_phrases': ['BBQ', 'Merica', 'USAUSAUSA'],
#                        'language': {'iso_6391': 'en',
#                                     'name': 'English',
#                                     'score': 1.0},
#                        'sentiment': 0.8411877,
#                        'text': "@NateHeffner it will be fixed by BBQ's and "
#                                'Kart! #USAUSAUSA #Merica'}
```
