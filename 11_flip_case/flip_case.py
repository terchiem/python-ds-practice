def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    flipped = ''

    for ch in phrase:
        if ch.lower() == to_swap.lower():
            if ch == ch.lower():
                flipped += ch.upper()
            else:
                flipped += ch.lower()
        else:
            flipped += ch
    
    return flipped