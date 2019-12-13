"""
This file contains functions used for modifing database.txt and logfile.txt
"""
from datetime import date

# sign given for not borrowed book id is "0"
in_storage_sign = "0"
    

def search_by_name(target_book_name = ""):
    """
    this function takes in a book name and returns a list of possible matches
    """
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
    """
    this function takes in a book id and returns a list of possible matches
    """
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
    """
    this function takes in a target id and a member id,
    then it will modify the member id in database based on the mode
    (return / checkout)
    """

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


def get_book_history(general_book_id):
    """
    this function takes in a general book id (x when id is x_y, shared by
    the same series of books) and return a list [[borrow_count_per_year], 
    first_borrow_date, last_borrow_date]
    """
    f = open("logfile.txt", 'r')
    
    history = f.readlines()
    record_list = []
    for record in history:
        # in logfile.txt, the second last part of the record is book id
        # (last is \n)
        record_arr = record.split(",")[:-1]
        if record_arr[-1].split("_")[0] == general_book_id:
            record_list.append(record_arr)

    if len(record_list) == 0:
        # not found
        return 1
    # sort by the first element, which is borrow time
    record_list.sort()
    
    # so the first borrow time is the time of first element
    # same as the last borrow time
    first_borrow_year = int(record_list[0][0].split("/")[0])
    last_borrow_year = int(record_list[-1][0].split("/")[0])
    borrow_count_per_year = []
    year = int(first_borrow_year) - 1
    for record in record_list:
        # record[0]: yyyy/mm/dd
        if year == int(record[0].split("/")[0]):
                
            borrow_count_per_year[year - first_borrow_year] += 1
        else:
            year += 1
            borrow_count_per_year.append(0)
            
    return (borrow_count_per_year, first_borrow_year, last_borrow_year)


def checkout_log(book_id):
    """
    function used to add new log entries to the logfile
    """
    f = open("logfile.txt", "r+")
    content = f.readlines()
    # ",," means no return date yet
    content.append(date.today().strftime("%m/%d/%y") + ",," + book_id + ",")
    # clear
    f.seek(0)
    f.truncate()
    # write new
    f.writelines(content)
    f.close()

def return_checkout_log(book_id):
    """
    function used to locate borrow log entry that haven't been returned
    take in complete id book_id (include general and special id)
    """
    f = open("logfile.txt", "r+")
    content = f.readlines()
    for i in range(len(content)):
        # splite entry into array
        entry = content[i].split(",")[:-1]
        # if id match and return date is blank
        if entry[-1] == book_id and entry[-2] == "":
            # add return date to blank space
            entry[-2] = date.today().strftime("%m/%d/%y")
        # recombine entry into string and replace old string
        content[i] = entry[0] + "," + entry[1] + "," + entry[2] + ",\n"
    # clear
    f.seek(0)
    f.truncate()
    # rewrite
    f.writelines(content)
    f.close()


# test code
if __name__ == "__main__":
    checkout_log("12_2")
    return_checkout_log("12_2")