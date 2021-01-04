import cv2

#for showing the result in a separate window
def show_img(img):
    cv2.imshow('img',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows() 

#dodging the image would lighten the image
def dodgefunc(x,y):
  return cv2.divide(x,255-y,scale=256)

#burning the image would darken the image
def burnfunc(image, mask):
  return 255 - cv2.divide(255-image, 255-mask, scale=256)


def pencil_sketch(img):
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    #converting to negative using bitwise_not (bitwise operations are used for image manipulation in opencv)
    img_invert=cv2.bitwise_not(gray)
    
    #using gaussian blur to smoothen the image, change the kernel size accordingly and see the sketch will darken on lighten based on the kernel value
    gblur_img=cv2.GaussianBlur(img_invert,(21,21),sigmaX=0,sigmaY=0)
    
    dodged_img=dodgefunc(gray,gblur_img)
    final_image=burnfunc(dodged_img,gblur_img)
    show_img(final_image)

#For getting the pencil sketch, load your image using imread() function of cv2 library and pass it as an argument to the pencil_sketch function to obtain the sketch result.
if __name__ =='__main__':
    img=cv2.imread('image.jpeg')
    final_img=pencil_sketch(img)
    cv2.write('Final_sketch', final_img)
