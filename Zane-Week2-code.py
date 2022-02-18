import board
import time
from digitalio import DigitalInOut, Direction, Pull
import neopixel

# create a neopixel object
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)
pixels.brightness = 0.1
# create a color as a tuple value
ac_red = 0xff0000
pixels[9] = ac_red
ac_blue = 0x0000ff
pixels[0] = ac_blue
ac_green = 0x00ff00
pixels[1] = ac_green

time.sleep(1)

# declare a digitial input
button_a = DigitalInOut(board.BUTTON_A)
button_a.switch_to_input(pull=Pull.DOWN)
button_b = DigitalInOut(board.BUTTON_B)
button_b.switch_to_input(pull=Pull.DOWN)

# A variable to track the LED led state
led_state = True


while True:
    # gather all input values from sensors
    # print the value of our button_a object
    button_a_read = button_a.value
    print("button a read is:", button_a_read)
    button_b_read = button_b.value
    print("button b read is:", button_b_read)

    if button_a_read and button_b_read == True:
        pixels.fill(ac_green)
        
    elif button_a_read == True:
        pixels.fill(ac_red)
        
    elif button_b_read == True:
        pixels.fill(ac_blue)
        
    else:
        led_state = False
        pixels.fill(0)
    time.sleep(0.2)




