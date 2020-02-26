from math import floor
import random
import string

#declaring test variables
test_string = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])
test_float = float(random.random() * 10)
test_int = int(floor(random.random() * 10))

#Currently supported test types (input and return)
supported_types = ['int', 'float', 'str']
autotest_result = {}

#A sample test that returns the anticipated type
def int_ret(number: int) -> str:
    string = "cactusmonster"
    return string

#A sample test that returns the wrong type
def false_test(number: int) -> str:
    floating = 3.2222
    return floating

def test_typematching(glob):
    for name in list(glob):
        if not name.startswith('__'):
            try:
                return_type = str((glob[name].__annotations__)['return'])
                autotest_result.update({name: return_type.replace("<class '", "").replace("'>", "")})
            except:
                continue
    for func in autotest_result:
        if autotest_result[func] != None:
            this_func = glob[func].__annotations__
            for arg in this_func:
                if arg != 'return':
                    input_type = str(this_func[arg]).replace("<class '", "").replace("'>", "")
                    for available in supported_types:
                        if available == input_type:
                            func_return = glob[func]("test_" + input_type)
                            actual_return_type = str(type(func_return)).replace("<class '", "").replace("'>", "")
                            if actual_return_type == autotest_result[func]:
                                autotest_result[func] = 'Passed'
                            else:
                                autotest_result[func] = 'Failed'
    return autotest_result



