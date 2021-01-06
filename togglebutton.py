class ToggleButton:
	def __init__(self,parent,width=15,bg='white',fg='black',hbg=False,hfg=False,state=0):
		
		def on_click(event):
			if self.state==0:
				self.switch.pack(padx=(self.width,0))
				self.switch.config(bg=self.hfg)
				self.toggle_frame.config(bg=self.hbg)
				self.state=1
			else:
				self.switch.pack(padx=(0,self.width))
				self.switch.config(bg=self.fg)
				self.toggle_frame.config(bg=self.bg)
				self.state=0

		self.parent=parent
		self.width=width
		self.fg=fg
		self.bg=bg
		if not hbg:
			self.hbg=self.bg
		else:
			self.hbg=hbg
		if not hfg:
			self.hfg=self.fg
		else:
			self.hfg=hfg
		self.state=state
		self.toggle_frame=tk.Frame(self.parent,width=self.width*2,bd=5)
		self.switch=tk.Frame(self.toggle_frame,height=self.width,width=self.width)
		if self.state==0:
			self.switch.pack(padx=(0,self.width))
			self.switch.config(bg=self.fg)
			self.toggle_frame.config(bg=self.bg)
		elif self.state==1:
			self.switch.pack(padx=(self.width,0))
			self.switch.config(bg=self.hfg)
			self.toggle_frame.config(bg=self.hbg)
		self.toggle_frame.bind('<Button-1>',on_click)
		self.switch.bind('<Button-1>',on_click)

	def pack(self,**kwargs):
		self.toggle_frame.pack(expand=True,**kwargs)
		self.toggle_frame.pack_propagate(True)

	def get(self):
		return self.state