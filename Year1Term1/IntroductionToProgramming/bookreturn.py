import database as db

def go(book_id):
    result = db.modify_member_id(book_id, "0")
    if result == 0:
        # add log entry
        pass
    else:
        pass
    return result