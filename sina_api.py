# -*- coding: utf-8 -*- 
#!/usr/bin/python
import urllib2
import logging
import json
import csv
import sys
reload(sys)
sys.setdefaultencoding('utf8')
logging.getLogger().setLevel(logging.INFO)

csvfile = file('sina_msg.csv', 'wb')


def http_get():
    try:
        sina_url = 'https://api.weibo.com/2/statuses/public_timeline.json?' \
                   'access_token=2.00xT7VtCiePQ9C288debf103k3HgcE&count=200'
        response = urllib2.urlopen(sina_url)
        sina_data = response.read()
        sina_statuses = json.loads(sina_data)['statuses']
        print 'sina_msg_example:', sina_statuses[0]
        writer = csv.writer(csvfile)
        writer.writerow(['user_name', 'user_id', 'user_location', 'msg_content'])
        datas = []
        for status in sina_statuses[:10]:  # 输出前十个
            user_name = status.get('user', {}).get('screen_name')
            user_id = status.get('user', {}).get('id')
            user_location = status.get('user', {}).get('location')
            msg_content = status.get('text', '')
            print 'user_name：', user_name
            print 'user_id：', user_id
            print 'user_location：', user_location
            print 'msg_content:', msg_content
            datas.append((user_name, user_id, user_location, msg_content))
	print  '------------------>>>>>>>>>>'
        writer.writerows(datas)
        csvfile.close()
    except Exception, ex:
        logging.info(str(ex))


if __name__ == "__main__":
    http_get()
