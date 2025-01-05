import RPi.GPIO as GPIO
import time

# Suppress warnings and set up GPIO mode
GPIO.setwarnings(False)  # Suppress warnings about GPIO already in use
GPIO.setmode(GPIO.BCM)

# Set up GPIO18 (Pin 12) for PWM signal
GPIO.setup(18, GPIO.OUT)

# Set up PWM on GPIO18 with a frequency of 50Hz
pwm = GPIO.PWM(18, 50)  # 50Hz is standard for servo motors
pwm.start(0)  # Start PWM with 0% duty cycle

# Function to set the angle of the servo motor (0 to 180 degrees)
def set_angle(angle):
    """
    Sets the servo motor to the specified angle (0 to 180 degrees).
    Converts the angle to the appropriate PWM duty cycle.
    """
    duty = (angle / 18) + 2  # Convert angle to duty cycle
    GPIO.output(18, True)
    pwm.ChangeDutyCycle(duty)  # Apply duty cycle
    time.sleep(0.05)  # Short delay for the servo to move
    GPIO.output(18, False)
    pwm.ChangeDutyCycle(0)  # Stop signal to prevent jitter

try:
    # Sweep the servo motor from 0 to 180 degrees
    print("Sweeping from 0 to 180 degrees...")
    for angle in range(0, 181, 1):  # Increment angle by 1 degree
        set_angle(angle)
        time.sleep(0.05)  # Delay for smooth movement

    # Sweep the servo motor back from 180 to 0 degrees
    print("Sweeping back from 180 to 0 degrees...")
    for angle in range(180, -1, -1):  # Decrement angle by 1 degree
        set_angle(angle)
        time.sleep(0.05)

except KeyboardInterrupt:
    # Gracefully handle script interruption
    print("\nScript interrupted by user.")

finally:
    # Cleanup GPIO setup
    print("Cleaning up GPIO...")
    pwm.stop()  # Stop PWM signal
    GPIO.cleanup()  # Reset GPIO settings
    print("Cleanup complete.")
