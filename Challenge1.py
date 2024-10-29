def type_check(input_output):
    def compare_types(*expected_types):
        if input_output == "in":
            """ Decorate to check input types. """
            def compare_input(func):
                def decorated_input(*args, **kwargs):
                    """ Check for input type mismatch. """
                    is_valid_input = True
                    for arg in args:
                        if not any(isinstance(arg, t) for t in expected_types):
                            is_valid_input = False
                            break
                    
                    if not is_valid_input:
                        result_str = ', '.join(str(t) for t in expected_types)
                        print(f"Invalid input arguments, expected {result_str}!")
                        
                    return func(*args, **kwargs)
                return decorated_input
            return compare_input
        
        elif input_output == "out":
            """ Decorate to check output types. """
            def compare_output(func):
                def decorated_output(*args, **kwargs):
                    """ Check for output type mismatch. """
                    result = func(*args, **kwargs)
                    
                    if not any(isinstance(result, t) for t in expected_types):
                        result_str = ', '.join(str(t) for t in expected_types)
                        print(f"Invalid output value, expected {result_str}!")
                    
                    return result
                return decorated_output
            return compare_output
    return compare_types