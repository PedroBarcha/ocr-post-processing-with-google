## THE PROJECT
Currently, the program wraps the text into 5 words blocks, query them to google and print whether they produced a "did you mean" (and if so, what was it). However it still doesn't subtitute the given suggestion for the original excerpt. In the middle of the project I found out that google provides only 100 queries per day which isn't quite enough for me (if you need more than this you need to pay A LOT) and, hence, I've been looking for free alternative search engines, leaving this project in standby for now. UPDATE: Yandex allows huge number of queries/day. I'm currently upgrading this project to Yandex and will soon make it available.

## USAGE
1. Get an API Key and a Google's Custom Search cx, as explained here https://developers.google.com/custom-search/json-api/v1/overview
2. Put your key inside the brackets  in "API_key" field, at spellchecker.py file. Right bellow, put your cx  inside the brackets.
3. From the terminal, run inside the programs's directory: python main.py

## TODO
- [ ] Substituter: substitute google's suggestions for the original phrases
- [ ] Make a Python Package, with config to the cx and api_key
