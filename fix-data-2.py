# import json

# # Load your data (replace with your actual file path)
# with open("./updated_tracks_full.json", "r") as file:
#     data = json.load(file)

# # Iterate through the mixes
# for mix in data["mixes"]:
#     # Iterate through the tracks within each mix
#     for track in mix["tracks"]:
#         # print(track)
#         # Remove the "track-audio-data" key if it exists
#         if "track-audio-features" in track:
#             del track["track-audio-features"]["track-audio-data"]
#         # if "track-audio-data" in track["track-audio-features"]:
#         #     del track["track-audio-features"]["track-audio-data"]
#         # break
#     # break

# # Save the modified data (optional, replace with your desired file path)
# with open("modified_data.json", "w") as file:
#     json.dump(data, file, indent=2)

import math


def logic_pan_to_pro_tools(logic_pan):
    """Converts a Logic Pro X panning value (-64 to 63) to a Pro Tools panning value (-100 to 100).

    Args:
        logic_pan (float): The Logic Pro X panning value.

    Returns:
        float: The equivalent Pro Tools panning value.
    """

    # Check if the Logic pan value is within the valid range
    if logic_pan < -64 or logic_pan > 63:
        print(logic_pan)
        raise ValueError("Invalid Logic Pro X pan value. Must be between -64 and 63.")

    # Map the Logic pan range to the Pro Tools range using linear interpolation
    pro_tools_pan = math.floor((logic_pan + 64) * (200 / 127) - 100)

    return pro_tools_pan

import json

# Load your data (replace with your actual file path)
with open("./modified_data-fix.json", "r") as file:
    data = json.load(file)

# Iterate through the mixes
for mix in data["mixes"]:
    if mix["song-name"] == "Vermont":
        if mix["mix-name"] == "DU-P2" or mix["mix-name"] == "DU-O2":
            continue
        else:
            # print(mix["tracks"])
            for track in mix["tracks"]:
                print(track)
                if "track-audio-features" in track:
                    if track["channel-mode"] == "MONO":
                        logic_pan = track["parameters"]["pan"][0]
                        print(track["track-name"])
                        pro_tools_pan = logic_pan_to_pro_tools(logic_pan)
                        track["parameters"]["pan"][0] = pro_tools_pan
                    elif track["channel-mode"] == "STEREO":
                        for i in range(2):  # Update both left and right pan values
                            logic_pan = track["parameters"]["pan"][i]
                            pro_tools_pan = logic_pan_to_pro_tools(logic_pan)
                            track["parameters"]["pan"][i] = pro_tools_pan
                     
        # if "track-audio-data" in track["track-audio-features"]:
        #     del track["track-audio-features"]["track-audio-data"]
        # break
    # break

# Save the modified data (optional, replace with your desired file path)
with open("modified_data-fix-fix.json", "w") as file:
    json.dump(data, file, indent=2)