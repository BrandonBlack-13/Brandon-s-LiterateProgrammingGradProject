import RPi.GPIO as GPIO
import time
import cv2
import drivers

#face detection algorithm
def detect_features(frame, sto):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.05, 4)

    maxArea = 0
    x = 0
    y = 0
    w = 0
    h = 0
    for (_x, _y, _w, _h) in faces:
        if _w*_h > maxArea:
            x = _x
            y = _y
            w = _w
            h = _h
            maxArea = w*h
        if maxArea > 0:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    if y == 0:
        y = sto
    
    if y < 10:
        GPIO.output(8, True)
        GPIO.output(10, False)
        GPIO.output(19, True)
        GPIO.output(21, False)
    elif y > 30:
        GPIO.output(8, False)
        GPIO.output(10, True)
        GPIO.output(19, False)
        GPIO.output(21, True)
    else:
        GPIO.output(8, False)
        GPIO.output(10, False)
        GPIO.output(19, False)
        GPIO.output(21, False)
    
    sto = y

    return frame, sto

#converts to 480p
def make_480p():
    stream.set(3, 72)
    stream.set(4, 96)

#scales down image by 30%
def rescale(frame, percent=75):
    scale_percent = 20
    width = int(frame.shape[1] * scale_percent / 100)
    height = int(frame.shape[0] * scale_percent / 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)

def sensor():
    #sensor code
    GPIO.output(16, False)
    time.sleep(0.000002)
    GPIO.output(16, True)
    time.sleep(0.00001)
    GPIO.output(16, False)

    while GPIO.input(18) == 0:
        pulse_start = time.time()
    while GPIO.input(18) == 1:
        pulse_end = time.time()
    duration = pulse_end - pulse_start
    distance = duration * 17150
    distance = distance/2.54
    distance = round(distance, 2)
    _string = str(distance)
    display.lcd_display_string("                  ", 1)
    display.lcd_display_string("Distance:" + _string + "in", 1)

#Function for manual input mode
def input(count, stoon):
    try:
        while True:

            #Button Code
            if GPIO.input(15) == True:
                GPIO.output(8, True)
                GPIO.output(10, False)
                GPIO.output(19, True)
                GPIO.output(21, False)

            elif GPIO.input(13) == True:
                GPIO.output(8, False)
                GPIO.output(10, True)
                GPIO.output(19, False)
                GPIO.output(21, True)

            else:
                GPIO.output(8, False)
                GPIO.output(10, False)
                GPIO.output(19, False)
                GPIO.output(21, False)

            #Switch Code
            if GPIO.input(11) == False:
                display.lcd_clear()
                display.lcd_display_string("Mode: Auto", 2)
                auto(0, stoon)
            
            if count == 40000:
                sensor()
                count = 0

            count = count + 1
    
    except KeyboardInterrupt:
        GPIO.cleanup()
        stream.release()
        cv2.destroyAllWindows()
        display.lcd_clear()

#Function for Automatic Mode
def auto(count, stoot)

    try:
        while True:

            #Camera Code
            ret, frame = stream.read()

            if not ret:
                break    

            frame = rescale(frame, percent=5)

            frame, stoot = detect_features(frame, stoot)

            if GPIO.input(11) == False:
                hey = 5
            
            else:
                display.lcd_clear()
                display.lcd_display_string("Mode:Manual", 2)
                input(0, stoot)

            if count == 40000:
                sensor()
                count = 0
            
            count = count + 1

    except KeyboardInterrupt:
        GPIO.cleanup()
        stream.release()
        cv2.destroyAllWindows()
        display.lcd_clear()

#Main Begins Here
GPIO.setmode(GPIO.BOARD)

#Buttons
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#Switch
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#Motor Controller
GPIO.setup(8, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)

#Sensor
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.IN)

#Motor Controller 2
GPIO.setup(19, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

#Camera
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

stream = cv2.VideoCapture(0)

if not stream.isOpened():
    exit()

make_480p()

display = drivers.lcd()
display.lcd_clear()
display.lcd_display_string("Mode: Manual", 2)

stoop = 25

input(0, stoop)