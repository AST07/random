from tkinter import *

class _Toplevels():
    def __init__(self):
        self.toplevels=[]

    def append(self,toplevel):
        self.toplevels.append(toplevel)

    def lift(self):
        for top in self.toplevels:
            top.toplevel.lift()

    def position(self,event):
        try:
            for top in self.toplevels:
                top.position()
        except:
            pass

class TransparentLabel():
    def __init__(self,master,opacity=1,transcolor='SystemButtonFace',**kwargs):
        self.master=master
        self.opacity=opacity
        self.transcolor=transcolor
        self.toplevel=Toplevel(self.master)
        self.toplevel.configure(bg=self.transcolor)
        self.toplevel.overrideredirect(True)
        self.toplevel.attributes('-alpha',self.opacity)
        self.toplevel.wm_attributes("-transparentcolor",self.transcolor)
        self.toplevel.withdraw()
        self.label=Label(self.toplevel,**kwargs,bg=self.transcolor)
        toplevels.append(self)
        self.master.bind('<Configure>',toplevels.position)
        self.master.bind('<Map>',self._on_map)
        self.master.bind('<Unmap>',self._on_unmap)

    def _on_unmap(self,event):
        self.toplevel.withdraw()

    def _on_map(self,event):
        self.toplevel.deiconify()
        toplevels.position(None)

    def position(self):
        self.x=self.cover_frame.winfo_rootx()
        self.y=self.cover_frame.winfo_rooty()
        self.center_x=self.cover_frame.winfo_width()//2-self.dimentions[0]//2
        self.center_y=self.cover_frame.winfo_height()//2-self.dimentions[1]//2
        self.toplevel.geometry(f'+{self.center_x+self.x}+{self.center_y+self.y}')
        self.master.update_idletasks()
        toplevels.lift()

    def pack(self,**kwargs):
        self.cover_frame=Frame(self.master)
        self.label.pack(**kwargs)
        self.toplevel.update()
        self.dimentions=(self.toplevel.winfo_width(),self.toplevel.winfo_height())
        if 'padx' in kwargs:
            kwargs['padx']+=self.dimentions[0]//2
        else:
            kwargs['padx']=self.dimentions[0]//2
        if 'pady' in kwargs:
            kwargs['pady']+=self.dimentions[1]//2
        else:
            kwargs['pady']=self.dimentions[1]//2
        self.cover_frame.pack(**kwargs)
        self.cover_frame.pack_propagate(False)
        self.toplevel.deiconify()
        toplevels.position(None)

toplevels=_Toplevels()

root=Tk()
root.config(bg='lightblue')

label=TransparentLabel(root,text='Transparent Label 1',opacity=0.5)
label.pack(pady=20)
def_label=Label(text='Default Label')
def_label.pack()
label=TransparentLabel(root,text='Transparent Label 2')
label.pack(pady=20)

canvas=Canvas(bg='yellow')
canvas.pack()
nested_label=TransparentLabel(canvas,text='Transparent Label in Canvas')
nested_label.pack()

root.mainloop()
