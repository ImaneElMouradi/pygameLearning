import turtle as t
import time

t.color("red")
t.begin_fill()

counter = 0

while counter < 4:
	t.forward(100)
	t.left(90)
	counter += 1

t.end_fill()
time.sleep(5)

