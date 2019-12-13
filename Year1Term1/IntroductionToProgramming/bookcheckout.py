"""
This file handles the checkout of books, with log entry added
"""

import database as db

# member_id is a 4-digit numebr and checkout_list is a list containing the full detail of the book being checked out
def go(checkout_list = [], member_id = "0"):
    """
    This function takes in a list of books and a member id, 
    then modify the database.txt file so that these books are borrowed
    by this member
    """
    # since only the available books can be add to the checkout_list, there is no need to check again
    for target_book in checkout_list:
        
        result = db.modify_member_id(target_book[0], member_id)
        # check if this checkout is succeed
        if result == 0:
            # add log entry
            # target_book[0] is book id
            db.checkout_log(target_book[0])
            # stop checkout process and report back (highly unlikely)
            return result
    return 0

# test code
if __name__ == "__main__":
    # go([
    #     [['32_0', '"La crise europeene et la premiere guerre mondiale"', 'Pierre Renouvin.', '1/5/2015', '0'], 
    #     ['21_0', '"Institutions of economic growth"', 'J.P.Powelson', '30/3/2015', '0'], 
    # ])
    pass