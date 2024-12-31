import RPi.GPIO as GPIO
import time

# Set up GPIO mode
GPIO.setmode(GPIO.BCM)

# Set up GPIO pin 17 as output for PWM signal
GPIO.setup(17, GPIO.OUT)

# Set up PWM (Pulse Width Modulation) on GPIO 17 with a frequency of 50Hz
pwm = GPIO.PWM(17, 50)  # 50Hz for servo motor control
pwm.start(0)  # Start with 0% duty cycle

# Function to set the angle of the servo motor (0 to 180 degrees)
def set_angle(angle):
    duty = (angle / 18) + 2  # Convert angle to duty cycle (0-180 degrees to PWM)
    GPIO.output(17, True)  # Start PWM signal
    pwm.ChangeDutyCycle(duty)  # Set the PWM duty cycle
    time.sleep(1)  # Wait for the servo to reach the position
    GPIO.output(17, False)  # Stop PWM signal
    pwm.ChangeDutyCycle(0)  # Stop PWM

# Example: Move the servo to 90 degrees
set_angle(90)
time.sleep(2)

# Clean up GPIO setup
pwm.stop()  # Stop PWM signal
GPIO.cleanup()  # Clean up GPIO settings