def top_n(items, n):
    """Return the top n items in an array in desc order.
    Arguments:
       items(array): List or array-like object
       n(int): number of items to return
    Return:
       array : top n items in desc order
    Examples:
        >>> top_n([6,5,9,8], 3)
            [9,8,6]
    """
    sorted_items = sorted(items, reverse=True)  #normally sorted() returns list in ascending order, reverse = True brings in output in descending order.
    
    return sorted_items[:n]