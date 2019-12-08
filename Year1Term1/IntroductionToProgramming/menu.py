import tkinter as tk

from bookcheckout import *
from booklist import *
from bookreturn import *
from booksearch import *
from database import *

# main program

# create window instance
window = tk.Tk()

# full screen window
window.attributes("-fullscreen", True)
# to rename the title of the window
window.title("Library Management System")

# main page
main_page = tk.Frame(window)
# green background containing title and copyright
title_green_canvas = tk.Canvas(main_page, bg = "#55aa55", height = 150, highlightthickness=0)
# fill horizontally
title_green_canvas.pack(fill = "x", side = "top")
# big large title
title = title_green_canvas.create_text(500, 70, text = "Library Management System", font = ('Helvetica', 40, 'bold'), fill = "white")
# copyright
copyright_text = title_green_canvas.create_text(1300, 120, text = "© Lin Zexin     v1.0", font = ('Helvetica', 15), fill = "white")

frame = tk.Frame(main_page, bg = "#ffffff", height = 10000).pack(fill="both")

book_name = tk.StringVar()
book_search_prompt = tk.Label(main_page, text = "Enter Book Title", font = ('Helvetica', 40), background = "#ffffff").place_configure(x = 200, y = 280)
book_name_search_box = tk.Entry(main_page, textvariable = book_name, width = 35, font = ('Helvetica', 32), background = "#eeeeee", bd=0, borderwidth=7, relief=tk.FLAT).place_configure(x = 200, y = 350)

def search_book_button_pressed():
    global book_name
    print(book_name.get())
    call_book_list_window()

search_book_button = tk.Button(main_page, width = 8, text = "Search", font = ('Helvetica', 26), bd=0, background = "#0088ee", foreground = "white", command = search_book_button_pressed).place_configure(x = 1080, y = 350)


returnbook_ID = tk.StringVar()
return_ID_prompt = tk.Label(main_page, text = "Return Book ID", font = ('Helvetica', 40), background = "#ffffff").place_configure(x = 200, y = 480)
book_name_search_box = tk.Entry(main_page, textvariable = returnbook_ID, width = 35, font = ('Helvetica', 32), background = "#eeeeee", bd=0, borderwidth=7, relief=tk.FLAT).place_configure(x = 200, y = 550)

def confirm_ID_button_pressed():
    global returnbook_ID
    print(returnbook_ID.get())

search_name_button = tk.Button(main_page, width = 8, text = "Confirm", font = ('Helvetica', 26), bd=0, background = "#0088ee", foreground = "white", command = confirm_ID_button_pressed).place_configure(x = 1080, y = 550)

exit_button = tk.Button(main_page, width = 8, text = "EXIT", font = ('Helvetica', 26), bd=0, background = "#ee0000", foreground = "white", command = quit).place_configure(x = 1080, y = 650)

main_page.pack(fill = "both")


# book list page
newWindow = tk.Toplevel(window)
# full screen window
newWindow.attributes("-fullscreen", True)
# to rename the title of the window
newWindow.title("Library Management System")

# green background containing title and copyright
title_green_canvas = tk.Canvas(newWindow, bg = "#55aa55", height = 150, highlightthickness=0)
# fill horizontally
title_green_canvas.pack(fill = "x", side = "top")
# big large title
title = title_green_canvas.create_text(500, 70, text = "Library Management System", font = ('Helvetica', 40, 'bold'), fill = "white")
# copyright
copyright_text = title_green_canvas.create_text(1300, 120, text = "© Lin Zexin     v1.0", font = ('Helvetica', 15), fill = "white")

book_list_frame = tk.Frame(newWindow, bg = "#ffffff")
exit_button = tk.Button(book_list_frame, width = 8, text = "EXIT", font = ('Helvetica', 26), bd=0, background = "#ee0000", foreground = "white", command = quit).pack()

book_list_frame.pack(fill="y")

def call_book_list_window():
    try:
        newWindow.lift()
        print("lift")
    except:
        newWindow.Toplevel(window)


window.mainloop()