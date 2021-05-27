import json
import os
import urllib
from collections import defaultdict
from urllib import request

count = 0

link_name = []
all_links = []
total_dic = {}


def input_data():
    # get_name = input("Enter a Name: ")
    link_name.append(input("Enter a Name: "))
    # get_link = input("Enter the Link: ")
    all_links.append(input("Enter the Link: "))

    def input_repeat():
        # open the existing file and update total_dir
        with open("total_db.json", encoding="utf8") as infile:
            #check if the file is empty, if yes, then pass
            if os.stat("total_db.json").st_size != 0:
                total_dic.update(json.load(infile))
            else:
                pass

        # add user input key value to total_dic
        for key in link_name:
            for value in all_links:
                total_dic[key] = value
                break

        # wtite the file with updated data
        with open("total_db.json", "w") as outfile:
            json.dump(total_dic, outfile)

    input_repeat()
    print("*********************************************")
    print("New Entry Added")

    def choice_two():
        print("1. Add More Links")
        print("2. View Live Count")
        print("3. Exit")

        ch = int(input("Enter Your Choice: "))

        if ch == 1:
            input_data()
            input_repeat()

        elif ch == 2:
            view_data()

        elif ch == 3:
            pass

    choice_two()


def view_data():
    global count
    with open("total_db.json", encoding="utf8") as infile:
        # check if the file is empty, if yes, then pass
        if os.stat("total_db.json").st_size != 0:
            total_dic.update(json.load(infile))
        else:
            pass

        for key in dict(total_dic).keys():
            link_name.append(key)
        for value in dict(total_dic).values():
            all_links.append(value)
        for items in all_links:
            file = urllib.request.urlopen(items)
            for line in file:
                decoded_line = line.decode("utf-8")
                print(link_name[count] + decoded_line[8:-1])
                count += 1


def choice():
    print("1. Input New Link")
    print("2. View Live Count")

    ch = int(input("Enter Your Choice: "))

    if ch == 1:
        input_data()

    elif ch == 2:
        view_data()


choice()

