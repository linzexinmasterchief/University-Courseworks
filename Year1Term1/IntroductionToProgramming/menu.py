import tkinter as tk
from tkinter import ttk

import bookcheckout as bc
import booklist as bl
import bookreturn as br
import booksearch as bs


#-------------------------< program preparations />-----------------------------
# create window instance
window = tk.Tk()

# full screen window
window.attributes("-fullscreen", True)
# to rename the title of the window
window.title("Library Management System")

# make the three root frames public so they can be accessed by all functions globally
# just generate a blank prototype for now
main_page = tk.Frame(window, background = "#ffffff")
search_result_page = tk.Frame(window, background = "#ffffff")
checkout_page = tk.Frame(window, background = "#ffffff")
detail_page = tk.Frame(window, background = "#ffffff")

# books prepared to be check out
checkout_list = []

# make book_name global so the search result page can access it
book_name = tk.StringVar()

#----------------------------< main page />-------------------------------------
def create_main_page():
    """
    function used to create the main page that has two search box for book 
    searching and book returning respectively
    """
    # access three global root pages
    global main_page
    global search_result_page
    global checkout_page
    global detail_page

    # main page
    main_page = tk.Frame(
        window, 
        background = "#ffffff")
    # generate the big green header
    create_library_management_system_header(main_page)

    main_page_frame = tk.Frame(
        main_page, 
        bg = "#ffffff", 
        height = 10000)

    
    book_search_prompt = tk.Label(
        main_page, 
        text = "Enter Book Title or ID", 
        font = ('Helvetica', 40), 
        background = "#ffffff"
        ).place_configure(x = 200, y = 280)
    
    book_name_search_box = tk.Entry(
        main_page, 
        textvariable = book_name, 
        width = 35, 
        font = ('Helvetica', 32), 
        background = "#eeeeee", 
        bd=0, borderwidth=7, 
        relief=tk.FLAT)
    add_hover_effect_to_widget(
        book_name_search_box, 
        '#f5f5f5', 
        '#eeeeee')
    book_name_search_box.place_configure(
        x = 200, 
        y = 350)

    
    def search_name_button_pressed():
        create_search_result_page(window)
        main_page.destroy()
        checkout_page.destroy()
    search_name_button = tk.Button(
        main_page, 
        width = 8, 
        text = "Search", 
        font = ('Helvetica', 26), 
        bd=0, 
        background = "#0088ee", 
        foreground = "white", 
        command = search_name_button_pressed)
    add_hover_effect_to_widget(
        search_name_button, 
        '#33aaee', 
        '#0088ee')
    search_name_button.place_configure(
        x = 1080, 
        y = 350)


    return_ID_prompt = tk.Label(
        main_page, 
        text = "Return Book ID", 
        font = ('Helvetica', 40), 
        background = "#ffffff")
    return_ID_prompt.place_configure(
        x = 200, 
        y = 480)

    return_book_ID = tk.StringVar()
    reutrn_book_id_search_box = tk.Entry(
        main_page, 
        textvariable = return_book_ID, 
        width = 35, 
        font = ('Helvetica', 32), 
        background = "#eeeeee", 
        bd=0, 
        borderwidth=7, 
        relief=tk.FLAT)
    add_hover_effect_to_widget(
        reutrn_book_id_search_box, 
        '#f5f5f5', 
        '#eeeeee')
    reutrn_book_id_search_box.place_configure(
        x = 200, 
        y = 550)

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
    return_book_button = tk.Button(
        main_page, 
        width = 8, 
        text = "Confirm", 
        font = ('Helvetica', 26), 
        bd=0, 
        background = "#0088ee", 
        foreground = "white", 
        command = return_book_button_pressed)
    add_hover_effect_to_widget(
        return_book_button, 
        '#33aaee', 
        '#0088ee')
    return_book_button.place_configure(
        x = 1080, 
        y = 550)

    return_book_error_text = tk.StringVar()
    return_book_error_display = tk.Label(
        main_page, 
        textvariable = return_book_error_text, 
        font = ('Helvetica', 20), 
        background = "#ffffff")
    return_book_error_display.place_configure(
        x = 230, 
        y = 650)

    exit_button = tk.Button(
        main_page, 
        width = 8, 
        text = "EXIT", 
        font = ('Helvetica', 26), 
        bd=0, 
        background = "#ee0000", 
        foreground = "white", 
        command = quit)
    add_hover_effect_to_widget(
        exit_button, 
        '#ee3333', 
        '#ee0000')
    exit_button.place_configure(
        x = 1080, 
        y = 650)
        
    def checkout_button_pressed():
        create_checkout_page(window)
        main_page.destroy()
        search_result_page.destroy()
    checkout_list_button = tk.Button(
        main_page, 
        width = 9, 
        text = "Cart(" + str(len(checkout_list)) + ") >", 
        font = ('Helvetica', 26), 
        bd=0, 
        background = "#55aa55", 
        foreground = "white", 
        command = checkout_button_pressed)
    add_hover_effect_to_widget(
        checkout_list_button, 
        '#55aa88', 
        '#55aa55')
    checkout_list_button.pack(
        side = "right", 
        anchor = "ne")


    main_page_frame.pack(fill="both")
    main_page.pack(fill = "both")


#--------------------------< search result page />------------------------------
# function used to generate the book search result diplay page
def create_search_result_page(parent):
    # access three global root pages
    global main_page
    global search_result_page
    global checkout_page
    global detail_page

    global checkout_list

    search_result_page = tk.Frame(
        parent, 
        bg = "#eeeeee")
    
    # generate the big green header
    create_library_management_system_header(search_result_page)

    def back_to_main_button_pressed():
        create_main_page()
        search_result_page.destroy()
    back_to_main_button = tk.Button(
        search_result_page, 
        width = 8, 
        text = "< Main", 
        font = ('Helvetica', 26), 
        bd=0, 
        background = "#ee8800", 
        foreground = "white", 
        command = back_to_main_button_pressed)
    add_hover_effect_to_widget(
        back_to_main_button, 
        '#eeaa33', 
        '#ee8800')
    back_to_main_button.pack(
        side = "left", 
        anchor = "nw")

    def checkout_button_pressed():
        create_checkout_page(window)
        search_result_page.destroy()
    checkout_list_button = tk.Button(
        search_result_page, 
        width = 9, 
        text = "Cart(" + str(len(checkout_list)) + ") >", 
        font = ('Helvetica', 26), 
        bd=0, 
        background = "#55aa55", 
        foreground = "white", 
        command = checkout_button_pressed)
    add_hover_effect_to_widget(
        checkout_list_button, 
        '#55aa88', 
        '#55aa55')
    checkout_list_button.pack(
        side = "right", 
        anchor = "ne")

    book_list_frame = book_list_frame = tk.Frame(
        search_result_page, 
        bg = "#eeeeee")
    book_list_canvas = tk.Canvas(
        book_list_frame, 
        width = 1100, 
        height = 980, 
        bg = "#eeeeee", 
        highlightthickness = 0)
    scrollbar = ttk.Scrollbar(
        book_list_frame, 
        orient="vertical", 
        command=book_list_canvas.yview)
    book_list_canvas.configure(
        yscrollcommand = scrollbar.set, 
        scrollregion=book_list_canvas.bbox('all'))
    scrollable_frame = tk.Frame(
        book_list_canvas, 
        bg = "#eeeeee")

    scrollable_frame.bind(
        "<Configure>",
        lambda e: book_list_canvas.configure(
            scrollregion=book_list_canvas.bbox("all")
        )
    )

    book_list_canvas.create_window(
        (0, 0), 
        window = scrollable_frame, 
        anchor="nw")

    book_list_canvas.configure(yscrollcommand = scrollbar.set)

    search_results = bs.go(book_name.get())
    display_results = []

    # only keep the original copy record to prevent duplicate
    for record in search_results:
        # explain:
        # search_results is a 2d array that contains multiple lines of records
        # each record is in standard record format
        # so search_results[i][0] is the first element of i-th record
        # which is obviously the id of this book
        # since the id is in the format of x_y
        #  - x is the book id
        #  - y is the copy num
        # which are splitted by split("_") => y = search_results[i][0].split("_")[1]
        # only when y == 0 is the original copy, others need to be deleted
        if record[0].split("_")[1] == "0":
            display_results.append(record)

    # show how many results found
    ttk.Label(
        scrollable_frame, 
        text = str(len(display_results)) + " search results found", 
        font = ('Helvetica', 30), 
        background = "#eeeeee", 
        width = 45
        ).pack(padx = 80, pady = 20)

    
    # add search results to display frame line by line
    for record in display_results:
        def book_detail_button_pressed():
            # as explained above, record[0].split("_")[1] is the general id of
            # this series of books
            create_detail_page(window, record[0].split("_")[1])
        make_record(
            scrollable_frame, 
            record, 
            "More", 
            '#0088ee', 
            '#33aaee', 
            book_detail_button_pressed, 
            0)
        # # checkout_list stores the full details of book, same as display_results above
        # # check if the book is available
        # if record[-1] == "0":
        #     if record in checkout_list:
        #         make_record(scrollable_frame, record, "In cart", '#55aa55', '#55aa55', None, -1)
        #     else:
        #         # used to refresh the search result page
        #         def search_result_page_refresh():                
        #             scrollbar_pos = scrollbar.get()
        #             # destroy current book result page
        #             search_result_page.destroy()
        #             # recreate boo result page (refresh to show in cart button changes)
        #             create_search_result_page(window)
        #         make_record(scrollable_frame, record, "Add to cart", '#0088ee', '#33aaee', search_result_page_refresh, 0)
        # else:
        #     make_record(scrollable_frame, record, "Unavailable", '#dddddd', '#dddddd', None, -1)

    book_list_frame.pack()
    book_list_canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    book_list_frame.pack(fill="y")
    search_result_page.pack(fill="x")



#----------------------------------------------------------< checkout page />--------------------------------------------------------------
def create_checkout_page(parent, book_id):
    """
    function used to create the page for book details
    """
    # access three global root pages
    global main_page
    global search_result_page
    global checkout_page
    global detail_page

    global checkout_list

    checkout_page = tk.Frame(window, bg = "#eeeeee")
    
    # generate the big green header
    create_library_management_system_header(checkout_page)

    def back_to_main_button_pressed():
        create_main_page()
        checkout_page.destroy()
    back_to_main_button = tk.Button(
        checkout_page, 
        width = 8, 
        text = "< Main", 
        font = ('Helvetica', 26), 
        bd=0, 
        background = "#ee8800", 
        foreground = "white",
        command = back_to_main_button_pressed)
    add_hover_effect_to_widget(
        back_to_main_button, 
        '#eeaa33', 
        '#ee8800')
    back_to_main_button.pack(
        side = "left", 
        anchor = "nw")

    def back_to_search_list_button_pressed():
        create_search_result_page(window)
        checkout_page.destroy()
    back_to_search_list_button = tk.Button(
        checkout_page, 
        width = 9, 
        text = "< List", 
        font = ('Helvetica', 26), 
        bd=0, 
        background = "#55aa55", 
        foreground = "white", 
        command = back_to_search_list_button_pressed)
    add_hover_effect_to_widget(
        back_to_search_list_button, 
        '#55aa88', 
        '#55aa55')
    back_to_search_list_button.pack(
        side = "right", 
        anchor = "ne")

    book_list_frame = book_list_frame = tk.Frame(
        checkout_page, 
        bg = "#eeeeee")
    book_list_canvas = tk.Canvas(
        book_list_frame, 
        width = 1100, 
        height = 980, 
        bg = "#eeeeee", 
        highlightthickness = 0)
    scrollbar = ttk.Scrollbar(
        book_list_frame, 
        orient="vertical", 
        command=book_list_canvas.yview)
    scrollable_frame = tk.Frame(
        book_list_canvas, 
        bg = "#eeeeee")

    # bind the canvas scroll region to scrollable_frame
    scrollable_frame.bind(
        "<Configure>",
        lambda e: book_list_canvas.configure(
            scrollregion=book_list_canvas.bbox("all")
        )
    )

    # put the scrollable_frame into canvas
    book_list_canvas.create_window(
        (0, 0), 
        window=scrollable_frame, anchor="nw")

    # bind the scroll control to scrollbar
    book_list_canvas.configure(yscrollcommand=scrollbar.set)
    
    # show how many results found
    ttk.Label(
        scrollable_frame, 
        text = str(len(checkout_list)) + " book ready for checkout", 
        font = ('Helvetica', 30), 
        background = "#eeeeee", 
        width = 45
        ).pack(padx = 80, pady = 20)

    # checkout confirmation ui group
    checkout_confirm_frame = tk.Frame(
        scrollable_frame, 
        background = "#ffffff")
    # prompt the user to enter the member ID
    ttk.Label(
        checkout_confirm_frame, 
        text = "Please enter you member ID to checkout", 
        font = ('Helvetica', 20), 
        background = "#ffffff"
        ).pack(pady = 20)
    
    # entry box for entering member ID
    member_ID = tk.StringVar()
    member_ID_box = tk.Entry(
        checkout_confirm_frame, 
        textvariable = member_ID, 
        width = 35, 
        font = ('Helvetica', 32), 
        background = "#eeeeee", 
        bd=0, 
        borderwidth=7, 
        relief=tk.FLAT)
    add_hover_effect_to_widget(
        member_ID_box, 
        '#f5f5f5', 
        '#eeeeee')
    member_ID_box.pack()

    # message displayed to the user if there is any error
    message_var = tk.StringVar()
    return_message = tk.Label(
        checkout_confirm_frame, 
        textvariable = message_var, 
        font = ('Helvetica', 20), 
        background = "#ffffff")
    return_message.pack(
        side = "left", 
        pady = 20, 
        padx = 200, 
        anchor = "w")

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
            # clear checkout list, since all books have been checked out
            checkout_list = []
            checkout_page_refresh()
        elif member_id_validation_result == 1:
            # if the id input is not 4 digits
            message_var.set("Member ID should be 4-digits")
            return_message.config(foreground = "#ff0000")
        elif member_id_validation_result == 2:
            # if the member id input not only contains numbers
            message_var.set("Member ID should be a number")
            return_message.config(foreground = "#ff0000")

    # place holder used to avoid the confirm checkout button being pushed out of
    # the checkout confirm frame
    tk.Frame(
        checkout_confirm_frame, 
        width = 149, 
        background = "#ffffff"
        ).pack(side = "right")

    confirm_checkout_button = tk.Button(
        checkout_confirm_frame, 
        width = 8, 
        text = "Confirm", 
        font = ('Helvetica', 26), 
        bd=0, 
        background = "#0088ee", 
        foreground = "white", 
        command = confirm_checkout_button_pressed)
    add_hover_effect_to_widget(
        confirm_checkout_button, 
        '#33aaee', 
        '#0088ee')
    confirm_checkout_button.pack(side = "right")

    checkout_confirm_frame.pack(
        fill = "x", 
        pady = 10)

    # add search results to display frame line by line
    for i in range(len(checkout_list)):
        # checkout_list stores the full details of book, 
        # same as search_results above
        make_record(
            scrollable_frame, 
            checkout_list[i], 
            "Remove", 
            '#cc0000', 
            '#ee0000', 
            checkout_page_refresh, 
            1)

    book_list_frame.pack()
    book_list_canvas.pack(
        side="left", 
        fill="both",
        expand=True)
    scrollbar.pack(
        side="right", 
        fill="y")

    book_list_frame.pack(fill="y")

    checkout_page.pack(fill = "both")

def checkout_page_refresh():
    # destroy current book result page
    checkout_page.destroy()
    # recreate boo result page (refresh to show in cart button changes)
    create_checkout_page(window)



def create_detail_page():



#--------------------------< general functions />-------------------------------
def create_library_management_system_header(parent):
    # green background containing title and copyright
    title_green_canvas = tk.Canvas(
        parent, 
        bg = "#55aa55", 
        height = 150, 
        highlightthickness = 0)
    # big large title
    title = title_green_canvas.create_text(
        500, 
        70, 
        text = "Library Management System", 
        font = ('Helvetica', 40, 'bold'), 
        fill = "white")
    # copyright
    copyright_text = title_green_canvas.create_text(
        1300, 
        120, 
        text = "© Lin Zexin     v1.0  13/12/2019", 
        font = ('Helvetica', 15), 
        fill = "white")
    # fill horizontally
    title_green_canvas.pack(
        fill = "x", 
        side = "top")


def member_id_validation(input_id):
    """
    function used to check if the input member id is valid
    """
    if len(input_id) != 4:
        # if the id input is not 4 digits
        return 1
    elif input_id.isdigit():
        # if the input id is a number
        return 0
    else:
        # if not a number
        return 2


def make_record(
    parent, 
    record, 
    button_text, 
    button_original_color, 
    button_hover_color, 
    additional_button_function,
    mode = 0):
    """
    function used to make the information block on book search result page and
    the check out page, mode 0 for add to cart mode, mode 1 for remove from cart
    mode
    """
    # check if the record input has enough information needed
    if len(record) < 4:
        return
    record_frame = tk.Frame(
        parent, 
        bg = "#ffffff")
    # book title
    tk.Label(
        record_frame, 
        text = str(record[1]), 
        font = ('Helvetica', 18), 
        bg = "#ffffff", 
        anchor = "w"
        ).pack(fill = "x", pady = 20, ipady = 10, padx = 50)
    # book details
    tk.Label(
        record_frame, 
        text = "ID: " + str(record[0]) + " > " + "Author: " + str(record[2]) 
        + " > " + "Purchase date: " + str(record[3]), 
        bg = "#ffffff", anchor = "w", justify = tk.LEFT
        ).pack(side = "left", padx = 50)
    # pkaceholder used to aviud the add to cart button being pushed out from the frame
    tk.Frame(
        record_frame, 
        width = 100, 
        background = "#ffffff"
        ).pack(side = "right")
    def button_pressed():
        """
        function bind to the button trigger below
        """
        if mode == 0:
            # when the mode is set to 0 (add to checkout list mode)
            # add the book id to cart list
            checkout_list.append(record)
        elif mode == 1:
            # when the mode is set to 1 (remove from checkout list mode)
            checkout_list.remove(record)
        else:
            # otherwise means the button does nothing
            pass

        if additional_button_function != None:
            additional_button_function()
    button = tk.Button(
        record_frame, width = 8, 
        text = button_text, 
        font = ('Helvetica', 15), 
        bd=0, background = button_original_color, 
        foreground = "white", padx = 20, 
        command = button_pressed
        )
    add_hover_effect_to_widget(
        button, button_hover_color, 
        button_original_color)
    button.pack(
        side = "right", 
        ipadx = 20)

    record_frame.pack(
        fill = "x", 
        pady = 10)


def add_hover_effect_to_widget(
    widget, hover_color = '#ffffff', original_color = '#eeeeee'
    ):
    """
    function used to add hover effects to tk widgets
    (widget is the item waiting to add effect, hover_color is the color when
    mouse is on it, original_color is the color when mouse is not on it)
    """
    def on_enter(e):
        widget['background'] = hover_color
    def on_leave(e):
        widget['background'] = original_color
    widget.bind("<Enter>", on_enter)
    widget.bind("<Leave>", on_leave)

#-----------------------------< program start />--------------------------------
# create main page to start
create_main_page()
window.mainloop()