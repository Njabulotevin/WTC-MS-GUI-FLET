import tkinter
import customtkinter


# Systme setup

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")


# window
app = customtkinter.CTk()
app.title("WTC-LMS-GUI")
app.geometry("1600x900")


# Top Menu
top_menu = tkinter.Menu(app)
app.config(menu=top_menu)
top_menu.add_cascade(label="File", command=lambda a: print("File clicked"))
top_menu.add_cascade(label="Edit", command=lambda a: print("Edit clicked"))


# Sub menu

file_menu = tkinter.Menu(top_menu, tearoff=0)
file_menu.add_command(label='New')
file_menu.add_command(label='Open...')
file_menu.add_command(label='Close')
file_menu.add_separator()

# file_menu = tkinter.Menu()


# Tab View
tab_frame = customtkinter.CTkFrame(
    app, width=1600, height=40, corner_radius=0, border_width=1)
tab_frame.place(y=0, x=0)


# tab buttons
modules_button = customtkinter.CTkButton(
    tab_frame, text="Modules", bg_color="transparent")
modules_button.grid(column=0, row=0)
reviews_button = customtkinter.CTkButton(
    tab_frame, text="Reviews", bg_color="transparent")
reviews_button.grid(column=2, row=0)
assessments_button = customtkinter.CTkButton(
    tab_frame, text="Assessments", bg_color="transparent")
assessments_button.grid(column=3, row=0)

app.mainloop()
