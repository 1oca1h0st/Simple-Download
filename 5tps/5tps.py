# -*- coding: utf-8 -*-
#---------------------------------import---------------------------------------
import urllib;
import urllib2;
import re;
import os;
#------------------------------------------------------------------------------
def down(url_download):
    print url_download;
    #获取正文内容
    userMainUrl = url_download;
    req = urllib2.Request(userMainUrl);
    resp = urllib2.urlopen(req);
    respHtml = resp.read();
    #print "respHtml=",respHtml;

    #找到iframe的src地址
    iframe = re.findall("iframe.*", respHtml);
    #print iframe;
    iframe_url = iframe[0].split('"')[1];
    iframe_url = "http://www.5tps.com" + iframe_url;
    #print iframe_url;

    #iframn内容获取
    i_headers = {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1) Gecko/20090624 Firefox/3.5",
        "Host": "www.5tps.com",
        "Referer": "http://www.5tps.com/down/4563_47_1_3.html"
    }
    iframe_req = urllib2.Request(iframe_url, headers=i_headers);
    iframe_resq = urllib2.urlopen(iframe_req);
    iframe_html = iframe_resq.read();
    #print iframe_html;

    random_seq = iframe_html.split("'")[1];
    random_1 = random_seq;
    print random_1;
    random_2 = iframe_html.split("'")[3];
    print random_2;    
    random_3 = iframe_html.split("'")[5];
    print random_3;  
    random_4 = iframe_html.split("'")[7];
    print random_4;
    random_5 = iframe_html.split("'")[9];
    print random_5;
    random_6 = iframe_html.split("'")[11];
    print random_6;
    random_7 = iframe_html.split("'")[13]
    print random_7;
    random_8 = re.findall(r"\?\d", iframe_html)[0];
    print random_8; 
    mp3_url =  re.findall(r"http://.*p3", iframe_html)[0];
    print mp3_url;

    filename = re.findall(r"\d{3}\.mp3", mp3_url)[0]
    print filename;
    
    os.chdir(r'Z:/down');
    url = mp3_url + random_7 + random_1 + random_5 + random_2 + random_5 + random_3 + random_6 + random_4 + random_8;
    print url;
    urllib.urlretrieve(url,filename);

def people_list(url_people):
    req = urllib2.Request(url_people);
    resp = urllib2.urlopen(req);
    respHtml = resp.read();
    print respHtml;

def main():
    i = 0;
    while i<101:
        i = i+1;
        url_start = "http://www.5tps.com/down/14031_47_1_";
        url = url_start + str(i) + ".html";
        down(url);
    #people_list("http://www.5tps.com/mlist/1_1.html");

###############################################################################
if __name__=="__main__":
    main();
