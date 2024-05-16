import librosa
import numpy as np
from keras.models import load_model

class GenreProcessing:
    @staticmethod
    def get_mfcc(y, sr):
        """
        Mel Frequency Cepstral Coefficients (MFCC) describe the overall shape of
        the spectral envelope.

        :param y: np.ndarray [shape=(n,)] or None, Audio time series.
        :param sr: number > 0 [scalar], Sampling rate of `y`.
        :return: np.ndarray [shape=(n_mfcc, t)], Mel-frequency cepstral coefficients.
        """
        mfcc = librosa.feature.mfcc(y=y, sr=sr)
        return np.array(mfcc)
    
    @staticmethod
    def get_mel_spectogram(y, sr):
        """
        Mel Spectogram is a spectorgam where frequencies are converted to the mel scale.

        :param y: np.ndarray [shape=(n,)] or None, Audio time series.
        :param sr: number > 0 [scalar], Sampling rate of `y`.
        :return: np.ndarray [shape=(n_mfcc, t)], Mel-spectogram.
        """
        mel_spectogram = librosa.feature.melspectrogram(y=y, sr=sr)
        return np.array(mel_spectogram)
    
    @staticmethod
    def get_chroma_vector(y, sr):
        """
        Chroma-based features represent the tonal content of a musical audio signal
        in a condensed form.

        :param y: np.ndarray [shape=(n,)] or None, Audio time series.
        :param sr: number > 0 [scalar], Sampling rate of `y`.
        :return: np.ndarray [shape=(n_chroma, t)], Chroma feature matrix.
        """
        chroma_vector = librosa.feature.chroma_stft(y=y, sr=sr)
        return np.array(chroma_vector)

    @staticmethod    
    def get_tonnetz(y, sr):
        """
        Tonnetz is a pictorial representation of projected Chroma features onto a 6-
        dimensional basis representing the perfect fifth, minor third, and major third.

        :param y: np.ndarray [shape=(n,)] or None, Audio time series.
        :param sr: number > 0 [scalar], Sampling rate of `y`.
        :return: np.ndarray [shape=(6, t)], Tonnetz feature matrix.
        """
        tonnetz = librosa.feature.tonnetz(y=y, sr=sr)
        return np.array(tonnetz)
    
    @staticmethod
    def get_features(y, sr):
        """
        Concatenate all features into an array.

        :param y: np.ndarray [shape=(n,)] or None, Audio time series.
        :param sr: number > 0 [scalar], Sampling rate of `y`.
        :return: np.ndarray [shape=(n_features,)], Concatenated features array.
        """
        # MFCC feature
        mfcc = GenreProcessing.get_mfcc(y, sr)
        mfcc_feature = np.concatenate((mfcc.mean(axis=1), mfcc.min(axis=1),
                                       mfcc.max(axis=1)))
        
        # Mel Spectogram feature
        mel_spectogram = GenreProcessing.get_mel_spectogram(y, sr)
        mel_spectogram_feature = np.concatenate((mel_spectogram.mean(axis=1),
                                                 mel_spectogram.min(axis=1),
                                                 mel_spectogram.max(axis=1)))
        
        # Chroma Vector feature
        chroma_vector = GenreProcessing.get_chroma_vector(y, sr)
        chroma_vector_feature = np.concatenate((chroma_vector.mean(axis=1),
                                                chroma_vector.min(axis=1),
                                                chroma_vector.max(axis=1)))
        
        # Tonnetz feature
        tonnetz = GenreProcessing.get_tonnetz(y, sr)
        tonnetz_feature = np.concatenate((tonnetz.mean(axis=1), tonnetz.min(axis=1),
                                          tonnetz.max(axis=1)))
        
        feature = np.concatenate((chroma_vector_feature, mel_spectogram_feature, 
                                  mfcc_feature, tonnetz_feature))
        return feature
    
    @staticmethod
    def predict_genre(features):
        """
        Evaluate the model by loading the weights.

        :param features: np.ndarray [shape=(n_features,)], Concatenated features array.
        :return: Dictionary containing genres and their respective correspondence.
        """
        # model = load_model("models/sentiment_model.h5", custom_objects={
        #     'features': GenreProcessing.get_features()
        # })

        # prediction = model.predict(features)
        
        genres = ['blues', 'classical', 'country', 'disco', 
                  'hiphop', 'jazz', 'metal', 'pop', 'reggae', 'rock']
        
        # Create final dict combining genres and predictions
        prediction_dict = {genres[0]: 0.1, genres[1]: 0.1, genres[2]: 0.1,
                           genres[3]: 0.1, genres[4]: 0.1, genres[5]: 0.1,
                           genres[6]: 0.1, genres[7]: 0.1, genres[8]: 0.1,
                           genres[9]: 0.2}
        
        return prediction_dict 
    
