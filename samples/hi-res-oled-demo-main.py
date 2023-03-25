from microbit import *
from ssd1306 import initialize, clear_oled, draw_screen
from ssd1306_text import add_text
from ssd1306_px import set_px
from ssd1306_bitmap import show_bitmap

initialize()

clear_oled()

set_px(127,63,1) 

sleep(9000)

while True:
    clear_oled()

    # add_text(1, 1, "222")
    add_text(0, 0, "01234567890")
    add_text(1, 1, "1")
    add_text(2, 2, "2")
    add_text(3, 3, "3")
    add_text(4, 4, "4")
    add_text(5, 5, "5")
    add_text(6, 6, "6")
    add_text(7, 7, "temp = "+str(temperature())+"C")

    sleep(3000)
    
    y = 63
    for x in range(127):
        set_px(x,int(y),1)
        y = y - 0.5
    
    sleep(3000)
    
    show_bitmap("xfiles2")
    
    sleep(3000)
    
    clear_oled()
    
    add_text(0, 0, "The truth is out there")

    sleep(3000)

