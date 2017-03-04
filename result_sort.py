#-*- coding:utf-8 -*-
#!/usr/bin/python
import csv
import sys
import logging
logging.getLogger().setLevel(logging.INFO)


def sort_msg_by_count():
    user_counts = {}
    try:
        reader = csv.reader(sys.stdin, delimiter=' ')
        for row in reader:
            try:
                info = row[0].split('\t')
                user_id = info[0]
                count = info[1]
                if not user_id:
                    continue
                user_counts[user_id] = count
            except Exception, ex:
                logging.info(str(ex))
    except Exception, ex:
        logging.info(str(ex))
    user_counts = sorted(user_counts.items(), key=lambda c: int(c[1]), reverse=True)
    for user, count in user_counts:
        print '---------------%s\t%s' % (user, count)


if __name__ == "__main__":
    sort_msg_by_count()
