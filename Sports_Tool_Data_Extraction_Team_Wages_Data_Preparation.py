#!/usr/bin/env python
# coding: utf-8

# In[ ]:


### importing libraries
import pandas as pd
import numpy as np
from tqdm import tqdm
import warnings


# In[ ]:


#### config
#### change the links according to the requirement

la_liga_wages = 'https://fbref.com/en/comps/12/wages/La-Liga-Wages'
premier_league_wages = 'https://fbref.com/en/comps/9/wages/Premier-League-Wages'
serie_a_wages = 'https://fbref.com/en/comps/11/wages/Serie-A-Wages'
bundesliga_wages = 'https://fbref.com/en/comps/20/wages/Bundesliga-Wages'
ligue_1_wages = 'https://fbref.com/en/comps/13/wages/Ligue-1-Wages'


# In[ ]:


#### variables
player_wages_list = []

#### Do not change the order of the list
league_list = ['LaLiga', 'Premier League', 'Serie A', 'Bundesliga', 'League 1'] ## for instering league column value

#### Do not change the order of the list
big_five_links = [la_liga_wages, premier_league_wages, serie_a_wages, bundesliga_wages, ligue_1_wages] ## order in which data is saved


# In[ ]:


def currency_data_column_prep(data):
    """
    Prepare currency data column.

    This function takes a list of data as input and extracts numerical values from each element
    of the list. The expected format of each element is "Currency Value". It then converts the 
    extracted values into floating-point numbers and removes any comma separators.

    Args:
        data (list): A list of strings containing currency values.

    Returns:
        tuple: A tuple containing two floating-point values. The first value represents the 
        currency value from the first element of the input list, and the second value represents
        the currency value from the second element of the input list.

    Example:
        data = ["USD 1,234.56", "EUR 2,345.67"]
        result = currency_data_column_prep(data)
        # result will be (1234.56, 2345.67)
    """
    return float((data[0].split(' ')[1]).replace(',',"")), float((data[1].split(' ')[1]).replace(',',""))


# In[ ]:


#### data downloading (Scraping)
for index, links in enumerate(tqdm(big_five_links)):
    data = pd.read_html(links)[1] ## selecting table 2nd
    data['League'] = league_list[index] ## adding league name column to the data
    player_wages_list.append(data) ## appending data to a single list

all_big_five_eu_player_wages_list = pd.concat(player_wages_list) ## getting all the data into a single dataframe
all_big_five_eu_player_wages_list.drop_duplicates(inplace=True) ## removing duplicates if any


# In[ ]:


#### removing cuurency symbol/text from the currency values
all_big_five_eu_player_wages_list[['Weekly Wages','Annual Wages']] = all_big_five_eu_player_wages_list[['Weekly Wages','Annual Wages']]                                                            .apply(currency_data_column_prep,axis=1,result_type='expand')


# In[ ]:


#### saving the data locally in the same directory as the codebase
all_big_five_eu_player_wages_list.to_csv("combined_squad_wages_data.csv",index=False,encoding='utf-8-sig')

