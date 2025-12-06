#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """
    Prints x elements of a list, stopping if x is too large.
    Uses try/except to detect the end of the list without using len().
    
    Returns: The real number of elements printed.
    """
    count = 0
    i = 0
    try:
        # Loop up to x
        while i < x:
            # Attempt to access and print the element. 
            # This is where IndexError will occur if the list runs out.
            print("{}".format(my_list[i]), end="")
            count += 1
            i += 1
    except IndexError:
        # We catch the IndexError and simply stop the printing attempt.
        # The 'count' already holds the number of successfully printed elements.
        pass
    
    # This must run regardless of whether an error occurred or not, 
    # to complete the line output as required.
    print() 
    
    return count
