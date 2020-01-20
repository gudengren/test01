import requests
import re

class DownHtml(object):

    def __init__(self, url, path):
        self.headers = self.get_headers()
        self.headers_info = self.get_header_info(url)
        self.url = url
        self.path = path
        self.html_name = self.get_html_name()

    def get_headers(self):
        return {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Cookie': 'Hm_lvt_83df31d49b864f0ebcac80b58631bda1=1579325884,1579347945,1579396912,1579484854; _pk_ref.5.fb23=%5B%22%22%2C%22%22%2C1579484854%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DfFyVBZS35YeYjHCZX3Rot4qiAkidmsIzSGkT9WOiPjIqp_YgGBLPp7qgMC8RLyhe%26wd%3D%26eqid%3Dd8ebb68e005b933b000000045e2506ae%22%5D; _pk_ses.5.fb23=*; _pk_id.5.fb23=cee5aa2395e322cb.1579325884.7.1579485003.1579484854.; Hm_lpvt_83df31d49b864f0ebcac80b58631bda1=1579485003; ci_session=2gbpidtcaafugcen36igd3b1smv015i2',
            'Host': 'www.tecalliance.cn',
            'Referer': 'https://www.tecalliance.cn/cn/search/1?lbid=43',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
        }

    def get_header_info(self, url):
        return {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Cookie': 'Hm_lvt_83df31d49b864f0ebcac80b58631bda1=1577956597,1578027270,1578100129,1578116515; _pk_ref.5.fb23=%5B%22%22%2C%22%22%2C1578119311%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DIxvIekeAP6RpLv_m0W7U2abXl6N758YMWqyUP5EKkVlyCxRRK2JaQ3kZ0vMud1EI%26wd%3D%26eqid%3Deafd9ade00056e59000000045e102599%22%5D; _pk_ses.5.fb23=*; Hm_lpvt_83df31d49b864f0ebcac80b58631bda1=1578119926; ci_session=qs048ui5fro1s5kdk9s8l84n61j3iokn; _pk_id.5.fb23=ff38ca617f90a877.1577932203.13.1578120618.1578119311.',
            'Host': 'www.tecalliance.cn',
            'Referer': '{}'.format(url),
            # 'Referer': 'https://www.tecalliance.cn/cn/part/CAM1001?lbid=141&ctx_lbid=141&lgid=436493328',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
        }


    def get_html_name(self):
        # return self.url.split('/')[-1].replace('?', '')
        return re.findall(r'search/(.*?)?lbid', self.url)[0].replace('?', '')

    def req_ser(self):
        """
        请求服务器
        :return:
        """
        return requests.get(self.url, headers=self.headers, timeout=5)

    def save_html(self):
        try:
            temp = self.req_ser()
            response = temp.text
            if response.__contains__("验证码"):
                raise Exception("出现验证码")
            with open(r'{}/{}.html'.format(self.path, self.html_name), 'w', encoding='utf-8') as f:
                f.write(response)
        except Exception as err:
            raise err
