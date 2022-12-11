from bs4 import BeautifulSoup
import requests
start_url = 'https://boston.craigslist.org/search/jjj?' #  home page
jobs = {} # list of job kinds extrcted from dropdown -> name : link
job_offers = [] # list of offers for selected job -> data-pid : {name:NAME,link:LINK}

def pars_by_url(url):
    try:
        page = requests.get(url)
        soup = BeautifulSoup(page.text , 'html.parser')
        if page.ok:
            return soup
        return False
    except:
        print(f'Could not connect to {url} .')

def get_job_selection(url):
    #f'{start_url[:-4]}{jobs["security"]}?' to creat url by links stored in jobs
    soup = pars_by_url(url)
    if soup:
        selection = soup.find('select',{'class':'js-only','id':'subcatAbb'}).find_all('option')
        for option in selection:
            jobs[option.text.strip()] = option.get('value')


def get_job_offers(url):
    soup = pars_by_url(url)
    if soup:
        offers = soup.find('ul',{'class':'rows','id':'search-results'}).find_all('li')
        job_offers.clear()
        for offer in offers:
            if offer not in job_offers:
                job_offers.append({'name':offer.find('div').find('a').text.strip(),'link':offer.find('div').find('a').get('href')})

def get_offer_detail(url):
    table = ''
    soup = pars_by_url(url)
    if soup:
        details = soup.find('section',{'id':'postingbody'})
        label_info = soup.find('p',class_ = 'attrgroup').find_all('span')
        for label in label_info:
            if label.find('b'):
                table += label.text +':   '+ label.find('b').text +'\n'
            else:
                table += label.text
        if 'QR Code Link to This Post' in details.text:
            index = details.text.index('QR Code Link to This Post')+25
        return table,details.text[index:].strip()
    else:
        print('NO respones')
if __name__ == '__main__':
    pass




    