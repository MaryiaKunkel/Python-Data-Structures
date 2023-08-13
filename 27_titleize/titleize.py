def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    new_phrase=[]
    list=phrase.lower().split(' ')
    for word in list:
        new_phrase.append(word.capitalize())
    return ' '.join(new_phrase)