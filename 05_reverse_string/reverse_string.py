def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    reversed_list=list(phrase)
    reversed_list.reverse()
    return ''.join(reversed_list)