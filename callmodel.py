import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image
import os
import io
from sklearn.preprocessing import LabelEncoder

# Load the trained model
class catPredictor():

    def __init__(self): 
        self.model=None

    # Load model from file
    def loadmodel(self,fn):
        try:
            self.model = tf.keras.models.load_model(fn)
            return True
        except Exception as e:
            print(f"{fn} fail with {str(e)}")
            return False

    # Prepare the image
    def setimage(self,imgdb):
        imgSize = (224, 224)  # Image size expected by the model
        try:
            # pimg = load_img(r"test.jpg", target_size=imgSize) # +D+
            # pimg.save("test01.jpg", format='JPEG')
            img = Image.open(io.BytesIO(imgdb))
            img = img.resize(imgSize,Image.NEAREST)
            # img.save("test02.jpg", format='JPEG') # +D+
            
            # pimg_array = img_to_array(pimg) # +D+
            # img_array = img_to_array(img)
            # are_same = np.array_equal(pimg_array, img_array)
            # print("Изображения одинаковые:" if are_same else "Изображения разные.")            
            img_array = img_to_array(img) / 255.0  # Normalize to [0, 1]
            img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
            return img_array
        except Exception as e:
            print(f"Load failed: {str(e)}")
            return None

    # Prepare metadata
    def setmetadata(self,age, gender):
    # Prepare age
        age_array = np.array([[age]], dtype='float32')  # Shape (1,1)
        gender_array =np.array([[gender]], dtype='float32')
        metadata = {
            'age': age_array,  # Shape (1,1)
            'gender': gender_array,  # Shape (1,1)
        }
        return metadata

    def exec(self,img,age,gender):
        print("Diag...")
        if self.model==None: return None

        prepared_image = self.setimage(img)
        prepared_metadata = self.setmetadata(age, gender)

        if prepared_image is None or prepared_metadata is None: return None
        inputs = {
            'image': prepared_image,  # Shape (1, 224, 224, 3)
            'age': prepared_metadata['age'],  # Shape (1,1)
            'gender': prepared_metadata['gender'],  # Shape (1,1)
        }
        prediction = self.model.predict(inputs)
        return prediction[0]
    
    # Output the class probabilities
    # classes = le_label.classes_
    # print("Prediction Results:")
    # for i, class_name in enumerate(classes):
    #     print(f"{class_name}: {prediction[0][i] * 100:.2f}%")


#--------------------------------------------
# Sample input
# print("Predictor ready")
# imgSize = (224, 224)
# pimg = load_img(r"test.jpg", target_size=imgSize) # +D+
# pimg.save(r"test01.jpg",imgSize = (224, 224))


# exit(0)
# image_path = r"C:\Users\KARINA\Desktop\data_cats_clean\checking\Conj_0F_0y_Korean Shorthair.jpg"
# prepared_image = prepare_image(image_path)

# # Prepare metadata for prediction
# age = 5  # Age of the cat (in years)
# gender = 'Male'  # 'Male' or 'Female'

# prepared_metadata = prepare_metadata(age, gender)

# # Make a prediction using the loaded model
