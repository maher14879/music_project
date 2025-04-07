# Welcome to My Music Project

## How to run
To install the necessary requirements:

* Create virtual environment using "python3 -m venv .venv"
* Run "pip install -r requirements.txt"

# About the project

## Hypothesis

The main hypothesis of this project is that music can be split into two statistical parts: chords and melody. We are basing our model on the fact that: 
* Chords are more likely to be repeat and have structure than melody. By grouping each bar together and using a loss function that penalizes wrong notes, we get a model that predicts the notes that surely are in the chord. We then use this model to remove all the chord notes, and train a new model that looks for melody notes.
* Some notes are likely to be in specific chords and in a specific melodic order. By using the aforementioned melody notes, we can create a model that predicts what type of notes are in a specific bar. 

This project is divided into three main parts:

1. Import midi data
2. Transform the data
3. Build a neural network to predict the next note
4. Integrate the functionality into my website, allowing users to create their own music

## Data
For the music data, I am using a MIDI archive of Bach's compositions. However, I may expand the scope to include other musical pieces in the future.

## Transformation
We will transform the data by:
* Centralize all the music so its in the key of C
* Put all notes together in a bar
* Have separate data set for notes without chords

## Model
The current approach involves building two separate models:
1. A model to predict chords
2. A model to predict notes