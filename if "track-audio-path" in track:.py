if "track-audio-path" in track:
            audio_path = '.' + str(track['track-audio-path'])
            data, samplerate = sf.read(audio_path, dtype='float32')
            print(f"Sample rate: {samplerate}")
            print(f"Shape: {data}")
            track['track-audio-sample-rate'] = samplerate
            track['track-audio-data'] = data
            
            
            # Iterate over each track and modify it
for mix in data['mixes']:
    for track in mix['tracks']:
        if "track-audio-path" in track:
            # Create the new 'track-audio-features' dictionary
            track_audio_features = {
                'track-audio-path': track.pop('track-audio-path', None)  # Remove the track-audio-path and get its value
            }
            # Add the 'track-audio-features' dictionary to the track
            track['track-audio-features'] = track_audio_features