from hub import light_matrix
from hub import port
import motor_pair
import runloop
import color_sensor
import color

# color get function
def getColor(port):
    if color_sensor.color(port) == 0:
        return "Black"
    if color_sensor.color(port) == 1:
        return "Magneta"
    if color_sensor.color(port) == 2:
        return "Purple"
    if color_sensor.color(port) == 3:
        return "Blue"
    if color_sensor.color(port) == 4:
        return "Azure"
    if color_sensor.color(port) == 5:
        return "Turquoise"
    if color_sensor.color(port) == 6:
        return "Green"
    if color_sensor.color(port) == 7:
        return "Yellow"
    if color_sensor.color(port) == 8:
        return "Orange"
    if color_sensor.color(port) == 9:
        return "Red"
    if color_sensor.color(port) == 10:
        return "White"
    if color_sensor.color(port) == -1:
        return "Unknown"

async def main():

    motor_pair.pair(motor_pair.PAIR_1, port.C, port.D)

    while (True):
        if (getColor(port.B) == "Blue" or getColor(port.B) == "Azure" or getColor(port.B) == "Turquoise"):

            motor_pair.move(motor_pair.PAIR_1, 0, velocity=1000, acceleration=1000)
        else:
            motor_pair.move(motor_pair.PAIR_1, -100, velocity=1000, acceleration=1000)

runloop.run(main())
