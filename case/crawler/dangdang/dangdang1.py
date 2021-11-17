import requests

url = 'http://www.dangdang.com/'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64;x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
# headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}

headers = {

    'user-agent': user_agent                      #浏览器头文件信息

}

message = requests.get(url=url, headers=headers)  # 对目标网页发送访问请求

message = message.content.decode('gbk')           # 对爬取的页面数据进行解码

print(message)