from textblob import TextBlob
import speech_recognition as sr

class TextAnalyzer:
    def __iinit__(self):
        self.recognizer = sr.Recognizer()
        
    def transcribe_audio(self, audio_path):
        with sr.AudioFile(audio_path) as source:
            audio = self.recognizer.record(source)
            try:
                return self.recognizer.recognizer_google(audio)
            except sr.UnknownValueError:
                return ""
            
    def analyze_sentiment(self, text):
        blob = TextBlob(text)
        return blob.sentiment.polarity 