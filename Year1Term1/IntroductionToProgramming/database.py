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

def check_out(target_book_id = "", member_id = ""):
    # do nothing if no name given
    if target_book_id == "":
        # -1 represents not found
        return -1

    f = open("database.txt","r+")
    database_arr = f.readlines()

    for line_num in range(len(database_arr)):
        # [:-1] removes the last \n character in record_arr
        record_arr = database_arr[line_num].split(',')[:-1]
        # in record_arr, 0: book id, 1: book name, 2: author name, 3: purchase date, 4: Member id (0 if not borrowed)
        if target_book_id == record_arr[0]:
            if record_arr[4] == "0":
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
                # -1 represents book is borrowed
                return 1
    f.close()
    # -1 represents not found
    return -1

def return_book(target_book_id = ""):
    # do nothing if no name given
    if target_book_id == "":
        # -1 represents not found
        return -1

    f = open("database.txt","r+")
    database_arr = f.readlines()

    for line_num in range(len(database_arr)):
        # [:-1] removes the last \n character in record_arr
        record_arr = database_arr[line_num].split(',')[:-1]
        # in record_arr, 0: book id, 1: book name, 2: author name, 3: purchase date, 4: Member id (0 if not borrowed)
        if target_book_id == record_arr[0]:
            if record_arr[4] != "0":
                record_arr[4] = "0"
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
                # -1 represents book is borrowed
                return 1
    f.close()
    # -1 represents not found
    return -1

# print(search_by_id("1"))