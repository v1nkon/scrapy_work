
from scrapy.exceptions import NotConfigured
import pymysql, logging
from scrapy import signals

class SqlSetting(object):
    def __init__(self,host,port,user,password, database):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database

class MysqlUtil(object):
    def __init__(self, sql_setting):
        self.sql_setting = sql_setting
        self.connect = None
        self.cursor = None
        pass

    @classmethod
    def from_crawler(cls, crawler):
        if not crawler.settings.getbool("DATABASE_ENABLED"):
            raise NotConfigured
        DATABASE_NAME = crawler.settings.get("DATABASE_NAME", "")
        if DATABASE_NAME == "":
            raise NotConfigured

        DATABASE_HOST = crawler.settings.get("DATABASE_HOST", "")

        DATABASE_PORT = crawler.settings.getint("DATABASE_PORT", 0)

        DATABASE_USER = crawler.settings.get("DATABASE_USER", "")

        DATABASE_PASSWORD = crawler.settings.get("DATABASE_PASSWORD", "")
        sql_setting = SqlSetting(DATABASE_HOST,DATABASE_PORT,DATABASE_USER,DATABASE_PASSWORD, DATABASE_NAME)
        mysql_util = cls(sql_setting)
        crawler.mysql_util = mysql_util
        crawler.signals.connect(mysql_util.spider_opend, signal=signals.spider_opened)
        crawler.signals.connect(mysql_util.spider_closed, signal=signals.spider_closed)

        return mysql_util

    def executemany(self, _sql, items):
        self.cursor.executemany(_sql, items)
        self.connect.commit()
    def execute(self, _sql):
        self.cursor.execute(_sql)
        self.connect.commit()
    def insertValue(self, _sql, _val):
        self.cursor.execute(_sql, _val)
        self.connect.commit()

    def spider_opend(self):
        logging.info("连接数据库")
        self.connect = pymysql.connect(
                            host = self.sql_setting.host,
                            port = self.sql_setting.port,
                            user = self.sql_setting.user,
                            password = self.sql_setting.password,
                            database = self.sql_setting.database
                        )
        self.cursor = self.connect.cursor()

    def spider_closed(self):
        logging.info("关闭数据库连接")
        self.cursor.close()
        self.connect.close()
