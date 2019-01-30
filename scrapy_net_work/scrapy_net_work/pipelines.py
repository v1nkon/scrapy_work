# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import NotConfigured

class ScrapyNetWorkPipeline(object):

    def spider_opened(self, spider):
        self.logging.info('----------------------open spider----------------------')
    def process_item(self, item, spider):
        return item
    def spider_closed(self, spider):
        self.logging.info('----------------------closed spider----------------------')


class LagouPositionPipeline(object):
    def __init__(self, mysql_util):
        self.mysql_util = mysql_util

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls(crawler.mysql_util)
        return s

    def process_item(self, item, spider):
        mysql_util = self.mysql_util
        _sql = "insert into lagou_position( city ,companyFullName ,companyId ,companyLogo ,companyName ,createTime ,positionId ,positionName ,salary ) values( %(city)s, %(companyFullName)s, %(companyId)s, %(companyLogo)s, %(companyName)s, %(createTime)s, %(positionId)s, %(positionName)s, %(salary)s ) "
        if type(item) == list:
            mysql_util.executemany(_sql, item)
        else:
            mysql_util.insertValue(_sql, item._values)

class LagouPositionDetailPipeline(object):
    def __init__(self, mysql_util):
        self.mysql_util = mysql_util

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls(crawler.mysql_util)
        return s

    def process_item(self, item, spider):
        mysql_util = self.mysql_util
        _sql = "insert into lagou_detail_position( adWord, appShow, approve, businessZones, city, companyFullName, companyId, companyLabelList, companyLogo, companyShortName, companySize, createTime, deliver, district, education, financeStage, firstType, formatCreateTime, gradeDescription, hitags, imState, industryField, industryLables, isSchoolJob, jobNature, lastLogin, latitude, linestaion, longitude, pcShow, plus, positionAdvantage, positionId, positionLables, positionName, promotionScoreExplain, publisherId, resumeProcessDay, resumeProcessRate, salary, score, secondType, skillLables, stationname, subwayline, thirdType, workYear ) values(  %(adWord)s, %(appShow)s, %(approve)s, %(businessZones)s, %(city)s, %(companyFullName)s, %(companyId)s, %(companyLabelList)s, %(companyLogo)s, %(companyShortName)s, %(companySize)s, %(createTime)s, %(deliver)s, %(district)s, %(education)s, %(financeStage)s, %(firstType)s, %(formatCreateTime)s, %(gradeDescription)s, %(hitags)s, %(imState)s, %(industryField)s, %(industryLables)s, %(isSchoolJob)s, %(jobNature)s, %(lastLogin)s, %(latitude)s, %(linestaion)s, %(longitude)s, %(pcShow)s, %(plus)s, %(positionAdvantage)s, %(positionId)s, %(positionLables)s, %(positionName)s, %(promotionScoreExplain)s, %(publisherId)s, %(resumeProcessDay)s, %(resumeProcessRate)s, %(salary)s, %(score)s, %(secondType)s, %(skillLables)s, %(stationname)s, %(subwayline)s, %(thirdType)s, %(workYear)s ) "
        if type(item) == list:
            mysql_util.executemany(_sql, item)
        else:
            mysql_util.insertValue(_sql, item._values)