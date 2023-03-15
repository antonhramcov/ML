from PIL import Image
import numpy as np

filename = "1.jpg"
with Image.open(filename) as img:
    img.load()

gray_img = img.convert("L") #Перевод изображения в градации серого

'''
img.size[1] - высота (колличество строк)
img.size[0] - ширина (колличество столбцов)
'''

matrix_gray_img = np.asarray(Image.open(filename).convert('L'))
#print(img)
new_img = Image.fromarray(matrix_gray_img, mode='L')
#new_img.show()
#print(img.size[1])
new_matrix_gray_img = np.zeros([img.size[1]*2 - 1, img.size[0]], dtype=np.uint8) # создание массива с высотой в два раза больше
#print(new_matrix_gray_img)

# копирование строк
j = 0
for i in range(0, img.size[1]):
    new_matrix_gray_img[j] = matrix_gray_img[i]
    j+=2

# заполнение пустых строк путем вычета среднего значения двух соседних ячеек
for j in range(1, img.size[1] * 2 - 1, 2): #строки 0-1598
    m = 0
    #print("j = ", j)
    for i in range(0, img.size[0]): #0-599
        new_matrix_gray_img[j, i] = new_matrix_gray_img[j-1, i] / 2 + new_matrix_gray_img[j+1, i] / 2
        '''
        print("j-1", new_matrix_gray_img[j-1, i])
        print("j+1", new_matrix_gray_img[j + 1, i])
        print(new_matrix_gray_img[j, i])
        '''

new_gray_img = Image.fromarray(new_matrix_gray_img, mode='L')   # создание картинки из нового массива
#new_gray_img.show()



new2_matrix_gray_img = np.zeros([img.size[1]*2 - 1, img.size[0]*2 -1], dtype=np.uint8) # создание массива с высотой и шириной в два раза больше

# копирование столбцов
for j in range(0, img.size[1] * 2 - 1): #строки 0-1598
    m = 0
    #print("j = ", j)
    for i in range(0, img.size[0]): #0-599
        new2_matrix_gray_img[j, m] = new_matrix_gray_img[j, i]
        m +=2

# заполнение пустых столбцов путем вычета среднего значения двух соседних ячеек
for j in range(0, img.size[1] * 2 - 1): #строки 0-1598
    m = 0
    #print("j = ", j)
    for i in range(1, img.size[0]*2 - 1, 2): # 1 - 1599
        new2_matrix_gray_img[j, i] = new2_matrix_gray_img[j, i -1] / 2 + new2_matrix_gray_img[j, i + 1] / 2
        '''
        print("j-1", new_matrix_gray_img[j-1, i])
        print("j+1", new_matrix_gray_img[j + 1, i])
        print(new_matrix_gray_img[j, i])
        '''

new2_gray_img = Image.fromarray(new2_matrix_gray_img, mode='L') # создание картинки из нового массива
new2_gray_img.show()




#matrix_img = np.array(img.getdata()).reshape(img.size[0], img.size[1], 3) # массив значений rgb пикселей, в формате строка/столбец/цветовой канал

#gray_img.show()

#matrix_gray_img = np.array(gray_img.getdata()).reshape(gray_img.size[0], gray_img.size[1]) # массив значений градаций серого для каждого пикселя, в формате строка/столбец
#new_img = Image.fromarray(matrix_gray_img, mode='L')
#new_img.show()
#new_matrix_gray_img = np.zeros((gray_img.size[0], gray_img.size[1]*2), dtype=np.uint8)
#j=0
###
#for i in range(0,len(new_matrix_gray_img),2):
#    new_matrix_gray_img[i] = matrix_gray_img[j]
#    j += 1
###
#for i in range(0, img.size[1], 2):
#    new_matrix_gray_img[i] = matrix_gray_img[j]
#    j+=1

#new_img = Image.fromarray(new_matrix_gray_img, mode='L')
#new_img.show()
#new_img = Image.fromarray(new_gray_img, mode='RGB')
