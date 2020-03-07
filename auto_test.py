import inspect
import types
from create_object_by_type import create_object


def test_typematching(glob):
    autotest_result = {}

    # Create a list of functions that can be tested. This requires type hints for all parameters and return.
    for function_name, function_pointer in glob.items():
        # Ignore non functions
        if not isinstance(function_pointer, types.FunctionType):
            continue

        # Ignore this function
        if function_name == inspect.currentframe().f_code.co_name:
            continue

        parameters = inspect.getfullargspec(function_pointer).args
        hints = inspect.getfullargspec(function_pointer).annotations

        # Ensure a return type hint exists
        if 'return' not in hints:
            continue

        # Ensure all parameters type hints exist
        def all_parameters_hinted() -> bool:
            for param in parameters:
                if param not in hints:
                    return False
            return True

        if not all_parameters_hinted():
            continue

        autotest_result[function_name] = function_pointer

    # Test the given functions
    for function_name, function_pointer in autotest_result.items():

        # This function only works if all parameters are hinted so the argument list can be built from hint list
        hints = inspect.getfullargspec(function_pointer).annotations

        # Convert return types of None to NoneType
        hinted_return_type = type(None) if hints['return'] is None else hints['return']

        # Build the argument list
        arguments = {}
        for parameter_name, parameter_type in hints.items():

            # Skip return hint
            if parameter_name == 'return':
                continue

            # Define automatically generated arguments for all other hints
            arguments[parameter_name] = create_object(parameter_type)

        # Call function and check return type
        result = function_pointer(*arguments)
        if isinstance(result, hinted_return_type):
            autotest_result[function_name] = 'Passed'
        else:
            autotest_result[function_name] = 'Failed'

    return autotest_result
