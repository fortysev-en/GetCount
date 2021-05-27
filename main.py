import json
import os
import urllib
from urllib import request

count = 0

link_name = []
all_links = []
total_dic = {}


def input_data():
    print("=========================")
    get_name = input("Enter a Name: ")
    get_link = input("Enter the Link: ")
    # if get_name == "" or get_link == "":
    #     print("*************************")
    #     print("Enter A Valid Data")
    #     input_data()
    # else:
    link_name.append(get_name)
    all_links.append(get_link)
    print("=========================")

    def get_data():
        if not os.path.exists('total_db.json'):
            open("total_db.json", "w")
        # open the existing file and update total_dir
        with open("total_db.json", encoding="utf8") as infile:
            #check if the file is empty, if yes, then pass
            if os.stat("total_db.json").st_size != 0:
                total_dic.update(json.load(infile))
                print(total_dic)
            else:
                pass

    def update_data():
        # add user input key value to total_dic
        res = {link_name[i]: all_links[i] for i in range(len(link_name))}
        total_dic.update(res)

        # wtite the file with updated data
        with open("total_db.json", "w") as outfile:
            json.dump(total_dic, outfile)

    get_data()
    update_data()
    print("*************************")
    print("New Entry Added")

    def choice_two():
        print("=========================")
        print("1. Add More Links")
        print("2. View Live Count")
        print("3. Exit")
        print("=========================")

        ch = int(input("Enter Your Choice: "))

        if ch == 1:
            input_data()

        elif ch == 2:
            view_data()

        elif ch == 3:
            pass

    choice_two()


def view_data():
    total_dic.clear()
    global count
    with open("total_db.json", encoding="utf8") as infile:
        # check if the file is empty, if yes, then pass
        if os.stat("total_db.json").st_size != 0:
            total_dic.update(json.load(infile))
        else:
            pass

        print("=========================")
        print("Live Count Are As Follows: ")
        print("=========================")
        for key in dict(total_dic).keys():
            link_name.append(key)
        for value in dict(total_dic).values():
            all_links.append(value)
        for items in all_links:
            file = urllib.request.urlopen(items)
            for line in file:
                decoded_line = line.decode("utf-8")
                print(link_name[count] + ":\t" + decoded_line[9:-1])
                print("*************************")
                count += 1


def choice():
    print(r'''

    ██████╗ ███████╗████████╗ ██████╗ ██████╗ ██╗   ██╗███╗   ██╗████████╗
    ██╔════╝ ██╔════╝╚══██╔══╝██╔════╝██╔═══██╗██║   ██║████╗  ██║╚══██╔══╝
    ██║  ███╗█████╗     ██║   ██║     ██║   ██║██║   ██║██╔██╗ ██║   ██║   
    ██║   ██║██╔══╝     ██║   ██║     ██║   ██║██║   ██║██║╚██╗██║   ██║   
    ╚██████╔╝███████╗   ██║   ╚██████╗╚██████╔╝╚██████╔╝██║ ╚████║   ██║   
     ╚═════╝ ╚══════╝   ╚═╝    ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   

                a tool to manage Count API links
                            by
                        fortyseven                                                                      
                https://fortysev-en.github.io''')
    print("                         ")
    print("=========================")
    print("1. Input New Link")
    print("2. View Live Count")
    print("3. Exit")
    print("=========================")

    ch = int(input("Enter Your Choice: "))

    if ch == 1:
        input_data()

    elif ch == 2:
        view_data()

    elif ch == 3:
        pass


choice()

