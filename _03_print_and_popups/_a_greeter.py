from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block 
if __name__ == '__main__':

    window = Tk()
    window.withdraw()
    N = simpledialog.askstring('hi', 'What is your name?')
    messagebox.showinfo('hi',N)
    print('I hope the Padres win today, unlike their game yesterday.')
    messagebox.showerror()

    # Make a new window variable, window = Tk()
    
    # Hide the window using the window's .withdraw() method
    
    # Ask the user for their name and save it to a variable
    # name = simpledialog.askstring(title='Greeter', prompt="What is your name?")
    
    # Show a message box with your message using the .showinfo() method
    
    # Print your message to the console using the print() function
    
    # Show an error message using messagebox.showerror()

    # Run the window's .mainloop() method

    pass
