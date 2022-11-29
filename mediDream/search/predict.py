import os
import cv2
from PIL import Image
import numpy as np
import tensorflow as tf
from django.conf import settings
from list.models import pillInfo

def img_clf(test_image):

#test_image='mediDream/media/test.jpg'

    img = Image.open(test_image)
    img = img.resize((250,250))
    data = np.asarray(img)
    X = np.array(data)
    X = X.astype("int") / 256
    X = X.reshape(-1,250,250,3)

    # load model
    model = tf.keras.models.load_model(os.getcwd() + '\model.h5')

    # 예측
    pred = model.predict(X)
    result = [np.argmax(value) for value in pred]   # 예측 값 중 가장 높은 클래스 반환

    return (result[0]+1)