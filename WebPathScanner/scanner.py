# coding=utf-8
import requests
import sys
from multiprocessing.dummy import Pool as ThreadPool
from optparse import OptionParser
s = requests.session()
s.keep_alive = False
TIMEOUT = 5

def _get_args():
    parser = OptionParser(usage="usage: %prog [options] args")
    parser.add_option("-u", "--url", help="Target URL", dest='url')
    parser.add_option("-d", "--dic", help="Dictionary path", dest='dic')
    parser.add_option("-n", "--number", help="Number of Thread,Default 5",
                      dest="num", type="int", default=5)
    parser.add_option("-t", "--timeout", help="Timeout,Default 5",
                      dest="timeout", type="int", default=5)
    opts, args = parser.parse_args()
    return opts


def _mult_getdata(alist, pro_num):

    pool = ThreadPool(processes=pro_num)
    result = pool.map(_check, alist)
    pool.close()
    pool.join()
    return result

def _check(target_list):
    final_url = target_list
    try:
        requests.adapters.DEFAULT_RETRIES = 5
        r = requests.head(final_url, timeout=TIMEOUT)
        if r.status_code < 400:
            return final_url
    except Exception as e:
        print (e)
    return

def main():
    opts = _get_args()
    # url = opts.url
    url  = 'http://xx.xx.com'
    num = opts.num
    dict_path = opts.dic or "all.txt"
    global TIMEOUT
    TIMEOUT = opts.timeout
    f = open('all.txt')
    while True:
        text1 = f.readline()
        if text1:
            tempdirs = []
            tempdirs.append((url+text1))
            result = _mult_getdata(tempdirs, num)

        else:
            break
        output = sys.stdout
        outputfile = open("allurls.txt", "a")
        sys.stdout = outputfile

if __name__ == "__main__":
    main()
