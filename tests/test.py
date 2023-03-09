from MyPackage import myModule

def test_top_n():
    """ 
    Make sure top_n works right
    """
    assert myModule.top_n([7,8,3,5,6,9], 3) == [9,8,7], 'Incorrect'
    assert myModule.top_n([8,3,5,6,9], 4) == [9,8,6,5], 'Incorrect'
    assert myModule.top_n([7,6,9], 2) == [9,7], 'Incorrect'