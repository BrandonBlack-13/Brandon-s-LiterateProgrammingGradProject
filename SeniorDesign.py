# <h1>M.T. Desk</h1>
# <p><img style="display: block; margin-left: auto; margin-right: auto;"
#         src="desk%20schematic.png" alt="" width="622" height="466"></p>
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
# <p class="MsoNormal"
#     style="margin-bottom: 9.6pt; mso-para-margin-bottom: .8gd; line-height: normal; vertical-align: baseline;">
#     <span
#         style="font-family: 'Times New Roman',serif; mso-fareast-font-family: 'Times New Roman';">&nbsp;</span>
# </p>
# <p class="MsoNormal"
#     style="margin-bottom: 9.6pt; mso-para-margin-bottom: .8gd; line-height: normal; vertical-align: baseline;">
#     <span
#         style="font-family: 'Times New Roman',serif; mso-fareast-font-family: 'Times New Roman';"><img
#             style="display: block; margin-left: auto; margin-right: auto;"
#             src="Microcontroller.png" alt="" width="628" height="471"></span>
# </p>
# <p class="MsoNormal"
#     style="margin-bottom: 9.6pt; mso-para-margin-bottom: .8gd; line-height: normal; vertical-align: baseline;">
#     &nbsp;</p>
# <p class="MsoNormal"
#     style="margin-bottom: 9.6pt; mso-para-margin-bottom: .8gd; line-height: normal; vertical-align: baseline;">
#     <span
#         style="font-family: 'Times New Roman',serif; mso-fareast-font-family: 'Times New Roman';"><img
#             style="display: block; margin-left: auto; margin-right: auto;"
#             src="Components.png" alt="" width="720" height="368"><br></span>
# </p>
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
# <p><span
#         style="font-family: 'Times New Roman',serif; mso-fareast-font-family: 'Times New Roman';"><img
#             src="Soft(1).png" alt=""><img
#             style="display: block; margin-left: auto; margin-right: auto;"
#             src="Soft%20(1).png" alt="" width="647" height="485"><img
#             src="Soft.png" alt=""><br></span></p>
# <h2>Code Implementation:</h2>
# <p><span style="text-decoration: underline;"><strong>Imports</strong></span>:
#     To start off, you must import all needed libraries to execute this script.
#     You will need to get the GPIO functions from the RPi <a
#         href="https://medium.com/geekculture/gpio-programming-on-the-raspberry-pi-python-libraries-e12af7e0a812">library</a>
#     in order to communicate with the pins on the raspberry pi. You will need
#     the time in order to calculate distance with the sensors. It comes as a
#     default library in python. You will need to download the OpenCV <a
#         href="https://pypi.org/project/opencv-python/">software</a> in order
#     to use the camera to track the user. And lastly, you will need specific
#     files in this driver <a
#         href="https://www.youtube.com/watch?v=3XLjVChVgec">library</a> to
#     communicate with the lcd screen by using I2C protocols.&nbsp;</p>
import RPi.GPIO as GPIO
import time
import cv2
import drivers

# <p>Definitions: I am defining nine global variables that go along with the 9
#     GPIO pins that I will be using to have the different peripherals
#     communicate with the raspberry pi.&nbsp;</p>
# <p>In place of the physical pin number on the raspberry pi, I will be
#     addressing the specific peripheral instead.</p>
# <p>Below is also a schematic in which I plugged in each peripheral into my
#     raspberry pi. I denoted each wire as well. The switch and both buttons
#     will have two wires as well. One to the GPIO and the other will go to
#     ground.&nbsp;</p>
# <p><img src="Scheme.png" alt="" width="622" height="352"></p>
Up_Button = 15
Down_Button = 13
Mode_Switch = 11
Motor1_Up = 8
Motor1_Down = 10
Motor2_Up = 19
Motor2_Down = 21
Sensor_Trig = 16
Sensor_Echo = 18

# <p><span style="text-decoration: underline;"><strong>Setup GPIO
#             Pins:</strong></span><strong>&nbsp;</strong>Using the schematic
#     below, you can connect all peripherals to the microcontroller. Use the Pin
#     number <strong>NOT&nbsp;</strong>the GPIO number to setup the GPIO. Set
#     the mode to "GPIO.BOARD" to take the pin numbers as where the device is
#     connected. Then use the setup function to set that pin as an input or an
#     output, and if it is a switch or button, you must also define the type of
#     pull-up resistor.&nbsp;</p>
# <p><img style="float: left;" src="GPIOs.png" alt="" width="562" height="362">
# </p>
def initialize_GPIO():
    GPIO.setmode(GPIO.BOARD)

    #Buttons
    GPIO.setup(Up_Button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(Down_Button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    #Switch
    GPIO.setup(Mode_Switch, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    #Motor Controller
    GPIO.setup(Motor1_Down, GPIO.OUT)
    GPIO.setup(Motor1_Up, GPIO.OUT)

    #Sensor
    GPIO.setup(Sensor_Trig, GPIO.OUT)
    GPIO.setup(Sensor_Echo, GPIO.IN)

    #Motor Controller 2
    GPIO.setup(Motor2_Down, GPIO.OUT)
    GPIO.setup(Motor2_Up, GPIO.OUT)


# <p><span style="text-decoration: underline;"><strong>Face Detection
#             Function:</strong></span> I learned how to utilize the OpenCV
#     software from the link <a
#         href="https://www.youtube.com/watch?v=anMzDYSwndE&amp;list=PLlD0XVjVhLaLVZWgJuOBrv4JBsWK99DGV&amp;index=6">here</a>.
#     I learned that OpenCV detects faces by looking for unique features in your
#     face such as eyes, a nose, and mouth. If enough of these features are
#     present, then the software will recognize this part as a face and draw a
#     box around it. The first line of the function uses the "cvtColor" function
#     to convert the color of the image frame to a gray color. This makes the
#     processing time faster and easier on the CPU because it does not have to
#     render different colors. With the second line, we are applying the cascade
#     that is created in the main function at the bottom of this script and
#     using it in the frame given by the camera. The parameter "previous" will
#     be explained in the following sections.&nbsp;</p>
def detect_features(frame, previous):
    color = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_detection_frame = face_cascade.detectMultiScale(color, 1.05, 4)

    maxArea = 0
    x = 0
    y = 0
    w = 0
    h = 0

# <p>This next section defines the exact coordinates of the rectangle. Once
#     again, if you want an entire in-depth explanation of how this works.
#     This&nbsp;<a
#         href="https://www.youtube.com/playlist?list=PLlD0XVjVhLaLVZWgJuOBrv4JBsWK99DGV">link
#     </a>takes you to a playlist of YouTube videos teaching you how to use it.
#     Essentially, for each x, y, width, and height in the frame, we want to
#     find the largest area to make sure the camera is only responding to the
#     face closest to the camera. This way, the desk will not move for someone
#     in the background. Once the largest area has been determined, we draw a
#     square around that area using the coordinates of on the frame, along with
#     the width and height.&nbsp;</p>
# <p><img src="Face.png" alt=""></p>

    for (_x, _y, _w, _h) in face_detection_frame:
        if _w*_h > maxArea:
            x = _x
            y = _y
            w = _w
            h = _h
            maxArea = w*h
        if maxArea > 0:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

# <p>This section of the function takes the data discovered in the previous
#     parts and outputs them to the motors. The value assigned to y represents
#     the pixel in the image. To explain, if the y value of the box is the 10th
#     pixel or less, move the desk up. If it is the 30th pixel or higher, move
#     the desk down. If it does not fit in those constraints, it does not move.
#     These specific values took testing of how much the user should have to
#     move for the desk to follow. The "previous" value comes in handy here. If
#     the camera does not find a face, it automatically assigns the y value with
#     0. This would mean that the desk would move up automatically. This
#     previous value keeps that from happening. If y equals zero, assign y to
#     what previous was from the last function call. Then assign previous to
#     that y at the end no matter the y value.&nbsp;</p>

    if y == 0:
        y = previous
    
    if y < 10:
        GPIO.output(Motor1_Up, True)
        GPIO.output(Motor1_Down, False)
        GPIO.output(Motor2_Up, True)
        GPIO.output(Motor2_Down, False)
    elif y > 30:
        GPIO.output(Motor1_Down, False)
        GPIO.output(Motor1_Up, True)
        GPIO.output(Motor2_Up, False)
        GPIO.output(Motor2_Down, True)
    else:
        GPIO.output(Motor1_Down, False)
        GPIO.output(Motor1_Up, False)
        GPIO.output(Motor2_Up, False)
        GPIO.output(Motor2_Down, False)
    
    previous = y

    return frame, previous

# <p><span style="text-decoration: underline;"><strong>480p
#             function:</strong></span> This function is simple; it takes the
#     frame and converts it to 480p resolution. These parameter values are
#     determined by image settings to reduce the quality to 480p. This is
#     essentially used to make processing faster and easier for the
#     microcontroller.</p>
def make_480p():
    stream.set(3, 72)
    stream.set(4, 96)
    

# <p><span style="text-decoration: underline;"><strong>Rescale
#             function:</strong></span> This function, similar to the one
#     before, is used to speed up the processing of the microcontroller. It
#     takes the overall size of the image and reduces it. It can rescale to any
#     value, but currently it is set to scale the image down to 20% of the
#     original size. Any lower would worsen the accuracy of the face
#     detection.&nbsp;</p>
def rescale(frame, percent=75):
    scale_percent = 20
    width = int(frame.shape[1] * scale_percent / 100)
    height = int(frame.shape[0] * scale_percent / 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)

# <p><span style="text-decoration: underline;"><strong>Sensor
#             Function:</strong></span><span
#         style="text-decoration: underline;">&nbsp;</span> I was able to learn
#     this code from this <a
#         href="https://www.bing.com/videos/search?q=how+to+use+a+distance+sensor+with+a+raspberry+pi&amp;view=detail&amp;mid=10402C61AD26343D1E7110402C61AD26343D1E71&amp;FORM=VIRE">link</a>.
#     Essentially, the sensor uses ultrasonic waves to determine length. It
#     sends these waves out, and depending on the time it takes for the waves to
#     rebound and return, this determines the distance measured. First, we set
#     the trig pin to False to reset it, and then, we set it to True to send out
#     the waves. We then start the timer while waiting for the Echo pin to
#     return true meaning that the waves have echoed back.&nbsp;</p>
# <p><img src="Sensor.png" alt=""></p>
def sensor():
    GPIO.output(Sensor_Trig, False)
    time.sleep(0.000002)
    GPIO.output(Sensor_Trig, True)
    time.sleep(0.00001)
    GPIO.output(Sensor_Trig, False)

    while GPIO.input(Sensor_Echo) == 0:
        pulse_start = time.time()
    while GPIO.input(Sensor_Echo) == 1:
        pulse_end = time.time()

    # <p>You then subtract the end time and start time to get your total
    #     duration, then convert it to height using constant conversion values
    #     that I got from using the equation: Distance = (Speed * Time) / 2 with
    #     speed being the speed of sound which is 17,150 in/s. Lastly, you
    #     display this height to the user.</p>

    duration = pulse_end - pulse_start
    distance = duration * 17150
    distance = distance/2.54
    distance = round(distance, 2)
    _string = str(distance)
    display.lcd_display_string("                  ", 1)
    display.lcd_display_string("Distance:" + _string + "in", 1)

# <p><span style="text-decoration: underline;"><strong>Manual Mode
#             Function:</strong></span> This is one of the two main functions
#     that the microcontroller will use. This one in particular utilizes buttons
#     to move the desk up and down. It loops infinitely until told
#     otherwise.&nbsp;</p>
def input(count, previous):
    try:
        while True:

            # <p>The buttons are simple to understand. If a button is true,
            #     raise or lower the desk depending on which button is
            #     pressed.&nbsp;</p>
            # <p><img src="buttons.png" alt="" width="264" height="260"></p>
            if GPIO.input(Up_Button) == True:
                GPIO.output(Motor1_Up, True)
                GPIO.output(Motor1_Down, False)
                GPIO.output(Motor2_Up, True)
                GPIO.output(Motor2_Down, False)

            elif GPIO.input(Down_Button) == True:
                GPIO.output(Motor1_Up, False)
                GPIO.output(Motor1_Down, True)
                GPIO.output(Motor2_Up, False)
                GPIO.output(Motor2_Down, True)

            else:
                GPIO.output(Motor1_Up, False)
                GPIO.output(Motor1_Down, False)
                GPIO.output(Motor2_Up, False)
                GPIO.output(Motor2_Down, False)

            # <p>The switch is very similar to the buttons. If the switch is
            #     flipped, swap to automatic function and change the lcd display
            #     to show this change.&nbsp;</p>
            if GPIO.input(Mode_Switch) == False:
                display.lcd_clear()
                display.lcd_display_string("Mode: Auto", 2)
                auto(0, previous)
            # <p>I pass in a count variable that is used to determine when to
            #     call the sensor function. If you call the sensor function
            #     every tick, the processor will be stuck doing that instead of
            #     other important jobs. Therefore every 40,000 iterations,
            #     update the desk height and reset the counter. We decided on
            #     40,000 iterations due to lots of testing and deciding what is
            #     a good amount of time that needs to pass before updating the
            #     LCD.&nbsp;</p>
            if count == 40000:
                sensor()
                count = 0

            count = count + 1
    # <p>This except portion is needed to cleanly close parts like the GPIO,
    #     stream, lcd, etc. When the desk turns off, it runs these commands, so
    #     next time the algorithm runs, there will be no issue.&nbsp;</p>
    except KeyboardInterrupt:
        GPIO.cleanup()
        stream.release()
        cv2.destroyAllWindows()
        display.lcd_clear()

# <p><span style="text-decoration: underline;"><strong>Automatic Mode
#             Function:</strong></span> This is the other main function utilized
#     by the desk. This function also loops infinitely. It takes an image and
#     calls the detect_features function to detect the face and calls this
#     function repeatedly until told otherwise.&nbsp;</p>
def auto(count, previous):

    try:
        while True:

            # <p>First, we read from the camera to get our image stored in the
            #     frame variable. Then we call rescale function to reduce the
            #     frame size. Lastly, call the detect_features function to track
            #     the user and respond accordingly.&nbsp;</p>
            ret, frame = stream.read()

            if not ret:
                break    

            frame = rescale(frame, percent=5)

            frame, previous = detect_features(frame, previous)

            # <p>The switch is used the exact same here except it converts to
            #     the manual mode instead.&nbsp;</p>
            if GPIO.input(Mode_Switch) == False:
                hey = 5
            
            else:
                display.lcd_clear()
                display.lcd_display_string("Mode:Manual", 2)
                input(0, previous)
            # <p>Count is also used the same as above to display the desk's
            #     current height.&nbsp;</p>
            if count == 40000:
                sensor()
                count = 0
            
            count = count + 1

    # <p>Keyboard interrupts are needed here as well in case the function closes
    #     while in automatic mode.&nbsp;</p>
    except KeyboardInterrupt:
        GPIO.cleanup()
        stream.release()
        cv2.destroyAllWindows()
        display.lcd_clear()

# <p><span style="text-decoration: underline;"><strong>Main:</strong></span>
#     This is where the program begins and makes the necessary function calls to
#     begin operation.&nbsp;</p>

# <p>Setup GPIO pins using the initialize function created.&nbsp;</p>
initialize_GPIO()

# <p>Define the specific cascade wanted to detect faces. This cascade in
#     particular is best when detecting facing directly at the camera which is
#     the most common orientation for desk users. Then, start the camera stream,
#     so we can take images from the stream in automatic mode.&nbsp;</p>
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

stream = cv2.VideoCapture(0)

if not stream.isOpened():
    exit()

# <p>Make the stream 480p to speed up processor. Then initialize the lcd and
#     display manual mode to start. Start the previous value at 25 which is the
#     default height until told otherwise. Lastly, call the manual mode function
#     to begin normal operation.&nbsp;</p>
make_480p()

display = drivers.lcd()
display.lcd_clear()
display.lcd_display_string("Mode: Manual", 2)

initial_coordinates = 25

input(0, initial_coordinates)
