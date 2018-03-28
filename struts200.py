#coding=utf-8
import re
import socket
import requests


#抓取域名
def getdomain():
    f=open('123.txt','rb')
    for xi in f.readlines():
        i1 = xi.rstrip()
        list1 = rep.findall(i1)
        for xii in list1:
            doamin_all.append(xii)
    f.close()

#验证域名的状态码为200
def get_domain_200(domainlist):
    f3=open('200.txt','w')
    for url in domainlist:
        url1="http://"+url
        url2="https://"+url
        try:
            r=requests.head(url1,timeout=6)
            status_code=r.status_code
            if status_code==200:
                print url1
                doamin_200.append(url)
                f3.write(url+"\n")
                f3.flush()
            else:
                r2=requests.head(url2,timeout=6)
                status_code2 = r2.status_code
                if status_code2 == 200:
                    print url2
                    doamin_200.append(url)
                    f3.write(url + "\n")
                    f3.flush()
                else:
                    pass
        except:
            pass
    f3.close()

#获取域名ip地址
def get_ip(domainlist):
    file2 = open("ok.txt", "w")
    iplist=[]
    for i in domainlist:
        try:
            url=i.rstrip()
            ip=socket.gethostbyname(url)
            print ip
            iplist.append(ip)
        except:
            pass
    iplist2=list(set(iplist))
    for ii in iplist2:
        file2.write(ii+"\n")
    file2.close()


def main():
    getdomain()
    get_domain_200(doamin_all)
    get_ip(doamin_200)


if __name__=="__main__":
    rep = re.compile(r'^.*\.ucloud\.cn$') #这里输入要匹配域名的正则表达式
    doamin_all = []
    doamin_200 = []
    main()