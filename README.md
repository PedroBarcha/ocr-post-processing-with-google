Currently, the program wrap the text into 5 words blocks, query them to google and print whether it produced a "did you mean". However it still doesn't subtitute the given suggestion for the original excerpt. In the middle of the project I found out that google provides only 100 queries per day which isn't quite enough for me (if you need more than this you need to pay A LOT) and, hence, I've been looking for free alternative search engines, leaving this project in standby for now.

USAGE:
1)Get an API Key at https://console.developers.google.com/apis/credentials
2)Put your key inside the brackets  in "API_key" field, at spellchecker.py file
3)From the terminal, run inside the programs's directory: python __main__.py

TODO:
-Substituter: substitute google's suggestions for the original phrases
-Make a Python Package, with config to the cx and api_key