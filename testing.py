import json
import os
from collections import defaultdict
import urllib
from collections import defaultdict
from urllib import request
# person_dict = defaultdict(list)
#
# with open("total_db.json", encoding="utf8") as f:
#     person_dict.update(json.load(f))
#
# print(person_dict)

link_name = []
all_links = []
total_dic = {}

link_name.append(input("Enter a Name: "))
all_links.append(input("Enter the Link: "))


with open("total_db.json", encoding="utf8") as infile:
    if os.stat("total_db.json").st_size != 0:
        total_dic.update(json.load(infile))
    else:
        pass

for key in link_name:
    for value in all_links:
        total_dic[key] = value
        break

with open("total_db.json", "w") as outfile:
    json.dump(total_dic, outfile)

with open("total_db.json", "w") as outfile:
    json.dump(total_dic, outfile)

for key in dict(total_dic).keys():
    print(key)

for value in dict(total_dic).values():
    print(value)

print(link_name)
print(all_links)
# print(dict(total_dic).values())
# for i, j in zip(link_name, all_links):
#     total_dic[i].append(j)
#
# with open("total_db.json", "w") as outfile:
#     json.dump(total_dic, outfile)
