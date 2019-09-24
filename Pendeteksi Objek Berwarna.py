import cv2.cv as cv
import time
capture = cv.CaptureFromCAM(0)
cv.SetCaptureProperty(capture,3,640)
cv.SetCaptureProperty(capture,4,480)

while True:
    img = cv.QueryFrame(capture)
    cv.Smooth(img,img,cv.CV_BLUR,3)
    hue_img = cv.CreateImage(cv.GetSize(img),8,3)
    cv.CvtColor(img,hue_img,cv.CV_BGR2HSV)
    threshold_img=cv.CreateImage(cv.GetSize(hue_img), \
                                 8,1)
    cv.InRangeS(hue_img,(0,150,0),(5,255,255), \
                threshold_img)
    storage = cv.CreateMemStorage(0)
    contour = cv.FindContours \
              (threshold_img,storage, \
               cv.CV_RETR_CCOMP, \
               cv.CV_CHAIN_APPROX_SIMPLE)
    points = []
    while contour:
        rect = cv.BoundingRect(list(contour))
        if rect[0]>157.00 and rect[0]<216.83 and \
           rect[1]>227.00 and rect[1]<336.67:
            print ('a')
        if rect[0]>216.83 and rect[0]<276.66 and \
           rect[1]>227.00 and rect[1]<336.67:
            print ('b')
        if rect[0]>276.66 and rect[0]<336.49 and \
           rect[1]>227.00 and rect[1]<336.67:
            print ('c')
        if rect[0]>336.49 and rect[0]<396.32 and \
           rect[1]>227.00 and rect[1]<336.67:
            print ('d')
        if rect[0]>396.32 and rect[0]<456.15 and \
           rect[1]>227.00 and rect[1]<336.67:
            print ('e')
        if rect[0]>456.15 and rect[0]<516.00 and \
           rect[1]>227.00 and rect[1]<336.67:
            print ('f')
        if rect[0]>157.00 and rect[0]<216.83 and \
           rect[1]>336.67 and rect[1]<396.34:
            print ('g')
        if rect[0]>216.83 and rect[0]<276.66 and \
           rect[1]>336.67 and rect[1]<396.34:
            print ('h')
        if rect[0]>276.66 and rect[0]<336.49 and \
           rect[1]>336.67 and rect[1]<396.34:
            print ('i')
        if rect[0]>336.49 and rect[0]<396.32 and \
           rect[1]>336.67 and rect[1]<396.34:
            print ('j')
        if rect[0]>396.32 and rect[0]<456.15 and \
           rect[1]>336.67 and rect[1]<396.34:
            print ('k')
        if rect[0]>456.15 and rect[0]<516.00 and \
           rect[1]>336.67 and rect[1]<396.34:
            print ('l')
        if rect[0]>157.00 and rect[0]<216.83 and \
           rect[1]>396.34 and rect[1]<456.00:
            print ('m')
        if rect[0]>216.83 and rect[0]<276.66 and \
           rect[1]>396.34 and rect[1]<456.00:
            print ('n')
        if rect[0]>276.66 and rect[0]<336.49 and \
           rect[1]>396.34 and rect[1]<456.00:
            print ('o')
        if rect[0]>336.49 and rect[0]<396.32 and \
           rect[1]>396.34 and rect[1]<456.00:
            print ('p')
        if rect[0]>396.32 and rect[0]<456.15 and \
           rect[1]>396.34 and rect[1]<456.00:
            print ('q')
        if rect[0]>456.15 and rect[0]<516.00 and \
           rect[1]>396.34 and rect[1]<456.00:
            print ('r')        
        contour = contour.h_next()
        size = (rect[2]*rect[3])
        if size > 100:
            pt1 = (rect[0],rect[1])
            pt2 = (rect[0]+rect[2],rect[1]+rect[3])
            cv.Rectangle(img,pt1,pt2,(38,160,60))

    cv.ShowImage("Colour Tracking",img)
    if cv.WaitKey(10)==27:
        break
