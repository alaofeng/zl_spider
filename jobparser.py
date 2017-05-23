# -*- coding: utf-8 -*-
import os
from bs4 import BeautifulSoup
import traceback
import codecs
import jieba
import sys
reload(sys)
sys.setdefaultencoding('utf8')




def parse(page):
    soup = BeautifulSoup(page)
    arr = soup.select("div[class='top-fixed-box'] div[class='fixed-inner-box'] div[class='inner-left fl'] h1")
    job_title ,job_company= '未解析出title','未解析出公司'
    if (len(arr) > 0):
        job_title = arr[0].string
    
    
    arr = soup.select("div[class='top-fixed-box'] div[class='fixed-inner-box'] div[class='inner-left fl'] h2")
    if (len(arr) > 0):
        job_company = arr[0].text    
    
    
    ul= soup.select("div[class='terminalpage-left'] ul[class='terminal-ul clearfix']")
    job_salary = "面议"
    if (ul): ul = ul[0]
        
    job_salary = ul.select("li strong")[0].text
    
    job_experience = "不限"
    job_experience = ul.select("li strong")[4].text
    
    job_education = "不限"
    job_education = ul.select("li strong")[5].text
    
    job_counter = 1
    
    job_counter = ul.select("li strong")[6].text
    
    job_category = "不限"
    
    job_category = ul.select("li strong")[7].text
    
    
    job_words = ''
    
    div= soup.select("div[class='terminalpage-left'] div[class='terminalpage-main clearfix'] div[class='tab-cont-box'] div[class='tab-inner-cont']")
    try:
        if len(div) > 0:
            #获取里边所有的p标签
            p_list = div[0].select("p")
            for p in p_list[:-1]: job_words +=p.text.strip().s.expandtabs(4)
                
    except Exception ,e :
        print type(div), len(div)
        print traceback.format_exc()
        
    line = "\t".join([job_company.strip() ,job_title.strip(), job_salary.strip() ,job_experience.strip() , job_counter.strip(), job_education.strip() , job_category.strip(),job_words.strip()])
    return line
        
    



def html(file="jobs/186958818256099.htm"):
    f  = open(file)
    html = f.read()  
    f.close()
    return html
    
    
for job_dir in ('20170417','20170504','20170514'):
    jobs_file = codecs.open("$s.txt" % (job_dir), "w" , "utf-8")
    for parent,dirs,files in os.walk(job_dir):
        for file in files:
            path = os.path.join(parent,file)
            ab_path = os.path.abspath(path)
            try:
                line = parse(html(ab_path))
                print >> jobs_file,line
            except Exception ,e :
                print ab_path 
                print traceback.format_exc()
    jobs_file.close()

    

