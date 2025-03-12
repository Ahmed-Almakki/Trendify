"""
utils function to use inside the app
"""


def checkCorrectParameter(arg, lst):
    """
    check if request have the right parameters of the model
    this help if a request made with wrong parameter name
    :param arg: request parameter
    :param lst: list to check if the parameter belong to one of the Model
    :return: Bool depend on if the correct parameters used
    """
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


def TopOrBottom(req) -> str:
    """
    Help in choose which model to use, Top or Bottom
    :param req: request parameters
    :return: top or bottom Model to use
    """
    lst = ["length", "sleeve"]
    for i in req:
        if i in lst:
            if i == "length":
                return 'bottom'
            return 'top'
