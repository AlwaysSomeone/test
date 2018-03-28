import html_downloader,html_parser,html_outputer
from bs4 import BeautifulSoup
downloader = html_downloader.HtmlDownloader()
parser = html_parser.HtmlParser()
outputer = html_outputer.HtmlOutputer()

num_list = [i for i in range(1000,2001)]
url_list =[]
for num in num_list:
    url = 'http://jib.xywy.com/il_sii/gaishu/' + str(num) + '.htm'
    url_list.append(url)

def spyder(url):
    html_cont = downloader.download(url)
    soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
    #new_urls, new_data = parser.parse(url, html_cont)
    #print(new_data)
    #print(new_urls)
    res_data = {}

    res_data['url'] = url

    title_node = soup.find('div', class_="jb-name fYaHei gre")
    if title_node == None:
        pass
    else:
        res_data['title'] = title_node.get_text()

    summary_node = soup.find('div', class_='jib-articl-con jib-lh-articl').find('p')
    if title_node == None:
        pass
    else:
        gaishu = summary_node.get_text()
    gaishu = gaishu.replace('\r\n\t','')
    res_data['summary'] = gaishu.strip()

    outputer.collect_data(res_data)

for url in url_list:
    print(url)
    spyder(url)

outputer.output_html()