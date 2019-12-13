import database as db

def go(target = ""):
    result = []
    if target.isdigit():
        # if the input is all numbers, then treat it as an id
        result = db.search_by_id(target)
    else:
        # otherwise treat it as a book name
        result = db.search_by_name(target)
    # add log entry
    return result
