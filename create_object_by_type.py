def create_object(arg_type: type):
    # Try to instantiate the empty var
    try:
        empty_var = arg_type()
        if isinstance(empty_var, arg_type):
            return empty_var
    except Exception:  # Anything other than TypeError occurs here?
        pass

    # Try to instantiate a var based on 1 int
    try:
        empty_var = arg_type(1)
        if isinstance(empty_var, arg_type):
            return empty_var
    except Exception:  # Anything other than TypeError occurs here?
        pass

    # Try to instantiate a var based on an increasing number of int values in a tuple
    for i in range(1, 5):
        # Create the arg list
        a = (1 for i in range(i))

        try:
            empty_var = arg_type(*a)
            if isinstance(empty_var, arg_type):
                return empty_var
        except Exception:  # Anything other than TypeError occurs here?
            continue

    raise NotImplementedError('Cannot instantiate a variable of type {}'.format(arg_type))
