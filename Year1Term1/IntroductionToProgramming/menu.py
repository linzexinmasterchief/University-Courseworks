import tkinter as tk
from tkinter import ttk

import bookcheckout as bc
import booklist as bl
import bookreturn as br
import booksearch as bs

import widget_effects as we


# main program

# create window instance
window = tk.Tk()

# full screen window
window.attributes("-fullscreen", True)
# to rename the title of the window
window.title("Library Management System")

main_page = tk.Frame()
search_result_page = tk.Frame()
checkout_page = tk.Frame()


# books prepared to be check out
checkout_list = []

# make book_name global so the search result page can access it
book_name = tk.StringVar()

def create_main_page():
    global main_page
    global search_result_page
    global checkout_page

    # main page
    main_page = tk.Frame(window, background = "#ffffff")
    # green background containing title and copyright
    title_green_canvas = tk.Canvas(main_page, bg = "#55aa55", height = 150, highlightthickness=0)
    # fill horizontally
    title_green_canvas.pack(fill = "x", side = "top")
    # big large title
    title = title_green_canvas.create_text(500, 70, text = "Library Management System", font = ('Helvetica', 40, 'bold'), fill = "white")
    # copyright
    copyright_text = title_green_canvas.create_text(1300, 120, text = "© Lin Zexin     v1.0", font = ('Helvetica', 15), fill = "white")

    frame = tk.Frame(main_page, bg = "#ffffff", height = 10000)

    
    book_search_prompt = tk.Label(main_page, text = "Enter Book Title", font = ('Helvetica', 40), background = "#ffffff").place_configure(x = 200, y = 280)
    
    book_name_search_box = tk.Entry(main_page, textvariable = book_name, width = 35, font = ('Helvetica', 32), background = "#eeeeee", bd=0, borderwidth=7, relief=tk.FLAT)
    add_hover_effect_to_widget(book_name_search_box, '#f5f5f5', '#eeeeee')
    book_name_search_box.place_configure(x = 200, y = 350)

    
    def search_name_button_pressed():
        create_search_result_page(window)
        main_page.destroy()
        checkout_page.destroy()
    search_name_button = tk.Button(main_page, width = 8, text = "Search", font = ('Helvetica', 26), bd=0, background = "#0088ee", foreground = "white", command = search_name_button_pressed)
    add_hover_effect_to_widget(search_name_button, '#33aaee', '#0088ee')
    search_name_button.place_configure(x = 1080, y = 350)


    return_ID_prompt = tk.Label(main_page, text = "Return Book ID", font = ('Helvetica', 40), background = "#ffffff")
    return_ID_prompt.place_configure(x = 200, y = 480)

    return_book_ID = tk.StringVar()
    reutrn_book_id_search_box = tk.Entry(main_page, textvariable = return_book_ID, width = 35, font = ('Helvetica', 32), background = "#eeeeee", bd=0, borderwidth=7, relief=tk.FLAT)
    add_hover_effect_to_widget(reutrn_book_id_search_box, '#f5f5f5', '#eeeeee')
    reutrn_book_id_search_box.place_configure(x = 200, y = 550)

    def return_book_button_pressed():
        return_result = br.go(return_book_ID.get())
        if return_result == 0:
            return_book_error_text.set("Return Complete")
            return_book_error_display.config(foreground = "#55aa55")
        elif return_result == 1:
            return_book_error_text.set("This book is not borrowed")
            return_book_error_display.config(foreground = "#ff0000")
        elif return_result == 2:
            return_book_error_text.set("Book not found")
            return_book_error_display.config(foreground = "#ff0000")
        else:
            return_book_error_text.set("Unknown error")
            return_book_error_display.config(foreground = "#ff0000")
    return_book_button = tk.Button(main_page, width = 8, text = "Confirm", font = ('Helvetica', 26), bd=0, background = "#0088ee", foreground = "white", command = return_book_button_pressed)
    add_hover_effect_to_widget(return_book_button, '#33aaee', '#0088ee')
    return_book_button.place_configure(x = 1080, y = 550)

    return_book_error_text = tk.StringVar()
    return_book_error_display = tk.Label(main_page, textvariable = return_book_error_text, font = ('Helvetica', 20), background = "#ffffff")
    return_book_error_display.place_configure(x = 230, y = 650)

    exit_button = tk.Button(main_page, width = 8, text = "EXIT", font = ('Helvetica', 26), bd=0, background = "#ee0000", foreground = "white", command = quit)
    add_hover_effect_to_widget(exit_button, '#ee3333', '#ee0000')
    exit_button.place_configure(x = 1080, y = 650)
        
    def checkout_button_pressed():
        create_checkout_page(window)
        main_page.destroy()
        search_result_page.destroy()
    checkout_list_button = tk.Button(main_page, width = 9, text = "Cart(" + str(len(checkout_list)) + ") >", font = ('Helvetica', 26), bd=0, background = "#55aa55", foreground = "white", command = checkout_button_pressed)
    add_hover_effect_to_widget(checkout_list_button, '#55aa88', '#55aa55')
    checkout_list_button.pack(side = "right", anchor = "ne")


    frame.pack(fill="both")
    main_page.pack(fill = "both")



# make scrollable_frame global since search name button in main page needs to access it
scrollable_frame = ttk.Frame()
# make scrollbar global since the search button needs to set init position for it
scrollbar = ttk.Scrollbar()
def create_search_result_page(parent):
    global main_page
    global search_result_page
    global checkout_page

    global checkout_list

    search_result_page = tk.Frame(parent, bg = "#eeeeee")
    # green background containing title and copyright
    title_green_canvas = tk.Canvas(search_result_page, bg = "#55aa55", height = 150, highlightthickness=0)
    # fill horizontally
    title_green_canvas.pack(fill = "x", side = "top")
    # big large title
    title = title_green_canvas.create_text(500, 70, text = "Library Management System", font = ('Helvetica', 40, 'bold'), fill = "white")
    # copyright
    copyright_text = title_green_canvas.create_text(1300, 120, text = "© Lin Zexin     v1.0", font = ('Helvetica', 15), fill = "white")


    def back_to_main_button_pressed():
        create_main_page()
        search_result_page.destroy()
    back_to_main_button = tk.Button(search_result_page, width = 8, text = "< Main", font = ('Helvetica', 26), bd=0, background = "#ee8800", foreground = "white", command = back_to_main_button_pressed)
    we.add_hover_effect_to_widget(back_to_main_button, '#eeaa33', '#ee8800')
    back_to_main_button.pack(side = "left", anchor = "nw")

    def checkout_button_pressed():
        create_checkout_page(window)
        search_result_page.destroy()
    checkout_list_button = tk.Button(search_result_page, width = 9, text = "Cart(" + str(len(checkout_list)) + ") >", font = ('Helvetica', 26), bd=0, background = "#55aa55", foreground = "white", command = checkout_button_pressed)
    we.add_hover_effect_to_widget(checkout_list_button, '#55aa88', '#55aa55')
    checkout_list_button.pack(side = "right", anchor = "ne")

    book_list_frame = book_list_frame = tk.Frame(search_result_page, bg = "#eeeeee")
    book_list_canvas = tk.Canvas(book_list_frame, width = 1100, height = 980, bg = "#eeeeee", highlightthickness = 0)
    scrollbar = ttk.Scrollbar(book_list_frame, orient="vertical", command=book_list_canvas.yview)
    scrollable_frame = tk.Frame(book_list_canvas, bg = "#eeeeee")

    scrollable_frame.bind(
        "<Configure>",
        lambda e: book_list_canvas.configure(
            scrollregion=book_list_canvas.bbox("all")
        )
    )

    book_list_canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    book_list_canvas.configure(yscrollcommand=scrollbar.set)

    # clear the frame used for displaying search results
    # for widget in scrollable_frame.winfo_children():
    #     widget.destroy()
    scrollable_frame.bind(
        "<Configure>",
        lambda e: book_list_canvas.configure(
            scrollregion=book_list_canvas.bbox("all")
        )
    )
    # get search results
    search_results = bs.go(book_name.get())

    # show how many results found
    ttk.Label(scrollable_frame, text = str(len(search_results)) + " search results found", font = ('Helvetica', 30), background = "#eeeeee", width = 45).pack(padx = 80, pady = 20)

    
    # add search results to display frame line by line
    for i in range(len(search_results)):
        make_search_record(scrollable_frame, checkout_list, create_main_page, search_result_page, search_results[i])

    book_list_frame.pack()
    book_list_canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    book_list_frame.pack(fill="y")
    search_result_page.pack(fill="x")


# automatically make record ui for each result found
def make_search_record(parent, checkout_list, create_main_page, search_result_page, record = []):
    temp_frame = tk.Frame(parent, bg = "#ffffff")
    # title
    tk.Label(temp_frame, text = str(record[1]), font = ('Helvetica', 18), bg = "#ffffff", anchor = "w").pack(fill = "x", pady = 20, ipady = 10, padx = 100)
    # content
    tk.Label(temp_frame, text = "Author: " + str(record[2]) + "          " + "Purchase date: " + str(record[3]), bg = "#ffffff", anchor = "w", justify = tk.LEFT).pack(side = "left", padx = 150)
    
    
    tk.Frame(temp_frame, width = 100, background = "#ffffff").pack(side = "right")
    # check if the book is available
    if record[-1] == "0":
        if record in checkout_list:
            checkout_button = tk.Button(temp_frame, width = 8, text = "In cart", font = ('Helvetica', 15), bd=0, background = "#55aa55", foreground = "white", padx = 20)
            checkout_button.pack(side = "right", ipadx = 20)
        else:
            def on_Add_to_cart_button_pressed():
                # add the book id to cart list
                checkout_list.append(record)
                # destroy current book result page
                search_result_page.destroy()
                # recreate boo result page (refresh to show in cart button changes)
                create_search_result_page(window)
            Add_to_cart_button = tk.Button(temp_frame, width = 8, text = "Add to cart", font = ('Helvetica', 15), bd=0, background = "#0088ee", foreground = "white", padx = 20, command = on_Add_to_cart_button_pressed)
            we.add_hover_effect_to_widget(Add_to_cart_button, '#33aaee', '#0088ee')
            Add_to_cart_button.pack(side = "right", ipadx = 20)
    else:
        unavailable_button = tk.Button(temp_frame, width = 8, text = "Unavailable", font = ('Helvetica', 15), bd=0, background = "#dddddd", foreground = "white", padx = 20)
        unavailable_button.pack(side = "right", ipadx = 20)

    temp_frame.pack(fill = "x", pady = 10)


def create_checkout_page(parent):
    global main_page
    global search_result_page
    global checkout_page

    global checkout_list

    checkout_page = tk.Frame(window, bg = "#eeeeee")
    # green background containing title and copyright
    title_green_canvas = tk.Canvas(checkout_page, bg = "#55aa55", height = 150, highlightthickness=0)
    # fill horizontally
    title_green_canvas.pack(fill = "x", side = "top")
    # big large title
    title = title_green_canvas.create_text(500, 70, text = "Library Management System", font = ('Helvetica', 40, 'bold'), fill = "white")
    # copyright
    copyright_text = title_green_canvas.create_text(1300, 120, text = "© Lin Zexin     v1.0", font = ('Helvetica', 15), fill = "white")

    def back_to_main_button_pressed():
        create_main_page()
        checkout_page.destroy()
    back_to_main_button = tk.Button(checkout_page, width = 8, text = "< Main", font = ('Helvetica', 26), bd=0, background = "#ee8800", foreground = "white", command = back_to_main_button_pressed)
    we.add_hover_effect_to_widget(back_to_main_button, '#eeaa33', '#ee8800')
    back_to_main_button.pack(side = "left", anchor = "nw")

    def back_to_search_list_button_pressed():
        create_search_result_page(window)
        checkout_page.destroy()
    back_to_search_list_button = tk.Button(checkout_page, width = 9, text = "< List", font = ('Helvetica', 26), bd=0, background = "#55aa55", foreground = "white", command = back_to_search_list_button_pressed)
    we.add_hover_effect_to_widget(back_to_search_list_button, '#55aa88', '#55aa55')
    back_to_search_list_button.pack(side = "right", anchor = "ne")

    book_list_frame = book_list_frame = tk.Frame(checkout_page, bg = "#eeeeee")
    book_list_canvas = tk.Canvas(book_list_frame, width = 1100, height = 980, bg = "#eeeeee", highlightthickness = 0)
    scrollbar = ttk.Scrollbar(book_list_frame, orient="vertical", command=book_list_canvas.yview)
    scrollable_frame = tk.Frame(book_list_canvas, bg = "#eeeeee")

    scrollable_frame.bind(
        "<Configure>",
        lambda e: book_list_canvas.configure(
            scrollregion=book_list_canvas.bbox("all")
        )
    )

    book_list_canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    book_list_canvas.configure(yscrollcommand=scrollbar.set)

    # clear the frame used for displaying search results
    
    # show how many results found
    ttk.Label(scrollable_frame, text = str(len(checkout_list)) + " book ready for checkout", font = ('Helvetica', 30), background = "#eeeeee", width = 45).pack(padx = 80, pady = 20)

    # checkout confirmation ui group
    checkout_confirm_frame = tk.Frame(scrollable_frame, background = "#ffffff")
    # prompt the user to enter the member ID
    ttk.Label(checkout_confirm_frame, text = "Please enter you member ID to checkout", font = ('Helvetica', 20), background = "#ffffff").pack(pady = 20)
    
    # entry box for entering member ID
    member_ID = tk.StringVar()
    member_ID_box = tk.Entry(checkout_confirm_frame, textvariable = member_ID, width = 35, font = ('Helvetica', 32), background = "#eeeeee", bd=0, borderwidth=7, relief=tk.FLAT)
    add_hover_effect_to_widget(member_ID_box, '#f5f5f5', '#eeeeee')
    member_ID_box.pack()

    # message displayed to the user if there is any error
    message_var = tk.StringVar()
    return_message = tk.Label(checkout_confirm_frame, textvariable = message_var, font = ('Helvetica', 20), background = "#ffffff")
    return_message.pack(side = "left", pady = 20, padx = 200, anchor = "w")

    def confirm_checkout_button_pressed():
        global checkout_list
        input_id = member_ID.get()
        # if there is nothing ready to be checkout
        if len(checkout_list) == 0:
            message_var.set("Nothing to checkout")
            return_message.config(foreground = "#ff0000")
            return
        
        member_id_validation_result = member_id_validation(input_id)
        if member_id_validation_result == 0:
            # succeed
            bc.go(checkout_list, input_id)

            checkout_list = []
            # destroy current book result page
            checkout_page.destroy()
            # recreate boo result page (refresh to show changes)
            create_checkout_page(window)
        elif member_id_validation_result == 1:
            # if the id input is not 4 digits
            message_var.set("Member ID should be 4-digits")
            return_message.config(foreground = "#ff0000")
        elif member_id_validation_result == 2:
            # if the member id input not only contains numbers
            message_var.set("Member ID should be a number")
            return_message.config(foreground = "#ff0000")

    # place holder used to avoid the confirm checkout button being pushed out of the checkout confirm frame
    tk.Frame(checkout_confirm_frame, width = 149, background = "#ffffff").pack(side = "right")

    confirm_checkout_button = tk.Button(checkout_confirm_frame, width = 8, text = "Confirm", font = ('Helvetica', 26), bd=0, background = "#0088ee", foreground = "white", command = confirm_checkout_button_pressed)
    add_hover_effect_to_widget(confirm_checkout_button, '#33aaee', '#0088ee')
    confirm_checkout_button.pack(side = "right")

    checkout_confirm_frame.pack(fill = "x", pady = 10)

    # add search results to display frame line by line
    for i in range(len(checkout_list)):
        # checkout_list stores the full details of book, same as search_results above
        make_checkout_record(scrollable_frame, checkout_list[i])

    book_list_frame.pack()
    book_list_canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    book_list_frame.pack(fill="y")

    checkout_page.pack(fill = "both")

# both member id and book id are using this function to validate, since they are all numbers
def member_id_validation(input_id):
    if len(input_id) != 4:
        # if the id input is not 4 digits
        return 1
    elif input_id.isalnum():
        return 0
    else:
        return 2


def make_checkout_record(parent, record):
    temp_frame = tk.Frame(parent, bg = "#ffffff")
    # book title
    tk.Label(temp_frame, text = str(record[1]), font = ('Helvetica', 18), bg = "#ffffff", anchor = "w").pack(fill = "x", pady = 20, ipady = 10, padx = 100)
    # book details
    tk.Label(temp_frame, text = "Author: " + str(record[2]) + "          " + "Purchase date: " + str(record[3]), bg = "#ffffff", anchor = "w", justify = tk.LEFT).pack(side = "left", padx = 150)
    # pkaceholder used to aviud the add to cart button being pushed out from the frame
    tk.Frame(temp_frame, width = 100, background = "#ffffff").pack(side = "right")

    def on_remove_button_pressed():
        checkout_list.remove(record)
        # destroy current book result page
        checkout_page.destroy()
        # recreate boo result page (refresh to show in cart button changes)
        create_checkout_page(window)
    remove_from_cart_button = tk.Button(temp_frame, width = 8, text = "Remove", font = ('Helvetica', 15), bd=0, background = "#cc0000", foreground = "white", padx = 20, command = on_remove_button_pressed)
    we.add_hover_effect_to_widget(remove_from_cart_button, '#ee0000', '#cc0000')
    remove_from_cart_button.pack(side = "right", ipadx = 20)

    temp_frame.pack(fill = "x", pady = 10)


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