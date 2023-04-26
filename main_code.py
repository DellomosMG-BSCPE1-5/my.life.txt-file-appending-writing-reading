#Write a method in python to write multiple line of text contents
#into a text file mylife.txt

#Define a function 
def entry_writing():
    #Open a text file named mylife.txt (append)
    while True:
        with open("mylife.txt", "a") as main_file:
            #Ask user for a line text input
            date_of_entry = input("Date of Entry: ")
            entry = input(str("Kindly enter a text: "))
            #Append/write the input text to mylife.txt file
            main_file.write((str(date_of_entry) + "\n" + str(entry) + "\n\n"))            
            #Ask the user if he/she wants to enter a line of text again
            check = input("\nDo you want to start again? Yes or No: ")
            #Go back to top
            if check.upper() == "Y" or check == "yes" or check == "YES" or check == "Yes":  
                continue
        break
entry_writing()   
