# a simple tkinter app ased on a video tutorial by @NeuralNine
# import the tkinter package under alias TK
import tkinter as tk
# import time functions for calculating speed of typing
import time
# import threading from os functionality for runtime execution
import threading
# import the random package from maths in order to undertake mathematical derivation
import random

# ///////COMPILATION \\\\\\\\\\\
# class containing compilation of the app's gui
class TypeSpeedGUI 
	# recursive constructor method -refering to self as an instantiator of an object instance of the TypeSpeedGUI class
	def  __init__(self):
	# /// GUI BOX \\\\
		# assign to self.gui an instance of the tkinter gui 					
		# constructor - i.e. tk()
		self.gui = tk.Tk()
		# set the title of the GUI
		self.gui.title = 'Typing Speed Tester'
		# set the pixel heightxwidth: 
		self.gui.geometry = '800x600'
		self.frame = tk.frame(self.gui)
	# /// TEXT LOADING AND OUTPUT \\\\	
		#load up the sample text from text file: 
		open (filename, readbytes modifier r).read().spl
		#it('\n') -i.e. at each new line separate these se
		# ntences so they become like elements of an array. 
		# They then will be jumbled up using Math.random.c
		# hoice()
		self.sample = open('sample.txt', 'r').read().split('\n') 
		# create a label that will spit out the randomly jumbled up text that was previously read into main memory:
		self.sample_lbl = tk.Label(self.frame, font=('Helvetica', 18) text=random.choice(self.sample))
		# grid layout of the label - no rows or columns, padding both sides.
		self.sample_lbl.grid(row=0, column=0, columnspan=2, padx=5, pady=10)
	# /// KEYBOARD INPUT LISTENER \\\\
		self.key_entry = tk.Entry(self.frame, width=40, font=('Helvetica', 20))
		self.key_entry.grid(row=1, column=0, columnspan=2, padx=5, pady=10)
		# bind a keydown event listener to trigger the beg
		# beginning of the timer:
		self.key_entry.bind("<KeyPress>", self.startCount)
	# /// SPEED INDICATOR \\\\	
		self.speed_lbl = tk.Label(self.frame, font=('Helvetica', 18) text='Speed : \n 0.00 Chars Per Sec \n 0.00 Chars Per Min')
		self.speed_lbl.grid(row=2, column=0, columnspan=2, padx=5, pady=10)
	# /// RESET BUTTON \\\\
		self.reset_btn = tk.Button(self.frame, font=('Helvetica', 18) text='Reset' command=self.reset)
		self.reset_btn.grid(row=3, column=0, columnspan=2, padx=5, pady=10)
	# //// PACKUP GUI FRAME\\\\
		self.frame.pack(expand=True)	
	# //// DEF'D FUNCTIONS \\\\
		#Prepare vars to be called in the widgets above
		counter=0 # char counterset at init position
		running=False #count hasn't started yet by default
		#start func. pass event as arg2 as the event listener.
		def startCount(self, event):
		# if not currently running the thread...
			if not self.running:
			# if user has not entered keys 16(shift) 17(ctrl), 18(alt) then turn the thread on 
				if not event.keycode in [16,17,18]:
					self.running = True
			# set and sart and instance of the timer function
					t = threading.Thread(target=self.timeThread)
					t.start()
	# if the users input as gotten(via get()) does not startwith() the text served up in the sample_lbl widget (fetched using cget- which is a c function implemented in the tkinter package) then...				
			if not self.sample_lbl.cget('text').startswith(self.key_entry.get()):
			# then make the entered text red to indicated a mistake
				self.key_entry.config(fg='red')
			else:
			# otherwise text stays black
				self.key_entry.config(fg='black')
			# second if... if the fetched text entered into key_entry widget by user matches the text cget'd from sample text widget (-1 array pos due to addition of an extra whitespace by cget upon its execution) then: 
			if self.key_entry.get() == self.sample_lbl.cget('text')[:-1]:
			# stop the thread
			self.running = False
			#make text green to indicate success 
			self.key_entry.config(fg='green')
		pass
		#timer funct
		def timeThread(self):
		# while a thread is running
			while self.running:
			#start with a microsecond advance on timer
				time.sleep(0.1)
			# add a microsecond value for length of process to the counter variable
				self.counter += 0.1
			#characters per second = length of the enter text as it is fetched divided by the counter variable's value
				cps = len(self.key_entry.get()) / self.counter 
			# chars per minut
				cpm = cps*60
			# update the widge's label by using f string configuration of the text being presented. pass the variables but only up to 2 decimal points (.2f)	
				self.speed_lbl.config(text=f'Speed : \n {cps:.2f} Chars Per Sec \n {cpm:.2f} Chars Per Min')						
		pass	
		#reset func
		def reset(self):
		# reset the thread counter and widget text to 0
			self.running = False
			self.counter = 0
			self.speed_lbl.config(text='Speed : \n 0.00 Chars Per Sec \n 0.00 Chars Per Min'))
			#throw up another random part of the text
			self.sample.config(text=random.choice(self.sample))
			# delete what user has written into the box so far
			self.key_entry.delete(0, tk.END)
		pass	 
		#
	# //// RUNTIME \\\\
		self.gui.mainloop()
	
