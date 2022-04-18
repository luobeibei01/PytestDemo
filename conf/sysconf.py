import records
import pymysql
pymysql.install_as_MySQLdb()

host='https://testservice.muju001.com'
db = records.Database('mysql://inke_db_testuser:inekoedb0testgv3@tx5-inno-funbox-test-db01.bj:3306/funbox_user_account')
# id=db.query('select id from funbox_user_account.user_account where phone=11111112000')

# list=[{1},{2},{3}]
# print(list[0])
# for i in list:
#     print(i)