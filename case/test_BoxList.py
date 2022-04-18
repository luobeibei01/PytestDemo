import pytest
import requests
from conf.sysconf import host

def test_BoxList():
    url = host + '/api/v1/mall/item/box/list'
    res= requests.get(url=url,verify=False)
    print(res.json())
    assert res.json()['error_msg']=='success'
