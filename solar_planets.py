import cv2
img=cv2.imread("solar-system.jpg")
cv2.putText(img,"Sun",(20,300),cv2.FONT_HERSHEY_COMPLEX,1.5,(255,0,0))
cv2.putText(img,"Mercury",(100,250),cv2.FONT_HERSHEY_COMPLEX,.5,(255,255,255))
cv2.putText(img,"Venus",(190,250),cv2.FONT_HERSHEY_COMPLEX,.5,(255,255,255))
cv2.putText(img,"Earth",(290,250),cv2.FONT_HERSHEY_COMPLEX,.5,(255,255,255))
cv2.putText(img,"Mars",(380,250),cv2.FONT_HERSHEY_COMPLEX,.5,(255,255,255))
cv2.putText(img,"Jupiter",(520,360),cv2.FONT_HERSHEY_COMPLEX,.5,(255,255,255))
cv2.putText(img,"Saturn",(750,300),cv2.FONT_HERSHEY_COMPLEX,.5,(255,255,255))
cv2.putText(img,"Uranus",(970,300),cv2.FONT_HERSHEY_COMPLEX,.5,(255,255,255))
cv2.putText(img,"Neptune",(1100,300),cv2.FONT_HERSHEY_COMPLEX,.5,(255,255,255))
cv2.imshow("solar_planets",img)
cv2.waitKey(0)
