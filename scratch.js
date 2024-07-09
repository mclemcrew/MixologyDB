{
    "mix-name": "",
        "song-name": "",
            "artist-name": "",
                "genre": "",
                    "tracks": [
                    ]
}

{
    "mix-name": "UCP-B1",
        "song-name": "Good Time",
            "artist-name": "Louis Cressy Band",
                "genre": "ROCK",
}


"gate": {
    "name": "Noise Gate",
        "thres": -24,
            "reduction": -100,
                "attack": 3,
                    "hold": 170,
                        "release": 48.7
}

"reverb": [
    {
        "name": "Space Designer",
        "type": "SPRING",
        "gain": 0,
        "pan": [0],
        "pre-delay": 23,
        "length": 1010
    }
]

"reverb": [
    {
        "name": "AIR Reverb",
        "type": "HALL",
        "pre-delay": 12,
        "length": 1700,
        "room- size": 100,
        "mix": 100
    }
]


"compression": [{
    "name": "Compressor",
    "attack": 19,
    "release": 310,
    "thres": -14.5,
    "gain": 0,
    "ratio": "2.4:1",
    "knee": 1
}]



"reverb": [{
    "name": "Space Designer",
    "type": "PLATE",
    "gain": -10,
    "pan": [0]
}]


"reverb": [
    {
        "name": "LexRoom",
        "type": "ROOM",
        "gain": -12.9,
        "pan": [0]
    },
    {
        "name": "LexHall",
        "type": "HALL",
        "gain": -23.0,
        "pan": [0]
    },
    {
        "name": "LexPlate",
        "type": "PLATE",
        "gain": -12.3,
        "pan": [0]
    },
    {
        "name": "AIR Non-Linear Reberb",
        "type": "ROOM",
        "pre-delay": 43,
        "dry-delay": 15,
        "length": 286,
        "reverse": "True",
        "mix": 1,
        "gain": -14,
        "pan": [-100, 100],
        "send": "True"
    }
]


{
    "track-name": "test",
        "track-type": "AUDIO",
            "track-audio-path": ""
    "track-group": "",
        "channel-mode": "MONO",
            "parameters": {
        "gain": 0,
            "pan": [
                0
            ]
    },
}

"delay": {
    "name": "Stereo Delay",
        "left-delay-time": 220,
            "left-note": "1/8",
                "left-deviation": -34,
                    "left-output-mix": 100,
                        "right-delay-time": 334,
                            "right-note": "1/8",
                                "right-deviation": 0,
                                    "right-output-mix": 100
}


"gate": {
    "name": "Noise Gate",
        "thres": -24,
            "reduction": -100,
                "attack": 3,
                    "hold": 170,
                        "release": 48.7
}

"compression": [
    {
        "name": "Compressor/Limiter",
        "attack": 0.3592,
        "release": 10.1,
        "thres": -21.8,
        "gain": 0,
        "ratio": "3.4:1",
        "knee": 7.6
    }
]


"gate": [
    {
        "name": "Expander/Gate",
        "attack": 0.01,
        "release": 234.7,
        "thres": -24,
        "hold": 20,
        "ratio": "100.0:1",
        "range": -30
    }
],

    "compression": [{
        "name": "Channel Strip",
        "attack": 60.3,
        "release": 10.7,
        "thres": -32.7,
        "depth": -36,
        "gain": 2.1,
        "ratio": "3.7:1",
        "knee": 0
    }]

"gate": [{
    "name": "Channel Strip",
    "attack": 0.02,
    "release": 200,
    "thres": -58,
    "depth": -36,
    "ratio": "1:1",
    "knee": 0,
    "hold": 1
}]

"flanger": [
    {
        "name": "AIR Flanger",
        "pre-delay": 0.75,
        "rate": 1,
        "depth": 3,
        "feedback": 0,
        "mix": 0.15
    }
]


"compression": [
    {
        "name": "Compressor/Limiter",
        "attack": 0.1123,
        "release": 80,
        "thres": -11.8,
        "gain": 0,
        "ratio": "3.0:1",
        "knee": 0
    },
    {
        "name": "BF-76",
        "attack": 1,
        "release": 2,
        "input": 0,
        "output": 18,
        "ratio": "20:1"
    },
    {
        "name": "Maxim",
        "thres": -24,
        "ceiling": 0,
        "release": 1,
        "mix": 1
    }
]

"delay": [
    {
        "name": "Air Multi-Delay",
        "delay-time": "4.48/16th",
        "feedback": 0,
        "high-cut": 1410,
        "low-cut": 209,
        "mix": 1
    }
]

"reverb": [
    {
        "name": "D-Verb",
        "type": "HALL",
        "gain": -20.3,
        "pan": [0]
    }
]

"reverb": [
    {
        "name": "D-Verb",
        "type": "HALL",
        "gain": 0,
        "pre-delay": 0,
        "length": 2200,
        "mix": 20
    }
]

"delay": [
    {
        "name": "Mod Delay III",
        "gain": -24.7,
        "pan": [0]
    }
]

"chorus": [
    {
        "name": "AIR Chorus",
        "rate": 0.48,
        "depth": 2.02,
        "feedback": 0,
        "pre-delay": 6,
        "mix": 34
    }
]


"delay": [{
    "name": "Mod Delay III",
    "left-delay-time": 29.9,
    "left-note": "1/4",
    "left-rate": 0.74,
    "left-depth": 0.44,
    "left-output-mix": 0.3,
    "left-gain": 0,
    "right-delay-time": 238.1,
    "right-note": "1/4",
    "right-rate": 0.74,
    "right-depth": 0.44,
    "right-output-mix": 0.2,
    "right-gain": 0,
}]

"eq": [
    {
        "type": "NOTCH",
        "value": {
            "freq": 200,
            "q": 0.71,
            "gain": 18
        }
    },
    {
        "type": "NOTCH",
        "value": {
            "freq": 1000,
            "q": 10,
            "gain": -18
        }
    }
],


    "chorus": [
        {
            "name": "AIR Chorus",
            "rate": 0.48,
            "depth": 2.02,
            "feedback": 0,
            "pre-delay": 6,
            "mix": 34
        }
    ]

"reverb": [
    {
        "name": "AIR Vintage Filter",
        "type": "ROOM",
        "cutoff": 3100,
        "resonance": 0.3,
        "fat": 2,
        "output": 0
    }
],


    "reverb": [
        {
            "name": "LexRoom",
            "type": "ROOM",
            "gain": -11.1,
            "pan": [0],
            "send": "True"
        }
    ]


{
    "name": "Mod Delay III",
        "left-delay-time": 175.9,
            "left-note": "N/A",
                "left-rate": 0,
                    "left-depth": 0,
                        "left-gain": 0,
                            "left-output-mix": 0.35,
                                "right-delay-time": 269.2,
                                    "right-note": "N/A",
                                        "right-rate": 0,
                                            "right-depth": 0,
                                                "right-gain": 0,
                                                    "right-output-mix": 0.4
}

{
    "name": "Mod Delay III",
        "delay-time": 21.7,
            "note": "N/A",
                "rate": 2.01,
                    "depth": 0.32,
                        "gain": 0,
                            "mix": 1
}


"compression": [
    {
        "name": "Maxim",
        "thres": -8.3,
        "ceiling": 0,
        "release": 1,
        "mix": 1
    }
]

"reverb": [
    {
        "name": "AIR Spring Reberb",
        "type": "ROOM",
        "pre-delay": 4,
        "length": 1100,
        "mix": 0.17
    }
]


"reverb": [
    {
        "name": "D-Verb",
        "type": "HALL",
        "gain": 0,
        "pre-delay": 8,
        "length": 400,
        "mix": 1,
        "pan": [0],
        "send": "True"
    },
    {
        "name": "D-Verb",
        "type": "ROOM",
        "gain": 0,
        "pre-delay": 11,
        "length": 208,
        "mix": 1,
        "pan": [0],
        "send": "True"
    },
    {
        "name": "D-Verb",
        "type": "PLATE",
        "gain": 0,
        "pre-delay": 0,
        "length": 1300,
        "mix": 1,
        "pan": [0],
        "send": "True"
    }
]

"delay": [{
    "name": "AIR Dynamic Delay",
    "feedback": 0.1,
    "note": "1/8 dotted",
    "mix": 1,
    "gain": 0,
    "pan": [0],
    "send": "True"
}]

"phaser": [
    {
        "name": "AIR Phaser",
        "rate": 1,
        "depth": 0.5,
        "feedback": 0.15,
        "mix": 0.1
    }
]



"name": "Mod Delay III",
    "gain": -7.0,
        "pan": [0],
            "delay-time": 9.4,
                "note": "N/A",
                    "rate": 1.14,
                        "depth": 0.4,
                            "output-mix": 1

