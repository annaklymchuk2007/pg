import sys
import requests


def download_url_and_get_all_hrefs(url):
    """
    Funkce stahne url predanou v parametru url pomoci volani response = requests.get(),
    zkontroluje navratovy kod response.status_code, ktery musi byt 200,
    pokud ano, najdete ve stazenem obsahu stranky response.content vsechny vyskyty
    <a href="url">odkaz</a> a z nich nactete url, ktere vratite jako seznam pomoci return
    """
    hrefs = []
    
    response = requests.get(url)
    
    if response.status_code != 200:
        raise Exception(f"HTTP chyba: {response.status_code}")
    
    html_content = response.text
    
    index = 0
    while index < len(html_content):
        start_a = html_content.find('<a ', index)
        if start_a == -1:
            break
            
        start_href = html_content.find('href=', start_a)
        if start_href == -1:
            index = start_a + 1
            continue
            
        start_href += 5
        
        quote_char = html_content[start_href]
        if quote_char not in ['"', "'"]:
            end_url = start_href
            while end_url < len(html_content) and html_content[end_url] not in [' ', '>']:
                end_url += 1
            url_content = html_content[start_href:end_url]
        else:
            start_href += 1 
            end_url = html_content.find(quote_char, start_href)
            if end_url == -1:
                index = start_href
                continue
            url_content = html_content[start_href:end_url]
        
        if url_content.strip():
            hrefs.append(url_content)
        
        index = end_url + 1 if end_url > start_a else start_a + 1
    
    return hrefs


if __name__ == "__main__":
    try:
        url = sys.argv[1]
        links = download_url_and_get_all_hrefs(url)
        
        print(f"Nalezené odkazy na stránce {url}:")
        for i, link in enumerate(links, 1):
            print(f"{i}. {link}")
            
    except IndexError:
        print("Chyba: Zadejte URL jako parametr")
        print("Použití: python cv.18.11.py <URL>")
    except Exception as e:
        print(f"Program skoncil chybou: {e}")