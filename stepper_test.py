import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
coil_A_1_pin = 4  # pink
coil_A_2_pin = 17  # orange
coil_B_1_pin = 23  # blue
coil_B_2_pin = 24  # yellow

# adjust if different
steps_in_1_degree = 512.0 / 360
StepCount = 8
Seq = range(0, StepCount)
Seq[0] = [1,0,0,0]
Seq[1] = [1,1,0,0]
Seq[2] = [0,1,0,0]
Seq[3] = [0,1,1,0]
Seq[4] = [0,0,1,0]
Seq[5] = [0,0,1,1]
Seq[6] = [0,0,0,1]
Seq[7] = [1,0,0,1]

GPIO.setup(coil_A_1_pin, GPIO.OUT)
GPIO.setup(coil_A_2_pin, GPIO.OUT)
GPIO.setup(coil_B_1_pin, GPIO.OUT)
GPIO.setup(coil_B_2_pin, GPIO.OUT)


def setStep(a):
    GPIO.output(coil_A_1_pin, a[0])
    GPIO.output(coil_A_2_pin, a[1])
    GPIO.output(coil_B_1_pin, a[2])
    GPIO.output(coil_B_2_pin, a[3])


def forward(delay, steps):
    for i in range(steps):
        for j in range(StepCount):
            setStep(Seq[j])
            time.sleep(delay)


def backwards(delay, steps):
    for i in range(steps):
        for j in reversed(range(StepCount)):
            setStep(Seq[j])
            time.sleep(delay)

def rotateCW(degrees):
    steps = int(round(degrees * steps_in_1_degree, 0))
    forward(0.001, steps)


def rotateCCW(degrees):
    steps = int(round(degrees * steps_in_1_degree, 0))
    backwards(0.001, steps)

if __name__ == '__main__':
    while True:
        # delay = raw_input("Time Delay (ms)?")
        # steps = raw_input("How many steps forward? ")
        # forward(int(delay) / 1000.0, int(steps))
        # steps = raw_input("How many steps backwards? ")
        # backwards(int(delay) / 1000.0, int(steps))
        degrees = int(raw_input("How many degreees clockwise? "))
        rotateCW(degrees)
        degrees = int(raw_input("How many degreees counter-clockwise? "))
        rotateCCW(degrees)
