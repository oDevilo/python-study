# encoding: utf-8
# 爬取企查查信息
import requests
from bs4 import BeautifulSoup
from urllib.parse import quote
import sys
import time
 
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
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36',
            'Cookie': 'QCCSESSID=bfgk3kc680jodna5jdk4bkv9l1;_uab_collina=155539723210924146028556;acw_tc=73e72d9b15553971319887831e026678a567815c250dcfddc98dda8eec;'
        }
        html = requests.get(url, headers=header, )
        return html.text
 
    def parser_home_html(self, html, name):
        soup = BeautifulSoup(html, 'lxml')
        print(soup)
        try:
            for i in soup.find('section', id='searchlist').find('tbody').find_all('tr'):
                try:
                    print('https://www.qichacha.com' + i.find('a', 'ma_h1')['href'], i.find('a', 'ma_h1').get_text(),)
                    yield 'https://www.qichacha.com' + i.find('a', 'ma_h1')['href'], i.find('a', 'ma_h1').get_text()
                except:
                    print(i.find('a', 'ma_h1').get_text(),
                        i.find('span', 'nstatus text-warning m-l-xs').get_text().strip())
        except:
            print('没有查到该公司 ' + name)
 
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
        
        # 其他信息
        try:
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
        except:
            print()
        
        #print(basic_list)
        print(basic_list['name'], basic_list['logo'])
 
    def main(self, name):
        url = 'http://www.qichacha.com/search?key={}'.format(quote(name))
        #url = 'http://www.qichacha.com/search?key={}'.format(quote(sys.argv[1]))
        print(url)
        home_html = self.get_html(url)
        print('开始爬取' + name)
        for detail_url, name in self.parser_home_html(home_html, name):
            detail_html = self.get_html(detail_url, url)
            self.parser_detail_html(detail_html, name)
 
if __name__ == '__main__':
    companyNames="Amazon,Apple,Autodesk,Citrix,Cisco,Coolapk (酷安),Douban (豆瓣),eBay,EMC,Ericsson,Google,Grab,HP,HSBC,Hulu,IBM,Intel,LeetCode,LintCode/九章算法,Microsoft,National Instruments,NVIDIA,Oracle,PayPal,Pivotal,RingCentral,SAP,Splunk,SUSE,ThoughtWorks,Trend Micro,Vipshop (唯品会),VMware,WeWork,Works Applications,华为,华为外包,阿里巴巴,蚂蚁金服,京东,58同城,苏宁,途家网,有赞,字节跳动,拼多多,大疆创新,用友,深信服,鲸鱼游戏,盛赫游戏,神策数据,顺舟智能,中软国际,柯莱特,高伟达,跨越速运,砸立,一喂,智贝科技,氪细胞,同花顺,游族网络,马上金融,霁云科技,多益网络,蝴蝶互动,深圳市世纪纵横科技发展有限公司,北京关键科技股份有限公司,山东国子软件股份有限公司,上海联影医疗科技有限公司,首约科技（北京）有限公司,海尔集团,Boss直聘(北京华品博睿网络技术有限公司),北京游奕互动软件有限公司,长城汽车股份有限公司天津园区,蓝鸽集团有限公司,依图网络科技有限公司,深圳市环球易购电子商务有限公司,杭州海康威视数字技术股份有限公司,浙江大华技术股份有限公司,	浙江宇视科技有限公司,腾讯,小米,亚信(AsiaInfo),猎聘网,饿了么,步步高,百度,网易游戏,便利蜂,网易考拉海购,美的集团,VIPKID,房多多,天眼查,去哪儿网,tap4fun,德邦物流,万兴科技,4399游戏,普联软件,云鸟科技,追一科技,兴业数字金融服务,iCourt,小红书,三七互娱,依图科技,小黑鱼,深圳市猜猜城科技有限公司,初见科技,道通科技,尊豪网络科技有限公司,浪潮软件,作业帮,天津天地伟业科技有限公司,上海壹米滴答供应链管理有限公司,广州蓝鸽集团,广州创思信息技术有限公司（9377 游戏）,金杜律师事务所,数美科技,快方送药,苏州同思软件有限公司,凌志软件股份有限公司,武汉精臣智慧标识科技有限公司,山东兆物网络技术股份有限公司,盘石信息科技有限公司,快陪练,广东虚拟现实科技有限公司(Ximmerse),成都二次元动漫有限公司,东华软件股份公司,易思维(杭州/天津)科技有限公司,湖南创发科技有限公司,金山软件,信美人寿相互保险社,辉讯网络技术有限公司,上海鱼泡泡信息科技有限公司,武汉星云海数字科技股份有限公司,北京中广创思文化传播有限公司,北京必胜课教育有限公司-天津部门,福建浔兴拉链科技股份有限公司,掌门一对一教育有限公司,易车网,大连东软集团,中科曙光,微付充科技有限公司,深圳市前海手绘科技文化有限公司,七牛云,邻趣网络有限公司,北京数码视讯科技股份有限公司,中富通集团股份有限公司,北京声智科技有限公司"
    companyNameArr=companyNames.split(',')

    # 防止请求过快 休眠1秒
    time.sleep(1)
    #for name in companyNameArr:
    #    Qi().main(name)
    Qi().main("阿里巴巴(中国)网络技术有限公司")
    #Qi().main()