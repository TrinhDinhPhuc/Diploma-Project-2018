import imgaug as ia
from imgaug import augmenters as iaa
import numpy as np
import cv2
import matplotlib.pyplot as plt
# random example images
images = np.random.randint(0, 255, (16, 128, 128, 3), dtype=np.uint8)

image_to_predict = cv2.imread("F:/data/fruits-360/test-multiple_fruits/banana_red2.jpg", cv2.IMREAD_COLOR)  # cv2.imread() to read an image
image_to_predict = cv2.cvtColor(image_to_predict, cv2.COLOR_RGB2BGR)
print("The dimension: ", image_to_predict.shape)
plt.imshow(image_to_predict)
plt.show()

seq = iaa.OneOf([
    iaa.Fliplr(), # horizontal flips (lật ảnh theo chiều ngang)
    iaa.Affine(rotate=20), # quay hình ảnh
    iaa.Multiply((1.2, 1.5))]) #random cho sáng cường độ ảnh

aug_img1 = seq.augment_image(image_to_predict)
aug_img2 = seq.augment_image(image_to_predict)
aug_img1 = cv2.cvtColor(aug_img1, cv2.COLOR_BGR2RGB)
aug_img2 = cv2.cvtColor(aug_img2, cv2.COLOR_BGR2RGB)
aug_img1 = aug_img1.astype(np.float32) / 255.
aug_img2 = aug_img2.astype(np.float32) / 255.
plt.imshow(aug_img2)
plt.show()