import re
import json


def extract_info(text):
    tracks = text.split("TRACK NAME:")
    data = []
    for track in tracks[1:]:
        track_dict = {}
        lines = track.split("\n")
        track_dict["track-name"] = lines[0].strip()
        plugins_line = [line for line in lines if "PLUG-INS:" in line][0]
        plugins = plugins_line.split("PLUG-INS:")[1].strip().split("\t")
        track_dict["plug-ins"] = [plugin.strip() for plugin in plugins if plugin]
        clip_name_line = [line for line in lines if re.match(r'\d+\s+\d+\s+\S+', line)][0]
        clip_name = clip_name_line.split("\t")[2]
        track_dict["clip-name"] = clip_name.strip()
        data.append(track_dict)
    return data


# Read the text file
with open('/Volumes/SSD-MClem/Mixing Datasets/MixEvaluationDataset/TheDoneFors/LeadMe/Mixes/McG-E/LeadMe_E.txt', 'r') as file:
    content = file.read()

track_data = extract_info(content)

# Create a dictionary to store the CLIP NAME to Source File mapping
clip_to_source_mapping = {}

# Define a regular expression pattern to extract clip mappings
clip_mapping_pattern = re.compile(r"O F F L I N E  C L I P S  I N  S E S S I O N\n(.*?)\n\n", re.DOTALL)
clip_mapping_section = clip_mapping_pattern.search(content)

if clip_mapping_section:
    clip_mapping_content = clip_mapping_section.group(1)
    clip_mappings = re.findall(r"(.+?)\t+(.+?)(\n|$)", clip_mapping_content)
    
    for clip_name, source_file, any in clip_mappings:
        clip_name = clip_name.strip()
        source_file = source_file.strip()
        clip_to_source_mapping[clip_name] = source_file
        
# Define a dictionary to store the track data
tracks = []

# Iterate through the extracted track listings
for track in track_data:
    
    track_name = track['track-name']
    plugins = track['plug-ins']
    clip_name = track['clip-name']
    audio_filename = "./audio/LeadMe/"
    
    if clip_name in clip_to_source_mapping:
        audio_filename += clip_to_source_mapping[clip_name]
                  
    track_data = {
        "track-name": track_name.strip(),
        "track-type": "AUDIO",
        "channel-mode": "MONO",
        "track-audio-path": audio_filename,
        "parameters": {
            "gain": 0,
            "pan": [0],
            "plug-ins": plugins,
        }
    }

    tracks.append(track_data)

# Create a JSON array
json_output = json.dumps(tracks, indent=2)

# Write the JSON data to a file
with open('output.json', 'w') as output_file:
    output_file.write(json_output)

print(json_output)
