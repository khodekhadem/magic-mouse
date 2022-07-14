import os

import time
from pynput.keyboard import Key, Controller

from pynput.mouse import Listener
import threading
keyboard = Controller()

ls = ["1"]
def	func1 ():
	def on_click(x , y, button, pressed):
		print(button , pressed)
		ls.append(str(button)+str(pressed))
				

	def on_scroll(x, y, dx, dy):
		#print(dx, dy)
		ls.append(str(dy))

	with Listener(on_scroll=on_scroll,on_click=on_click) as listener:
		listener.join()
	
def func2 ():
	while 1 == 1 :
		time.sleep(0.1)
		last_button = ls[len(ls)-1]
		#print(last_button)
		if last_button == "Button.button8True" :
			keyboard.press(Key.alt)
			while 1==1:
				print("inloot")
				time.sleep(0.08)
				last_button = ls[len(ls)-1]

				if last_button == "Button.button8False":
					keyboard.press(Key.alt)
					keyboard.release(Key.alt)
					break

				elif last_button == "1":

					del ls[len(ls)-1]
					keyboard.press(Key.alt)
					keyboard.press(Key.tab)
					time.sleep(0.1)
					keyboard.release(Key.tab)

				elif last_button == "-1":
					del ls[len(ls)-1]
					keyboard.press(Key.tab)
					time.sleep(0.1)
					keyboard.release(Key.tab)

def func3 () :
	while 1 == 1 :
		time.sleep(0.1)
		last_button = ls[len(ls)-1]
		#print(last_button)
		if last_button == "Button.button9True" :
			while 1==1:
				#print("inloopwile")
				last_button = ls[len(ls)-1]

				if last_button == "Button.button9False":
					break

				elif last_button == "1":
					print("volume up")
					keyboard.press(Key.ctrl)
					keyboard.press(Key.up)
					keyboard.release(Key.up)
					keyboard.release(Key.ctrl)
					del ls[len(ls)-1]
					break

				elif last_button == "-1":
					print("volume down")
					keyboard.press(Key.ctrl)
					keyboard.press(Key.down)
					keyboard.release(Key.down)
					keyboard.release(Key.ctrl)
					del ls[len(ls)-1]
					break
y = threading.Thread(target=func2)
x = threading.Thread(target=func1)
z = threading.Thread(target=func3)
x.start()
y.start()
z.start()
