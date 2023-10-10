#!/usr/bin/env python
# coding: utf-8

# In[4]:


### importing libraries
import pandas as pd
import numpy as np
import warnings
from tqdm import tqdm


# In[ ]:


# pd.set_option("display.max_rows",500)
# pd.set_option("display.max_columns",100)
# warnings.filterwarnings("ignore")


# In[3]:


## variables
year_lst = ['2017-2018','2018-2019','2019-2020','2020-2021','2021-2022','2022-2023']
complete_data_dict = {}

home_level_data_index = [2,3,4,5,6,7,8,9,10,11,12,13,14]
away_level_data_index = [15,16,17,18,19,20,21,22,23,24,25,26,27]


fbref_link_first_half = 'https://fbref.com/en/comps/12/'
fbref_link_second_half = '-La-Liga-Stats'


# In[6]:


for index, year in enumerate(tqdm(year_lst)):
    extarcted_data = pd.read_html(fbref_link_first_half +year +'/'+year + fbref_link_second_half)
    complete_data_dict['team_'+str(year.split('-')[0])] = extarcted_data


# # Regular Season

# In[16]:


regular_season_data = pd.DataFrame()
regular_season_stats_list = [] 
for key, value in complete_data_dict.items():
    
    ### overall stats data preparation
    league_result = value[0].copy()
    column_names = league_result.columns[:1].map(lambda x: 'Overall_'+ x).tolist() +                    league_result.columns[1:2].tolist() +                    league_result.columns[2:].map(lambda x: 'Overall_'+ x).tolist()
    league_result.columns = column_names
    league_result['Overall_GF-xG'] = league_result['Overall_GF'] - league_result['Overall_xG']
    league_result['Overall_GA-xGA'] = league_result['Overall_GA'] - league_result['Overall_xGA']
    league_result.insert(0,'Year',key.split('_')[1])
    
    ### other stats data preparation
    league_result_home_away = value[1].iloc[:,2:].copy()
    league_result_home_away.columns = league_result_home_away.columns.map('_'.join)
    league_result_home_away = pd.concat([league_result,league_result_home_away],axis=1)

    
    ## data appending into single list for all dataframes
    regular_season_stats_list.append(league_result_home_away)
    

## data appending into single dataframe
regular_season_data = pd.concat(regular_season_stats_list)
regular_season_melt_data = regular_season_data.melt(id_vars=['Year','Squad'],var_name='Metric',value_name='Value')


# In[ ]:


# regular_season_data.to_csv("regular_season_stats_v1.csv",index=False,encoding='utf-8-sig')


# #### La Liga Data

# In[17]:


laliga_df = pd.DataFrame({'Squad':['La Liga']})


# In[18]:


standard_stats_data = pd.DataFrame()
standard_stats_list = [] 
for key, value in complete_data_dict.items():
    ### extarcting basic standard stats details
    standard_stats_basic_details = value[2].iloc[:,[0]]
    standard_stats_basic_details.columns = standard_stats_basic_details.columns.droplevel(level=0)
    
    ### laliga
    standard_stats_basic_details = pd.concat([standard_stats_basic_details,laliga_df],ignore_index=True)
    
    ### rest stats data preparation
    expected_stats = value[2].iloc[:,1:]
    expected_stats.columns = expected_stats.columns.map('_'.join)
    
    ### laliga values
    laliga_df_values = expected_stats.describe().reset_index(drop=True).iloc[1:2]
    expected_stats = pd.concat([expected_stats,laliga_df_values],ignore_index=True)
    
    expected_stats = pd.concat([standard_stats_basic_details,expected_stats],axis=1)
    expected_stats.insert(0,'Year',key.split('_')[1])
    
    
    ### data appending into single list for all dataframes
    standard_stats_list.append(expected_stats)
    

### data appending into single dataframe
standard_stats_data = pd.concat(standard_stats_list)
standard_melt_data = standard_stats_data.melt(id_vars=['Year','Squad'],var_name='Metric',value_name='Value')


# In[ ]:


# standard_stats_data.to_csv("standard_stats_v1.csv",index=False,encoding='utf-8-sig')


# # Goalkeeping Data

# In[19]:


goalkeeping_stats_data = pd.DataFrame()
goalkeeping_stats_list = [] 
for key, value in complete_data_dict.items():
    ### extarcting basic goalkeeping stats details
    goalkeeping_basic_info = value[4].iloc[:,[0]] 
    goalkeeping_basic_info.columns = goalkeeping_basic_info.columns.droplevel(level=0)
    
    ### laliga
    goalkeeping_basic_info = pd.concat([goalkeeping_basic_info,laliga_df],ignore_index=True)
    
    ### rest stats data preparation
    goalkeeping_stats = value[4].iloc[:,1:]
    goalkeeping_stats.columns = goalkeeping_stats.columns.map('_'.join)
    
    ### laliga values
    laliga_df_values = goalkeeping_stats.describe().reset_index(drop=True).iloc[1:2]
    goalkeeping_stats = pd.concat([goalkeeping_stats,laliga_df_values],ignore_index=True)
    
    goalkeeping_stats['Performance_Saves90'] = goalkeeping_stats['Performance_Saves']/ goalkeeping_stats['Playing Time_90s']
    goalkeeping_stats['Performance_GA%'] = goalkeeping_stats['Performance_GA90']
    goalkeeping_stats = pd.concat([goalkeeping_basic_info,goalkeeping_stats],axis=1)
    goalkeeping_stats.insert(0,'Year',key.split('_')[1])
    
    
    ### data appending into single list for all dataframes
    goalkeeping_stats_list.append(goalkeeping_stats)
    

### data appending into single dataframe
goalkeeping_stats_data = pd.concat(goalkeeping_stats_list)
goalkeeping_melt_data = goalkeeping_stats_data.melt(id_vars=['Year','Squad'],var_name='Metric',value_name='Value')


# In[ ]:


# goalkeeping_stats_data.to_csv("goalkeeping_stats_v1.csv",index=False,encoding='utf-8-sig')


# # Shooting Data

# In[20]:


shooting_stats_data = pd.DataFrame()
shooting_stats_list = [] 
for key, value in complete_data_dict.items():
    
    ### extarcting basic passing stats details
    shooting_stats_basic_details = value[8].iloc[:,[0]]
    shooting_stats_basic_details.columns = shooting_stats_basic_details.columns.droplevel(level=0)
    
    ### laliga
    shooting_stats_basic_details = pd.concat([shooting_stats_basic_details,laliga_df],ignore_index=True)
    
    ### rest stats data preparation
    shooting_stats = value[8].iloc[:,1:]
    shooting_stats.columns = shooting_stats.columns.map('_'.join)
    
    ### laliga values
    laliga_df_values = shooting_stats.describe().reset_index(drop=True).iloc[1:2]
    shooting_stats = pd.concat([shooting_stats,laliga_df_values],ignore_index=True)
    
    shooting_stats['Standard_Gls%'] = shooting_stats['Standard_Gls']/ shooting_stats['Unnamed: 2_level_0_90s']
    shooting_stats['Standard_Sh%'] = shooting_stats['Standard_Sh/90']
    shooting_stats['Standard_ShofT'] = shooting_stats['Standard_Sh'] - shooting_stats['Standard_SoT'] 
    shooting_stats = pd.concat([shooting_stats_basic_details,shooting_stats],axis=1)
    shooting_stats.insert(0,'Year',key.split('_')[1])
    
    ### vs rest stats data preparation
    vs_shooting_stats = value[9].iloc[:,3:]
    vs_shooting_stats.columns = vs_shooting_stats.columns.map('_'.join)
    
    ### laliga values
    laliga_df_values = vs_shooting_stats.describe().reset_index(drop=True).iloc[1:2]
    vs_shooting_stats = pd.concat([vs_shooting_stats,laliga_df_values],ignore_index=True)
    
    vs_shooting_stats['Standard_Sh%'] = vs_shooting_stats['Standard_Sh/90']
    vs_shooting_stats.columns = vs_shooting_stats.columns.map(lambda x: 'vs-'+ x)
    vs_shooting_stats = pd.concat([shooting_stats_basic_details,vs_shooting_stats],axis=1)
    vs_shooting_stats.insert(0,'Year',key.split('_')[1])
    
    all_shooting_data = shooting_stats.merge(vs_shooting_stats,on=['Year','Squad'])
    
    
    ## data appending into single list for all dataframes
    shooting_stats_list.append(all_shooting_data)
    

### data appending into single dataframe
shooting_stats_data = pd.concat(shooting_stats_list)
shooting_melt_data = shooting_stats_data.melt(id_vars=['Year','Squad'],var_name='Metric',value_name='Value')


# In[ ]:


# shooting_stats_data.to_csv("shooting_data_stats_v1.csv",index=False,encoding='utf-8-sig')


# # Passing Data

# In[21]:


passing_stats_data = pd.DataFrame()
passing_stats_list = [] 
for key, value in complete_data_dict.items():
    
    ### extarcting basic passing stats details
    passing_stats_basic_details = value[10].iloc[:,[0]]
    passing_stats_basic_details.columns = passing_stats_basic_details.columns.droplevel(level=0)
    
    ### laliga
    passing_stats_basic_details = pd.concat([passing_stats_basic_details,laliga_df],ignore_index=True)
    
    ### rest stats data preparation
    passing_stats = value[10].iloc[:,1:]
    passing_stats.columns = passing_stats.columns.map('_'.join)
    
    ### laliga values
    laliga_df_values = passing_stats.describe().reset_index(drop=True).iloc[1:2]
    passing_stats = pd.concat([passing_stats,laliga_df_values],ignore_index=True)
    
    passing_stats['Long_Cmp90'] = passing_stats['Long_Cmp']/ passing_stats['Unnamed: 2_level_0_90s'] 
    passing_stats = pd.concat([passing_stats_basic_details,passing_stats],axis=1)
    passing_stats.insert(0,'Year',key.split('_')[1])
    
    
    
    
    ### data appending into single list for all dataframes
    passing_stats_list.append(passing_stats)
    

### data appending into single dataframe
passing_stats_data = pd.concat(passing_stats_list)
passing_stats_melt_data = passing_stats_data.melt(id_vars=['Year','Squad'],var_name='Metric',value_name='Value')


# In[ ]:


# passing_stats_data.to_csv("passing_stats_v1.csv",index=False,encoding='utf-8-sig')


# # Pass Type Data

# In[22]:


pass_type_stats_data = pd.DataFrame()
passing_type_stats_list = [] 
for key, value in complete_data_dict.items():
    
    ### extarcting basic passing stats details
    pass_type_stats_basic_details = value[12].iloc[:,[0]]
    pass_type_stats_basic_details.columns = pass_type_stats_basic_details.columns.droplevel(level=0)
    
    ### laliga
    pass_type_stats_basic_details = pd.concat([pass_type_stats_basic_details,laliga_df],ignore_index=True)
    
    ### rest stats data preparation
    passing_type_stats = value[12].iloc[:,1:]
    passing_type_stats.columns = passing_type_stats.columns.map('_'.join)
    
    ### laliga values
    laliga_df_values = passing_type_stats.describe().reset_index(drop=True).iloc[1:2]
    passing_type_stats = pd.concat([passing_type_stats,laliga_df_values],ignore_index=True)
    
    passing_type_stats = pd.concat([pass_type_stats_basic_details,passing_type_stats],axis=1)
    passing_type_stats.insert(0,'Year',key.split('_')[1])
    
    
    
    
    ### data appending into single list for all dataframes
    passing_type_stats_list.append(passing_type_stats)
    

### data appending into single dataframe
pass_type_stats_data = pd.concat(passing_type_stats_list)
passing_type_melt_data = pass_type_stats_data.melt(id_vars=['Year','Squad'],var_name='Metric',value_name='Value')


# In[ ]:


# pass_type_stats_data.to_csv("passing_type_stats_v1.csv",index=False,encoding='utf-8-sig')


# # Shot & Goal Creation Data

# In[23]:


goal_and_shot_creation_stats_data = pd.DataFrame()
goal_and_shot_creation_stats_data_list = [] 
for key, value in complete_data_dict.items():
    
    ### extarcting basic passing stats details
    shot_and_goal_creation_basic_info = value[14].iloc[:,[0]]
    shot_and_goal_creation_basic_info.columns = shot_and_goal_creation_basic_info.columns.droplevel(level=0)
    
    ### laliga
    shot_and_goal_creation_basic_info = pd.concat([shot_and_goal_creation_basic_info,laliga_df],ignore_index=True)
    
    ### rest stats data preparation
    shot_and_goal_creation_stats = value[14].iloc[:,1:]
    shot_and_goal_creation_stats.columns = shot_and_goal_creation_stats.columns.map('_'.join)
    
    ### laliga values
    laliga_df_values = shot_and_goal_creation_stats.describe().reset_index(drop=True).iloc[1:2]
    shot_and_goal_creation_stats = pd.concat([shot_and_goal_creation_stats,laliga_df_values],ignore_index=True)
    
    shot_and_goal_creation_stats = pd.concat([shot_and_goal_creation_basic_info,shot_and_goal_creation_stats],axis=1)
    shot_and_goal_creation_stats.insert(0,'Year',key.split('_')[1])
    
    
    
    
    ### data appending into single list for all dataframes
    goal_and_shot_creation_stats_data_list.append(shot_and_goal_creation_stats)
    

### data appending into single dataframe
goal_and_shot_creation_stats_data = pd.concat(goal_and_shot_creation_stats_data_list)
goal_and_shot_creation_melt_data = goal_and_shot_creation_stats_data.melt(id_vars=['Year','Squad'],var_name='Metric',value_name='Value')


# In[ ]:


# goal_and_shot_creation_stats_data.to_csv("shot_and_goal_creation_stats_v1.csv",index=False,encoding='utf-8-sig')


# # Defensive Action Data

# In[24]:


defensive_action_stats_data = pd.DataFrame()
defensive_stats_data_list = [] 
for key, value in complete_data_dict.items():
    
    ### extarcting basic passing stats details
    defensive_basic_info = value[16].iloc[:,[0]]
    defensive_basic_info.columns = defensive_basic_info.columns.droplevel(level=0)
    
    ### laliga
    defensive_basic_info = pd.concat([defensive_basic_info,laliga_df],ignore_index=True)
    
    ### rest stats data preparation
    tackle_stats = value[16].iloc[:,1:]
    tackle_stats.columns = tackle_stats.columns.map('_'.join)
    
    ### laliga values
    laliga_df_values = tackle_stats.describe().reset_index(drop=True).iloc[1:2]
    tackle_stats = pd.concat([tackle_stats,laliga_df_values],ignore_index=True)
    
    tackle_stats['Tackles_Tkl%'] = tackle_stats['Tackles_TklW']/tackle_stats['Tackles_Tkl']
    tackle_stats = pd.concat([defensive_basic_info,tackle_stats],axis=1)
    tackle_stats.insert(0,'Year',key.split('_')[1])
    
    
    
    ### data appending into single list for all dataframes
    defensive_stats_data_list.append(tackle_stats)
    

### data appending into single dataframe
defensive_action_stats_data = pd.concat(defensive_stats_data_list)
defensive_action_melt_data = defensive_action_stats_data.melt(id_vars=['Year','Squad'],var_name='Metric',value_name='Value')


# In[ ]:


# defensive_action_stats_data.to_csv("defensive_action_stats_v1.csv",index=False,encoding='utf-8-sig')


# # Possession Data

# In[25]:


possession_stats_data = pd.DataFrame()
possession_stats_data_list = [] 
for key, value in complete_data_dict.items():
    
    ### extarcting basic passing stats details
    possession_basic_info = value[18].iloc[:,[0]]
    possession_basic_info.columns = possession_basic_info.columns.droplevel(level=0)
    
    ### laliga
    possession_basic_info = pd.concat([possession_basic_info,laliga_df],ignore_index=True)
    
    ### rest stats data preparation
    touches_stats = value[18].iloc[:,1:]
    touches_stats.columns = touches_stats.columns.map('_'.join)
    
    ### laliga values
    laliga_df_values = touches_stats.describe().reset_index(drop=True).iloc[1:2]
    touches_stats = pd.concat([touches_stats,laliga_df_values],ignore_index=True)
    
    touches_stats = pd.concat([possession_basic_info,touches_stats],axis=1)
    touches_stats.insert(0,'Year',key.split('_')[1])
    
    
    
    
    ### data appending into single list for all dataframes
    possession_stats_data_list.append(touches_stats)
    

### data appending into single dataframe
possession_stats_data = pd.concat(possession_stats_data_list)
possession_melt_data = possession_stats_data.melt(id_vars=['Year','Squad'],var_name='Metric',value_name='Value')


# In[ ]:


# possession_stats_data.to_csv("possession_data_stats_v1.csv",index=False,encoding='utf-8-sig')


# # Playing Time Data

# In[26]:


playing_time_stats_data = pd.DataFrame()
playing_time_stats_data_list = [] 
for key, value in complete_data_dict.items():
    
    ### extarcting basic passing stats details
    playing_time_stats_basic_details = value[20].iloc[:,[0]]
    playing_time_stats_basic_details.columns = playing_time_stats_basic_details.columns.droplevel(level=0)
    
    ### laliga
    playing_time_stats_basic_details = pd.concat([playing_time_stats_basic_details,laliga_df],ignore_index=True)
    
    ### rest stats data preparation
    playing_time_stats_ = value[20].iloc[:,1:]
    playing_time_stats_.columns = playing_time_stats_.columns.map('_'.join)
    
    ### laliga values
    laliga_df_values = playing_time_stats_.describe().reset_index(drop=True).iloc[1:2]
    playing_time_stats_ = pd.concat([playing_time_stats_,laliga_df_values],ignore_index=True)
    
    playing_time_stats_ = pd.concat([playing_time_stats_basic_details,playing_time_stats_],axis=1)
    playing_time_stats_.insert(0,'Year',key.split('_')[1])
    
    
    
    
    ### data appending into single list for all dataframes
    playing_time_stats_data_list.append(playing_time_stats_)
    

### data appending into single dataframe
playing_time_stats_data = pd.concat(playing_time_stats_data_list)
playing_time_melt_data = playing_time_stats_data.melt(id_vars=['Year','Squad'],var_name='Metric',value_name='Value')


# In[ ]:


# playing_time_stats_data.to_csv("playing_time_stats_v1.csv",index=False,encoding='utf-8-sig')


# # Miscellaneous Stats Data

# In[27]:


miscellaneous_stats_data = pd.DataFrame()
miscellaneous_stats_data_list = [] 
for key, value in complete_data_dict.items():
    
    ### extarcting basic passing stats details
    miscellaneous_stats_basic_details = value[22].iloc[:,[0]]
    miscellaneous_stats_basic_details.columns = miscellaneous_stats_basic_details.columns.droplevel(level=0)
    
    ### laliga
    miscellaneous_stats_basic_details = pd.concat([miscellaneous_stats_basic_details,laliga_df],ignore_index=True)
    
    ### rest stats data preparation
    miscellaneous_stats_ = value[22].iloc[:,1:]
    miscellaneous_stats_.columns = miscellaneous_stats_.columns.map('_'.join)
    
    ### laliga values
    laliga_df_values = miscellaneous_stats_.describe().reset_index(drop=True).iloc[1:2]
    miscellaneous_stats_ = pd.concat([miscellaneous_stats_,laliga_df_values],ignore_index=True)
    
    miscellaneous_stats_['Performance_Crs90'] = miscellaneous_stats_['Performance_Crs'] / miscellaneous_stats_['Unnamed: 2_level_0_90s']
    miscellaneous_stats_ = pd.concat([miscellaneous_stats_basic_details,miscellaneous_stats_],axis=1)
    miscellaneous_stats_.insert(0,'Year',key.split('_')[1])
    
    
    
    
    ### data appending into single list for all dataframes
    miscellaneous_stats_data_list.append(miscellaneous_stats_)
    

### data appending into single dataframe
miscellaneous_stats_data = pd.concat(miscellaneous_stats_data_list)
miscellaneous_melt_data = miscellaneous_stats_data.melt(id_vars=['Year','Squad'],var_name='Metric',value_name='Value')


# In[ ]:


# miscellaneous_stats_data.to_csv("miscellaneous_stats_v1.csv",index=False,encoding='utf-8-sig')


# # Joining Data

# In[28]:


team_overview = ['Per 90 Minutes_Gls', 'Standard_Sh/90', 'Performance_CS%', 'Unnamed: 2_level_0_Poss', 'Performance_GA90', 
                 'vs-Standard_Sh/90', 'Long_Cmp90', 'Performance_Crs90']
attacking = ['Standard_Gls%', 'Standard_SoT%']
defencive = ['Performance_GA%', 'Tackles_Tkl%']
possession = ['Total_Cmp%','Unnamed: 3_level_0_Poss']
efficiency = ['Performance_Save%', 'Standard_G/SoT']
attacking_vs_defensive = ['Standard_Sh%','vs-Standard_Sh%']
expected_goal_performance = ['Overall_GF-xG','Overall_GA-xGA']


# In[29]:


def chart_type(data):
    if data in team_overview:
        chart_type = 'Team_Overview'
    elif data in attacking:
        chart_type = 'Attack'
    elif data in defencive:
        chart_type = 'Defence'
    elif data in possession:
        chart_type = 'Possession'
    elif data in efficiency:
        chart_type = 'Efficiency'
    elif data in attacking_vs_defensive:
        chart_type = 'Attack_Vs_Defence'
    elif data in expected_goal_performance:
        chart_type = 'Expected_Goal_Performace'
    else:
        chart_type = 'NA'
    return chart_type


# In[35]:


complete_data = [regular_season_melt_data, standard_melt_data, goalkeeping_melt_data, shooting_melt_data,                  passing_stats_melt_data, passing_type_melt_data, goal_and_shot_creation_melt_data,                  defensive_action_melt_data, possession_melt_data, playing_time_melt_data, miscellaneous_melt_data]

intermediate_all_data = pd.concat(complete_data)
intermediate_all_data['Chart_data'] = intermediate_all_data.Metric.apply(chart_type)
intermediate_all_data.insert(3,"KPIs","NA")


# In[36]:


def col_split(data):
    if str(data[0].split('_')[0]).startswith('Unnamed') or str(data[0].split('_')[0]).startswith('vs-Unnamed'):
        col_a = 'NA'
        col_b = data[0].split('_')[3]
        return col_a, col_b
    else:
        col_a = data[0].split('_')[0]
        col_b = data[0].split('_')[1]
        return col_a, col_b


# In[37]:


intermediate_all_data[["Metric","KPIs"]] = intermediate_all_data[["Metric","KPIs"]].apply(col_split,axis=1,result_type='expand')


# In[38]:


intermediate_all_data['Key'] = intermediate_all_data['Year'] + intermediate_all_data['Squad'] 


# In[39]:


intermediate_all_data.to_csv("combined_data.csv",index=False,encoding='utf-8-sig')


# # Regular Season

# In[42]:


regular_season_stats_list = [] 
for key, value in complete_data_dict.items():

    ### extracting team info
    team_info = value[0].iloc[:,[0,1]].copy()
    
    ### overall data preparation
    league_result = value[0].copy()
    league_result.insert(0,'Year',key.split('_')[1])
    league_result.insert(1,'Data_level','Overall')
    
    
    ### home level data preparation
    home_stats = value[1].iloc[:,home_level_data_index].copy()
    home_stats.columns = home_stats.columns.droplevel(level=0)
    home_data = pd.concat([team_info,home_stats],axis=1)
    home_data.insert(0,'Year',key.split('_')[1])
    home_data.insert(1,'Data_level','Home')
    
    
    ### away level data preparation
    away_stats = value[1].iloc[:,away_level_data_index].copy()
    away_stats.columns = away_stats.columns.droplevel(level=0)
    away_data = pd.concat([team_info,away_stats],axis=1)
    away_data.insert(0,'Year',key.split('_')[1])
    away_data.insert(1,'Data_level','Away')
    
    ## complete_data for a single year
    complete_data = pd.concat([league_result,home_data,away_data])
    
    ## data appending into single list for all dataframes
    regular_season_stats_list.append(complete_data)
    
    
# ### data appending into single dataframe
regular_season_data = pd.concat(regular_season_stats_list)
regular_season_data.drop(['Attendance','Top Team Scorer','Goalkeeper','Notes'],axis=1,inplace=True)


# In[43]:


regular_season_data = regular_season_data.merge(playing_time_stats_data.iloc[:,[0,1,3]], on = ['Year','Squad'])                                         .rename({'Unnamed: 2_level_0_Age':'Age'},axis=1)


# In[44]:


regular_season_data['Key'] = regular_season_data['Year'] + regular_season_data['Squad'] 


# In[46]:


regular_season_data.to_csv("regular_season_stats_main.csv",index=False,encoding='utf-8-sig')


# # Bridge Data

# In[40]:


bridge_data = intermediate_all_data[['Year','Squad']].drop_duplicates()
bridge_data['Key'] = bridge_data['Year'] + bridge_data['Squad'] 


# In[41]:


bridge_data.to_csv("Bridge Table.csv",index=False,encoding='utf-8-sig')

