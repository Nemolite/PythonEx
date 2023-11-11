from main import oper,get_info_of_file

def test_oper():
    assert oper(4,2)==2


def test_get_info_of_file():
    assert get_info_of_file == ['one', 'two', 'three']



