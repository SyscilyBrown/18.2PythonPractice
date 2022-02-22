
def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    #return [True for items in lst if isinstance(items, list)]
    #return [lsts for lsts in lst if isinstance(lsts, list)]
    for item in lst:
        if not isinstance(item, list):
            return False
    return True