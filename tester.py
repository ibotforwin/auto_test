from auto_test import test_typematching


def int_ret_newfile(number: int) -> str:
    string="cactusmonster"
    # print(string)
    # return type(number)
    return string

print(test_typematching(globals()))