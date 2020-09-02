import pytest


@pytest.mark.parametrize("hdl_val,expected",[
    (71,'Normal'),
    (41,'Borderline Low'),
    (30,'Low')])
def test_check_HDL_(hdl_val,expected):
    from calculator import check_HDL
    result=check_HDL(hdl_val)
    assert result ==expected


@pytest.mark.parametrize("ldl_val,expected",[
    (191,'very high'),
    (161,'high'),
    (131,'borderline high'),
    (120,'normal')])
def test_check_LDL(ldl_val,expected):
    from calculator import check_LDL
    result=check_LDL(ldl_val)
    assert result ==expected


@pytest.mark.parametrize("chl_val,expected",[
    (199,'Normal'),
    (201,'borderline high'),
    (240,'high')])
def test_check_Cholesterol(chl_val,expected):
    from calculator import check_Cholesterol
    result=check_Cholesterol(chl_val)
    assert result ==expected

 


