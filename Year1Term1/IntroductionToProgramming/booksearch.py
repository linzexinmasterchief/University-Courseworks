import database as db

def go(target = ""):
    result = db.search_by_name(target)
    return result
