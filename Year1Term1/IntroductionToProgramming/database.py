# sign given for not borrowed book id is "0"
in_storage_sign = "0"

def search_by_name(target_book_name = ""):
    # do nothing if no name given
    if target_book_name == "":
        # [] represents not found
        return []

    # open file and load file contents to an array
    f = open("database.txt","r")
    database_arr = f.readlines()
    f.close()

    # search_results is [] by default which means target not found
    search_results = []
    for record in database_arr:
        # [:-1] removes the last \n character in record_arr
        record_arr = record.split(',')[:-1]
        # in record_arr, 0: book id, 1: book name, 2: author name, 3: purchase date, 4: Member id (0 if not borrowed)
        # use in instead of "==" allow non-accurate search, both convert to lower case prevents capital letter problem
        if target_book_name.lower() in record_arr[1].lower():
            # if book name found, add this line into search result array
            search_results.append(record_arr)
    return search_results

def search_by_id(target_book_id = ""):
    # do nothing if no name given
    if target_book_id == "":
        # [] represents not found
        return []

    # open file and load file contents to an array
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
            # if book name found, add this line into search result array
            search_results.append(record_arr)
    return search_results

def modify_member_id(target_book_id = "", member_id = ""):
    # is_return is used to tell this function whether this is a return process or a checkout process
    # if input member id match in storage sign, then this is a return process
    # otherwise it is a checkout process
    is_return = member_id == in_storage_sign
    # if is_return parameter is not assigned, return 3
    if is_return == None:
        return 3
    # do nothing if no name given
    if target_book_id == "":
        # 2 represents not found
        return 2

    f = open("database.txt","r+")
    database_arr = f.readlines()

    for line_num in range(len(database_arr)):
        # [:-1] removes the last \n character in record_arr
        record_arr = database_arr[line_num].split(',')[:-1]
        # in record_arr, 0: book id, 1: book name, 2: author name, 3: purchase date, 4: Member id (0 if not borrowed)
        if target_book_id == record_arr[0]:
            # if the id of current record is in_storage_sign, then the return book process can't continue
            # likewise, if the id is not in_storage_sign, then this book can't be check out
            if (record_arr[4] == in_storage_sign and not is_return) or (record_arr[4] != in_storage_sign and is_return):
                record_arr[4] = member_id
                # modify the line containing target book id
                database_arr[line_num] = record_arr[0] + "," + record_arr[1] + "," + record_arr[2] + "," + record_arr[3] + "," + record_arr[4] + "," + "\n"
                # clear file
                f.seek(0)
                f.truncate()
                # write new content to file
                f.writelines(database_arr)
                # f.writelines(database_arr)
                f.close()
                # 0 represents checkout successful
                return 0
            else:
                f.close()
                # 1 represents book is borrowed when checkout
                # 1 represents book is not borrowed when return
                return 1
    f.close()
    # 2 represents not found
    return 2