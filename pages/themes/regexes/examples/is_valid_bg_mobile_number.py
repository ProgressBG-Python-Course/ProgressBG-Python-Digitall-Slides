import re

def is_valid_bg_mobile_number(number):
    """ Validates a Bulgarian mobile number.
        Note:
            The format of a valid Bulgarian mobile number is: +359 XX XDDD DDD,
            where X is in [7, 8, 9], and D is in [0-9].
        Args:
            number (str): The mobile number to be validated.

        Returns:
            bool: True if the number is a valid Bulgarian mobile number, False otherwise.
    """
    rg = re.compile(r'^\+359\s[7-9]{2}\s[7-9]\d{3}\s\d{3}$')

    m = rg.match(number)

    return True if m else False


if __name__=="__main__":
    phone_numbers = [
        '+359 88 7123 456', #yes
        '+359 88 7123456',  #no
        '+359 88 1123 456', #no
        '+359 87 9123 456'  #yes
    ]

    for number in phone_numbers:
        if is_valid_bg_mobile_number(number):
            print(f'{number:18} #yes')
        else:
            print(f'{number:18} #no')