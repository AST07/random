from tkinter import *
from tkinter.ttk import Button
from threading import Thread
import ctypes

class Timer:
	def __init__(self,time):
		self.time_toplevel=Toplevel(root)
		self.tb='lawn green'
		self.time_toplevel.attributes('-topmost',True)
		self.time_toplevel.overrideredirect(True)
		self.time_toplevel.wm_attributes('-transparentcolor',self.tb)
		self.label=Label(self.time_toplevel,font=('',14),fg='cyan',bg=self.tb)
		self.label.pack()
		self.time_toplevel.withdraw()
		self.time=time
		self.stop=False
		self.hour=time[0]
		self.minute=time[1]
		self.second=time[2]
		self.template=f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'
		self.label.config(text=self.template)

	def _timer(self):
		if self.template!='00:00:00' and not self.stop:
			if self.second==0:
				self.second=60
				self.minute-=1
			if self.minute==00 and self.hour!=0:
				self.hour-=1
			self.second-=1
			self.template=f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'
			self.label.config(text=self.template)
			self.time_toplevel.update()
			self.time_toplevel.after(1000,self._timer)
		else:
			self.time_toplevel.destroy()
	def start(self):
		self.time_toplevel.deiconify()
		self.time_toplevel.update()
		self.time_toplevel.after(1000)
		self._timer()

	def end(self):
		self.stop=True
		self.time_toplevel.destroy()

def on_close():
	try:
		timer.end()
	except:
		pass
	root.destroy()

def launch():
	global timer
	try:
		timer=Timer([var.get() for var in var_list])
		timer.start()
	except:
		for var in var_list:
			var.set(0)

if __name__=='__main__':
	ctypes.windll.shcore.SetProcessDpiAwareness(1)
	root=Tk()
	root.title('Timer')
	root.resizable(False,False)
	root.config(bg='RoyalBlue')
	root.protocol('WM_DELETE_WINDOW',on_close)
	cyprt_label=Label(root,text='Copyright © 2020 Aditya Singh Tejas',bg='grey35',fg='white')
	cyprt_label.pack(side=BOTTOM,fill='x')
	button_frame=Frame(root,bg='white')
	button_frame.pack(side=BOTTOM,ipady=10,fill='both')
	hour=IntVar()
	hour_entry=Entry(root,font=('',32),width=2,bd=10,relief='flat',textvariable=hour)
	hour_entry.pack(side='left',padx=10,pady=10)
	minute=IntVar()
	min_entry=Entry(root,font=('',32),width=2,bd=10,relief='flat',textvariable=minute)
	min_entry.pack(side='left',padx=(0,10),pady=10)
	second=IntVar()
	sec_entry=Entry(root,font=('',32),width=2,bd=10,relief='flat',textvariable=second)
	sec_entry.pack(side='left',padx=(0,10),pady=10)
	var_list=[hour,minute,second]
	start_button=Button(button_frame,text='Start',command=lambda:launch())
	start_button.pack(side='right',padx=10)
	end_button=Button(button_frame,text='Stop',command=lambda:timer.end())
	end_button.pack(side='right',padx=(10,0))
	root.mainloop()