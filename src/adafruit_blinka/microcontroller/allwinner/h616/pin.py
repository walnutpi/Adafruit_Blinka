# SPDX-FileCopyrightText: 2021 Melissa LeBlanc-Williams for Adafruit Industries
#
# SPDX-License-Identifier: MIT
"""Allwinner H616 Pin Names"""
# from adafruit_blinka.microcontroller.generic_linux.libgpiod_pin import Pin
from aw.gpio.H616 import Pin

PC0 = Pin((0, 64))
SPI0_SCLK = PC0
PC1 = Pin((0, 65))
PC2 = Pin((0, 66))
SPI0_MOSI = PC2
PC3 = Pin((0, 67))
SPI0_CS0 = PC3
PC4 = Pin((0, 68))
SPI0_MISO = PC4
PC5 = Pin((0, 69))
PC6 = Pin((0, 70))
PC7 = Pin((0, 71))
PC8 = Pin((0, 72))
PC9 = Pin((0, 73))
PC10 = Pin((0, 74))
PC11 = Pin((0, 75))
PC12 = Pin((0, 76))
PC13 = Pin((0, 77))
PC14 = Pin((0, 78))
PC15 = Pin((0, 79))

PF0 = Pin((0, 160))
PF1 = Pin((0, 161))
PF2 = Pin((0, 162))
PF3 = Pin((0, 163))
PF4 = Pin((0, 164))
PF5 = Pin((0, 165))
PF6 = Pin((0, 166))

PG0 = Pin((0, 192))
PG1 = Pin((0, 193))
PG2 = Pin((0, 194))
PG3 = Pin((0, 195))
PG4 = Pin((0, 196))
PG5 = Pin((0, 197))
PG6 = Pin((0, 198))
PG7 = Pin((0, 199))
PG8 = Pin((0, 200))
PG9 = Pin((0, 201))
PG10 = Pin((0, 202))
PG11 = Pin((0, 203))
PG12 = Pin((0, 204))
PG13 = Pin((0, 205))
PG14 = Pin((0, 206))
PG15 = Pin((0, 207))
PG16 = Pin((0, 208))
PG17 = Pin((0, 209))
PG18 = Pin((0, 210))
PG19 = Pin((0, 211))

PH0 = Pin((0, 224))
PH1 = Pin((0, 225))
PH2 = Pin((0, 226))
UART5_TX = PH2
PH3 = Pin((0, 227))
UART5_RX = PH3
PH4 = Pin((0, 228))
TWI3_SCL = PH4
PH5 = Pin((0, 229))
UART2_TX = PH5
TWI3_SDA = PH5
SPI1_CS0 = PH5
PH6 = Pin((0, 230))
UART2_RX = PH6
SPI1_SCLK = PH6
PH7 = Pin((0, 231))
SPI1_MOSI = PH7
PH8 = Pin((0, 232))
SPI1_MISO = PH8
PH9 = Pin((0, 233))
SPI1_CS1 = PH9
PH10 = Pin((0, 234))

PI0 = Pin((0, 256))
PI1 = Pin((0, 257))
PI2 = Pin((0, 258))
PI3 = Pin((0, 259))
PI4 = Pin((0, 260))
PI5 = Pin((0, 261))
PI6 = Pin((0, 262))
PI7 = Pin((0, 263))
TWI1_SCL = PI7
PI8 = Pin((0, 264))
TWI1_SDA = PI8
PI9 = Pin((0, 265))
TWI2_SCL = PI9
PI10 = Pin((0, 266))
TWI2_SDA = PI10
PI11 = Pin((0, 267))
PI12 = Pin((0, 268))
PI13 = Pin((0, 269))
UART4_TX = PI13
PI14 = Pin((0, 270))
UART4_RX = PI14
PI15 = Pin((0, 271))
PI16 = Pin((0, 272))

i2cPorts = (
    (1, TWI1_SCL, TWI1_SDA),
    (2, TWI2_SCL, TWI2_SDA),
    (3, TWI3_SCL, TWI3_SDA),
)
# ordered as spiId, sckId, mosiId, misoId
spiPorts = (
    (0, SPI0_SCLK, SPI0_MOSI, SPI0_MISO),
    (1, SPI1_SCLK, SPI1_MOSI, SPI1_MISO),
)
# ordered as uartId, txId, rxId
uartPorts = (
    (2, UART2_TX, UART2_RX),
    (4, UART4_TX, UART4_RX),
    (5, UART5_TX, UART5_RX),
)
