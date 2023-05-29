from pyfirmata import Arduino, util
import time

board = Arduino('COM3')

it = util.Iterator(board)
it.start()

servo = board.get_pin('d:9:s')

while True :
    servo_angle = 0
    for angle in range(180):
        servo_angle = angle
        servo.write(servo_angle)

        time.sleep(0.05)