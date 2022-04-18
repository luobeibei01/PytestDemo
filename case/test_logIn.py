import json

import pytest
import requests
from conf.sysconf import host

# @pytest.allure('登录接口')
def test_LogIn():
    url = host + '/api/v1/account/login'
    print(url)
    payload = {
         "country_code": "86",
         "sms_code": 'EGJAqB6hTSKj+fyJnTiZyxtra7psb3WtE0NpxsJ4bZI/HruF7udJPKFn8kd3377Mu/WoDSptwGN4\nBQtvn6I9N2qx40zVGNOBHeNYFvHEiKLOEPRjD0TD0bbbJiRAWKkbPgtf7B8tIUPqJpw38zfBSucB\n2T5j3XxGOJsGUuIbO7U=\n',
         "phone_number": 't16yRnNopCf4vstmxyoiZKUlZQ+0l601NgNCtEC1eDJ5EbxGuJrCR7NRdEj4bx0CYUS2mw6vtczI\nFAKuqtx65pdsrkzEQrjLWzykQKtVf/8xjg4MBA4lZfdOj2XFn74Gnw55807dEOuz4QMA3Jw26CVj\nzCIGB2W9eX7irlsdA4I=\n'
    }
    res=requests.post(url=url,data=json.dumps(payload,separators=(',',':')),verify=False)
    assert res.json()['error_msg']=='操作成功'
    assert res.json()['data']['uid']==1000218
