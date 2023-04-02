import pickle
import re
from pathlib import Path
import logging

BASE_DIR = Path(__file__).resolve(strict=True).parent

class Model:
    def __init__(self):
        self.model_pipeline = None
        self.label_encoder = None
        self.load_model()

    def load_model_pipeline(self):
        with open(f"{BASE_DIR}/language_detection_pipeline.pkl", "rb") as f:
            self.model_pipeline = pickle.load(f)
            logging.info("Model pipeline loaded")

    def load_label_encoder(self):
        with open(f"{BASE_DIR}/label_encoder.pkl", "rb") as f:
            self.label_encoder = pickle.load(f)
            logging.info("Label encoder loaded")

    def load_model(self):
        self.load_model_pipeline()
        self.load_label_encoder()


def preprocess(text):
    text = text.lower()
    text = re.sub(r'[!@#$(),\n"%^*?\:;~`0-9]', ' ', text) # remove punctuations
    text = re.sub(r'[[]]', ' ', text) # remove square brackets
    text = re.sub(r"\s+"," ",text) # remove extra spaces
    text = re.sub(r"\'s"," ",text) # remove 's
    return text


def predict(text):
    text = preprocess(text)
    model = Model()
    prediction = model.model_pipeline.predict([text])
    prediction = model.label_encoder.inverse_transform(prediction)
    return prediction[0]
