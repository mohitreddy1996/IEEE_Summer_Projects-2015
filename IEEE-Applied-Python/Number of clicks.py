from Tkinter import *
class Application(Frame):
	def create_wigdet(self):
		self.bttn=Button(self,text="Number of Clicks: 0")
		self.bttn["command"]=self.update_count
		self.bttn.grid()
	def update_count(self):
		self.bttn_clicks += 1
		self.bttn["text"]="Number of Clicks: "+str(self.bttn_clicks)
	def __init__(self,master):
		Frame.__init__(self,master)
		self.grid()
		self.bttn_clicks=0
		self.create_wigdet()
	


	
root=Tk()
root.title("First GUI")
root.geometry("200x100")
app=Application(root)
app.grid()
root.mainloop()
