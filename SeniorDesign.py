# <h1>M.T. Desk</h1>
# <h2>Project Overview:&nbsp;</h2>
# <h3>Purpose:</h3>
# <p class="MsoNormal"
#     style="margin-bottom: 9.6pt; mso-para-margin-bottom: .8gd; text-align: justify; line-height: normal;">
#     <span
#         style="font-family: 'Times New Roman',serif; mso-fareast-font-family: 'Times New Roman'; color: black; mso-themecolor: text1;">The
#         Movement Tracking Desk (M.T. Desk) is an auto-adjusting standing desk.
#         The desk tracks user movement and adjusts its height
#         accordingly.&nbsp;</span><span
#         style="font-family: 'Times New Roman',serif; mso-fareast-font-family: 'Times New Roman'; color: black; mso-themecolor: text1;">M.T.
#         Desk also allows for manual input to adjust the desk, and it measures
#         the height of the desk from the ground at all times as well. The core
#         issue trying to be solved is the lack of integration between sitting
#         and standing desks. While adjustable desks exist, having to physically
#         lift the desk to move it can be inconvenient and break workflow as it
#         is best to alternate between sitting and standing while working.
#         Electronic standing desks can be heavy, slow, and quite expensive.
#         M.T. Desk is an option that is not only affordable, but it allows you
#         to seamlessly transition between sitting and standing without breaking
#         your workflow.&nbsp;</span></p>
# <h3>Hardware:</h3>
# <p class="MsoNormal"
#     style="margin-bottom: 9.6pt; mso-para-margin-bottom: .8gd; line-height: normal; vertical-align: baseline;">
#     <span
#         style="font-family: 'Times New Roman',serif; mso-fareast-font-family: 'Times New Roman';">M.T.
#         Desk&rsquo;s hardware is organized into six major subsystems: motors,
#         display, manual input, camera, sensors, and power. The desk is moved
#         by two linear actuators that serve as the motors, allowing for the
#         desk to move up and down smoothly. Manual input, consisting of buttons
#         for an option to move the desk and a switch mechanism to turn the
#         motion tracking on or off, is provided for the user. A simple LCD
#         conveys the status and height of the desk to the user. For a clear
#         picture of the user, a personal webcam with 4K resolution allows for
#         precise tracking by relaying a live camera feed to the
#         microcontroller. The distance sensor calculates the distance from the
#         desktop to the floor. The power is supplied by a nearby AC outlet in a
#         home or office. M.T. Desk also features a surge protector supplying AC
#         outlets and USB ports.&nbsp;&nbsp;</span></p>
# <h3 class="MsoNormal"
#     style="margin-bottom: 9.6pt; mso-para-margin-bottom: .8gd; line-height: normal; vertical-align: baseline;">
#     <span
#         style="font-family: 'Times New Roman',serif; mso-fareast-font-family: 'Times New Roman';">Software:</span>
# </h3>
# <p><span
#         style="font-family: 'Times New Roman',serif; mso-fareast-font-family: 'Times New Roman';">The
#         software for M.T. Desk consists of the Raspberry Pi Operating System,
#         Python for the programming language, and OpenCV (Open-Source Computer
#         Vision Library) for the programming software. The camera uses the
#         face-tracking algorithm to collect and send data to the Raspberry Pi.
#         It then uses the OpenCV software using Python script to send the
#         signal to the motors, moving the desk accordingly.&nbsp;</span></p>
# <h2>Code Implementation:</h2>
# <p>Imports</p>
import RPi.GPIO as GPIO
import time
import cv2
import drivers

# <p>face detection algorithm Explain overview and add images of how this
#     algorithm works</p>
def detect_features(frame, previous):
    color = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_detection_frame = face_cascade.detectMultiScale(color, 1.05, 4)

    maxArea = 0
    x = 0
    y = 0
    w = 0
    h = 0

# <p>Explain how it Detects X, Y, W, H</p>

    for (_x, _y, _w, _h) in face_detection_frame:
        if _w*_h > maxArea:
            x = _x
            y = _y
            w = _w
            h = _h
            maxArea = w*h
        if maxArea > 0:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

# <p>Explain Output to Motors</p>

    if y == 0:
        y = previous
    
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
    
    previous = y

    return frame, previous

# <p>converts to 480p</p>
def make_480p():
    stream.set(3, 72)
    stream.set(4, 96)

# <p>scales down image by 30%</p>
def rescale(frame, percent=75):
    scale_percent = 20
    width = int(frame.shape[1] * scale_percent / 100)
    height = int(frame.shape[0] * scale_percent / 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)

# <p>Sensor Explanation and get pictures and graph</p>
def sensor():
    GPIO.output(16, False)
    time.sleep(0.000002)
    GPIO.output(16, True)
    time.sleep(0.00001)
    GPIO.output(16, False)

    while GPIO.input(18) == 0:
        pulse_start = time.time()
    while GPIO.input(18) == 1:
        pulse_end = time.time()

    # <p>Explain Math</p>

    duration = pulse_end - pulse_start
    distance = duration * 17150
    distance = distance/2.54
    distance = round(distance, 2)
    _string = str(distance)
    display.lcd_display_string("                  ", 1)
    display.lcd_display_string("Distance:" + _string + "in", 1)

# <p>Function for manual input mode: Give pictures of buttons, datasheets, and
#     switches.</p>
def input(count, previous):
    try:
        while True:

            # <p>Button Code</p>
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

            # <p>Switch Code</p>
            if GPIO.input(11) == False:
                display.lcd_clear()
                display.lcd_display_string("Mode: Auto", 2)
                auto(0, previous)
            # <p>Explain Count</p>
            if count == 40000:
                sensor()
                count = 0

            count = count + 1
    # <p>Explain Keyboard Cleanup</p>
    except KeyboardInterrupt:
        GPIO.cleanup()
        stream.release()
        cv2.destroyAllWindows()
        display.lcd_clear()

# <p>Function for Automatic Mode: Same as before, graphs, datasheets, and
#     pictures.</p>
def auto(count, previous)

    try:
        while True:

            # <p>Explain Camera Code</p>
            ret, frame = stream.read()

            if not ret:
                break    

            frame = rescale(frame, percent=5)

            frame, previous = detect_features(frame, previous)

            # <p>Explain LCD</p>
            if GPIO.input(11) == False:
                hey = 5
            
            else:
                display.lcd_clear()
                display.lcd_display_string("Mode:Manual", 2)
                input(0, previous)
            # <p>Explain Count</p>
            if count == 40000:
                sensor()
                count = 0
            
            count = count + 1

    # <p>Keyboard</p>
    except KeyboardInterrupt:
        GPIO.cleanup()
        stream.release()
        cv2.destroyAllWindows()
        display.lcd_clear()

# <p>Main Begins Here along with setting up all Used GPIO Pins</p>
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

# <p>Camera</p>
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

stream = cv2.VideoCapture(0)

if not stream.isOpened():
    exit()

# <p>Function Calls</p>
make_480p()

display = drivers.lcd()
display.lcd_clear()
display.lcd_display_string("Mode: Manual", 2)

initial_coordinates = 25

input(0, initial_cordinates)
