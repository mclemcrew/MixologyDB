import json
import random

# Load the JSON data from positive-sentences-spacy.json
with open('evals/positive-sentences-spacy.json', 'r') as file:
    sentences = json.load(file)
    
    # Randomly sample 25 sentences
    sampled_sentences = random.sample(sentences, 25)

    # Output the sampled sentences as JSON
    print(json.dumps(sampled_sentences, indent=2))