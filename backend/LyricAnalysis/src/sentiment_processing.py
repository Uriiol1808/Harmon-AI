import pickle
import tensorflow.keras.backend as K

from keras_preprocessing.sequence import pad_sequences
from nltk.tokenize import word_tokenize
from keras.models import load_model


class SentimentProcessing:
    @staticmethod
    def recall_m(y_true, y_pred):
        y_true_int = K.cast(y_true, 'float32')  # Cast y_true to float32
        y_pred_int = K.cast(y_pred, 'float32')  # Cast y_true to float32
        
        true_positives = y_true_int * y_pred_int
        possible_positives = K.sum(K.round(K.clip(y_true_int, 0, 1)))
        recall = true_positives / (possible_positives + K.epsilon())
        return recall

    @staticmethod
    def precision_m(y_true, y_pred):
        y_true_int = K.cast(y_true, 'float32')  # Cast y_true to float32
        y_pred_int = K.cast(y_pred, 'float32')  # Cast y_true to float32

        true_positives = K.sum(K.round(K.clip(y_true_int * y_pred_int, 0, 1)))
        predicted_positives = K.sum(K.round(K.clip(y_pred, 0, 1)))
        precision = true_positives / (predicted_positives + K.epsilon())
        return precision

    @staticmethod
    def f1_m(y_true, y_pred):
        y_true_int = K.cast(y_true, 'float32')  # Cast y_true to float32
        y_pred_int = K.cast(y_pred, 'float32')  # Cast y_true to float32
        
        precision = SentimentProcessing.precision_m(y_true_int, y_pred_int)
        recall = SentimentProcessing.recall_m(y_true_int, y_pred_int)
        return 2*((precision*recall)/(precision+recall+K.epsilon()))

    @staticmethod
    def lyrics_processing(text):
        with open('models/tokenizer_config.pickle', 'rb') as handle:
            data = pickle.load(handle)
            tokenizer = data['tokenizer']
            highest_tokens = data['highest_tokens']
        
            tokens = word_tokenize(text) 
            sequence_tokens = tokenizer.texts_to_sequences([tokens]) 
            sequence = pad_sequences(sequence_tokens, maxlen=highest_tokens) 
            
            return sequence
        
    @staticmethod
    def model_evaluation(sequence):
        model = load_model("backend/LyricAnalysis/models/sentiment_model.h5", custom_objects={
            'f1_m': SentimentProcessing.f1_m,
            'precision_m': SentimentProcessing.precision_m, 
            'recall_m': SentimentProcessing.recall_m
            }
        )

        prediction = model.predict(sequence)
        rounded_preds = [float(round(val, 3)) for val in prediction[0]]
        keys = ["happy", "angry", "sad", "relaxed"]
        prediction_dict = dict(zip(keys, rounded_preds))
        return prediction_dict