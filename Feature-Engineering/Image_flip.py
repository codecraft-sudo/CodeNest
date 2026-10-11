from PIL import Image

#open the image
image=Image.open("D:\\tour.jpg")

#Horizontal Flip
hoz_flip=image.transpose(Image.FLIP_LEFT_RIGHT)
hoz_flip.save("horiz_flip.jpg")

#vertical Flip
ver_flip=image.transpose(Image.FLIP_TOP_BOTTOM)
ver_flip.save("ver_flip.jpg")

#Display the image
hoz_flip.show()
ver_flip.show()

print("Image flipped Horizontally and vertically successfull")    
