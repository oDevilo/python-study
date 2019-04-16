# encoding: utf-8
# 爬取企查查信息
import requests
from bs4 import BeautifulSoup
from urllib.parse import quote
import sys
 
 
class Qi(object):
    def __init__(self):
        self.coolie = []
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36',
        }
        b = requests.get('http://www.qichacha.com', headers=self.header)
        for i in b.cookies:
            self.coolie.append(i.value)
 
    def get_html(self, url, referer='https://m.qichacha.com/'):
        print(self.coolie)
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36',
            'Cookie': 'QCCSESSID=bfgk3kc680jodna5jdk4bkv9l1;_uab_collina=155539723210924146028556;acw_tc=73e72d9b15553971319887831e026678a567815c250dcfddc98dda8eec;'
        }
        html = requests.get(url, headers=header, )
        return html.text
 
    def parser_home_html(self, html):
        soup = BeautifulSoup(html, 'lxml')
        try:
            for i in soup.find('section', id='searchlist').find('tbody').find_all('tr'):
                try:
                    print('https://www.qichacha.com' + i.find('a', 'ma_h1')['href'], i.find('a', 'ma_h1').get_text(),)
                    yield 'https://www.qichacha.com' + i.find('a', 'ma_h1')['href'], i.find('a', 'ma_h1').get_text()
                except:
                    print(i.find('a', 'ma_h1').get_text(),
                        i.find('span', 'nstatus text-warning m-l-xs').get_text().strip())
        except:
            print('没有查到该公司')
 
    def parser_detail_html(self, html, name):
        basic_list = {}
        soup = BeautifulSoup(html, 'lxml')
        # 法人
        try:
            basic_list['legalPersonName'] = soup.find('a', 'bname').get_text()
        except:
            basic_list['legalPersonName'] = ''
        # 企业名
        basic_list['name'] = name
        # 企业logo
        basic_list['logo'] = soup.find('div', 'imgkuang').img['src']
        # 联系方式
        try:
            basic_list['contact'] = soup.find('div', 'content').find_all('div', 'row')[1].find('span',
                                                                                               'cvlu').span.get_text().strip()
        except:
            basic_list['contact'] = ''
        #官网
        try:
            basic_list['websiteList'] = soup.find('div', 'content').find_all('div', 'row')[2].find_all('span','cvlu')[-1].get_text()
        except:
            basic_list['websiteList'] =''
        # 
        content = soup.find('section', id='Cominfo').find_all('table')[0].find_all('tr')
        # 注册资本：
        try:
            basic_list['regCapital'] = content[0].find_all('td')[1].get_text().strip()
        except:
            basic_list['regCapital'] = ''
       
        # 成立日期：
        try:
            basic_list['estiblishTime'] = content[1].find_all('td')[3].get_text().strip()
        except:
            basic_list['estiblishTime'] = ''
        # 注册号：
        try:
            basic_list['regNumber'] = content[2].find_all('td')[1].get_text().strip()
        except:
            basic_list['regNumber'] = ''
 
        # 公司类型：
        try:
            basic_list['companyOrgType'] = content[4].find_all('td')[1].get_text().strip()
        except:
            basic_list['companyOrgType'] = ''
        # 所属行业：
        try:
            basic_list['industry'] = content[4].find_all('td')[3].get_text().strip()
        except:
            basic_list['industry'] = ''
 
        # 营业期限
        try:
            basic_list['operatingPeriod'] = content[8].find_all('td')[3].get_text().strip()
        except:
            basic_list['operatingPeriod'] = ''
        # 企业地址：
        try:
            basic_list['regLocation'] = content[9].find_all('td')[1].get_text().strip().split('查看地图')[0].strip()
        except:
            basic_list['regLocation'] = ''
        # 经营范围：
        try:
            basic_list['range'] = content[-1].find_all('td')[1].get_text().strip()
        except:
            basic_list['range'] = ''
        #print(basic_list)
        print(basic_list['name'], basic_list['logo'])
 
    def main(self, name):
        url = 'http://www.qichacha.com/search?key={}'.format(quote(name))
        #url = 'http://www.qichacha.com/search?key={}'.format(quote(sys.argv[1]))
        print(url)
        home_html = self.get_html(url)
        print('开始爬取')
        for detail_url, name in self.parser_home_html(home_html):
            detail_html = self.get_html(detail_url, url)
            self.parser_detail_html(detail_html, name)
 
if __name__ == '__main__':
    Qi().main("阿里巴巴(中国)网络技术有限公司")
    #Qi().main()