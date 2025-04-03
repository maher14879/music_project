# Welcome to My Music Project

This project is divided into three main parts:

1. Import and create data for training a music model
2. Build a neural network to predict the next note
3. Integrate the functionality into my website, allowing users to create their own music

## Data
For the music data, I am using a MIDI archive of Bach's compositions. However, I may expand the scope to include other musical pieces in the future.

## Transformation
The data is transformed to focus on two key elements:
- The beat/bar of each note
- The note itself

## Model
The current approach involves building three separate models:
1. A model to predict which chord/notes should come next
2. A model to predict the correct order of notes
3. A model to determine the duration of each note

I will also consult with a musical expert to help refine my model's hypotheses and loss functions.