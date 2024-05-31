import json
from transformers import pipeline

sentiment_model = pipeline(model="mclemcrew/MixologyDB")

something = sentiment_model("I love this move")

print(something[0]['label'])

json.load()
