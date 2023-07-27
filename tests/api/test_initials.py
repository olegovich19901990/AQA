def test_lists():
    assert [1,2,3] == [1,2,3]
   #if [1,2,3] != [1,2,3]
    #    raise AssertionError("Not equal")
    #identical to assert


def test_lists_fail():
    assert ["a",2,3] == [1,2,3]
