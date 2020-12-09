import cv2

def show_img(img):
    cv2.imshow('img',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows() 

def dodgefunc(x,y):
  return cv2.divide(x,255-y,scale=256)

def burnfunc(image, mask):
  return 255 - cv2.divide(255-image, 255-mask, scale=256)

def pencil_sketch(img):
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img_invert=cv2.bitwise_not(gray)
    gblur_img=cv2.GaussianBlur(img_invert,(21,21),sigmaX=0,sigmaY=0)
    dodged_img=dodgefunc(gray,gblur_img)
    final_image=burnfunc(dodged_img,gblur_img)
    show_img(final_image)


img=cv2.imread('image3.jpeg')
pencil_sketch(img)