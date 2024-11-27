def is_a_bush(potential_bush, total_cost):
    valid_names = ("храст", "bush", "shrub")
    
    name = potential_bush.get('name', '').lower()

    # Checking if the name is valid
    for curr_name in valid_names:
        if curr_name.lower() == name:
            cost = potential_bush.get('cost', 0)

            # Checking if the cost is valid - int or float
            if isinstance(cost, (int, float)):
                total_cost += cost
                
            return True, total_cost
                
    return False, total_cost
                    
def function_that_says_ni(*args, **kwargs):
    total_cost = 0
    unique_letters = set()

    # Looping through all args and searching for a bush
    for arg in args:
        if isinstance(arg, dict):
            _, total_cost = is_a_bush(arg, total_cost)

    # Looping through all kwargs and searching for a bush
    for var_name, kwarg in kwargs.items():
        if isinstance(kwarg, dict):
            is_bush, total_cost = is_a_bush(kwarg, total_cost)
            if is_bush:
                unique_letters.update(set(var_name))
    
    unique_symbols_count = len(unique_letters)

    if (int(total_cost) != 0 and total_cost <= 42 and unique_symbols_count >= 0 
       and unique_symbols_count % int(total_cost) == 0):
        return f"{total_cost:.2f}лв"
    else:
        return "Ni!"