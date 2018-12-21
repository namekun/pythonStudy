# 39 : Justin
# 14 : John
# 67 : Mike
# 105 : Summer


stuInfo = {
    39: "Justin",
    14: "John",
    67: "Mike",
    105: "Summer"
}


def findStu(num):
    if num in stuInfo:
        return stuInfo[num]
    else:
        return "?"


print(findStu(14))
print(findStu(68))
