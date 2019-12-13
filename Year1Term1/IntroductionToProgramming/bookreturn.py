"""
This file handles the return of books, with log entry added
"""

import database as db

def go(book_id):
    """
    This function takes in a list of books then modify the database.txt
    file so that these books are marked as returned
    """
    result = db.modify_member_id(book_id, "0")
    if result == 0:
        # add log entry
        db.return_checkout_log(book_id)
        return result

# test code
if __name__ == "__main__":
    # go([
    #     [['32_0', '"La crise europeene et la premiere guerre mondiale"', 'Pierre Renouvin.', '1/5/2015', '0'], 
    #     ['21_0', '"Institutions of economic growth"', 'J.P.Powelson', '30/3/2015', '0'], 
    # ])
    pass