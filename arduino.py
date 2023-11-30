import pyfirmata
import time

board = pyfirmata.ArduinoMega('COM10')

pin_2 = board.get_pin('d:2:p')
pin_3 = board.get_pin('d:3:p')
pin_4 = board.get_pin('d:4:p')
pin_5 = board.get_pin('d:5:p')
pin_6 = board.get_pin('d:6:p')
pin_7 = board.get_pin('d:7:p')

pin_8 = board.get_pin('d:8:p')
pin_9 = board.get_pin('d:9:p')
pin_10 = board.get_pin('d:10:p')
pin_11 = board.get_pin('d:11:p')
pin_12 = board.get_pin('d:12:p')
pin_13 = board.get_pin('d:13:p')
def forward():
    pin_2.write(0.5)
    pin_7.write(0.5)

    pin_3.write(0.5)
    pin_4.write(0)

    pin_5.write(0.5)
    pin_6.write(0)


def stop():
    pin_2.write(0)
    pin_7.write(0)

    pin_3.write(0)
    pin_4.write(0)
    pin_5.write(0)
    pin_6.write(0)


def right():
    pin_2.write(1)
    pin_7.write(0.5)

    pin_3.write(0)
    pin_4.write(0.5)
    pin_5.write(0.5)
    pin_6.write(0)

def left():
    pin_2.write(0.5)
    pin_7.write(0.5)

    pin_3.write(0.5)
    pin_4.write(0)
    pin_5.write(0)
    pin_6.write(0.5)

def backward():
    pin_2.write(0.5)
    pin_7.write(1)

    pin_3.write(0)
    pin_4.write(0.5)
    pin_5.write(0)
    pin_6.write(0.5)



# while True:
#     pin_6.write(0)
#     pin_7.write(1)
#     pin_5.write(0.5)
#
#     time.sleep(2)
#     pin_6.write(0)
#     pin_7.write(0)
#
#     time.sleep(2)
#     pin_6.write(0.5)
#     pin_7.write(0)
#     pin_5.write(0.5)
#
#     time.sleep(2)
