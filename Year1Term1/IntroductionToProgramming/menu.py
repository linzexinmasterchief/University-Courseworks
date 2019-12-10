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

main_page = tk.Frame()
search_result_page = tk.Frame()

def create_main_page():
    global main_page
    global search_result_page
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

    frame = tk.Frame(main_page, bg = "#ffffff", height = 10000)

    book_name = tk.StringVar()
    book_search_prompt = tk.Label(main_page, text = "Enter Book Title", font = ('Helvetica', 40), background = "#ffffff").place_configure(x = 200, y = 280)
    
    book_name_search_box = tk.Entry(main_page, textvariable = book_name, width = 35, font = ('Helvetica', 32), background = "#eeeeee", bd=0, borderwidth=7, relief=tk.FLAT)
    add_hover_effect_to_widget(book_name_search_box, '#f5f5f5', '#eeeeee')
    book_name_search_box.place_configure(x = 200, y = 350)

    # automatically make record ui for each result found
    def make_search_record(record = []):
        temp_frame = tk.Frame(scrollable_frame, bg = "#ffffff")
        # title
        tk.Label(temp_frame, text = str(record[1]), font = ('Helvetica', 18), bg = "#ffffff", anchor = "w").pack(fill = "x", pady = 20, ipady = 10, padx = 100)
        # content
        tk.Label(temp_frame, text = "Author: " + str(record[2]) + " | " + "Purchase date: " + str(record[3]), bg = "#ffffff", anchor = "w", justify = tk.LEFT).pack(side = "left", padx = 150)
        
        # check if the book is available
        if record[-1] == "0":
            checkout_button = tk.Button(temp_frame, width = 8, text = "Check out", font = ('Helvetica', 15), bd=0, background = "#0088ee", foreground = "white", padx = 20)
            add_hover_effect_to_widget(checkout_button, '#33aaee', '#0088ee')
            checkout_button.pack(side = "right", ipadx = 20)
        else:
            checkout_button = tk.Button(temp_frame, width = 8, text = "Unavailable", font = ('Helvetica', 15), bd=0, background = "#dddddd", foreground = "white", padx = 20)
            checkout_button.pack(side = "right", ipadx = 20)

        temp_frame.pack(fill = "x", pady = 10)

    def search_name_button_pressed():
        global scrollable_frame
        
        create_search_result_page()
        # get search results
        search_results = bs.go(book_name.get())
        # clear the frame used for displaying search results
        for widget in scrollable_frame.winfo_children():
            widget.destroy()
        # show how many results found
        ttk.Label(scrollable_frame, text = str(len(search_results)) + " search results found", font = ('Helvetica', 30), background = "#eeeeee", width = 45).pack(padx = 80, pady = 20)

        # add search results to display frame line by line
        for i in range(len(search_results)):
            make_search_record(search_results[i])

        main_page.destroy()
    search_name_button = tk.Button(main_page, width = 8, text = "Search", font = ('Helvetica', 26), bd=0, background = "#0088ee", foreground = "white", command = search_name_button_pressed)
    add_hover_effect_to_widget(search_name_button, '#33aaee', '#0088ee')
    search_name_button.place_configure(x = 1080, y = 350)


    return_ID_prompt = tk.Label(main_page, text = "Return Book ID", font = ('Helvetica', 40), background = "#ffffff")
    return_ID_prompt.place_configure(x = 200, y = 480)

    returnbook_ID = tk.StringVar()
    book_id_search_box = tk.Entry(main_page, textvariable = returnbook_ID, width = 35, font = ('Helvetica', 32), background = "#eeeeee", bd=0, borderwidth=7, relief=tk.FLAT)
    add_hover_effect_to_widget(book_id_search_box, '#f5f5f5', '#eeeeee')
    book_id_search_box.place_configure(x = 200, y = 550)

    def confirm_ID_button_pressed():
        pass

    search_id_button = tk.Button(main_page, width = 8, text = "Confirm", font = ('Helvetica', 26), bd=0, background = "#0088ee", foreground = "white", command = confirm_ID_button_pressed)
    add_hover_effect_to_widget(search_id_button, '#33aaee', '#0088ee')
    search_id_button.place_configure(x = 1080, y = 550)

    exit_button = tk.Button(main_page, width = 8, text = "EXIT", font = ('Helvetica', 26), bd=0, background = "#ee0000", foreground = "white", command = quit)
    add_hover_effect_to_widget(exit_button, '#ee3333', '#ee0000')
    exit_button.place_configure(x = 1080, y = 650)


    frame.pack(fill="both")
    main_page.pack(fill = "both")



# make scrollable_frame global since search name button in main page needs to access it
scrollable_frame = ttk.Frame()
def create_search_result_page():
    global main_page
    global search_result_page

    global scrollable_frame
    search_result_page = tk.Frame(window, bg = "#eeeeee")
    # green background containing title and copyright
    title_green_canvas = tk.Canvas(search_result_page, bg = "#55aa55", height = 150, highlightthickness=0)
    # fill horizontally
    title_green_canvas.pack(fill = "x", side = "top")
    # big large title
    title = title_green_canvas.create_text(500, 70, text = "Library Management System", font = ('Helvetica', 40, 'bold'), fill = "white")
    # copyright
    copyright_text = title_green_canvas.create_text(1300, 120, text = "© Lin Zexin     v1.0", font = ('Helvetica', 15), fill = "white")


    book_list_frame = tk.Frame(search_result_page, bg = "#ffffff")

    book_list_canvas = tk.Canvas(book_list_frame, width = 1100, height = 1000, bg = "#eeeeee", highlightthickness = 0)

    scrollbar = ttk.Scrollbar(search_result_page, orient="vertical", command=book_list_canvas.yview)

    scrollable_frame = tk.Frame(book_list_canvas, bg = "#eeeeee")
    scrollable_frame.bind(
        "<Configure>",
        lambda e: book_list_canvas.configure(
            scrollregion=book_list_canvas.bbox("all")
        )
    )
    scrollable_frame.pack(fill = "x")

    book_list_canvas.create_window((0, 0), window=scrollable_frame)
    book_list_canvas.configure(yscrollcommand=scrollbar.set)

    book_list_canvas.pack()
    scrollbar.pack(side="right", fill="y")

    def back_to_main_button_pressed():
        create_main_page()
        search_result_page.destroy()
    back_to_main_button = tk.Button(search_result_page, width = 8, text = "< Back", font = ('Helvetica', 26), bd=0, background = "#ee8800", foreground = "white", command = back_to_main_button_pressed)
    add_hover_effect_to_widget(back_to_main_button, '#eeaa33', '#ee8800')
    back_to_main_button.place_configure(x = 0, y = 150)

    book_list_frame.pack(fill="y")
    search_result_page.pack(fill="x")

def add_hover_effect_to_widget(widget, hover_color = '#ffffff', original_color = '#eeeeee'):
    def on_enter(e):
        widget['background'] = hover_color
    def on_leave(e):
        widget['background'] = original_color
    widget.bind("<Enter>", on_enter)
    widget.bind("<Leave>", on_leave)

# create main page to start
create_main_page()
window.mainloop()