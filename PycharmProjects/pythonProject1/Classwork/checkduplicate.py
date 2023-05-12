def duplicate():
    nameoffood1 = ["rice", "beans", "spaghetti", "rice"]
    #nameoffood2 = ["John", "sultan", "David"]
    count = 0
    for i in nameoffood1:
        for j in range(i+ 1, len(nameoffood1)):
            if nameoffood1[i] == nameoffood1[j]:
                count = count + 1
                if count == 2:
                    print("There is duplicate")
                else:
                    print("there is no duplicate")


duplicate()
# def duplicate2(lzt: list):
#     for item in lzt:
#         if lzt.count(item) > 1:
#             print(f"The item {item} occured more than once")
#         else:
#             print(f"There's no duplicate")



# duplicate2()