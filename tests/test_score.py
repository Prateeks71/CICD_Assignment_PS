import pytest

#def test_name(name):
#    threshold=0.5
#    val='fail'
#    print(name)
#    if(abs(name-threshold)>1e-8):
#        val='pass'
#    assert val=='pass'

#def test_name(name):
#    name=float(name)
#    assert name == float('almond')

def test_score():
    val='fail'
    if(abs(0.329-0.5)<1e-8):
        val='pass'
    assert val=='pass'    