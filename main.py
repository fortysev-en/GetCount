import json
import os
import urllib
from urllib import request

count = 0

link_name = []
all_links = []
total_dic = {}
last_count = {}
last_counts = []


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
            else:
                pass

    def update_data():
        # add user input key value to total_dic
        res = {link_name[i]: all_links[i] for i in range(len(link_name))}
        total_dic.update(res)

        # write the file with updated data
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

    if not os.path.exists('total.json'):
        open("total.json", "w")

    with open("total.json", encoding="utf8") as inf:
        if os.stat("total.json").st_size != 0:
            last_count.update(json.load(inf))
        else:
            pass

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
        for value in dict(last_count).values():
            last_counts.append(value)
        for value in all_links:
            file = urllib.request.urlopen(value)
            for line in file:
                decoded_line = line.decode("utf-8")
                current_count = decoded_line[9:-1]
                if len(last_counts) == 0:
                    print(link_name[count] + ":\t" + current_count)
                if not len(last_counts) == 0:
                    print(link_name[count] + ":\t" + last_counts[count] + "\t" + current_count)
                res2 = {link_name[count]: current_count}
                last_count.update(res2)
                count += 1
    with open("total.json", "w") as outfile:
        json.dump(last_count, outfile)


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

