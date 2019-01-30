# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyNetWorkItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class ImageItem(scrapy.Item):
    image_urls = scrapy.Field()
    images = scrapy.Field()


class PositionItem(scrapy.Item):
    city = scrapy.Field()
    companyFullName = scrapy.Field()
    companyId = scrapy.Field()
    companyLogo = scrapy.Field()
    companyName = scrapy.Field()
    createTime = scrapy.Field()
    positionId = scrapy.Field()
    positionName = scrapy.Field()
    salary = scrapy.Field()

def listToStr(arr):
    return ",".join(arr)

class PositionDetailItem(scrapy.Item):
    adWord = scrapy.Field()
    appShow = scrapy.Field()
    approve = scrapy.Field()
    businessZones = scrapy.Field()
    city = scrapy.Field()
    companyFullName = scrapy.Field()
    companyId = scrapy.Field()
    companyLabelList = scrapy.Field(serializer = listToStr)
    companyLogo = scrapy.Field()
    companyShortName = scrapy.Field()
    companySize = scrapy.Field()
    createTime = scrapy.Field()
    deliver = scrapy.Field()
    district = scrapy.Field()
    education = scrapy.Field()
    financeStage = scrapy.Field()
    firstType = scrapy.Field()
    formatCreateTime = scrapy.Field()
    gradeDescription = scrapy.Field()
    hitags = scrapy.Field()
    imState = scrapy.Field()
    industryField = scrapy.Field()
    industryLables = scrapy.Field(serializer = listToStr)
    isSchoolJob = scrapy.Field()
    jobNature = scrapy.Field()
    lastLogin = scrapy.Field()
    latitude = scrapy.Field()
    linestaion = scrapy.Field()
    longitude = scrapy.Field()
    pcShow = scrapy.Field()
    plus = scrapy.Field()
    positionAdvantage = scrapy.Field()
    positionId = scrapy.Field()
    positionLables = scrapy.Field(serializer = listToStr)
    positionName = scrapy.Field()
    promotionScoreExplain = scrapy.Field()
    publisherId = scrapy.Field()
    resumeProcessDay = scrapy.Field()
    resumeProcessRate = scrapy.Field()
    salary = scrapy.Field()
    score = scrapy.Field()
    secondType = scrapy.Field()
    skillLables = scrapy.Field(serializer = listToStr)
    stationname = scrapy.Field()
    subwayline = scrapy.Field()
    thirdType = scrapy.Field()
    workYear = scrapy.Field()
