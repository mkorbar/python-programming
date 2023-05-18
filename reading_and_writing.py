
# demo_file = open("resources/demo.txt")
#
# contents = demo_file.read()
# print(contents)
#
# demo_file.close()


# boljša alternativa za odpiranje file-a

# with open("resources/demo.txt") as demo_file:
#     contents = demo_file.read()
#     print(contents)


# branje vsebine iz file-a po vrsticah

# with open("resources/demo.txt", "r") as demo_file:
#     demo_lines = demo_file.read().splitlines()
#
#     line_num = 0
#     for line in demo_lines:
#         line_num = line_num + 1
#         print(line_num, line)

####################################
# zapisovanje v file-e


with open("resources/data.txt", "w") as data_file:
    data_file.write("test\n")

