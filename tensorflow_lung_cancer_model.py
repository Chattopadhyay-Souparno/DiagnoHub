import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np


def predict(model,image_path):
# Load the saved model
    model = tf.keras.models.load_model(str(model))

# Load and preprocess the image to make it compatible with the model
    img_path = str(image_path)  # Replace with the actual path to your image
    img = image.load_img(img_path, target_size=(256, 256))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0  # Normalize the image

# Make a prediction
    prediction = model.predict(img_array)


# Interpret the prediction
    if prediction[0][0] > 9e-29:
        
        a = "The Patient has a healthy Lung"
        #print(a)
        return a
    else:
        return"The Patient is suffering from either Squamous Cell or Adenocarcinoma"
        
    
#model = 'lung_cancer_detection_model.h5'

#image_path = 'lung_colon_image_set/lung_image_sets/lung_n/lungn40.jpeg'

#predict(model,image_path)

