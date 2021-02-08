from tkinter import *

class TransparentLabel:
    def __init__(self,master,opacity=1,**kwargs):
        self.master=master
        self.opacity=opacity
        self.toplevel=Toplevel(self.master)
        self.toplevel.configure(bg="#42f57b")
        self.toplevel.overrideredirect(True)
        self.toplevel.attributes('-alpha',self.opacity)
        self.toplevel.wm_attributes("-transparentcolor","#42f57b")
        self.toplevel.withdraw()
        self.label=Label(self.toplevel,**kwargs,bg="#42f57b")
        self.master.bind('<Configure>',self._position)

    def _position(self,event):
        self.x=self.master.winfo_rootx()
        self.y=self.master.winfo_rooty()
        self.toplevel.geometry(f'+{self.place[0]+self.x}+{self.place[1]+self.y}')
        self.toplevel.lift()

    def pack(self,place=(0,0),**kwargs):
        self.place=place
        self.label.pack(**kwargs)
        self._position(None)
        self.master.update()
        self.toplevel.deiconify()

root=Tk()

label=TransparentLabel(root,text='Hello World',opacity=0.5)
label.pack(place=(20,0))

root.mainloop()
