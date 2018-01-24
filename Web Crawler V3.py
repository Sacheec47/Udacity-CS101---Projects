def get_page (website_url):
    from urllib.request import urlopen
    x = urlopen(website_url).read()
    source = x.decode('utf-8')
    return source

page = 'b<html>\n<body>\nThis is a test page for learning to crawl!\n<p>\nIt is a good idea to \n<a href="https://udacity.github.io/cs101x/crawling.html">learn to crawl</a>\nbefore you try to \n<a href="https://udacity.github.io/cs101x/walking.html">walk</a> or \n<a href="https://udacity.github.io/cs101x/flying.html">fly</a>.\n</p>\n</body>\n</html>\n\n'

def get_url(website_url):
    list1 = []
    end_pos = 0
    
    while True:
        target = page.find('<a href=',end_pos)        
        if target > -1:
            start_pos = page.find('"', target)
            end_pos = page.find('"',start_pos+1)
            url = page[start_pos+1:end_pos]
            list1.append(url)
                     
        else:
            #return list1
            break
    return list1

def get_url2(website_url):
    list1 = []
    page = get_page(website_url)
    end_pos = 0
    
    while True:
        target = page.find('<a href=',end_pos)        
        if target > -1:
            start_pos = page.find('"', target)
            end_pos = page.find('"',start_pos+1)
            url = page[start_pos+1:end_pos]
            list1.append(url)
                     
        else:
            #return list1
            break
    return list1

def union(a,b):
    for e in b:
        if e not in a:
            a.append(e)


def crawl_web(website_url):
    tocrawl = get_url(website_url)
    crawled = []

    for e in tocrawl:
        union(tocrawl,get_url2(e))
        index1 = tocrawl.index(e)
        crawled.append(tocrawl.pop(index1))
        
        
    return crawled
        #break
        




               
print (crawl_web(page))
