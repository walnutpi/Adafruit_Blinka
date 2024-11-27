# SPDX-FileCopyrightText: 2021 Melissa LeBlanc-Williams for Adafruit Industries
#
# SPDX-License-Identifier: MIT
"""Allwinner T527 Pin Names"""
# from adafruit_blinka.microcontroller.generic_linux.libgpiod_pin import Pin
from gpioc.pin import Pin

# from adafruit_blinka.microcontroller.generic_linux.libgpiod_pin import Pin

__chip_num = 1
__chip_num_r = 0
with open("/sys/class/gpio/gpiochip0/label", "r") as f:
    label = f.read().strip()
    if label == "2000000.pinctrl":
        __chip_num = 0
        __chip_num_r = 1

PB0 = Pin((__chip_num, 32))
PB1 = Pin((__chip_num, 33))
PB2 = Pin((__chip_num, 34))
PB3 = Pin((__chip_num, 35))
PB4 = Pin((__chip_num, 36))
PB5 = Pin((__chip_num, 37))
PB6 = Pin((__chip_num, 38))
PB7 = Pin((__chip_num, 39))
PB8 = Pin((__chip_num, 40))
PB9 = Pin((__chip_num, 41))
PB10 = Pin((__chip_num, 42))
PB11 = Pin((__chip_num, 43))
PB12 = Pin((__chip_num, 44))
PB13 = Pin((__chip_num, 45))
PB14 = Pin((__chip_num, 46))

PC0 = Pin((__chip_num, 64))
PC1 = Pin((__chip_num, 65))
PC2 = Pin((__chip_num, 66))
PC3 = Pin((__chip_num, 67))
PC4 = Pin((__chip_num, 68))
PC5 = Pin((__chip_num, 69))
PC6 = Pin((__chip_num, 70))
PC7 = Pin((__chip_num, 71))
PC8 = Pin((__chip_num, 72))
PC9 = Pin((__chip_num, 73))
PC10 = Pin((__chip_num, 74))
PC11 = Pin((__chip_num, 75))
PC12 = Pin((__chip_num, 76))
PC13 = Pin((__chip_num, 77))
PC14 = Pin((__chip_num, 78))
PC15 = Pin((__chip_num, 79))

PF0 = Pin((__chip_num, 160))
PF1 = Pin((__chip_num, 161))
PF2 = Pin((__chip_num, 162))
PF3 = Pin((__chip_num, 163))
PF4 = Pin((__chip_num, 164))
PF5 = Pin((__chip_num, 165))
PF6 = Pin((__chip_num, 166))

PG0 = Pin((__chip_num, 192))
PG1 = Pin((__chip_num, 193))
PG2 = Pin((__chip_num, 194))
PG3 = Pin((__chip_num, 195))
PG4 = Pin((__chip_num, 196))
PG5 = Pin((__chip_num, 197))
PG6 = Pin((__chip_num, 198))
PG7 = Pin((__chip_num, 199))
PG8 = Pin((__chip_num, 200))
PG9 = Pin((__chip_num, 201))
PG10 = Pin((__chip_num, 202))
PG11 = Pin((__chip_num, 203))
PG12 = Pin((__chip_num, 204))
PG13 = Pin((__chip_num, 205))
PG14 = Pin((__chip_num, 206))
PG15 = Pin((__chip_num, 207))
PG16 = Pin((__chip_num, 208))
PG17 = Pin((__chip_num, 209))
PG18 = Pin((__chip_num, 210))
PG19 = Pin((__chip_num, 211))

PH0 = Pin((__chip_num, 224))
PH1 = Pin((__chip_num, 225))
PH2 = Pin((__chip_num, 226))
PH3 = Pin((__chip_num, 227))
PH4 = Pin((__chip_num, 228))
PH5 = Pin((__chip_num, 229))
PH6 = Pin((__chip_num, 230))
PH7 = Pin((__chip_num, 231))
PH8 = Pin((__chip_num, 232))
PH9 = Pin((__chip_num, 233))
PH10 = Pin((__chip_num, 234))

PI0 = Pin((__chip_num, 256))
PI1 = Pin((__chip_num, 257))
PI2 = Pin((__chip_num, 258))
PI3 = Pin((__chip_num, 259))
PI4 = Pin((__chip_num, 260))
PI5 = Pin((__chip_num, 261))
PI6 = Pin((__chip_num, 262))
PI7 = Pin((__chip_num, 263))
PI8 = Pin((__chip_num, 264))
PI9 = Pin((__chip_num, 265))
PI10 = Pin((__chip_num, 266))
PI11 = Pin((__chip_num, 267))
PI12 = Pin((__chip_num, 268))
PI13 = Pin((__chip_num, 269))
PI14 = Pin((__chip_num, 270))
PI15 = Pin((__chip_num, 271))
PI16 = Pin((__chip_num, 272))

PL0 = Pin((__chip_num_r, 0))
PL1 = Pin((__chip_num_r, 1))
PL2 = Pin((__chip_num_r, 2))
PL3 = Pin((__chip_num_r, 3))
PL4 = Pin((__chip_num_r, 4))
PL5 = Pin((__chip_num_r, 5))
PL6 = Pin((__chip_num_r, 6))
PL7 = Pin((__chip_num_r, 7))
PL8 = Pin((__chip_num_r, 8))
PL9 = Pin((__chip_num_r, 9))
PL10 = Pin((__chip_num_r, 10))
PL11 = Pin((__chip_num_r, 11))
PL12 = Pin((__chip_num_r, 12))
PL13 = Pin((__chip_num_r, 13))


TWI1_SCL = PB4
TWI1_SDA = PB5
TWI2_SCL = PI15
TWI2_SDA = PI16

UART2_TX = PB0
UART2_RX = PB1


SPI1_SCLK = PH6
SPI1_MOSI = PH7
SPI1_MISO = PH8
SPI1_CS0 = PH5
SPI1_CS1 = PH9

i2cPorts = (
    (1, TWI1_SCL, TWI1_SDA),
    (2, TWI2_SCL, TWI2_SDA),
)
# ordered as spiId, sckId, mosiId, misoId
spiPorts = ((1, SPI1_SCLK, SPI1_MOSI, SPI1_MISO),)
# ordered as uartId, txId, rxId
uartPorts = ((2, UART2_TX, UART2_RX),)
