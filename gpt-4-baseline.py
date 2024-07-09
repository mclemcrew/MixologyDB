import os
import json
import jsonlines
from openai import OpenAI
from dotenv import load_dotenv

output_data = []


def write_array_to_file(array, filename):
    with open(filename, 'w') as f:
        json.dump(array, f, indent=2)


load_dotenv()  # take environment variables from .env.

OPEN_API_KEY = os.getenv("OPEN_API_KEY")
ORGANIZATION_API_KEY = os.getenv("ORGANIZATION_API_KEY")

client = OpenAI(
  organization=ORGANIZATION_API_KEY,
  api_key=OPEN_API_KEY
)


def chatCompletion(track):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": 'You are an expert in mixing music and have a deep technical understanding of gain, panning, equalization, gates, delays, reverbs, compressors, limiters, phasers, flangers, and choruses. You are to assist a music producer in selecting audio effects to apply to a track and suggest specific parameter settings for each audio effect that you deem necessary based on the track\'s description and the genre being mixed for. You will be given the genre of music the mix is being created for, the LUFS of the track, whether the track is MONO or STEREO, the track-instrument-type such as DRUMS or KEYS, and the track-instrument-subtype such as ELECTRIC or ACOUSTIC. Here\'s the list of audio effects you can suggest and their associated parameter values that you will suggest values for: EQ: TYPE (NOTCH, High-Pass (HP), Low-Pass (LP), High-Shelf (HS), Low-Shelf (LS)), VALUE which includes FREQ, Q, and GAIN COMPRESSION: THRESHOLD, ATTACK, RELEASE, GAIN, RATIO, and KNEE GAIN: value in dB PAN: value from -100 to 100 LIMITER: THRESHOLD, RELEASE, CEILING REVERB: TYPE (PLATE, HALL, ROOM), GAIN, PRE-DELAY, LENGTH, MIX (0 to 1), SEND (this value will be 0 if the reverb is applied to the track itself or 1 if the signal is being sent to an auxiliary track) PHASER: RATE, DEPTH, FEEDBACK, MIX (0 to 1) FLANGER: PRE-DELAY, RATE, DEPTH, FEEDBACK, MIX (0 to 1) GATE: ATTACK, RELEASE, THRESH, DEPTH, RATIO CHORUS: RATE, DEPTH, FEEDBACK, PRE-DELAY, MIX, GAIN DELAY: TIME, NOTE, RATE, DEPTH, OUTPUT-GAIN You may alter as many of these audio effects and their associated parameters as you wish. Please keep in mind there are other tracks included in this mix besides the current one you are suggesting parameters for and your recommendations on this instrument will have an effect on the overall mix. Do not include your reasoning behind any of these and only output your recommendations in a list format.',
            },
            {
                "role": "user",
                "content": 'GENRE: POP LUFS: -21.16 MODE: MONO TRACK-INSTRUMENT-TYPE: DRUMS TRACK-INSTRUMENT-SUBTYPE: KICK',
            },
            {
                "role": "assistant",
                "content": 'EQ: TYPE - NOTCH, FREQ - 60 Hz, Q - 1.4, GAIN -2 dB EQ: TYPE - High-Pass (HP), FREQ - 40 Hz, Q - 0.7, GAIN - N/A COMPRESSION: THRESHOLD - -20 dB, ATTACK - 10 ms, RELEASE - 100 ms, GAIN - 2 dB, RATIO - 4:1, KNEE - Soft GAIN: -2 dB PAN: 0 LIMITER: THRESHOLD - -10 dB, RELEASE - 60 ms, CEILING - -0.3 dB GATE: ATTACK - 5 ms, RELEASE - 30 ms, THRESH - -40 dB, DEPTH - -40 dB, RATIO - 10:1 DELAY: TIME - 75 ms, NOTE - Quarter, RATE - 2 Hz, DEPTH - 50%, OUTPUT-GAIN - -3 dB',
            },
            {
                "role": "user",
                "content": 'GENRE: SOUL LUFS: -32.55 MODE: MONO TRACK-INSTRUMENT-TYPE: KEYS TRACK-INSTRUMENT-SUBTYPE: ACOUSTIC'
            },
            {
                "role": "assistant",
                "content": 'EQ: TYPE - Low-Shelf (LS), FREQ - 200 Hz, Q - 0.8, GAIN - 3 dB EQ: TYPE - High-Shelf (HS), FREQ - 8000 Hz, Q - 0.7, GAIN - -2 dB COMPRESSION: THRESHOLD - -18 dB, ATTACK - 20 ms, RELEASE - 250 ms, GAIN - 5 dB, RATIO - 3:1, KNEE - Hard GAIN: 5 dB PAN: 0 REVERB: TYPE - HALL, GAIN - 3 dB, PRE-DELAY - 20 ms, LENGTH - 2.2 s, MIX - 0.3, SEND - 0 CHORUS: RATE - 0.5 Hz, DEPTH - 50%, FEEDBACK - 25%, PRE-DELAY - 5 ms, MIX - 0.2, GAIN - 1 dB DELAY: TIME - 380 ms, NOTE - Dotted Eighth, RATE - 2.5 Hz, DEPTH - 20%, OUTPUT-GAIN - 4 dB'
            },
            {
                "role": "user",
                "content": f'GENRE: {track.genre} LUFS: {track.lufs} MODE: {track.channel_mode} TRACK-INSTRUMENT-TYPE: {track.track_instrument_type} TRACK-INSTRUMENT-SUBTYPE: {track.track_instrument_subtype}',
            },
        ],
        model="gpt-4",
        temperature=1
    )
    return chat_completion.choices[0].message.content


if __name__ == '__main__':
    # Load the JSON file
    with open('../test.json') as json_file:
        data = json.load(json_file)

    mixes = data.get('mixes', [])

    for mix in mixes:
        print(mix)
        genre = mix['genre']
        for track in mix["tracks"]:
            if "track-audio-path" in track:
                lufs = track['lufs']
                channel_mode = mix['channel-mode']
                track_instrument_type = track['track-instrument-type']
                track_instrument_subtype = track['track-instrument-subtype']

            # Create a dictionary for each track
            track_dict = {
                "genre": genre,
                "channel-mode": channel_mode,
                "lufs": lufs,
                "track-instrument-type": track_instrument_type,
                "track-instrument-subtype": track_instrument_subtype
            }

            print(track_dict)
            
            # track_instructions = chatCompletion(track_dict)

            # Append the track dictionary to the output list
            # output_data.append(track_dict)
            print("Passed")

    # write_array_to_file(output_data, 'output.txt')