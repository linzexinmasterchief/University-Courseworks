import tkinter as tk
from tkinter import ttk

import database as db

# input a list of book, output a sorted list of book
# sorted based on the popularity (amount of apperance in logfile)
def go(book_list = []):
    borrow_count_per_year_list = []
    for book in book_list:
        # book[0] is id, split("_")[0] is the general id, the first element of
        # book history is the amount of borrow per year list
        borrow_count_per_year_tuple = db.get_book_history(book[0].split("_")[0])[0]
        total_borrow = 0
        for amount in borrow_count_per_year_tuple:
            total_borrow += amount
        borrow_count_per_year_list.append(total_borrow)
        

# test code
if __name__ == "__main__":
    print(go([
        ['70_0', '"Highly dispersed aerosols"', 'N.A. Fuchs and A.G. Sutugin.', '1/9/2015', '0'],
        ['69_0', '"Molecules and life : historical essays on the interplay of chemistry and biology"', 'J.S. Fruton.', '28/8/2015', '0'],
        ['68_0', '"Fine powders : preparation', ' properties and uses"', 'C.R. Veale.', '26/8/2015', '0']
    ]))