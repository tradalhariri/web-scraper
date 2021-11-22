import requests
from bs4 import BeautifulSoup

def get_citations_needed_count(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    mw_content_text = soup.find('div',id='mw-content-text')
    citation_needed = mw_content_text.find_all('a',title='Wikipedia:Citation needed')
    return len(citation_needed)

def get_citations_needed_report(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    mw_content_text = soup.find('div',id='mw-content-text')
    citation_needed = mw_content_text.find_all('a',title='Wikipedia:Citation needed')
    result = ""
    for citation in citation_needed:
        result = result + f'Citation needed for "{citation.parent.parent.parent.get_text().strip()}"\n\n'
    with open('result.txt','w') as f:
        f.write(result)
    return result

if __name__ == '__main__':
    print(get_citations_needed_count("https://en.wikipedia.org/wiki/History_of_Mexico"))
    print(get_citations_needed_report("https://en.wikipedia.org/wiki/History_of_Mexico"))