import librosa
import aubio
import numpy as np

class AudioProcessor:
    def __init__(self, audio_path):
        self.audio_path = audio_path
        self.y, self.sr = librosa.load(audio_path)
    
    def extract_features(self):
        # Extract Tempo
        tempo. _ = librosa.beat.tempo(y=self.y, sr=self.sr)
        
        # Extract Spectral features
        spectral_centroid = np.mean(librosa.feature.spectral_centroid(y=self.y, sr=self.sr))
        
        # Extract Pitch using Aubio
        pitch_o = aubio.pitch("default", 2048, 2048 // 2, self.sr)
        pitches = []
        with open(self.audio_path, 'rb') as f:
            while True:
                samples, read = aubio.source(f, 2048)
                if read < 2048:
                    break
                pitch = pitch_o(samples)[0]
                pitches.append(pitch)
            avg_pitch = np.mean(pitches) if pitches else 0
            
            return {
                'tempo': tempo,
                'spectral_centroid': spectral_centroid,
                'avg_pitch': avg_pitch
            }
