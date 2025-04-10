# Welcome to My Music Project <3 UwU

## How to run
To install the necessary requirements:

* Create virtual environment using "python3 -m venv venv"
* Enter the environment by "source venv/bin/activate"
* Run "pip install -r requirements.txt"

# Attempt 1: Split Neural Network 

## Hypothesis

The main hypothesis of this project is that music can be split into two statistical parts: chords and melody. We are basing our model on the fact that: 
* Chords are more likely to be repeat and have structure than melody. By grouping each bar together and using a loss function that penalizes wrong notes, we get a model that predicts the notes that surely are in the chord. We then use this model to remove all the chord notes, and train a new model that looks for melody notes.
* Some notes are likely to be in specific chords and in a specific melodic order. By using the aforementioned melody notes, we can create a model that predicts what type of notes are in a specific bar. 

This project is divided the following parts:

1. Import midi data
2. Transform the data
3. Build a neural network to predict the next note
4. Create an algorithm that replaces notes in a song with predicted ones
5. Integrate the functionality into my website, allowing users to create their own music

## Data
For the music data, I am using a MIDI archive of Bach's compositions. However, I may expand the scope to include other musical pieces in the future.

## Transformation
We will transform the data by:
* Centralize all the music so its in the key of C
* Put all notes together in a bar
* Have separate data set for notes without chords

## Model
The current approach involves building two separate models.

### Chords predicter
A model to predict chords using sigmoud loss function given that we want the propability of each note being between a set of chords. 
```text
┌─────────────┐    ┌────────────────┐    ┌─────────────┐
│  Input      │    │  Hidden Layers │    │  Output     │
│  96-dim     ├───►│  96→96 → 96→32 ├───►│  12-dim     │
└─────────────┘    │  + ReLU        │    │  Sigmoid    │
                   └────────────────┘    └─────────────┘
```

The loss function $f(x) = x + \frac{b^2}{x + b} - b$ is created to penalize false positives more than false negatives. This effect can be ajusted using the b parameter. It only works for x values in (-1, 1). 

NOTE: This did not work and i instead used mean squared error like a loser.

### Note predicter
This model predicts a single note using softmax, based on the preceding/following 4 notes and current chord. 

```text
┌─────────────┐    ┌────────────────┐    ┌─────────────┐
│  Input      │    │  Hidden Layers │    │  Output     │
│  36-dim     ├───►│  36→36 → 36→36 ├───►│  12-dim     │
└─────────────┘    │  + ReLU        │    │  Sigmoid    │
                   └────────────────┘    └─────────────┘
```






# Attempt 2: Markovian Network

