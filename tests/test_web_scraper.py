from web_scraper import __version__

from web_scraper.scraper import get_citations_needed_count,get_citations_needed_report


def test_version():
    assert __version__ == '0.1.0'


def test_get_citations_needed_count():
    assert get_citations_needed_count("https://en.wikipedia.org/wiki/History_of_Mexico") == 5

def test_get_citations_needed_count_different_url():
    assert get_citations_needed_count("https://en.wikipedia.org/wiki/Here_Come_the_Brides") == 4

def test_get_citations_needed_report():
    result = ""
    with open("result.txt",'r') as f:
        result = f.read()

    assert get_citations_needed_report("https://en.wikipedia.org/wiki/History_of_Mexico") == result

