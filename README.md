# AudioMoodAnalyzer

A unique Python tool to analyze the mood of auydio files (music or speech) based on acoustic featrures and optional text sentiment analysis. This tool leverages lesser-lnown libraries like  **Librosa**, **Aubio**, and **TextBlob**

## Features
- Extracts audio features (tempo, pitch, spectral centroid) using Librosa and Aubio.
- Performs sentiment analysis on transcribed audio text using TextBlob.
- Classifies mood into categories like Energetic, Sad, Calm, or Melancholic.
- Visualizes results with Mathplotlib/Seaborn.

## Installation
1. CLone the repository:
   '''bash
   git clone https://github.com/AslanAilstair/AudioMoodAnalyzer.git
   cd AudioMoodAnalyzer

   pip install -r requirements.txt

   Ensure you have  ffmpeg installed for audio processiong (required by Aubio)

   
