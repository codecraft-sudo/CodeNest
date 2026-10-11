#resize a iamge

from PIL import Image

#open the image
image=Image.open("D:\\tour.jpg")
print("Total number of pixel of original image",image.size)

#Risize the image
resize_image=image.resize((300,100))

#save the resized image
resize_image.save("resized_image.jpg")

#show the image
resize_image.show()

print("Image resized successfully") 