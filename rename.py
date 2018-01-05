# -*- coding: utf-8 -*-
import os
import glob

episode_name_list = {1: "Descenso", 2: "The Sword of Simon Bolivar", 3: "The Men of Always", 4: "The Palace in Flames", 5: "There Will Be a Future", 6: "Explosivos", 7: "You Will Cry Tears of Blood", 8: "La Gran Mentira", 9: "La Catedral", 10: "Despegue"}

files = glob.glob('Nar*')

# print(files)
# print(episode_name_list)

for file in files:
    # print(file)
    os.rename(file, "Narcos {} {}.mkv".format(file.split(" ")[1], episode_name_list[int(file.split(" ")[1][-2:])]))

    # print("Narcos {} {}.mkv".format(file.split(" ")[1], episode_name_list[int(file.split(" ")[1][-2:])]))
# for file in files:
#     if file.split(".")[-1] == 'mkv':
#         # os.rename(file, "How to Get Away with Murder {}.mkv".format(file.split(".")[6]))
#         pass
#     else:
#         # print(file)
#         os.chdir(file)
#         inside = glob.glob("How*")
#         # print(inside)
#         for new_file in inside:
#             # print(new_file)
#             if new_file.split(".")[-1] == 'mkv':
#                 # print(new_file.split("."))
#                 # os.rename(new_file, "How to Get Away with Murder {}.mkv".format(new_file.split(".")[6]))
#                 pass
#         os.chdir("..")
#     # print(file.split("."))
#     # os.rename(file, '{}.m{}'.format(file.split('m')[0],file.split("m")[1]))
