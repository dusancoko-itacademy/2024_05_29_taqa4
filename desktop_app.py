import tkinter as tk 
import tkinter.messagebox as msg

def clicked_event():
    msg.showinfo("You have clicked the button!")

w = tk.Tk()
w.title("Debugging desktop app")

btnClick = tk.Button(w, text="Click me", command=clicked_event)
btnClick.pack()

if __name__ == "__main__":
    w.mainloop()
