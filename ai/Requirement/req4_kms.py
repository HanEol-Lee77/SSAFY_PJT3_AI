import numpy as np
from keras.applications import resnet50
from keras.preprocessing import image
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--img_path', type=str, default='Kuszma.jpg',
                    help="추출할 이미지파일 경로를 입력하세요")
args = parser.parse_args()
args_dict = args.__dict__

# 테스트용으로 사용할 모델 - Keras Pretrained ResNet 50
RESNET50_WEIGHTS = 'saved_models/resnet50_weights_tf_dim_ordering_tf_kernels.h5'
#RESNET50_NOTOP_WEIGHTS = 'saved_models/resnet50_weights_tf_dim_ordering_tf_kernels_notop.h5'

model = resnet50.ResNet50(weights=RESNET50_WEIGHTS)

#모델의 사이즈인 224,224에 맞게 변경

img = image.load_img(args_dict['img_path'], target_size=(224, 224))

#PIL 이미지를 numpy array로 변경
x = image.img_to_array(img)

# Add a forth dimension since Keras expects a list of images
x = np.expand_dims(x, axis=0)

# Scale the input image to the range used in the trained network
x = resnet50.preprocess_input(x)

# Run the image through the deep neural network to make a prediction
predictions = model.predict(x)

print(predictions)