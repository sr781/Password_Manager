from tkinter import *
from tkinter import messagebox
import random
letters_numbers_symbols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' '0', '1', '2', '3', '4', '5', '6', '7', '8', '9''!', '#', '$', '%', '&', '(', ')', '*', '+']


# ----------------- PASSWORD GENERATOR (Copied and modified from an earlier password generator project) ------------- #


def random_password():  # Function generates a password
    a = 0
    a_string_final = ""
    pw_input.delete(0, "end")
    password_length = random.randint(14, 19)  # The length of the password is between 14 and 18 characters long
    while a != password_length:
        a += 1
        a_str = letters_numbers_symbols[random.randint(0, len(letters_numbers_symbols) - 1)]  # Chooses a random character in the list
        a_string_final = a_string_final + a_str
    pw_input.insert(0, a_string_final)


# ---------------------------- SAVE PASSWORD --------------------------------------------#
def account_manager():   # This program saves the information into a text file
    website = website_input.get()
    email = em_us_input.get()
    password = pw_input.get()
    store = website + " | " + email + " | " + password + "\n"

    if len(website) == 0 or len(email) == 0 or len(password) == 0:  # This "if" statment checks to see if any entries are empty
        messagebox.showinfo(title="Error", message="One or more of the fields is empty")
    else:
        true_false = messagebox.askokcancel(title="Confirm Details", message=f"These are the details entered: \n Website: {website} \n Email: {email} \n Password: {password}")
        if true_false:
            password_file = open("passwords_sulav741.txt", "a")
            password_file.write(store)
            password_file.close()
            website_input.delete(0, "end")
            pw_input.delete(0, "end")


# ---------------------------- UI SETUP ------------------------------------------------- #

window = Tk()
window.title("Password manager")
window.config(padx=30, pady=30)

canvas = Canvas(width=300, height=140)
lock_img = PhotoImage(file="password_logo.PNG")
canvas.create_image(150, 70, image=lock_img)  # Canvas is used to create the lock image
canvas.grid(column=0, row=0, columnspan=2)

# ---------------------------- Website SETUP --------------- #
# Website Label
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
# Website Input
website_input = Entry(width=42)  # User enters the website that the password is for
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()  # When the program is first initialised, the cursor starts at this point
# ---------------------------- ------------- --------------- #

# ---------------------------- Email SETUP ----------------- #
# Email Label
em_us_label = Label(text="Email/Username:")
em_us_label.grid(column=0, row=2)
# Email Input
em_us_input = Entry(width=42)  # User enters the email/username for that website
em_us_input.grid(column=1, row=2, columnspan=2)
em_us_input.insert(0, "sulav_example@gmail.com")
# ---------------------------- ----------- ----------------- #

# ---------------------------- Password SETUP -------------- #
# Password Label
pw_label = Label(text="Password:")
pw_label.grid(column=0, row=3)
# Password Input
pw_input = Entry(width=24)  # User can either enter a password for the website or a random one can be generated
pw_input.grid(column=1, row=3)
# Password Button
pw_button = Button(text="Generate Password", command=random_password)  # Randomly generates the password
pw_button.grid(column=2, row=3)
# ---------------------------------------------------------- #

# ---------------------------- Button ---------------------- #
# "Add" Button
add_button = Button(text="Add", width=36, command=account_manager)  # Adds the information into a text file to be saved
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
