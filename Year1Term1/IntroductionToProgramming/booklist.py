"""
This file handles the sort of books list in the order of popularity
"""

import tkinter as tk
from tkinter import ttk

import database as db

# input a list of book, output a sorted list of book
# sorted based on the popularity (amount of apperance in logfile)
def go(book_list = []):
    """
    This function takes in a list of books, then sort them in popularity order
    and returns back
    """
    borrow_count_per_year_list = []
    for i in range(len(book_list)):
        # book[0] is id, split("_")[0] is the general id, the first element of
        # book history is the amount of borrow per year list
        borrow_count_per_year_tuple = db.get_book_history(book_list[i][0].split("_")[0])[0]
        total_borrow = 0
        for amount in borrow_count_per_year_tuple:
            total_borrow += amount
            
        # merge two lists, let borrow_count_per_year_list play the role of index
        entry = [total_borrow]
        entry.extend(book_list[i])
        borrow_count_per_year_list.append(entry)
    # sort
    borrow_count_per_year_list.sort()
    sorted_book_list = []
    for i in borrow_count_per_year_list:
        # remove the borrow_count_per_year_list (index)
        sorted_book_list.append(i[1:])
    return sorted_book_list

# test code
if __name__ == "__main__":
    print(go([
        ['70_0', '"Highly dispersed aerosols"', 'N.A. Fuchs and A.G. Sutugin.', '1/9/2015', '0'],
        ['69_0', '"Molecules and life : historical essays on the interplay of chemistry and biology"', 'J.S. Fruton.', '28/8/2015', '0'],
        ['68_0', '"Fine powders : preparation', ' properties and uses"', 'C.R. Veale.', '26/8/2015', '0']
    ]))