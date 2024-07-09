# import json

# # Load your JSON data into this variable from your 'tracks.json' file
# with open('./tracks.json', 'r') as f:
#     data = json.load(f)

# mixes = data.get('mixes', [])

# # print(tracks)

# # Mapping of instrument types to their respective instruments
# instrument_options = {
#     "DRUMS": ["KICK", "TAMBOURINE", "SNARE", "TOM", "HI-HAT", "RIDE", "CRASH", "OVERHEAD"],
#     "VOCALS": ["LEAD", "BACKGROUND"],
#     "KEYS": ["ELECTRIC", "ACOUSTIC"],
#     "GUITARS": ["LEAD", "RHYTHM"],
#     "BASS": ["BASS"],
#     "MISC": ["MISC"]
# }

# # Iterate through each track and prompt the user to fill in the details
# for mix in mixes:
#     for track in mix["tracks"]:
#         if "track-instrument" in track:
#             print(f"Track Name: {track['track-name']}")
        
#             # # Prompt for the track-instrument-type
#             # print("Select the track-instrument-type:")
#             # for i, type_option in enumerate(instrument_options.keys(), start=1):
#             #     print(f"{i}. {type_option}")
#             # type_choice = int(input("Enter the number for the track-instrument-type: ")) - 1
#             # track_instrument_type = list(instrument_options.keys())[type_choice]
#             # track["track-instrument-type"] = track_instrument_type

#             # # Prompt for the specific track-instrument
#             # print(f"Select the track-instrument for {track_instrument_type}:")
#             # for i, instrument in enumerate(instrument_options[track_instrument_type], start=1):
#             #     print(f"{i}. {instrument}")
#             # instrument_choice = int(input("Enter the number for the track-instrument: ")) - 1
#             # track_instrument = instrument_options[track_instrument_type][instrument_choice]
#             # track["track-instrument"] = track_instrument
#             # Prompt for the track-instrument-type
#             while True:
#                 print("Select the track-instrument-type:")
#                 for i, type_option in enumerate(instrument_options.keys(), start=1):
#                     print(f"{i}. {type_option}")
#                 try:
#                     type_choice = int(input("Enter the number for the track-instrument-type: ")) - 1
#                     track_instrument_type = list(instrument_options.keys())[type_choice]
#                     track["track-instrument-type"] = track_instrument_type
#                     break  # Break the loop if a valid option is chosen
#                 except (ValueError, IndexError):
#                     print("Please enter a valid number for the track-instrument-type.")

#             # Prompt for the specific track-instrument
#             while True:
#                 print(f"Select the track-instrument for {track_instrument_type}:")
#                 for i, instrument in enumerate(instrument_options[track_instrument_type], start=1):
#                     print(f"{i}. {instrument}")
#                 try:
#                     instrument_choice = int(input("Enter the number for the track-instrument: ")) - 1
#                     track_instrument = instrument_options[track_instrument_type][instrument_choice]
#                     track["track-instrument"] = track_instrument
#                     break  # Break the loop if a valid option is chosen
#                 except (ValueError, IndexError):
#                     print("Please enter a valid number for the track-instrument.")
                    
#             print()
#             print()
        

# # After running the script, you'll need to save the updated 'tracks_data' back to your 'tracks.json' file
# # with something like:
# with open('./tracks-fix.json', 'w') as f:
#     json.dump(mixes, f, indent=4)

# For the purpose of this script, let's just print the updated data
# print(json.dumps(tracks, indent=4))

# Print the updated first track
# print(json.dumps(mixes[0]["tracks"][0], indent=4))


import json

with open('./tracks.json', 'r') as f:
    data = json.load(f)

mixes = data.get('mixes', [])


def update_reverb_parameters(data):
    aux_reverb_params = {}
    
    # First, collect reverb params from AUX tracks
    for track in data:
        if track.get('track-type') == 'AUX':
            reverb_params = track['parameters'].get('reverb')
            if reverb_params:
                for reverb in reverb_params:
                    key = (reverb['name'], reverb['type'])
                    aux_reverb_params[key] = {
                        'pre-delay': reverb.get('pre-delay'),
                        'length': reverb.get('length'),
                        'size': reverb.get('size')
                    }
    
    # Now update the AUDIO tracks with the AUX reverb params
    for track in data:
        if track.get('track-type') == 'AUDIO':
            reverb_params = track['parameters'].get('reverb')
            if reverb_params:
                for reverb in reverb_params:
                    key = (reverb['name'], reverb['type'])
                    if key in aux_reverb_params:
                        reverb.update(aux_reverb_params[key])
                        reverb['send'] = "True"  # Add 'send': 'True' to the reverb parameters

    return data

# Load your JSON data
# json_data = [
#     # ... Your JSON data here ...
# ]


for mix in mixes:
    tracks = mix.get('tracks', [])
    updated_data = update_reverb_parameters(tracks)
    tracks = updated_data

# Update the reverb parameters
# updated_data = update_reverb_parameters(json_data)

# Output the updated JSON to a file
with open('updated_tracks.json', 'w') as outfile:
    json.dump(mixes, outfile, indent=2)