import librosa
import numpy as np
from keras.models import load_model

class GenreProcessing:
    @staticmethod
    def get_mfcc(path):
        """
        Mel Frequency Cepstral Coefficients (MFCC) describe the overall shape of
        the spectral envelope.
        """
        y, sr = librosa.load(path, offset=0, duration=30)
        mfcc = librosa.feature.mfcc(y=y, sr=sr)
        return np.array(mfcc)
    
    @staticmethod
    def get_mel_spectogram(path):
        """
        Mel Spectogram is a spectorgam where frequencies are converted to the mel scale.
        """
        y, sr = librosa.load(path, offset=0, duration=30)
        mel_spectogram = librosa.feature.melspectrogram(y=y, sr=sr)
        return np.array(mel_spectogram)
    
    @staticmethod
    def get_chroma_vector(path):
        """
        Chroma-based features represent the tonal content of a musical audio signal
        in a condensed form.
        """
        y, sr = librosa.load(path)
        chroma_vector = librosa.feature.chroma_stft(y=y, sr=sr)
        return np.array(chroma_vector)

    @staticmethod    
    def get_tonnetz(path):
        """
        Tonnetz is a pictorial representation of projected Chroma features onto a 6-
        dimensional basis representing the perfect fifth, minor third, and major third.
        """
        y, sr = librosa.load(path)
        tonnetz = librosa.feature.tonnetz(y=y, sr=sr)
        return np.array(tonnetz)
    
    @staticmethod
    def get_features(path):
        """
        Concatenate all features into an array.
        """

        # MFCC feature
        mfcc = GenreProcessing.get_mfcc(path)
        mfcc_feature = np.concatenate((mfcc.mean(axis=1),
                                       mfcc.min(axis=1),
                                       mfcc.max(axis=1)))
        
        # Mel Spectogram feature
        mel_spectogram = GenreProcessing.get_mel_spectogram(path)
        mel_spectogram_feature = np.concatenate((mel_spectogram.mean(axis=1),
                                                 mel_spectogram.min(axis=1),
                                                 mel_spectogram.max(axis=1)))
        
        # Chroma Vector feature
        chroma_vector = GenreProcessing.get_chroma_vector(path)
        chroma_vector_feature = np.concatenate((chroma_vector.mean(axis=1),
                                                chroma_vector.min(axis=1),
                                                chroma_vector.max(axis=1)))
        
        # Tonnetz feature
        tonnetz = GenreProcessing.get_tonnetz(path)
        tonnetz_feature = np.concatenate((tonnetz.mean(axis=1),
                                          tonnetz.min(axis=1),
                                          tonnetz.max(axis=1)))
        
        feature = np.concatenate((chroma_vector_feature, mel_spectogram_feature, mfcc_feature, tonnetz_feature))
        return feature
    
    @staticmethod
    def model_evaluation():
        """
        Evaluate the model by loading the weights.
        """
        model = load_model("models/sentiment_model.h5", custom_objects={
            'features': GenreProcessing.get_features()
        })

        prediction = model.predict()
    
