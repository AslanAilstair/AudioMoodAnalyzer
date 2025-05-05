class MoodClassifier:
    def __init__(self, audio_features, text_sentiment=None):
        self.audio_features = audio_features
        self.text_sentiment = text_sentiment
        
    def classify(self):
        tempo = self.audio_features.get("tempo", 0)
        spectral_centroid =  self.audio_features.get("spectral_centroid", 0)
        pitch = self.audio_features.get("pitch", 0)
        
        if tempo > 120 and spectral_centroid > 2000:
            mood = "Energetic"
        elif tempo <= 80 and pitch < 200:
            mood = "sad"
        elif self.text_sentiment and self.text_sentiment < -0.2:
            mood = "Melancholic"
        else:
            mood = "calm"
            
        return mood