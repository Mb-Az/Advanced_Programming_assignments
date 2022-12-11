
import os
import requests
from bs4 import BeautifulSoup



def pars_by_url(url):
    '''a function just to handle first site respons
    returning parsed page or False'''
    try:
        page = requests.get(url,allow_redirects=False)
        
        soup = BeautifulSoup(page.text , 'html.parser')
        if page.ok:
            return soup
        return False
    except:
        print(f'Could not connect to {url} .')

folder = os.path.join(os.getcwd(),'images') #path for creatinf a folder to hold images

def creat_folder():
    '''called to create images folder if none exists'''
    if not os.path.exists(folder):
        os.makedirs(folder)

def search_for(search)->int:
    '''main function, called to serach and find images and then saving them in images folder
     returning number og images'''
    soup = pars_by_url(f'https://www.bing.com/images/search?q={search}&first=1&tsc=ImageHoverTitle')
    if not soup:
        return False
    ul_rows = soup.find_all('ul',{'class':'dgControl_list'})
    count = 0
    for ul in ul_rows:
        lis = ul.find_all('li')
        for li in lis:
            img_tag = li.find('img')
            if img_tag:
                img_url = None
                if img_tag.get('src'):
                    img_url = img_tag.get('src')
                elif img_tag.get('data-src'):
                    img_url = img_tag.get('data-src')

                if img_url:
                    img = requests.get('https://th.bing.com'+img_url[24:]).content
                    os.chdir(folder)
                    with open(f'img{count}.gif','wb') as file:
                        file.write(img)
                    #print(f'{count} done.')
                    
                    count +=1
    return count
if __name__ == "__main__":
    creat_folder()
    search_for('m')