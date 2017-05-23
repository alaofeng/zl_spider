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
job_dir="hadoop_jobs"
if not os.path.exists(job_dir):
    os.makedirs(job_dir)
browser = Browser() #firefox
urls = [
    "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=hadoop&p=1&isadv=0",
    "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=storm&p=1&isadv=0",
    "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=spark&p=1&isadv=0",
    "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=hive&p=1&isadv=0",
    "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=hbase&p=1&isadv=0",
    "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=zookeeper&p=1&isadv=0",    
        
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
                    path = os.path.join(job_dir,file);
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
