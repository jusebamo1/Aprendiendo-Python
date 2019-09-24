import pyfacebook
import request
import json

api = pyfacebook.Api(app_id='517064205792863',   # use the second method.
                         app_secret='564ede9228591a3106edc1f61b1c34a2',
                         short_token='517064205792863|Ci2gu-_pDuXyGwlg7hWdbCUU7KU')

api = pyfacebook.Api(long_term_token='EAAHWRGRP9l8BAHrl6anjpZAjzUlMqPJENIUnXTfqQPoFsnb54LZCXKvSiMubJTgsO4ip0M4775pNE4szdEVBBciFZChY3pzoYTZCSmlBzjxhusY5x9wgaaqQB6xD0NZBwkojFpHtDCkNZAZCEPjuZAZAcEQWIEMgnVwZALKFFvdrFfWgZDZD')

api.get_token_info(return_json=True)

{'data': {'app_id': '517064205792863',
'type': 'USER',
'application': 'Prueba',
'data_access_expires_at': 1577050634,
'expires_at': 1574458337,
'is_valid': True,
'issued_at': 1574458337,
'scopes': ['public_profile'],
'user_id': '2023545087746283'}}

api.get_page_info(page_id='875426402857700')  # you can make return_json True to see more fields
print(Page(ID=100002724332031, username="Juan Sebastian Barragan Monsalve"))


api.get_published_posts(username='Juan Sebastian Barragan Monsalve', access_token='EAAHWRGRP9l8BAG22aD75vlfASQwV29GYyruY1BRLuHVuvJMLViBF42ahtddQaenrBZCO1Y9r2jGy32Q4BSBeK20w2IXiZAZCfHOoaVohQWAIQwPJFlZCuUaX5q2B9VdKaOrTCSJG1g4sQhszZCReOMSyhvsZCT6bc42CQu0fQuZBM85fcPy1bmEBC7paa4ZCHm9dc9WDIOYZCNwZDZD')


