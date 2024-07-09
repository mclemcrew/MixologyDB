import os
import json
import random
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

OPEN_API_KEY = os.getenv("OPEN_API_KEY")
ORGANIZATION_API_KEY = os.getenv("ORGANIZATION_API_KEY")

output_data = []

# audio_path_array = [ { "TRACK_NAME": "KIn", "TRACK_DESCRIPTION": "Kick In", "TRACK_AUDIO_PATH": "./audio/NotAlone/KIn_CONS.wav" }, { "TRACK_NAME": "KOut", "TRACK_DESCRIPTION": "Kick Out", "TRACK_AUDIO_PATH": "./audio/NotAlone/KOut_CONS.wav" }, { "TRACK_NAME": "HH", "TRACK_DESCRIPTION": "High Hat", "TRACK_AUDIO_PATH": "./audio/NotAlone/HH_CONS.wav" }, { "TRACK_NAME": "Sn", "TRACK_DESCRIPTION": "Snare", "TRACK_AUDIO_PATH": "./audio/NotAlone/Sn_CONS.wav" }, { "TRACK_NAME": "OH St (Stereo)", "TRACK_DESCRIPTION": "Overhead Drum Mic", "TRACK_AUDIO_PATH": "./audio/NotAlone/OH St_CONS.L.wav" }, { "TRACK_NAME": "BassDI", "TRACK_DESCRIPTION": "Bass Direct Input", "TRACK_AUDIO_PATH": "./audio/NotAlone/BassDI_CONS.wav" }, { "TRACK_NAME": "EGtr1a", "TRACK_DESCRIPTION": "Electric Guitar", "TRACK_AUDIO_PATH": "./audio/NotAlone/EGtr1a_CONS.wav" }, { "TRACK_NAME": "EGtr1b", "TRACK_DESCRIPTION": "Electric Guitar", "TRACK_AUDIO_PATH": "./audio/NotAlone/EGtr1b_CONS.wav" }, { "TRACK_NAME": "EKeys1a", "TRACK_DESCRIPTION": "Keyboard", "TRACK_AUDIO_PATH": "./audio/NotAlone/EKeys1a_CONS.wav" }, { "TRACK_NAME": "EKeys1b", "TRACK_DESCRIPTION": "Keyboard", "TRACK_AUDIO_PATH": "./audio/NotAlone/EKeys1b_CONS.wav" }, { "TRACK_NAME": "OrgODL", "TRACK_DESCRIPTION": "Organ", "TRACK_AUDIO_PATH": "./audio/NotAlone/OrgODL_CONS.wav" }, { "TRACK_NAME": "OrgODR", "TRACK_DESCRIPTION": "Organ", "TRACK_AUDIO_PATH": "./audio/NotAlone/OrgODR_CONS.wav" }, { "TRACK_NAME": "LdVC2", "TRACK_DESCRIPTION": "Lead Vocal", "TRACK_AUDIO_PATH": "./audio/NotAlone/LdVC2_CONS.wav" }, { "TRACK_NAME": "LdV3D", "TRACK_DESCRIPTION": "Lead Vocal", "TRACK_AUDIO_PATH": "./audio/NotAlone/LdV3D_CONS.wav" }, { "TRACK_NAME": "LdV3DH", "TRACK_DESCRIPTION": "Lead Vocal", "TRACK_AUDIO_PATH": "./audio/NotAlone/LdV3DH_CONS.wav" }, { "TRACK_NAME": "BkV1", "TRACK_DESCRIPTION": "Backing Vocal", "TRACK_AUDIO_PATH": "./audio/NotAlone/BkV1_CONS.wav" }, { "TRACK_NAME": "BkV1D", "TRACK_DESCRIPTION": "Backing Vocal", "TRACK_AUDIO_PATH": "./audio/NotAlone/BkV1D_CONS.wav" }, { "TRACK_NAME": "BkV2", "TRACK_DESCRIPTION": "Backing Vocal", "TRACK_AUDIO_PATH": "./audio/NotAlone/BkV2_CONS.wav" }, { "TRACK_NAME": "BkV2D", "TRACK_DESCRIPTION": "Backing Vocal", "TRACK_AUDIO_PATH": "./audio/NotAlone/BkV2D_CONS.wav" }, { "TRACK_NAME": "BkV3", "TRACK_DESCRIPTION": "Backing Vocal", "TRACK_AUDIO_PATH": "./audio/NotAlone/BkV3_CONS.wav" }, { "TRACK_NAME": "BkV3D", "TRACK_DESCRIPTION": "Backing Vocal", "TRACK_AUDIO_PATH": "./audio/NotAlone/BkV3D_CONS.wav" }, { "TRACK_NAME": "Mix (stereo)", "TRACK_DESCRIPTION": "Master / Final Mix", "TRACK_AUDIO_PATH": "./audio/NotAlone/Stereo_Mix.wav" } ]


def write_array_to_file(array, filename):
    with open(filename, 'w') as f:
        json.dump(array, f, indent=2)


client = OpenAI(
  organization=ORGANIZATION_API_KEY,
  api_key=OPEN_API_KEY
)

# messages=[
#             {
#                 "role": "system",
#                 "content": 'You are an expert in mixing music and have a deep technical understanding of gain, panning, equalization, gates, delay, reverb, compression, phasers, flangers, and choruses. A human user has evaluated the mix and provided a textual description of the mix. The textual description might include a list of descriptions about the track. You will need to separate them individually, provide a sentiment analysis of that individual statement, and provide an instruction that represents the same sentiment used in the textual description and task to achieve that effect using one of the audio effects previously listed. For separating each part, please try to separate by the sentiment rather than strictly a period. Follow the content of the sentence to understand where to separate them. To define the sentiment, please use 0 for negative and 1 for positive in your classification. For the instruction, you may only provide this with the following syntax: "Please { STATEMENT }." You must retain the same sentiment as determined in the sentiment classification. For example, if the originalStatement is "male vox way up front (uncomfortably)," the instruction could appear as: "Please make the male vocals too up front in the mix." The task is meant to change the instruction into an achievable task. The syntax for this statement can only be the following: "Please change the {EFFECT TYPE} on the {TRACK_AUDIO_PATH} track." You may only alter one parameter, so choose the one with the most significant effect on the final mix with that selected element added or removed from the tracks. For the TRACK_AUDIO_PATH, you have the following array to choose your values from: {audio_path_array} You will have to decide what track_audio_path. You will have to use the TRACK_DESCRIPTION and the TRACK_NAME to determine what track the user is mentioning and use that track\'s TRACK_AUDIO_PATH in the task. An example of task may look like this: "Please change the EQ on the ./audio/NotAlone/KIn_CONS.wav track." Here\'s a full example for you to learn the overall task: The text evaluation you will receive is the following: "Vocals very close, very dry. Need a bit of a sense of space around them. They are also too loud. Stick out" You will respond with each item in a JSON object within an array: [ { originalStatement: "Vocals very close, very dry", sentiment: 0, instruction: "Please make the vocals very close and very dry", task: "Change the Reverb on the ./audio/NotAlone/LdVC2_CONS.wav, ./audio/NotAlone/LdV3D_CONS.wav, and ./audio/NotAlone/LdV3DH_CONS.wav tracks" }, { originalStatement: "Need a bit of a sense of space around them", sentiment: 0, instruction: "Please make the vocals lack space", task: "Change the Pan on the ./audio/NotAlone/LdVC2_CONS.wav, ./audio/NotAlone/LdV3D_CONS.wav, and ./audio/NotAlone/LdV3DH_CONS.wav tracks" }, { originalStatement: "They are also too loud. Stick out", sentiment: 0, instruction: "Please make the vocals loud and stick out", task: "Change the Gain on the ./audio/NotAlone/LdVC2_CONS.wav track" }, ] ',
#             },
#             {
#                 "role": "user",
#                 "content": 'good balance kick bass. overall could be more reverb. good balance',
#             },
#             {
#                 "role": "assistant",
#                 "content": '[ { "originalStatement": "good balance kick bass", "sentiment": 1, "instruction": "Please balance the kick", "task": "Change the EQ on the ./audio/NotAlone/KIn_CONS.wav track" }, { "originalStatement": "good balance kick bass", "sentiment": 1, "instruction": "Please balance the bass", "task": "Change the EQ on the ./audio/NotAlone/BassDI_CONS.wav track" }, { "originalStatement": "overall could be more reverb", "sentiment": 0, "instruction": "Please reduce the amount of reverb", "response": "Change the Reverb on the ./audio/NotAlone/Stereo_Mix.wav track" }, { "originalStatement": "good balance", "sentiment": 1, "instruction": "Please increase the balance of the master track", "task": "Change the EQ on the ./audio/NotAlone/Stereo_Mix.wav track" } ]'
#             },
#             {
#                 "role": "user",
#                 "content": 'male vox way up front (uncomfortably)',
#             },
#             {
#                 "role": "assistant",
#                 "content": '[ { "originalStatement": "male vox way up front (uncomfortably)", "sentiment": 0, "instruction": "Please make the male vocals too up front in the mix", "task": "Please change the Gain on the ./audio/NotAlone/LdVC2_CONS.wav vox track" } ]'
#             },
#             {
#                 "role": "user",
#                 "content": 'good sounds, whoa fingersnaps! and dry',
#             },
#             {
#                 "role": "assistant",
#                 "content": '[ { "originalStatement": "good sounds", "sentiment": 1, "instruction": "Please maintain the good sounds", "task": "Change the EQ on the ./audio/NotAlone/Stereo_Mix.wav track" }, { "originalStatement": "whoa fingersnaps!", "sentiment": 1, "instruction": "Please highlight the fingersnaps", "task": "Change the Gain on the ./audio/NotAlone/OH St_CONS.L.wav track" }, { "originalStatement": "and dry", "sentiment": 0, "instruction": "Please make the track dry", "task": "Change the Reverb on the ./audio/NotAlone/Stereo_Mix.wav track" } ]'
#             },
#             {
#                 "role": "user",
#                 "content": 'too dry and sharp and aggressive sound, it seems like radio. Nice organ/synth.',
#             },
#             {
#                 "role": "assistant",
#                 "content": '[ { "originalStatement": "too dry and sharp and aggressive sound", "sentiment": 0, "instruction": "Please make the sound dry, sharp, and aggressive", "task": "Change the EQ on the ./audio/NotAlone/Stereo_Mix.wav track" }, { "originalStatement": "it seems like radio", "sentiment": 0, "instruction": "Please change the sound to resemble a radio", "task": "Change the EQ on the ./audio/NotAlone/Stereo_Mix.wav track" }, { "originalStatement": "Nice organ/synth", "sentiment": 1, "instruction": "Please maintain the nice organ/synth sound", "task": "Change the EQ on the ./audio/NotAlone/OrgODL_CONS.wav and ./audio/NotAlone/OrgODL_CONS.wav tracks" } ]'
#             },
#             {
#                 "role": "user",
#                 "content": 'Vocals a bit flat and dry sounding',
#             },
#             {
#                 "role": "assistant",
#                 "content": '[ { "originalStatement": "Vocals a bit flat and dry sounding", "sentiment": 0, "instruction": "Please make the vocals sound a bit flat and dry", "task": "Please change the EQ on the ./audio/NotAlone/LdVC2_CONS.wav, ./audio/NotAlone/LdV3D_CONS.wav, and ./audio/NotAlone/LdV3DH_CONS.wav tracks" } ]'
#             },
#             {
#                 "role": "user",
#                 "content": 'the voice lacks sense of space',
#             },
#             {
#                 "role": "assistant",
#                 "content": '[ { "originalStatement": "the voice lacks sense of space", "sentiment": 0, "instruction": "Please make the vocals lack space", "task": "Change the Pan on the ./audio/NotAlone/LdVC2_CONS.wav, ./audio/NotAlone/LdV3D_CONS.wav, and ./audio/NotAlone/LdV3DH_CONS.wav tracks" } ]'
#             },
#             {
#                 "role": "user",
#                 "content": f'{track_eval}',
#             },
        # ],


def chatCompletion(track_eval):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": 'You are an expert in mixing music and have a deep technical understanding of gain, panning, equalization, gates, delay, reverb, compression, phasers, flangers, and choruses.  A human user has evaluated a mix of a musical track and provided a textual description of the mix. You are to turn the textual evaluation of the track into instructions a user could follow to recreate a mix that would result in being regarded with a similar mix evaluation. In your instruction you may only alter one parameter, so choose the one with the most significant effect on the final mix with that selected element added, removed, or modified from the tracks. You will generate two statements: one that will only give a suggestion for the type of effect and track.  The other task will be to suggest the type of effect, the track being modified, and the explanation for why this will help. An example of this task may look like this: Succinct: "Update the EQ on the Kick track." Verbose: "Updating the EQ on the Kick by boosting the low end.  This will help bring out the lower frequencies in the mix that it\'s currently lacking." Here\'s a full example for you to learn the overall task: The text evaluation you will receive is the following: "cool, silky vox. rest of band sounds dark and far back. cooler if it was a bit closer and more intimate." Your response might look like: Succinct: "Update the EQ on the Vocal track." Verbose: "Update the EQ on the Vocal track and turn up the mids to make it sound smooth.  This will help position the vocal in the center of the mix and avoid overloading the lows and highs."',
            },
            {
                "role": "user",
                "content": 'Soft and warm.',
            },
            {
                "role": "assistant",
                "content": 'Succinct: Add reverb to the master track. Verbose: Adding a slight reverb to the overall master track can help glue the entire track together and help make it sound soft and warm.  Make sure to not add too much as to have a muddy mix.'
            },
            {
                "role": "user",
                "content": 'Nice width to the mix',
            },
            {
                "role": "assistant",
                "content": 'Succinct: Add panning on the master track. Verbose:  Adjusting the panning on the master track would help add a nice width to the mix.  Make sure to balance both the left and right channels.'
            },
            {
                "role": "user",
                "content": 'good mix but a bit dry',
            },
            {
                "role": "assistant",
                "content": 'Succinct: Add reverb to the master track. Verbose: Adding reverb to the master track can add a bit of warmth to the overall mix.  Try adjusting the type of the reverb and see what sounds best.'
            },
            {
                "role": "user",
                "content": f'{track_eval}',
            },
        ],
        model="gpt-4",
        temperature=1
    )
    return chat_completion.choices[0].message.content
    
    
if __name__ == '__main__':
    # Load the JSON file
    with open('../evals/positive-sentences-spacy.json', 'r') as file:
        sentences = json.load(file)
    
        # Randomly sample 25 sentences
        sampled_sentences = random.sample(sentences, 25)
        
    # Loop through the tracks
    for eval in sampled_sentences:
        
        # output_data.append(eval)
    
        track_instructions = chatCompletion(eval)
        # Create a dictionary for each track
        track_dict = {
            "track-num-eval": eval,
            "track-instructions": track_instructions
        }
        # Append the track dictionary to the output list
        output_data.append(track_dict)
        
    with open('instructions.json', 'w') as json_file:
        json.dump(output_data, json_file, indent=2)