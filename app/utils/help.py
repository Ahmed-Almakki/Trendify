"""
containg a helper fucntions make the work clean
"""


def conectModel(arguments: dict) -> dict:
    """
    connect each parameter to it's Model
    :param arguments: dictionary contain multiple paramter
    :return: a dictionary contain the model and it's paramter
    """
    validFilters = ['Cloth.color', 'Top.sleeve', 'Bottom.length', 'Cloth.company']
    big_dict = {}
    Cloth, Top, Bottom = {}, {}, {}
    for key in validFilters:
        frst = key.split('.')[0]
        scnd = key.split('.')[1]
        if scnd in arguments.keys():
            if frst == "Cloth":
                Cloth[scnd] = arguments[scnd]
                big_dict['Cloth'] = Cloth
            elif frst == "Top":
                Top[scnd] = arguments[scnd]
                big_dict['Top'] = Top
            else:
                Bottom[scnd] = arguments[scnd]
                big_dict['Bottom'] = Bottom
    return big_dict
