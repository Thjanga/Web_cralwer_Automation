from PIL import Image
import os

# img = Image.open(r'C:\Users\kspqi\Desktop\애플코딩 웹 크롤러, 업무자동화\Part3\photo1.jpg').convert('L')

# # img = img.resize((300,500))
# # img.thumbnail((300,500))
# img = img.crop((50,50,150,150)) ## 50,50 ~ 150,150 자르기

# img.save(r'C:\Users\kspqi\Desktop\애플코딩 웹 크롤러, 업무자동화\Part3\new_photo1.jpg') # quality=65,progressive=True

path = os.path.join(os.getcwd(), 'Part3', 'images')

for i in os.listdir(path):
    image_path = os.path.join(path, i)
    img = Image.open(image_path)
    img.thumbnail((500, 500))
    img.save(os.path.join(path,f'new_{i}'))