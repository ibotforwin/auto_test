import auto_test


def all_hints_valid(number: int) -> str:
    return "string"


def all_hints_invalid(number: int) -> str:
    return 0


def no_hints(number):
    return "string"


def input_hint_no_return_hint(number: int):
    return "string"


def no_input_hint_return_hint(number) -> str:
    return "string"


def input_hint_none_return_valid(number: int) -> None:
    return None


def input_hint_none_return_invalid(number: int) -> None:
    return "string"


def no_parameters_return_hint_valid() -> str:
    return "string"


def arg_list_return_hint_valid(*args) -> str:
    return "string"


def test_all():
    print(auto_test.test_typematching(globals()))


test_all()
