from gpiozero import Button
from signal import pause

# Corresponds to GPIO
button = Button(4)
joystick = Button(17)

counter = 0

def button_pressed():
    print("Button was pressed.")
    

def button_held():
    global counter
    counter += 1
    if counter == 3:
        counter = 0
    print(f"Button was held. State is now {counter}.")

def button_released():
    print("Button was released")

button.when_pressed = button_pressed
button.when_held = button_held
button.when_released = button_released


def joystick_pressed():
    print("Joystick was moved up.")
    

def joystick_held():
    global counter
    print(f"Joystick was held up. State is {counter}.")

def joystick_released():
    print("Joystick was brought back down.")

# when lever on/off set lever appropriately
# when use joystick, print state and lever position

joystick.when_pressed = joystick_pressed
joystick.when_held = joystick_held
joystick.when_released = joystick_released

pause()