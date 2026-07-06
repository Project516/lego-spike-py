from hub import light_matrix
from hub import port
import motor_pair
import runloop
import color_sensor
import color

async def main():
    # write your code here
    # await light_matrix.write("Hi!")

    # motor_pair.pair(motor_pair.PAIR_1, port.C, port.D)

    color_sensor.reflection(port.B)
    while (True):
        print(getColor(port.B))
        runloop.sleep_ms(1000)


# color get function
def getColor(port):
    if color_sensor.color(port) == 0:
        return "Black"
    if color_sensor.color(port) == 1:
        return "Magenta"
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
        

runloop.run(main())
