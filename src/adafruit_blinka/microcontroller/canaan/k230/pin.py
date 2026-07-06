# SPDX-FileCopyrightText: 2021 Melissa LeBlanc-Williams for Adafruit Industries
#
# SPDX-License-Identifier: MIT
"""Canaan K230 Names"""
# from adafruit_blinka.microcontroller.generic_linux.libgpiod_pin import Pin
from gpioc.pin import Pin

# from adafruit_blinka.microcontroller.generic_linux.libgpiod_pin import Pin


IO0 = Pin(0)
IO1 = Pin(1)
IO2 = Pin(2)
IO3 = Pin(3)
IO4 = Pin(4)
IO5 = Pin(5)
IO6 = Pin(6)
IO7 = Pin(7)
IO8 = Pin(8)
IO9 = Pin(9)
IO10 = Pin(10)
IO11 = Pin(11)
IO12 = Pin(12)
IO13 = Pin(13)
IO14 = Pin(14)
IO15 = Pin(15)
IO16 = Pin(16)
IO17 = Pin(17)
IO18 = Pin(18)
IO19 = Pin(19)
IO20 = Pin(20)
IO21 = Pin(21)
IO22 = Pin(22)
IO23 = Pin(23)
IO24 = Pin(24)
IO25 = Pin(25)
IO26 = Pin(26)
IO27 = Pin(27)
IO28 = Pin(28)
IO29 = Pin(29)
IO30 = Pin(30)
IO31 = Pin(31)
IO32 = Pin(32)
IO33 = Pin(33)
IO34 = Pin(34)
IO35 = Pin(35)
IO36 = Pin(36)
IO37 = Pin(37)
IO38 = Pin(38)
IO39 = Pin(39)
IO40 = Pin(40)
IO41 = Pin(41)
IO42 = Pin(42)
IO43 = Pin(43)
IO44 = Pin(44)
IO45 = Pin(45)
IO46 = Pin(46)
IO47 = Pin(47)
IO48 = Pin(48)
IO49 = Pin(49)
IO50 = Pin(50)
IO51 = Pin(51)
IO52 = Pin(52)
IO53 = Pin(53)
IO54 = Pin(54)
IO55 = Pin(55)
IO56 = Pin(56)
IO57 = Pin(57)
IO58 = Pin(58)
IO59 = Pin(59)
IO60 = Pin(60)
IO61 = Pin(61)
IO62 = Pin(62)
IO63 = Pin(63)
IO64 = Pin(64)


TWI2_SCL = IO11
TWI2_SDA = IO12

UART1_TX = IO3
UART1_RX = IO4
UART2_TX = IO11
UART2_RX = IO12
UART3_TX = IO50
UART3_RX = IO51


SPI0_SCLK = IO15
SPI0_MOSI = IO16
SPI0_MISO = IO17
SPI0_CS0 = IO14
SPI0_CS1 = IO61

i2cPorts = ((2, TWI2_SCL, TWI2_SDA),)
# ordered as spiId, sckId, mosiId, misoId
spiPorts = ((0, SPI0_SCLK, SPI0_MOSI, SPI0_MISO),)
# ordered as uartId, txId, rxId
uartPorts = (
    (1, UART1_TX, UART1_RX),
    (2, UART2_TX, UART2_RX),
    (3, UART3_TX, UART3_RX),
)
