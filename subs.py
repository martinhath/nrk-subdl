import urllib.request as u
import re
from html.parser import *

default_sub_length = 6000

times = []
lines = []
def get_url(episode):
    return "http://tv.nrk.no/programsubtitles/KMTE40003{}13/html".\
        format(episode)

def get_time(attrs):
    for a in attrs:
        if a[0] == 'data-begin':
            return a[1]
    return ''

class Parser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        t = get_time(attrs)
        if tag == 'br':
            self.append = True
        else:
            self.append = False
        if t != '':
            times.append(t)
    def handle_data(self, data):
        d = data.strip()
        if d != '':
            if self.append:
                lines.append(lines.pop()+'\n'+data)
            else:
                lines.append(data)

def time_msecs(t):
    nums = list(re.findall(r'[\d]+', t[0]))
    nums = list(map(int, nums))
    for _ in range(4-len(nums)):
        nums.insert(0, [0])
    tot = nums[0] * 1000 * 60 * 60 +\
          nums[1] * 1000 * 60 +\
          nums[2] * 1000 +\
          nums[3]
    return tot

def time_format(t):
    h = t // (1000*60*60)
    t -= h * (1000*60*60)
    m = t // (1000*60)
    t -= m * (1000*60)
    s = t // (1000)
    t -= s * (1000)
    return "{:02}:{:02}:{:02},{:03}".format(h, m, s, t)
    

def get_sub_length(curr, next, last=False):
    if last: 
        return time_format(time_msecs(curr) + 60000)
    s = min(time_msecs(next) - time_msecs(curr),\
            default_sub_length)
    return time_format(time_msecs(curr) + s)
    

def print_srt(pairs):
    i = 0
    n = len(pairs)
    print()
    while(i < n):
        p = pairs[i]
        if i == n-1:
            t1 = get_sub_length(p, None, True)
        else:
            t1 = get_sub_length(p, pairs[i+1])
        print(i)
        print("{} --> {}".format(p[0], t1))
        print(p[1])
        print()
        i += 1

if __name__ == '__main__':
    html = u.urlopen(get_url(2))
    string = "".join(html.read().decode("utf-8"))
    parser = Parser()
    parser.feed(string)

    res = list(zip(times, lines))
    print_srt(res)

