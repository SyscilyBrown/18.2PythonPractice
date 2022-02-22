def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    phrase_dict = {}

    for letter in phrase:
        #with .get(), 0 is the default. If the letter hasn't yet been count it, set it to zero, but add one if it's already been counted
        phrase_dict[letter] = phrase_dict.get(letter, 0)+1