import urllib
import urllib2
import codecs
from lxml import etree

def find_last(string,str):
    last_position=-1
    while True:
        position=string.find(str,last_position+1)
        if position==-1:
            return last_position
        last_position=position

def get_html(string):

    url=string
    req =  urllib2.Request(url)
    #print req
    res_data = urllib2.urlopen(req)
    res = res_data.read()
    #print res
    return res

def get_version(con, package_name):
    for each in con:
        a = each.text.encode('utf-8')
        a = a[len(package_name):]
        a.lstrip()
        print a

def deal_string(url ,package_name):
    return url+package_name

def getText(elem):
    rc = []
    for node in elem.itertext():
        rc.append(node.strip())
    return ''.join(rc)

def autoprint(pack):
    homepage = "http://layers.openembedded.org"
    url = "http://layers.openembedded.org/layerindex/branch/master/recipes/?q="
    package_name = pack
    community = "meta-oe"

    selector=etree.HTML(get_html(deal_string(url ,package_name)))
    con=selector.xpath(u'//h1')

    if len(con):
        get_version(con, package_name)
    else:
        list_num = selector.xpath(u'//a')
        for num in list_num:
            if(num.text.encode('utf-8') == package_name):
            
                newurl =  homepage+num.get('href')
                selector=etree.HTML(get_html(newurl))
                con=selector.xpath(u'//h1')
                get_version(con, package_name)
                con2 = selector.xpath('//table')
                for each in con2:
                    print each.encode('utf-8')

pack = "mesa"
autoprint(pack)
