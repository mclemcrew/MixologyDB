import json


def process_audio_wave(audio_wave_path, mix_evaluation_path, types_path):
    # Load JSON files
    with open(mix_evaluation_path, 'r') as mix_file:
        mix_data = json.load(mix_file)

    with open(types_path, 'r') as types_file:
        types_data = json.load(types_file)

    # Do some processing with the audio here

    # Perform the task based on mix evaluation instructions
    output_messages = []
    for task in mix_data['mix-evaluation'][0]['track-instructions']:
        task_text = task['task']
        parameter_type = next((t['type'] for t in types_data['types'] if t['type'].lower() in task_text.lower()), None)

        if parameter_type:
            param_info = next((t for t in types_data['types'] if t['type'] == parameter_type), None)

            if param_info:
                parameter_changed_list = [
                    f"{param}: {task['instruction'].split(': ')[1].strip()}" if param in param_info['type'] else f"{param}: N/A"
                    for param in param_info['parameters']
                ]
                list_of_tracks = [track['track-name'] for track in mix_data['tracks']]

                output_message = f"Sure! I changed the {parameter_type} on track(s) {', '.join(list_of_tracks)} with the following parameters: {', '.join(parameter_changed_list)}"
                output_messages.append(output_message)

    return output_messages

# Test/example for a single case
audio_wave_path = "whatever.wav"
mix_evaluation_path = "./test.json"
types_path = "./test-params.json"

output_messages = process_audio_wave(audio_wave_path, mix_evaluation_path, types_path)

for message in output_messages:
    print(message)
