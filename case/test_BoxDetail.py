import pytest
import pymysql
import random
from conf.sysconf import host
import requests

def setup():
    print('初始化完成')
# @pytest.mark.parametrize("BoxId")
def test_BoxDetail(BoxId):
    box_id =str(random.choice(BoxId))
    url = host+'/api/v1/mall/item/box/detail?box_id='+box_id
    res = requests.get(url=url,verify=False)
    assert res.json()['error_msg']=='success'
    assert res.json()['data']['id'] in BoxId
    assert res.json()['data']['sku_list'][0]['name']=='一发入魂'
    assert res.json()['data']['sku_list'][1]['name'] == '欧气双连'
    assert res.json()['data']['sku_list'][2]['name'] == '霸气三连'
    # assert res.json()['data']['sku_list'][3]['name'] =='霸气万连' or '豪气五连'

    # print(res.json())

