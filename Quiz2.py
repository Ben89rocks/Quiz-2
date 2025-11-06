from gpiozero import Button, LED
from time import sleep

#creates the variables that the code will pull from.
red_button = Button(25)
green_button = Button(24)
blue_button= Button(23)
red_led = LED(16)
green_led = LED(20)
blue_led = LED(21)

print("Please push a button to control the LED")

def main():
    #if statement for red button
    if red_button.is_pressed:
        print("Red is pressed")
        red_led.on()
    else:
        red_led.off()
    #if statement for blue button
    if blue_button.is_pressed:
        print("Blue is pressed")
        blue_led.on()
    else:
        blue_led.off()
    #if statement for green button
    if green_button.is_pressed:
        print("green is pressed")
        green_led.on()
    else:
        green_led.off()
        sleep(0.1)
    
while True:
    main()
        
    