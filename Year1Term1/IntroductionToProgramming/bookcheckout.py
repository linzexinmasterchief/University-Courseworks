import database as db


# member_id is a 4-digit numebr and checkout_list is a list containing the full detail of the book being checked out
def go(checkout_list = [], member_id = "0"):
    # since only the available books can be add to the checkout_list, there is no need to check again
    for target_book in checkout_list:
        
        result = db.modify_member_id(target_book[0], member_id)
        # check if this checkout is succeed
        if result != 0:
            # add log entry
            db.log("")
            # stop checkout process and report back (highly unlikely)
            return result
        else:
            pass
    return 0