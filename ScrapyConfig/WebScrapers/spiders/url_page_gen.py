def url_page_maker(urls,n):
    url_list = []
    for url in urls:
        index = url.find(".htm")
        for i in range(2,n+1):
            url_nxt_page = url[0:index]+"_P"+str(i)+".htm"
            url_list.append(url_nxt_page)
    
    return url_list