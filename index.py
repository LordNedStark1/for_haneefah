from pathlib import Path
#
# path = Path(r"\root\media\private\me.jpeg")
# print (path)
# path2 = path.home()
# path3 = path.cwd()
# print(path2)
# print (path3)


# from pathlib import Path
# import shutil
# path = Path.cwd()/"new_directory"/"dir_2"/"ridwan.txt"
# #
# path.touch()
# # destination = Path.cwd()/"new_directory2"/"ridwan.txt"
# # path.replace(destination)
#
# # new_path = Path.cwd()/"new_directory3"
# # new_path.rmdir()
#
# path_next = Path.cwd()/"new_directory2"
# if path_next.exists():
#     shutil.rmtree(path_next)

path = Path.cwd()/"new_directory"/ "lovestory.txt"

numbers =[
        [29, 43, 54, 65, 56],
        [23, 45, 66, 65, 67],
        [33, 43, 43, 34, 23],
        [67, 87, 56, 65, 65],
        ]

with open(path, encoding= "utf-8", mode= "w") as file:
    for number in numbers:
        file.write(str(number[0]))
        for num in number[1:]:
            file.write(f",{num}")
        file.write('\n')

with open(path, encoding= "utf-8", mode= "r") as file:
    for numb in
    print(file.readline())
# path.touch()

# file = path.open(mode="w", encoding= "utf-8")
# mass = "i love u soo much and can't stop loving u"
# file.write( mass)
# print(file)
# with path.open(mode="w", encoding= "utf-8") as file:
#     file.write("holle kemi,\n")
#     file.write("I really miss you. I will join in the next class\n")


# with path.open(mode="r+", encoding= "utf-8") as file:
#     print(file.read())
#     file.write("holle kemi,\n")
#     file.write("I really miss you. I will join in the next class\n")


# with path.(mode="a+", encoding= "utf-8") as file:
#     # file.write("holle kemi,\n")
#     # file.write("I really miss you. I will join in the next class\n")
#     print(file.read())
#     file.write("master plus")
#     print(file.read())

# with path.open(mode="r", encoding= "utf-8") as file:
#     # print(file.read())
#     # print(file.readline())
#
#     print(file.readlines()[1])

# with open(path, mode="r", encoding= "utf-8") as file:


# mass = "i love u soo much and can't stop loving u"
# file.write( mass)
# print(file)