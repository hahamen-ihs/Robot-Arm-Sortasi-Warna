import cv2.cv as cv     # import libarary openCV
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
servo1 = GPIO.PWM(14, 100)
servo2 = GPIO.PWM(15, 100)
servo3 = GPIO.PWM(18, 100)
servo4 = GPIO.PWM(23, 100)
servo5 = GPIO.PWM(24, 100)
servo1.start(90)
servo2.start(45)
servo3.start(0)
servo4.start(150)
servo5.start(100)

def posisi_a():
    sudut_5 = float(50) / 10.0 + 2.5
    servo5.ChangeDutyCycle(sudut_5)
    sudut_1 = float(110) / 10.0 + 2.5
    servo1.ChangeDutyCycle(sudut_1)
    sudut_3 = float(40) / 10.0 + 2.5
    servo3.ChangeDutyCycle(sudut_3)
    sudut_2 = float(180) / 10.0 + 2.5
    servo2.ChangeDutyCycle(sudut_2)
    sudut_4 = float(150) / 10.0 + 2.5
    servo4.ChangeDutyCycle(sudut_4)

def posisi_b():
    sudut_5 = float(50) / 10.0 + 2.5
    servo5.ChangeDutyCycle(sudut_5)
    sudut_1 = float(100) / 10.0 + 2.5
    servo1.ChangeDutyCycle(sudut_1)
    sudut_3 = float(35) / 10.0 + 2.5
    servo3.ChangeDutyCycle(sudut_3)
    sudut_2 = float(180) / 10.0 + 2.5
    servo2.ChangeDutyCycle(sudut_2)
    sudut_4 = float(150) / 10.0 + 2.5
    servo4.ChangeDutyCycle(sudut_4)

def posisi_c():
    sudut_5 = float(50) / 10.0 + 2.5
    servo5.ChangeDutyCycle(sudut_5)
    sudut_1 = float(91) / 10.0 + 2.5
    servo1.ChangeDutyCycle(sudut_1)
    sudut_3 = float(32) / 10.0 + 2.5
    servo3.ChangeDutyCycle(sudut_3)
    sudut_2 = float(180) / 10.0 + 2.5
    servo2.ChangeDutyCycle(sudut_2)
    sudut_4 = float(150) / 10.0 + 2.5
    servo4.ChangeDutyCycle(sudut_4)

def posisi_d():
    sudut_5 = float(50) / 10.0 + 2.5
    servo5.ChangeDutyCycle(sudut_5)
    sudut_1 = float(81) / 10.0 + 2.5
    servo1.ChangeDutyCycle(sudut_1)
    sudut_3 = float(32) / 10.0 + 2.5
    servo3.ChangeDutyCycle(sudut_3)
    sudut_2 = float(180) / 10.0 + 2.5
    servo2.ChangeDutyCycle(sudut_2)
    sudut_4 = float(150) / 10.0 + 2.5
    servo4.ChangeDutyCycle(sudut_4)

def posisi_e():
    sudut_5 = float(50) / 10.0 + 2.5
    servo5.ChangeDutyCycle(sudut_5)
    sudut_1 = float(73) / 10.0 + 2.5
    servo1.ChangeDutyCycle(sudut_1)
    sudut_3 = float(35) / 10.0 + 2.5
    servo3.ChangeDutyCycle(sudut_3)
    sudut_2 = float(180) / 10.0 + 2.5
    servo2.ChangeDutyCycle(sudut_2)
    sudut_4 = float(150) / 10.0 + 2.5
    servo4.ChangeDutyCycle(sudut_4)

def posisi_f():
    sudut_5 = float(50) / 10.0 + 2.5
    servo5.ChangeDutyCycle(sudut_5)
    sudut_1 = float(65) / 10.0 + 2.5
    servo1.ChangeDutyCycle(sudut_1)
    sudut_3 = float(37) / 10.0 + 2.5
    servo3.ChangeDutyCycle(sudut_3)
    sudut_2 = float(180) / 10.0 + 2.5
    servo2.ChangeDutyCycle(sudut_2)
    sudut_4 = float(150) / 10.0 + 2.5
    servo4.ChangeDutyCycle(sudut_4)

def posisi_g():
    sudut_5 = float(50) / 10.0 + 2.5
    servo5.ChangeDutyCycle(sudut_5)
    sudut_1 = float(112) / 10.0 + 2.5
    servo1.ChangeDutyCycle(sudut_1)
    sudut_3 = float(33) / 10.0 + 2.5
    servo3.ChangeDutyCycle(sudut_3)
    sudut_2 = float(180) / 10.0 + 2.5
    servo2.ChangeDutyCycle(sudut_2)
    sudut_4 = float(150) / 10.0 + 2.5
    servo4.ChangeDutyCycle(sudut_4)

def posisi_h():
    sudut_5 = float(50) / 10.0 + 2.5
    servo5.ChangeDutyCycle(sudut_5)
    sudut_1 = float(103) / 10.0 + 2.5
    servo1.ChangeDutyCycle(sudut_1)
    sudut_3 = float(27) / 10.0 + 2.5
    servo3.ChangeDutyCycle(sudut_3)
    sudut_2 = float(180) / 10.0 + 2.5
    servo2.ChangeDutyCycle(sudut_2)
    sudut_4 = float(150) / 10.0 + 2.5
    servo4.ChangeDutyCycle(sudut_4)

def posisi_i():
    sudut_5 = float(50) / 10.0 + 2.5
    servo5.ChangeDutyCycle(sudut_5)
    sudut_1 = float(94) / 10.0 + 2.5
    servo1.ChangeDutyCycle(sudut_1)
    sudut_3 = float(25) / 10.0 + 2.5
    servo3.ChangeDutyCycle(sudut_3)
    sudut_2 = float(180) / 10.0 + 2.5
    servo2.ChangeDutyCycle(sudut_2)
    sudut_4 = float(150) / 10.0 + 2.5
    servo4.ChangeDutyCycle(sudut_4)

def posisi_j():
    sudut_5 = float(50) / 10.0 + 2.5
    servo5.ChangeDutyCycle(sudut_5)
    sudut_1 = float(80) / 10.0 + 2.5
    servo1.ChangeDutyCycle(sudut_1)
    sudut_3 = float(22) / 10.0 + 2.5
    servo3.ChangeDutyCycle(sudut_3)
    sudut_2 = float(175) / 10.0 + 2.5
    servo2.ChangeDutyCycle(sudut_2)
    sudut_4 = float(150) / 10.0 + 2.5
    servo4.ChangeDutyCycle(sudut_4)

def posisi_k():
    sudut_5 = float(50) / 10.0 + 2.5
    servo5.ChangeDutyCycle(sudut_5)
    sudut_1 = float(70) / 10.0 + 2.5
    servo1.ChangeDutyCycle(sudut_1)
    sudut_3 = float(23) / 10.0 + 2.5
    servo3.ChangeDutyCycle(sudut_3)
    sudut_2 = float(175) / 10.0 + 2.5
    servo2.ChangeDutyCycle(sudut_2)
    sudut_4 = float(150) / 10.0 + 2.5
    servo4.ChangeDutyCycle(sudut_4))

def posisi_l():
    sudut_5 = float(50) / 10.0 + 2.5
    servo5.ChangeDutyCycle(sudut_5)
    sudut_1 = float(61) / 10.0 + 2.5
    servo1.ChangeDutyCycle(sudut_1)
    sudut_3 = float(27) / 10.0 + 2.5
    servo3.ChangeDutyCycle(sudut_3)
    sudut_2 = float(175) / 10.0 + 2.5
    servo2.ChangeDutyCycle(sudut_2)
    sudut_4 = float(150) / 10.0 + 2.5
    servo4.ChangeDutyCycle(sudut_4)

def posisi_m():
    sudut_5 = float(50) / 10.0 + 2.5
    servo5.ChangeDutyCycle(sudut_5)
    sudut_1 = float(117) / 10.0 + 2.5
    servo1.ChangeDutyCycle(sudut_1)
    sudut_3 = float(20) / 10.0 + 2.5
    servo3.ChangeDutyCycle(sudut_3)
    sudut_2 = float(175) / 10.0 + 2.5
    servo2.ChangeDutyCycle(sudut_2)
    sudut_4 = float(150) / 10.0 + 2.5
    servo4.ChangeDutyCycle(sudut_4)

def posisi_n():
    sudut_5 = float(50) / 10.0 + 2.5
    servo5.ChangeDutyCycle(sudut_5)
    sudut_1 = float(107) / 10.0 + 2.5
    servo1.ChangeDutyCycle(sudut_1)
    sudut_3 = float(15) / 10.0 + 2.5
    servo3.ChangeDutyCycle(sudut_3)
    sudut_2 = float(175) / 10.0 + 2.5
    servo2.ChangeDutyCycle(sudut_2)
    sudut_4 = float(150) / 10.0 + 2.5
    servo4.ChangeDutyCycle(sudut_4)

def posisi_o():
    sudut_5 = float(50) / 10.0 + 2.5
    servo5.ChangeDutyCycle(sudut_5)
    sudut_1 = float(95) / 10.0 + 2.5
    servo1.ChangeDutyCycle(sudut_1)
    sudut_3 = float(12) / 10.0 + 2.5
    servo3.ChangeDutyCycle(sudut_3)
    sudut_2 = float(175) / 10.0 + 2.5
    servo2.ChangeDutyCycle(sudut_2)
    sudut_4 = float(150) / 10.0 + 2.5
    servo4.ChangeDutyCycle(sudut_4)

def posisi_p():
    sudut_5 = float(50) / 10.0 + 2.5
    servo5.ChangeDutyCycle(sudut_5)
    sudut_1 = float(80) / 10.0 + 2.5
    servo1.ChangeDutyCycle(sudut_1)
    sudut_3 = float(12) / 10.0 + 2.5
    servo3.ChangeDutyCycle(sudut_3)
    sudut_2 = float(175) / 10.0 + 2.5
    servo2.ChangeDutyCycle(sudut_2)
    sudut_4 = float(150) / 10.0 + 2.5
    servo4.ChangeDutyCycle(sudut_4)

def posisi_q():
    sudut_5 = float(50) / 10.0 + 2.5
    servo5.ChangeDutyCycle(sudut_5)
    sudut_1 = float(70) / 10.0 + 2.5
    servo1.ChangeDutyCycle(sudut_1)
    sudut_3 = float(15) / 10.0 + 2.5
    servo3.ChangeDutyCycle(sudut_3)
    sudut_2 = float(175) / 10.0 + 2.5
    servo2.ChangeDutyCycle(sudut_2)
    sudut_4 = float(150) / 10.0 + 2.5
    servo4.ChangeDutyCycle(sudut_4)

def posisi_r():
    sudut_5 = float(50) / 10.0 + 2.5
    servo5.ChangeDutyCycle(sudut_5)
    sudut_1 = float(55) / 10.0 + 2.5
    servo1.ChangeDutyCycle(sudut_1)
    sudut_3 = float(20) / 10.0 + 2.5
    servo3.ChangeDutyCycle(sudut_3)
    sudut_2 = float(175) / 10.0 + 2.5
    servo2.ChangeDutyCycle(sudut_2)
    sudut_4 = float(150) / 10.0 + 2.5
    servo4.ChangeDutyCycle(sudut_4)

def posisi_s():
    sudut_5 = float(100) / 10.0 + 2.5
    servo5.ChangeDutyCycle(sudut_5)
    sudut_2 = float(60) / 10.0 + 2.5
    servo2.ChangeDutyCycle(sudut_2)
    sudut_3 = float(10) / 10.0 + 2.5
    servo3.ChangeDutyCycle(sudut_3)
    sudut_1 = float(150) / 10.0 + 2.5
    servo1.ChangeDutyCycle(sudut_1)
    sudut_4 = float(150) / 10.0 + 2.5
    servo4.ChangeDutyCycle(sudut_4)
    sudut_5 = float(50) / 10.0 + 2.5
    servo5.ChangeDutyCycle(sudut_5)
    time.sleep(0.001)
    sudut_5 = float(100) / 10.0 + 2.5
    servo5.ChangeDutyCycle(sudut_5)
    sudut_2 = float(45) / 10.0 + 2.5
    servo2.ChangeDutyCycle(sudut_2)
    sudut_3 = float(0) / 10.0 + 2.5
    servo3.ChangeDutyCycle(sudut_3)
    sudut_1 = float(90) / 10.0 + 2.5
    servo1.ChangeDutyCycle(sudut_1)
    sudut_4 = float(150) / 10.0 + 2.5
    servo4.ChangeDutyCycle(sudut_4)

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
               cv.CV_RETR_CCOMP,cv.CV_CHAIN_APPROX_SIMPLE)
    points = []
    while contour:
        rect = cv.BoundingRect(list(contour))

        # konversi koordinat objek menjadi karakter 
        # yang dikirimkan ke arduino
        if rect[0]>157.00 and rect[0]<216.83 and \
           rect[1]>227.00 and rect[1]<336.67:
            print ('a')
            posisi_a()
            posisi_s()
        if rect[0]>216.83 and rect[0]<276.66 and \
           rect[1]>227.00 and rect[1]<336.67:
            print ('b')
            posisi_b()
            posisi_s()
        if rect[0]>276.66 and rect[0]<336.49 and \
           rect[1]>227.00 and rect[1]<336.67:
            print ('c')
            posisi_c()
            posisi_s()
        if rect[0]>336.49 and rect[0]<396.32 and \
           rect[1]>227.00 and rect[1]<336.67:
            print ('d')
            posisi_d()
            posisi_s()
        if rect[0]>396.32 and rect[0]<456.15 and \
           rect[1]>227.00 and rect[1]<336.67:
            print ('e')
            posisi_e()
            posisi_s()
        if rect[0]>456.15 and rect[0]<516.00 and \
           rect[1]>227.00 and rect[1]<336.67:
            print ('f')
            posisi_f()
            posisi_s()
        if rect[0]>157.00 and rect[0]<216.83 and \
           rect[1]>336.67 and rect[1]<396.34:
            print ('g')
            posisi_g()
            posisi_s()
        if rect[0]>216.83 and rect[0]<276.66 and \
           rect[1]>336.67 and rect[1]<396.34:
            print ('h')
            posisi_h()
            posisi_s()
        if rect[0]>276.66 and rect[0]<336.49 and \
           rect[1]>336.67 and rect[1]<396.34:
            print ('i')
            posisi_i()
            posisi_s()
        if rect[0]>336.49 and rect[0]<396.32 and \
           rect[1]>336.67 and rect[1]<396.34:
            print ('j')
            posisi_j()
            posisi_s()
        if rect[0]>396.32 and rect[0]<456.15 and \
           rect[1]>336.67 and rect[1]<396.34:
            print ('k')
            posisi_ka()
            posisi_s()
        if rect[0]>456.15 and rect[0]<516.00 and \
           rect[1]>336.67 and rect[1]<396.34:
            print ('l')
            posisi_l()
            posisi_s()
        if rect[0]>157.00 and rect[0]<216.83 and \
           rect[1]>396.34 and rect[1]<456.00:
            print ('m')
            posisi_m()
            posisi_s()
        if rect[0]>216.83 and rect[0]<276.66 and \
           rect[1]>396.34 and rect[1]<456.00:
            print ('n')
            posisi_n()
            posisi_s()
        if rect[0]>276.66 and rect[0]<336.49 and \
           rect[1]>396.34 and rect[1]<456.00:
            print ('o')
            posisi_o()
            posisi_s()
        if rect[0]>336.49 and rect[0]<396.32 and \
           rect[1]>396.34 and rect[1]<456.00:
            print ('p')
            posisi_p()
            posisi_s()
        if rect[0]>396.32 and rect[0]<456.15 and \
           rect[1]>396.34 and rect[1]<456.00:
            print ('q')
            posisi_q()
            posisi_s()
        if rect[0]>456.15 and rect[0]<516.00 and \
           rect[1]>396.34 and rect[1]<456.00:
            print ('r')
            posisi_r()
            posisi_s()
        
        contour = contour.h_next()
        size = (rect[2]*rect[3])
        if size > 100:
            pt1 = (rect[0],rect[1])
            pt2 = (rect[0]+rect[2],rect[1]+rect[3])
            cv.Rectangle(img,pt1,pt2,(38,160,60))

    cv.ShowImage("Colour Tracking",img)
    if cv.WaitKey(10)==27:
        break
