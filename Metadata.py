# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 11:03:46 2018

@author: Reddy
"""



from bs4 import BeautifulSoup
import requests


def main():
    #r = requests.get('any url')
    
    #r = requests.get('https://Saichethan.github.io')
    
    u = input("Enter URL :\n")
    r = requests.get(u)
    soup = BeautifulSoup(r.content, "html")

    meta = soup.find_all('meta')
    
    for tag in meta:
        print("\n")
        print(tag)
        print("\n")
        
    
    
    title = soup.title.string
    print('TITLE :', title)
    print("\n")
    
    
    
    for tag in meta:
        
        if 'property' in tag.attrs.keys() and tag.attrs['property'].strip().lower() in ['og:type', 'og:url', 'og:image', 'og:site_name', 'og:title']: 
            print('Open Graph Protocol PROPERTY  : ',tag.attrs['content'].lower())
            print("\n")
            print('Open Graph Protocol CONTENT : ',tag.attrs['content'])
            print("\n")
            
        if 'name' in tag.attrs.keys(): 
            print('NAME    : ',tag.attrs['name'].lower())
            print("\n")
            print('CONTENT : ',tag.attrs['content'])
            print("\n")
        
        

if __name__ == '__main__':
    main()
