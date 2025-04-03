import muspy
import json
import math
import numpy as np
import matplotlib.pyplot as plt

def save_piano_roll_image(music: muspy.music.Music):
    piano_roll = music.to_pianoroll_representation()
    plt.imshow(piano_roll, cmap='gray', aspect='auto')
    plt.axis('off')
    plt.savefig("data/test/piano_roll.png", bbox_inches="tight", pad_inches=0)

def shift_to_common_key(music: muspy.music.Music, target_root=60):    
    original_key = music.key_signatures[0].key
    key_shift = -original_key
    
    for track in music.tracks:
        for note in track.notes:
            note.pitch += key_shift
    
    return music

def create_notes(music: muspy.music.Music, per_bar = False):
    if not music.time_signatures: raise ValueError("music does not have time_signatures")
    time_signature = music.time_signatures[0]
    beats_per_bar = time_signature.numerator if per_bar else 1
    ticks_per_beat = music.resolution
    bar_length = beats_per_bar * ticks_per_beat

    normalized_notes:dict[int, set] = {}
    for track in music.tracks:
        for note in track.notes:
            normalized_pitch = note.pitch % 12
            bar = math.floor(note.time / bar_length)
            if bar not in normalized_notes: normalized_notes[bar] = set()
            normalized_notes[bar].add(normalized_pitch)

    return normalized_notes

#test
music = muspy.read_midi("data/midi_files/bach/988-v05.mid")
notes = create_notes(music)

with open("data/test/score.json", "w") as file:
    json.dump({"notes": {bar: " ".join([str(note) for note in notes]) for bar, notes in notes.items()}}, file, indent=4)

shape = (12, (len(notes.keys())))
grid = np.zeros(shape)

for bar, notes in notes.items():
    for note in notes:
        grid[note][bar] = 1

plt.imshow(grid, cmap='gray', interpolation='none')
plt.axis('off')
plt.savefig("data/test/score.png", bbox_inches="tight", pad_inches=0)