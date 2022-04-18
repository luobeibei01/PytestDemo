import pytest
@pytest.fixture(scope='session')
def BoxId():
    '''
    可以下单的盲盒ID
    '''
    return [793,792,354,386,356,355]