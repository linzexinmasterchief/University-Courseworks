def search_by_name(target_book_name = ""):
    # do nothing if no name given
    if target_book_name == "":
        # [] represents not found
        return []

    f = open("database.txt","r")
    database_arr = f.readlines()
    f.close()

    # search_results is [] by default which means target not found
    search_results = []
    for record in database_arr:
        # [:-1] removes the last \n character in record_arr
        record_arr = record.split(',')[:-1]
        # in record_arr, 0: book id, 1: book name, 2: author name, 3: purchase date, 4: Member id (0 if not borrowed)
        if target_book_name == record_arr[1]:
            search_results.append(record_arr)
    return search_results

def search_by_id(target_book_id = ""):
    # do nothing if no name given
    if target_book_id == "":
        # [] represents not found
        return []

    f = open("database.txt","r")
    database_arr = f.readlines()
    f.close()

    # search_results is [] by default which means target not found
    search_results = []
    for record in database_arr:
        # [:-1] removes the last \n character in record_arr
        record_arr = record.split(',')[:-1]
        # in record_arr, 0: book id, 1: book name, 2: author name, 3: purchase date, 4: Member id (0 if not borrowed)
        if target_book_id == record_arr[0]:
            search_results.append(record_arr)
    return search_results

book_list = search_by_id("1")
print(book_list)