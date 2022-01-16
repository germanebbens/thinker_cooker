from importlib.resources import path
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import sys

URL_INIT = "https://www.recetasgratis.net/Recetas-de-Aperitivos-tapas-listado_receta-1_1.html"


def get_urls_create_list(url):
    """
    Get the all url's posts with the page (received url) and create a python list.
    Input: URL 
    Output: List with all recipes url's  
    """
    href_list = []
    resp = requests.get(url)

    html_entire = BeautifulSoup(resp.content, 'html.parser')

    html_section = html_entire.find_all('a', class_='titulo titulo--resultado', href = True)

    for i in range(len(html_section)):
        href_list.append(html_section[i].get('href'))

    return href_list

def get_new_page(url):
    """
    Get the next page url's.
    Input: URL  with galery
    Output: Next page url's  
    """
    resp = requests.get(url)

    html_entire = BeautifulSoup(resp.content, 'html.parser')
    url_next_page = html_entire.find('a', class_='next ga', href = True)
    return url_next_page.get("href")
    


def get_many_recipes_urls(initial_url, pages):
    """
    Get url's from many pages, iterate through the pages getting urls. 
    Input: 
        - URL  with initial page
        - pages to iterate 
    Output: Next page url's  
    """
    recipes_list_url = []

    if not recipes_list_url:
        recipes_list_url = get_urls_create_list(initial_url)
        new_url = get_new_page(initial_url)
        
    for i in range(pages):
        recipes_list_url.append(get_urls_create_list(new_url))
        new_url = get_new_page(new_url)

    return recipes_list_url

def create_recipes(href_list):
    """
    Get list of url's and go one for one to get information, create dataframe with this info. 
    Input: List of urls
    Output: Dataframe with information
    """
    ingredient_list = []
    steps_list = []
    recipes_df = pd.DataFrame(columns=['recipe_id','url','title','ingredients','steps','diners','duration','difficulty'])

    for i in range(len(href_list)-1):
        resp = requests.get(href_list[i])
        html_entire = BeautifulSoup(resp.content, 'html.parser')

        code_recipe = href_list[i][-10:-5]
        url_recipe = href_list[i]

        try:
            title_recipe = html_entire.find('h1', class_='titulo titulo--articulo').text
        except:
            title_recipe = None
            print("no encontre titulo")
        
        try:
            for i in html_entire.find_all('li', class_='ingrediente'):
                ingredient_list.append(i.text)
        except:
            ingredient_list = None
            print("no encontre ingredient_list")

        try:    
            for i in html_entire.find_all('div', class_='apartado'):
                steps_list.append(i.text)
        except:
            steps_list = None
            print("no encontre steps_list")

        try: 
            comensales = html_entire.find('span', class_="property comensales").text
        except:
            comensales = None
            print("no encontre comensales")
        try: 
            duration = html_entire.find('span', class_="property duracion").text
        except:
            duration = None
            print("no encontre duration")
        
        try: 
            difficulty = html_entire.find('span', class_="property dificultad").text
        except:
            difficulty = None
            print("no encontre difficulty")

        recipe = {'recipe_id': code_recipe,
                  'url': url_recipe,
                  'title': title_recipe,
                  'ingredients': ingredient_list,
                  'steps': steps_list,
                  'diners': comensales,
                  'duration': duration,
                  'difficulty': difficulty}
        print(recipe)

        recipes_df = recipes_df.append(recipe, ignore_index=True)
        recipes_df.to_excel('/Users/german/Desktop/thinker_cooker/recipes_df.xlsx')
        time.sleep(2)

    return recipes_df
    

if __name__ == "__main__":

    href_list = get_many_recipes_urls(URL_INIT, 1)

    recipes_df = create_recipes(href_list)


    


