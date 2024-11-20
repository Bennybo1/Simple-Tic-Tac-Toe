from tkinter import *
import random
import time

turn = 1

window = Tk()
#restarting the game function
def restart():
	print("restart")
	button1.config(bg='#e8e8e8', state=NORMAL, text='')
	button2.config(bg='#e8e8e8', state=NORMAL, text='')
	button3.config(bg='#e8e8e8', state=NORMAL, text='')
	button4.config(bg='#e8e8e8', state=NORMAL, text='')
	button5.config(bg='#e8e8e8', state=NORMAL, text='')
	button6.config(bg='#e8e8e8', state=NORMAL, text='')
	button7.config(bg='#e8e8e8', state=NORMAL, text='')
	button8.config(bg='#e8e8e8', state=NORMAL, text='')
	button9.config(bg='#e8e8e8', state=NORMAL, text='')
	
	if turn == 1:
		player.config(text='Xs is starting')
	else:
		player.config(text='Os is starting')


#chaning colors and detecting clicks
def alternate(button_id):
	global turn
	print(f"Button {button_id} was clicked")
	if turn == 1:
		buttons[button_id].config(text='X', state=DISABLED, bg='#831700')
		turn -= 1
		player.config(text='It is Os turn.', font=('roboto', 15))
		print(f"just placed X. Turn is now {turn}")
	else: 
		if turn == 0:
			buttons[button_id].config(text='O', state=DISABLED, bg='#066d89',)
			turn += 1
			player.config(text='It is Xs turn.', font=('roboto', 15))
			print(f"just placed O. Turn is now {turn}")

#window statistics
window.geometry("600x550")
window.resizable(False,False)
window.title('TIC-TAC-TOE')
icon = PhotoImage(file='C:\\Users\\benne\\OneDrive\\Pictures\\Saved Pictures\\settings.png')
window.iconphoto(True, icon)

#LABELS
header = Label(window, text="TIC-TAC-TOE", font=('roboto',40))
header.pack()
random = random.randint(0,1)
if random == 1:
	player = Label(window, text='Xs is starting', font=('roboto', 15))
	print('X will start')
else:
	player = Label(window, text='Os is starting', font=('roboto', 15))
	print('O will start')
player.pack()

#BUTTONS

restart_button = Button(window, text="Restart", command=restart,font=('roboto'), bg='#bd5a5a')
restart_button.place(x=255, y=507)

button1 = Button(window,text='', width=12, height=6, bg='#e8e8e8',command=lambda: alternate(1))
button1.place(x=100, y=100)

button2 = Button(window,text='', width=12, height=6, bg='#e8e8e8',command=lambda: alternate(2))
button2.place(x=250, y=100)

button3 = Button(window,text='', width=12, height=6, bg='#e8e8e8',command=lambda: alternate(3))
button3.place(x=400, y=100)

button4 = Button(window,text='', width=12, height=6, bg='#e8e8e8',command=lambda: alternate(4))
button4.place(x=100, y=250)

button5 = Button(window,text='', width=12, height=6, bg='#e8e8e8',command=lambda: alternate(5))
button5.place(x=250, y=250)

button6 = Button(window,text='', width=12, height=6, bg='#e8e8e8',command=lambda: alternate(6))
button6.place(x=400, y=250)

button7 = Button(window,text='', width=12, height=6, bg='#e8e8e8',command=lambda: alternate(7))
button7.place(x=100, y=400)

button8 = Button(window,text='', width=12, height=6, bg='#e8e8e8',command=lambda: alternate(8))
button8.place(x=250, y=400)

button9 = Button(window,text='', width=12, height=6, bg='#e8e8e8',command=lambda: alternate(9))
button9.place(x=400, y=400)

buttons = {1: button1, 2: button2, 3: button3, 4: button4, 5: button5, 6: button6,7: button7, 8: button8, 9: button9}

window.mainloop()