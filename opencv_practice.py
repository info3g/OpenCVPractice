import cv2

img = cv2.imread('C://Users//ILLUMINATI//Desktop//Computer-Vision-with-Python//DATA//00-puppy.jpg')
img = cv2.resize(img,(400,400))
cv2.rectangle(img,pt1=(200,200),pt2=(300,300),color=(255,0,0),thickness=5)
cv2.circle(img,center=(100,100),radius=50,color=(0,255,0),thickness=-1)
cv2.line(img,pt1=(0,0),pt2=(400,400),color=(255,0,0),thickness=3)

font = cv2.FONT_HERSHEY_PLAIN
cv2.putText(img,text='HI',org=(0,100),fontFace=font,fontScale=3,color=(255,255,0),thickness=5)
while True:
    cv2.imshow('puppy',img)
    print('in')

    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()    