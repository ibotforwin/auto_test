from math import floor
import os
import random



test_string='test_string'
test_float=float(random.random()*10)
test_int=int(floor(random.random()*10))


supported_types=['int','float','str']

autotest_result={}


def int_ret(number: int) -> str:
    string = "cactusmonster"
    # print(string)
    # return type(number)
    return string


def false_test(number: int) -> str:
    floating = 3.2222
    # print(string)
    # return type(number)
    return floating


def test_typematching():




    for name in list(globals()):
        if not name.startswith('__'):
            print(name)


            try:
                return_type=str((globals()[name].__annotations__)['return'])
                autotest_result.update({name:return_type.replace("<class '","").replace("'>","")})
            except:
                # autotest_result.update({name:None})
                continue

    print('checking dict')
    print(autotest_result)


    for func in autotest_result:
        if autotest_result[func]!=None:
            this_func=globals()[func].__annotations__
            for arg in this_func:
                if arg!='return':
                    input_type=str(this_func[arg]).replace("<class '","").replace("'>","")
                    for available in supported_types:
                        if available==input_type:
                            func_return=globals()[func]("test_"+input_type)
                            func_return=globals()[func]("test_"+input_type)
                            print('test ,in')
                            print(func_return)
                            print('test out')
                            actual_return_type=str(type(func_return)).replace("<class '","").replace("'>","")
                            if actual_return_type==autotest_result[func]:
                                print(func)
                                print('Passes')

                                print(type(func))
                                print(autotest_result[func])
                                print(actual_return_type)
                                print('testin name')
                                print(func)
                                autotest_result[func]='Passed'
                            else:
                                autotest_result[func]='Failed'

    print(autotest_result)
    return autotest_result

test_typematching()