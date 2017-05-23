# -*- coding: utf-8 -*-
import sys,re,types
import traceback
import time  
import os
from splinter.browser import Browser
import splinter

CLOSE_AFTER_TEST = False
reload(sys)
sys.setdefaultencoding('utf8')

encoding = lambda x:x.encode('gbk')

#http://jobs.zhaopin.com/365281238250017.htm

browser = Browser() #firefox
urls = [
    "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=%E5%A4%A7%E6%95%B0%E6%8D%AE&isadv=0&isfilter=1&p=1&re=2006", #朝阳
        "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=%E5%A4%A7%E6%95%B0%E6%8D%AE&isadv=0&isfilter=1&p=1&re=2001", #海淀
        "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=%E5%A4%A7%E6%95%B0%E6%8D%AE&isadv=0&isfilter=1&p=1&re=2005",#东城
        "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=%E5%A4%A7%E6%95%B0%E6%8D%AE&isadv=0&isfilter=1&p=1&re=2008",#石景山
        "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=%E5%A4%A7%E6%95%B0%E6%8D%AE&isadv=0&isfilter=1&p=1&re=2018",#延庆
        "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=%E5%A4%A7%E6%95%B0%E6%8D%AE&isadv=0&isfilter=1&p=1&re=2002",#西城
        "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=%E5%A4%A7%E6%95%B0%E6%8D%AE&isadv=0&isfilter=1&p=1&re=2013",#昌平
        "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=%E5%A4%A7%E6%95%B0%E6%8D%AE&isadv=0&isfilter=1&p=1&re=2007",#丰台
        "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=%E5%A4%A7%E6%95%B0%E6%8D%AE&isadv=0&isfilter=1&p=1&re=2014",#怀柔
        "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=%E5%A4%A7%E6%95%B0%E6%8D%AE&isadv=0&isfilter=1&p=1&re=2009",#通州
        "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=%E5%A4%A7%E6%95%B0%E6%8D%AE&isadv=0&isfilter=1&p=1&re=2017",#密云
        "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=%E5%A4%A7%E6%95%B0%E6%8D%AE&isadv=0&isfilter=1&p=1&re=2012",#大兴
        "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=%E5%A4%A7%E6%95%B0%E6%8D%AE&isadv=0&isfilter=1&p=1&re=2015",#平谷
        "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=%E5%A4%A7%E6%95%B0%E6%8D%AE&isadv=0&isfilter=1&p=1&re=2011",#房山
        "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=%E5%A4%A7%E6%95%B0%E6%8D%AE&isadv=0&isfilter=1&p=1&re=2016",#门头沟
        "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=%E5%A4%A7%E6%95%B0%E6%8D%AE&isadv=0&isfilter=1&p=1&re=2010",#顺义
        
        ]
for url in urls:
    hasnext = False
    while True:
        print url
        browser.visit(url)
        try :
            try:
                next_page = browser.find_link_by_text('下一页')
                if (isinstance(next_page, splinter.element_list.ElementList)) and len(next_page) > 0:
                    if next_page['href'] != None:
                        url = next_page['href']
                        hasnext = True
                    else:
                        hasnext = False
                else:
                    hasnext = False
            except Exception , e:
                print traceback.format_exc()
                hasnext = False
            print hasnext
            div = browser.find_by_id("newlist_list_content_table")
            if (isinstance(div, splinter.element_list.ElementList)):
                div = div[0]
            tables = div.find_by_tag('table')
            #如果找不到table，则返回一个空列表
            if len(tables) > 1 :
                job_urls = []
                for table in tables[1:]:
                    try :
                        tr = table.find_by_tag('tbody').find_by_tag('tr')[0]
                        a = tr.find_by_tag('td')[0].find_by_tag('a')
                        if (isinstance(a, splinter.element_list.ElementList) and len(a)) > 0:
                            job_urls.append(a.first['href'])
                        
                            
                    except Exception , e:
                        print traceback.format_exc()
                for job_url in job_urls:
                    file = job_url[24:]
                    path = "jobs/"+file;
                    if not os.path.exists(path):
                        if not os.path.exists(os.path.dirname(path)):
                            os.makedirs(os.path.dirname(path))
                        browser.visit(job_url)
                        try:
                            f = open(path , "w")
                            f.write(browser.html)
                            f.close()
                        except Exception, e:
                            print traceback.format_exc()
                
        except Exception , e:
            print traceback.format_exc()
        if not hasnext:
            break
    
if CLOSE_AFTER_TEST:
    browser.quit()
