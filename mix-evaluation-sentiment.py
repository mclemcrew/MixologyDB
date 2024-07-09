# import json
# import nltk
# from nltk.sentiment import SentimentIntensityAnalyzer
# import matplotlib.pyplot as plt

# nltk.download('vader_lexicon')
# nltk.download('punkt')

# # Load the tracks.json file
# with open('tracks.json') as file:
#     data = json.load(file)

# # Initialize the SentimentIntensityAnalyzer
# sia = SentimentIntensityAnalyzer()

# # Initialize counters for positive, negative, and neutral examples
# positive_count = 0
# negative_count = 0
# neutral_count = 0

# positive_sentences = []
# neutral_sentences = []
# negative_sentences = []

# # Loop through each mix in the 'mixes' array
# for mix in data['mixes']:
#     # Loop through each mix evaluation in the 'mix-evaluation' array
#     for evaluation in mix['mix-evaluation']:
#         # Get the track semantic evaluation
#         track_semantic_eval = evaluation['track-semantic-eval']

#         # Split the sentence by punctuation
#         # sentences = nltk.sent_tokenize(track_semantic_eval)

#         sentiment_scores = sia.polarity_scores(track_semantic_eval)
#         sentiment = sentiment_scores['compound']

#         # Increment the corresponding counter based on sentiment
#         if sentiment > 0:
#             positive_count += 1
#             positive_sentences.append(track_semantic_eval)
#         elif sentiment < 0:
#             negative_count += 1
#             negative_sentences.append(track_semantic_eval)
#         else:
#             neutral_count += 1
#             neutral_sentences.append(track_semantic_eval)

#         # print(f"Sentence: {track_semantic_eval}")
#         # print(f"Sentiment: {sentiment}")

# # Create a histogram to display the tally
# labels = ['Positive', 'Negative', 'Neutral']
# counts = [positive_count, negative_count, neutral_count]

# with open('positive-sentences-nltk.json', 'w') as json_file:
#     json.dump(positive_sentences, json_file, indent=2)
    
# print(counts)

# plt.bar(labels, counts)
# plt.xlabel('Sentiment')
# plt.ylabel('Count')
# plt.title('Sentiment Analysis Results with NLTK')
# plt.show()

# import json
# import spacy
# from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
# import matplotlib.pyplot as plt
# import random

# # Load the spaCy English model
# nlp = spacy.load("en_core_web_sm")

# # Initialize the SentimentIntensityAnalyzer from vaderSentiment
# sia = SentimentIntensityAnalyzer()

# # Load the tracks.json file
# with open('tracks.json') as file:
#     data = json.load(file)

# # Initialize counters for positive, negative, and neutral examples
# positive_count = 0
# negative_count = 0
# neutral_count = 0

# positive_sentences = []
# neutral_sentences = []
# negative_sentences = []

# # Loop through each mix in the 'mixes' array
# for mix in data['mixes']:
#     # Loop through each mix evaluation in the 'mix-evaluation' array
#     for evaluation in mix['mix-evaluation']:
#         # Get the track semantic evaluation
#         track_semantic_eval = evaluation['track-semantic-eval']

#         # Process the text using spaCy
#         doc = nlp(track_semantic_eval)

#         # Perform sentiment analysis using vaderSentiment
#         sentiment_scores = sia.polarity_scores(track_semantic_eval)
#         sentiment = sentiment_scores['compound']

#         # Increment the corresponding counter based on sentiment
#         if sentiment > 0:
#             positive_count += 1
#             positive_sentences.append(track_semantic_eval)
#         elif sentiment < 0:
#             negative_count += 1
#             negative_sentences.append(track_semantic_eval)
#         else:
#             neutral_count += 1
#             neutral_sentences.append(track_semantic_eval)

#         # Do something with the sentiment analysis result
#         # print(f"Text: {track_semantic_eval}")
#         # print(f"Sentiment: {sentiment}")

# # Create a histogram to display the tally
# labels = ['Positive', 'Negative', 'Neutral']
# counts = [positive_count, negative_count, neutral_count]

# # plt.bar(labels, counts)
# # plt.xlabel('Sentiment')
# # plt.ylabel('Count')
# # plt.title('Sentiment Analysis Results with spaCy')
# # plt.show()


import json
from transformers import pipeline
import matplotlib.pyplot as plt

sentiment_model = pipeline(model="mclemcrew/MixologyDB")

# Initialize counters for positive, negative, and neutral examples
positive_count = 0
negative_count = 0
neutral_count = 0

positive_sentences = []
neutral_sentences = []
negative_sentences = []

# # Load the tracks.json file
with open('tracks.json') as file:
    data = json.load(file)

# Loop through each mix in the 'mixes' array
for mix in data['mixes']:
    # Loop through each mix evaluation in the 'mix-evaluation' array
    for evaluation in mix['mix-evaluation']:
        # Get the track semantic evaluation
        track_semantic_eval = evaluation['track-semantic-eval']

        sentiment_scores = sentiment_model(track_semantic_eval)
        sentiment = sentiment_scores[0]['label']

        # Increment the corresponding counter based on sentiment
        if sentiment == 'POSITIVE':
            positive_count += 1
            positive_sentences.append(track_semantic_eval)
        elif sentiment == 'NEGATIVE':
            negative_count += 1
            negative_sentences.append(track_semantic_eval)
        elif sentiment == 'MIXED':
            neutral_count += 1
            neutral_sentences.append(track_semantic_eval)

        # print(f"Sentence: {track_semantic_eval}")
        # print(f"Sentiment: {sentiment}")

# Create a histogram to display the tally
labels = ['POSITIVE', 'NEGATIVE', 'MIXED']
counts = [positive_count, negative_count, neutral_count]

plt.bar(labels, counts)
plt.xlabel('Sentiment')
plt.ylabel('Count')
plt.title('Sentiment Analysis Results with HuggingFace - fine-tuned')
plt.show()

with open('positive-sentences-huggingface.json', 'w') as json_file:
    json.dump(positive_sentences, json_file, indent=2)

with open('negative-sentences-huggingface.json', 'w') as json_file:
    json.dump(negative_sentences, json_file, indent=2)
    
with open('mixed-sentences-huggingface.json', 'w') as json_file:
    json.dump(neutral_sentences, json_file, indent=2)
    
print(counts)