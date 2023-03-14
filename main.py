from PIL import Image
import numpy as np

filename = "1.jpg"
with Image.open(filename) as img:
    img.load()

matrix_img = np.array(img.getdata()).reshape(img.size[0], img.size[1], 3) # массив значений rgb пикселей, в формате строка/столбец/цветовой канал

gray_img = img.convert("L") #Перевод изображения в градации серого

matrix_gray_img = np.array(gray_img.getdata()).reshape(gray_img.size[0], gray_img.size[1]) # массив значений градаций серого для каждого пикселя, в формате строка/столбец

new_matrix_gray_img = np.zeros((gray_img.size[0]*2, gray_img.size[1]), dtype=np.uint8)
j=0
for i in range(0,len(new_matrix_gray_img),2):
    new_matrix_gray_img[i] = matrix_gray_img[j]
    j += 1



#new_img = Image.fromarray(new_gray_img, mode='RGB')
