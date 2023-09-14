# SPDX-FileCopyrightText: 2023 Xenokrates
#
# SPDX-License-Identifier: MIT
"""Allwinner A20 pin names"""
from adafruit_blinka.microcontroller.generic_linux.libgpiod_pin import Pin

# Pin descriptions at https://linux-sunxi.org/A20/PIO

PA0 = Pin(0)
PA1 = Pin(1)
PA2 = Pin(2)
UART2_TX = PA2
PA3 = Pin(3)
UART2_RX = PA3
PA6 = Pin(6)
PA7 = Pin(7)
PA8 = Pin(8)
PA9 = Pin(9)
PA10 = Pin(10)
UART1_TX = PA10
PA11 = Pin(11)
UART1_RX = PA11
PA12 = Pin(12)
PA13 = Pin(13)
PA14 = Pin(14)
PA15 = Pin(15)
PA16 = Pin(16)
PA17 = Pin(17)

PB0 = Pin(32)
TWI0_SCK = PB0
PB1 = Pin(33)
TWI0_SDA = PB1
PB2 = Pin(34)
PB3 = Pin(35)
IR0_TX = PB3
PB4 = Pin(36)
IR0_RX = PB4
PB5 = Pin(37)
PB6 = Pin(38)
PB7 = Pin(39)
PB8 = Pin(40)
PB12 = Pin(44)
PB13 = Pin(45)
PB18 = Pin(50)
TWI1_SCK = PB18
PB19 = Pin(51)
TWI1_SDA = PB19
PB20 = Pin(52)
TWI2_SCK = PB20
PB21 = Pin(53)
TWI2_SDA = PB21
PB22 = Pin(54)
UART0_TX = PB22
PB23 = Pin(55)
UART0_RX = PB23

PG2 = Pin(194)

PH2 = Pin(226)
PH4 = Pin(228)
UART4_TX = PH4
PH5 = Pin(229)
UART4_RX = PH5
PH20 = Pin(244)
CAN_TX = PH20
PH21 = Pin(245)
CAN_RX = PH21
PH24 = Pin(248)

PI0 = Pin(256)
TWI3_SCK = PI0
PI1 = Pin(257)
TWI3_SDA = PI1
PI3 = Pin(259)
PWM1 = PI3
PI10 = Pin(266)
SPI0_CS0 = PI10
PI11 = Pin(267)
SPI0_SCLK = PI11
PI12 = Pin(268)
SPI0_MOSI = PI12
PI13 = Pin(269)
SPI0_MISO = PI13
PI14 = Pin(270)
SPI0_CS1 = PI14
PI16 = Pin(272)
UART2_RTS = PI16
PI17 = Pin(273)
UART2_CTS = PI17
PI18 = Pin(274)
UART2_TX = PI18
PI19 = Pin(275)
UART2_RX = PI19
PI20 = Pin(276)
UART7_TX = PI20
PI21 = Pin(277)
UART7_RX = PI21

# SysFS pwm outputs, pwm channel and pin in first tuple
pwmOuts = (((0, 1), PWM1),)
# ordered as i2cId, sclId, sdaId
i2cPorts = (
    (0, TWI0_SCK, TWI0_SDA),
    (1, TWI1_SCK, TWI1_SDA),
    (2, TWI2_SCK, TWI2_SDA),
)
# ordered as spiId, sckId, mosiId, misoId
spiPorts = ((0, SPI0_SCLK, SPI0_MOSI, SPI0_MISO),)
# ordered as uartId, txId, rxId
uartPorts = (
    (0, UART0_TX, UART0_RX),
    (2, UART2_TX, UART2_RX),
    (4, UART4_TX, UART4_RX),
    (7, UART7_TX, UART7_RX),
)
