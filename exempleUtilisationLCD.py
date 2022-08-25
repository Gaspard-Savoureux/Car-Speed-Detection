from time import sleep
import I2C_LCD_driver

mylcd = I2C_LCD_driver.lcd()

mylcd.lcd_display_string("Miam", 1, 3)

sleep(3)

mylcd.lcd_clear()



