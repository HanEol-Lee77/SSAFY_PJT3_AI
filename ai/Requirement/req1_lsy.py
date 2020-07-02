import cv2


def img_load(img_path):
    img = cv2.imread(img_path)
    img = cv2.resize(img, dsize=(250, 250), interpolation=cv2.INTER_AREA)
    height, width, chanel = img.shape
    for c in range(0, chanel):
        sum = 0
        sqaure_sum = 0
        for y in range(0, height):
            for x in range(0, width):
                cell = img.item(y, x, c)
                sum += cell
            sqaure_sum += cell ** 2
    
        variance = sqaure_sum - (sum ** 2)
        mean = sum / (height + width)   

        for y in range(0, height):
               for x in range(0, width):   
                cell = img.item(y, x, c)
                img.itemset(y, x, c, (cell - mean)/ variance)
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# def load_image(image_path):
#     img = tf.io.read_file(image_path)
#     img = tf.image.decode_jpeg(img, channels=3)
#     # io.decode_image
#     img = tf.image.resize(img, (299, 299))
#     img = tf.keras.applications.inception_v3.preprocess_input(img)
#     return img, image_path