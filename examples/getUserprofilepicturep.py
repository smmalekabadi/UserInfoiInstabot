# -*- coding: utf-8 -*-


import sys
import os
import xlrd
import json
import requests
import shutil

# from Pyste.infos import use_auto_ptr
from pprint import pprint
import urllib
import xlsxwriter

sys.path.append(os.path.join(sys.path[0], '../instabot'))
from instabot import Bot


# from getdata import *

b = Bot()
# help(b)
b.login(username='union_confederation', password='newpass123')

idd = b.get_userid_from_username('morteza.malekabadi')
user = b.get_user_info(idd);

#

workbook = xlsxwriter.Workbook('Expenses01.xlsx', {'constant_memory': True})
worksheet = workbook.add_worksheet()
# print range(worksheet.nrows)
row = 0;
col = 0;

worksheet.write(row, col, "#")
worksheet.write(row, col + 1, "id")
worksheet.write(row, col + 2, "username")
worksheet.write(row, col + 3, "fullname")
worksheet.write(row, col + 4, "hd_profile_pic_versions 1")
worksheet.write(row, col + 5, "hd_profile_pic_versions 2")
worksheet.write(row, col + 6, "biography")
worksheet.write(row, col + 7, "profile_pic_url")
worksheet.write(row, col + 8, "external_url")

row += 1

k = 1
following = b.get_user_followers("union_confederation")
for i in range(0, len(following)):
    user1 = following[i]
    followers = b.get_user_following(user1)
    for j in range(0, len(followers)):
        print user
        if not user:
            print "hiiii"
            followers = b.get_user_following(user1)
        # user = b.get_user_info(followers[j])
        #
        # else :
        user = b.get_user_info(followers[j])
        print user1
        r = requests.get(str(user['profile_pic_url']), stream=True)

        worksheet.write(k, col, k)
        # worksheet.write(k, col + 1, user["id"])

        worksheet.write(k, col + 2, user["username"])
        worksheet.write(k, col + 3, user["full_name"])
        # if user["hd_profile_pic_versions"][0]["url"] :
        #     worksheet.write(k, col + 4, user["hd_profile_pic_versions"][0]["url"])
        # try :
        #     worksheet.write(k, col + 5, user["hd_profile_pic_versions"][1]["url"])
        # except IndexError:
        #     print

        worksheet.write(k, col + 6, user["biography"])
        worksheet.write(k, col + 7, user["profile_pic_url"])
        worksheet.write(k, col + 8, user["external_url"])
        # workbook.flush()
        if r.status_code == 200:
            with open("D:\linux stuff\instabot-master\\"+str(b.get_username_from_userid(followers[j]))+".jpg", 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)



                # output = open("D:\linux stuff\instabot-master\\"+str(b.get_username_from_userid(followers[j]))+".jpg", "wb")
        # # output = open(str(b.get_username_from_userid(followers[j])) + ".jpg", "wb")
        # output.write(resource.read())
        # output.close()


        k = k + 1



