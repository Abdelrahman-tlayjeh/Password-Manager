from database import database_script

#change searchBy to be accepted by sqlite database
def modify_searchBy(key):
    conv_dict = {
        "Username": "username",
        "e-mail": "eMail",
        "App name": "appName",
        "Password": "passwordKey",
        "Creation date": "creationDate"
    }
    return conv_dict[key]


def search(user, searchBy, searchKeyword, return_all=False):
    res = database_script.search_info(user, modify_searchBy(searchBy), searchKeyword)
    if return_all:
        return res
    else:
        return [list(tup[1:]) for tup in res]


def search_by_keyWord(user, keyWord):
    results = []
    for key in ["username", "eMail", "appName", "passwordKey", "creationDate"]:
        res = database_script.search_info(user, key, keyWord)
        for inf in res:
            results.append(inf)
    return results
    