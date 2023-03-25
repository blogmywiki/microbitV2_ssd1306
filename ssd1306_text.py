from microbit import Image, i2c, sleep

from ssd1306 import screen, set_pos, ADDR


def add_text(x, y, text, draw=1):
    for i in range(0, min(len(text), 24 - x)): # 24 was 12
        sleep(20)
        for c in range(0, 5):
            col = 0
            for r in range(1, 6):
                p = Image(text[i]).get_pixel(c, r - 1)
                col = col | (1 << r) if (p != 0) else col
#           ind = x * 10 + y * 128 + i * 10 + c * 2 + 1
            ind = x * 5 + y * 128 + i * 5 + c +1
#            print(ind,col)
#            screen[ind], screen[ind + 1] = col, col
            screen[ind] = col
    if draw == 1:
#        set_zoom(0)
        set_pos(x * 5, y)
#        print(x*5)
        ind0 = x * 5 + y * 128 + 1
#        print(ind0,ind)
#       ind0 = x * 10 + y * 128 + 1
        i2c.write(ADDR, b'\x40' + screen[ind0:ind + 1])
