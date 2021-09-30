import pymysql
from common import utils,read_config

env=utils.get_dafalut_environment()

codecmap=read_config.read_db()[env]["codecmap"]
platform=read_config.read_db()[env]["platform"]
codemao_app=read_config.read_db()[env]["codemao_app"]


class Mysql():
    def __init__(self,host=codecmap["host"],user=codecmap["user"],password=codecmap["password"],database=codecmap["database"]):
        try:
            self.conn=pymysql.connect(host=host,user=user,password=password,database=database)
            self.cur=self.conn.cursor()
        except pymysql.Error as e:
            print("connect mysql error")



if __name__=="__main__":
    pass
    # mysql=Mysql()
    # mysql.cur.execute("SELECT id from tbl_chapter where package_id="+str(packageId))
    # chapterId=(mysql.cur.fetchone()[0])
    # mysql.cur.close()


