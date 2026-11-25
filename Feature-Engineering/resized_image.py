#resize a iamge

from PIL import Image

#open the image
image=Image.open("E:\picture.jpg")
print("Total number of pixel of original image",image.size)

#Risize the image
resize_image=image.resize((600,600))

#save the resized image
resize_image.save("resized_image.jpg")

#show the image
resize_image.show()

print("Image resized successfully") 