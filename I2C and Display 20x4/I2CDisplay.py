import lcddriver
import datetime
from time import *

mRs = 0b00000001

lcd = lcddriver.lcd()

# Move cursor to line 3 col 5
# lcd.lcd_write(0x94)
# lcd.lcd_write(0x14, mRs)
# lcd.lcd_write(0x61, mRs)

while True:
    lcd.lcd_display_string("BRIGADA 7", 1)
    lcd.lcd_display_string("UNAM", 2)
    lcd.lcd_display_string("PRACTICA 4", 3)
    sleep(1)
