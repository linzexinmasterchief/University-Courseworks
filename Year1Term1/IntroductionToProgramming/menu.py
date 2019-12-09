import tkinter as tk
from tkinter import ttk

import bookcheckout as bc
import booklist as bl
import bookreturn as br
import booksearch as bs

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
book_name_search_box = tk.Entry(main_page, textvariable = book_name, width = 35, font = ('Helvetica', 32), background = "#eeeeee", bd=0, borderwidth=7, relief=tk.FLAT)
def on_enter(e):
    book_name_search_box['background'] = '#f5f5f5'

def on_leave(e):
    book_name_search_box['background'] = '#eeeeee'
book_name_search_box.bind("<Enter>", on_enter)
book_name_search_box.bind("<Leave>", on_leave)
book_name_search_box.place_configure(x = 200, y = 350)

def search_name_button_pressed():
    global book_name
    # get search results
    search_results = bs.go(book_name.get())
    # clear the frame used for displaying search results
    for widget in scrollable_frame.winfo_children():
        widget.destroy()
    if search_results == []:
        # show not found
        ttk.Label(scrollable_frame, text="not found").pack()

    # add search results to display frame line by line
    for i in range(len(search_results)):
        ttk.Label(scrollable_frame, text=str(search_results[i])).pack()
    newWindow.lift()

search_name_button = tk.Button(main_page, width = 8, text = "Search", font = ('Helvetica', 26), bd=0, background = "#0088ee", foreground = "white", command = search_name_button_pressed)
def on_enter(e):
    search_name_button['background'] = '#33aaee'
def on_leave(e):
    search_name_button['background'] = '#0088ee'
search_name_button.bind("<Enter>", on_enter)
search_name_button.bind("<Leave>", on_leave)
search_name_button.place_configure(x = 1080, y = 350)


return_ID_prompt = tk.Label(main_page, text = "Return Book ID", font = ('Helvetica', 40), background = "#ffffff")
return_ID_prompt.place_configure(x = 200, y = 480)

returnbook_ID = tk.StringVar()
book_id_search_box = tk.Entry(main_page, textvariable = returnbook_ID, width = 35, font = ('Helvetica', 32), background = "#eeeeee", bd=0, borderwidth=7, relief=tk.FLAT)
def on_enter(e):
    book_id_search_box['background'] = '#f5f5f5'
def on_leave(e):
    book_id_search_box['background'] = '#eeeeee'
book_id_search_box.bind("<Enter>", on_enter)
book_id_search_box.bind("<Leave>", on_leave)
book_id_search_box.place_configure(x = 200, y = 550)

def confirm_ID_button_pressed():
    global returnbook_ID

search_id_button = tk.Button(main_page, width = 8, text = "Confirm", font = ('Helvetica', 26), bd=0, background = "#0088ee", foreground = "white", command = confirm_ID_button_pressed)
def on_enter(e):
    search_id_button['background'] = '#33aaee'
def on_leave(e):
    search_id_button['background'] = '#0088ee'
search_id_button.bind("<Enter>", on_enter)
search_id_button.bind("<Leave>", on_leave)
search_id_button.place_configure(x = 1080, y = 550)

exit_button = tk.Button(main_page, width = 8, text = "EXIT", font = ('Helvetica', 26), bd=0, background = "#ee0000", foreground = "white", command = quit)
def on_enter(e):
    exit_button['background'] = '#ee3333'
def on_leave(e):
    exit_button['background'] = '#ee0000'
exit_button.bind("<Enter>", on_enter)
exit_button.bind("<Leave>", on_leave)
exit_button.place_configure(x = 1080, y = 650)

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

book_list_canvas = tk.Canvas(book_list_frame)

scrollbar = ttk.Scrollbar(newWindow, orient="vertical", command=book_list_canvas.yview)

scrollable_frame = ttk.Frame(book_list_canvas)
scrollable_frame.bind(
    "<Configure>",
    lambda e: book_list_canvas.configure(
        scrollregion=book_list_canvas.bbox("all")
    )
)

book_list_canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
book_list_canvas.configure(yscrollcommand=scrollbar.set)

book_list_canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

back_to_main_button = tk.Button(book_list_frame, width = 8, text = "Back", font = ('Helvetica', 26), bd=0, background = "#ee8800", foreground = "white", command = window.lift).pack()

book_list_frame.pack(fill="y")





window.mainloop()