def checkCorrectParameter(arg):
    lst = ["color", "company", "gender"]
    count = 0
    if len(arg) == len(lst):
        for i in lst:
            if i in arg:
                count += 1
        if count == len(arg):
            return True
        return False

    elif len(arg) < len(lst):
        for i in arg:
            if i in lst:
                count += 1
        if count == len(arg):
            return True
        return False

    else:
        return False
