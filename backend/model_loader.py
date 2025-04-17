import tensorflow as tf
from tensorflow.keras.models import load_model
import cv2
import numpy as np
import os

def load_models():
    mri_model_path = "./models/mri_detection_model.keras"
    # tumor_model_path = "./models/tumor_classification.keras"
    
    if not os.path.exists(mri_model_path):
        raise FileNotFoundError("Error: Model files not found.")
    
    mri_model = tf.keras.models.load_model(mri_model_path, custom_objects={'InputLayer': tf.keras.layers.InputLayer})
    # tumor_model = tf.keras.models.load_model(tumor_model_path, custom_objects={'InputLayer': tf.keras.layers.InputLayer})
    
    return mri_model

mri_model = load_models()

def is_mri_image(image_path):
    """Check if the given image is an MRI scan using the trained model."""
    img = cv2.imread(image_path)
    if img is None:
        print(f"Error: Could not read image {image_path}.")
        return None, "Error: Could not read image."
    img = cv2.resize(img, (128, 128)) / 255.0
    img = np.expand_dims(img, axis=0)
    prediction = mri_model.predict(img)
    print("is_mri_image chal gya")
    out = 1 if prediction[0][1] > 0.7 else 0
    print(out)
    return out
