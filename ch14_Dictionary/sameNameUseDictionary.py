def findSame(a):
    name_dict = dict()
    for x in a:
        if x in name_dict:
            name_dict[x] += 1
        else:
            name_dict[x] = 1

    result = set()

    for name in name_dict:
        if name_dict[name] >= 2:
            result.add(name)

    return result


name = ["tom", "john", "joe", "tom"]

print(findSame(name))
