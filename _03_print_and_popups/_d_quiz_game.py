from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    S = 0
    Q = simpledialog.askstring('Hi', 'Did the San Diego Padres win yesterday?')
    if Q == 'no':
        S+=1
    else:
        S-=1

    P = simpledialog.askstring('Hi', 'Which pitcher has the best ERA on the Padres?')
    if P == 'Joe Musgrove':
        S+=1
    else:
        S-=1

    N = simpledialog.askstring('Hi', 'Which pitcher has the most wins on the Padres?')
    if N == 'Yu Darvish':
        S+=1
    else:
        S-=1

    messagebox.showinfo('Final Score', str(S))
    # Make a new window variable, window = Tk()
    
    # Hide the window using the window's .withdraw() method
    
    # 1. Create a variable to hold the user's score. Set it equal to zero. 

    # ASK A QUESTION AND CHECK THE ANSWER

    #      // 2.  Ask the user a question 
    
    #      // 3.  Use an if statement to check if their answer is correct

    #      // 4.  if the user's answer was correct, add one to their score 
 
    # MAKE MORE QUESTIONS. Ask more questions by repeating the above 
    #      // Option: Subtract a point from their score for a wrong answer
 
    # After all the questions have been asked, tell the user their final score
    # remember to convert your variable to a string using the str() function 
    
    # Run the window's .mainloop() method
