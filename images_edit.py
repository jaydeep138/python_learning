from PIL import Image
img1=Image.open("3.jpg")
#img1.save('3.png')              #to change the extension of image
#img1.save("3.pdf")
#img1.show()     #to show image it can open in any default browser

####                          to change the size of image         ############
#max_size=(500,500)
#img1.thumbnail(max_size)
#img1.save("3small.jpg")


##########              sharpness              ##############
from PIL import ImageEnhance
#enhancer = ImageEnhance.Sharpness(img1)
#enhancer.enhance(-40).save("3_edited.jpg")        #0: blury 1:orginal 2:increase sharpnes

##################        colour                ##################3
#enh=ImageEnhance.Color(img1)
#enh.enhance(0).save("3_color.jpg")        #0:black and white   1:original      after 2 color is increasing


#                brigtness------------------------------------
#enh=ImageEnhance.Brightness(img1)
#enh.enhance(4).save("3_brightness.jpg")

# -             -- contrast---------
#enh=ImageEnhance.Contrast(img1)
#enh.enhance(4).save("3_contrast.jpg")


#~~~~~~~~~~~~~~~~~~~~~BLUR FILTER~~~~~~~~~~~~~!
from PIL import ImageFilter
img1.filter(ImageFilter.GaussianBlur(radius=4)).save("3_blur.jpg")