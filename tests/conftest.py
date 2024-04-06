#import pytest
#
#def pytest_addoption(parser):
#    parser.addoption("--name", action="store")
#
#@pytest.fixture(scope='session')
#def name(request):
#    name_value = request.config.option.name
#    #name_value=float(name_value)
#    print("PSC",name_value)
#    if name_value is None:
#        pytest.skip()
#    return name_value

def score(score):
    return score