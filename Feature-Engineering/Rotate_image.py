#Rotate image

from PIL import Image

#open the image
image=Image.open("D:\\tour.jpg")

rotate=image.rotate(-45)
rotate.save("ratate.jpg")
rotate.show()
print("The rotate successfuly")