# import json

# # Load the JSON file
# with open('test.json') as json_file:
#     data = json.load(json_file)

# # Initialize an empty list to store the output
# output_array = []

# # Loop through the tracks
# for track in data['tracks']:
#     track_name = track['track-name']
#     track_description = track['track-description']
#     track_audio_path = track['track-audio-path']

#     # Create a dictionary for each track
#     track_dict = {
#         "TRACK_NAME": track_name,
#         "TRACK_DESCRIPTION": track_description,
#         "TRACK_AUDIO_PATH": track_audio_path
#     }

#     # Append the track dictionary to the output list
#     output_array.append(track_dict)

# # Print the final output as a JSON array
# print(json.dumps(output_array, indent=2))

import json

# Load the tracks.json file
with open('tracks.json') as file:
    data = json.load(file)
    
output_array = []

# Loop through each mix in the 'mixes' array
for mix in data['mixes']:
    # Loop through each mix evaluation in the 'mix-evaluation' array
    for evaluation in mix['mix-evaluation']:
        # Get the track semantic evaluation
        track_semantic_eval = evaluation['track-semantic-eval']
        
        output_array.append(track_semantic_eval)
        
with open('mix-evals.json', 'w') as json_file:
    json.dump(output_array, json_file, indent=2)