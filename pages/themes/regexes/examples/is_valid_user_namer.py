import re

def is_valid_user_name(number):
    """ Validates a User name.

        Note:
            User name must follow next rules:
                1. Must consists of 3 to 10 characters inclusive.
                2. Username can only contain alphanumeric characters, dashes (-) and underscores (_).
                3. The first character of the username must be an alphabetic character

        Args:
            number (str): The user name to be validated.

        Returns:
            bool: True if the name is a valid, False otherwise.
    """
    rg = re.compile(r'''
    ^					# beginning of string
        [a-zA-Z]  		# rule 3
        [\w-]{2,9}		# rule 1 and 2
    $					# end of string
    ''', re.VERBOSE)
    m = rg.match(number)

    return True if m else False


if __name__=="__main__":
    user_names = [
        "ada", 	        # yes
        "a__", 	        # yes
        "a12345",       # yes
        "a1234567890",  # no (rule 1)
        "1aaaaaaa",     # no (rule 3)
        "aaa#", 	    # no (rule 2)
        "a", 		    # no (rule 1)
    ]

    for user_name in user_names:
        if is_valid_user_name(user_name):
            print(f'{user_name:18} #yes')
        else:
            print(f'{user_name:18} #no')