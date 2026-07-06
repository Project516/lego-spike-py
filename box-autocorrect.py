from hub import light_matrix
from hub import port
import motor_pair
import runloop
import color_sensor
import color

#start_time = 0

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

#def stopClock(on):
#    time = 0
#    while(on):
#        runloop.sleep_ms(1000)
#        time = time + 1

async def main():
    # write your code here
    # await light_matrix.write("Hi!")

    motor_pair.pair(motor_pair.PAIR_1, port.C, port.D)
    #global time

    while (True):
        if (getColor(port.B) == "Blue" or getColor(port.B) == "Azure" or getColor(port.B) == "Turquoise"):

            motor_pair.move(motor_pair.PAIR_1, 0)


        else:
            #elapsed_time = stopClock(on = 1)

            #if elapsed_time < 5:
                motor_pair.move(motor_pair.PAIR_1, -100)
            #else:
            #    motor_pair.move(motor_pair.PAIR_1, 100)
            #stopClock(on = 0)

runloop.run(main())
