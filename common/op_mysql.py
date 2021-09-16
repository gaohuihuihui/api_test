import pymysql


class OpMysql():
    def __init__(self,host,user,password,database):
        try:
            self.conn=pymysql.connect(host=host,user=user,password=password,database=database)
            self.cur=self.conn.cursor()
        except pymysql.Error as e:
            print("connect mysql error")


if __name__=="__main__":
    pass

