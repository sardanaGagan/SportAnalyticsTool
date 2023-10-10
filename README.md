# SportAnalyticsTool - ScoutGinie
Using a sports performance derived dataset, designed and produce a sports analytics-based tool to generate insight and support decision making.

## Tableau Dashboard Link - https://public.tableau.com/app/profile/gagan.sardana/viz/MIS41420-Group10-ScoutGenie/Story2?publish=yes

## Introduction
Welcome to the ScoutGenie User Manual, your comprehensive guide to this sophisticated tool specifically designed for football coaches, analysts, and enthusiasts. ScoutGenie is a patent platform that unlocks the power of football data analysis and visualisation. Built around a robust Tableau dashboard, it is composed of four key modules: Team Overview, Match Analyser, Player Finder and Player Profile. This manual aims to help you navigate the tool's installation, setup, and usage, empowering you to make data-driven decisions confidently.
Installation and Setup
Installation and Setup Here's how to install and set up ScoutGenie:
1.	Install Necessary Dependencies: The ScoutGenie application requires Python 3.9 or higher and Tableau 2023.1. Please make sure to install these before moving forward.
2.	Download the Project Repository: Access and download the project repository onto your system.
3.	Set up the Project Environment: Open your command prompt and navigate to the project directory. Once you're in the right place, install the necessary Python packages by running the command “pip install -r requirements.txt”.

## Data Download
ScoutGenie relies on a Python codebase to download the football data. Follow the steps below to get the data:
Open the command prompt in the codebase downloaded directory.
**1.	Open the Command Prompt:** Open the command prompt in the directory where you downloaded the codebase.
**2.	Configure Input Parameters:** Adjust any necessary input parameters like data source, URLs, or file paths directly within each Python script intended for data download.
**3.	Downloading Data:** Enter the command python “all_scripts_data_download.py” in the command prompt and wait for the data download to finish.
**4.	Optional -** Run Individual Python Files: If you need to run any Python files separately, simply replace all_scripts_data_download.py in the command with the desired file name.

## Tableau Interface
The ScoutGenie provides three main dashboards for analysing football data:
### 1.	Team Overview
The Team Overview Dashboard is an insightful and interactive tool designed to analyse team performance across various Key Performance Indicators (KPIs). It allows you to visualise and compare team statistics, trends, and playing styles.
### 2.	Match Analyser
The Match Analyser Dashboard is a comprehensive tool that helps you delve into the intricate details of football matches. It provides a detailed analysis of aspects such as passing, shot outcomes, player positions, pass success rates, and more.
### 3.	Player Finder
The Scouting Dashboard is an interactive tool designed to help you analyse and compare the performance of football players based on various Key Performance Indicators (KPIs). It provides a detailed, visual representation of player performance data, allowing you to scout players effectively.
### 4.	Player Profile
The Player Profile Dashboard is a detailed, interactive tool designed to provide a comprehensive analysis of individual player performance. It enables you to delve into a player's performance metrics, showcasing their abilities and contributions in different areas of play.

## Dashboard Navigation
The subsequent step-by-step instructions will efficiently guide you through the process of navigating and fully utilising the versatile features of the ScoutGenie:
### 1.	Launching the Workbook
Begin your data discovery journey by accessing the interactive analytics workbook through the provided Tableau Public hyperlink. This link serves as your doorway into a world of compelling visual data analysis.
### 2.	Dashboard Selection	
After the workbook is loaded, a range of dashboards will be at your disposal. Identify and select your preferred dashboard from the convenient dashboard navigation menu.
### 3.	Data Filtering
Enhance your data exploration by employing versatile filters. These filters allow you to customise the data based on distinct dimensions like team, player, and match, among others. Applying these filters effectively narrows down the breadth of your data, making your analyses more targeted and manageable.
### 4.	Interacting with Visualisations 
The dashboard is not just for viewing. You can directly interact with the displayed visualisations. Select specific data points, apply drill-downs for more detailed insights, or zoom in on areas of interest to explore your data in depth.
### 5.	Additional Instructions: 
Please refer to the specific guidelines and tips provided for each dashboard. These additional instructions are tailored to optimise your user experience and ensure a smooth data analysis process.

# Data Analysis
The ScoutGenie offers a range of data analysis capabilities:

## Team Overview
### A.	Dashboard Overview
**1.	360 Degree Team Analysis (P90):** This chart displays per 90-minute KPIs, such as crosses p90, goals p90, etc. It provides an at-a-glance view of a team's performance in multiple areas.
**2.	Team Trends:** This visual provides data for specific KPIs over the last six years. It allows you to track a team's performance over time and analyse the evolution of their playstyle and strategy.
**3.	Team Performance Comparison:** A scatter plot comparing two different KPIs under six different scenarios (attack, defensive, attack vs defence, etc). This visual helps understand the team's style in relation to other teams by showing how they perform in different quadrants based on their KPIs.
**4.	Comparative Analysis – Expected vs Actual:** This visualization contrasts the actual versus expected performance in terms of goals, assists, and goals conceded for two distinct teams. It provides a deeper understanding of teams' scoring capabilities and their ability to meet expectations.

### B.	Filters
**1.	Year:** Allows users to select the year of data they want to view, between 2017-2022. This filter applies to the 360 Degree Team Analysis, Team Performance Comparison and Comparative Analysis.
**2.	Club:** Allows users to select multiple clubs (limit two at a time for better understanding and comparison of teams’ performance) for comparing team overview and team trends.
**3.	KPIs:** Allow users to select from a range of Per 90 Minute (P90) KPIs to visualize and interpret trends. This filter operates on the Team Trend Visual dashboard, allowing a deeper understanding of performance metrics over time.
**4.	Playing Style:** Allows users to select different playing styles for comparison between teams. This filter applies to the Team Performance Comparison visual.

### C.	Insights
The dashboard can offer several valuable insights into team performance and styles:
**1.	Team Performance:** The 360 Degree Team Analysis provides a holistic view of a team's performance across several KPIs, helping identify areas of strength and weakness.
**2.	Performance Trends:** The Team Trends visual helps analyse the evolution of a team's performance over time, which can aid in identifying improvement or decline in certain areas.
**3.	Style Analysis:** The Team Performance Comparison visual allows for a deeper understanding of a team's playstyle in different scenarios (attack, defence, attack vs defence). It provides insight into a team's strategy and how it measures up against other teams.
**4.	Comparative Analysis:** By selecting multiple clubs, users can directly compare their expected vs actual performance, providing valuable insight for tactical planning and strategizing.

### D.	User Instructions:
#### Filter Selection 1:
**1.	Set the Year Filter:** Start by selecting the year of data you wish to view from the Year Filter. This will ensure that the visuals of the Team Overview and Team Style Comparison display the relevant data for your analysis.
**2.	Choose Clubs:** Select one or two clubs from the Club Filter to compare their team overviews and trends. Although the system allows the selection of multiple clubs, narrowing your focus to two clubs at a time aids in comprehending the nuances of each team's performance more effectively.
**3.	Select KPIs:** Use this filter to view different trends among different teams. 

### Exploring Dashboard:
**1.	Explore 360 Degree Team Analysis (P90):** Analyse the radar chart to gain an at-a-glance understanding of each club's performance across various KPIs. Identify areas of strength and weakness for each team. The difference in the two colours shows the performance of the two teams as per the selected filter for clubs. Use the highlighter to select the individual team and then hover over each edge to know the value of the KPIs.
**2.	Study Team Trends:** Examine the Team Trends visual to track a team's performance over time. Identify patterns, improvements, or declines in specific KPIs to understand their playstyle evolution. 
**3.	Comparative Analysis - Expected vs Actual:** Utilise this to understand the actual versus expected performance in terms of goals, assists, and goals conceded for two distinct teams.

#### Filter Selection 2 :
Playing Style: Use this filter to select different playing styles and analyse the team dynamics on the Team Performance Comparison visual.
#### Exploring Dashboard:	
**1.	Quadrant Graph:** We can compare the performance of the different teams based on the attacking vs defensive, expected goal performance and many more styles to understand the team's style in relation to other teams by showing how they perform in different quadrants based on their KPIs.

### The Team Overview Dashboard is a powerful tool for understanding and comparing team performance and styles. This information can provide a competitive edge in tactical decision-making and strategic planning.

## Match Analyser
### A.	Dashboard Overview
**1.	Passing Matrix:** A visual that demonstrates passing interplay between players. It shows who the passer was, who received it, and the number of passes between them.
**2.	Pass Cluster:** Visualising the location and frequency of passes on the pitch. The outcome of the pass can also be determined. This visual can be filtered using the Passing Matrix to understand specifics about passing interactions.
**3.	Average Player Pass Position:** Showcases average positions from which each player passes the ball, given they've made at least 10 passes in a match.
**4.	Shot Analyser:** Details the location from where shots were taken and their respective outcomes.
**5.	Pass Success % by Zone:** Analyses the success percentage of passes in different zones on the pitch. This can be controlled by the Average Player Pass Position visual or using a player filter to understand from what locations players were most successful in their passing.

### B.	Filters
**1.	Match Date:** Filter fixtures by date.
**2.	Fixture:** Select which match to analyse.
**3.	Team:** This filter allows the user to choose the specific team you wish to analyse. It applies to all the visuals on the dashboard, ensuring a consistent focus on the selected team across your entire analysis. 
**4.	Player:** Works in Pass Success % by Zone to analyse individual player passing.

### C.	Insights
This dashboard can provide insights into a wide array of game aspects including:
**1.	Understanding Player Connections:** The Passing Matrix can show you the relationship and understanding between players, which can then inform decisions on tactics and formations.
**2.	Visualising Game Flow:** The Pass Cluster helps visualise how the game is being controlled and played by showing where passes are being made.
**3.	Player Positioning:** The Average Player Pass Position can help in understanding how players are positioned on average throughout the game. This can inform strategy and tactics regarding player positions.
**4.	Shot Efficiency:** The Shot Analyser provides insights into where players are most successful in scoring from, which can inform attacking strategy.
**5.	Passing Success Rate:** The Pass Success% on Pitch by Zone gives insights into where on the pitch players are most successful with their passes. This can inform tactical decisions and training focuses.
**6.	Tactical Adjustment:** By using different filters you can analyse performance by match, by team, or by player. This allows for detailed analysis that can be used to inform tactics, training, and performance reviews.

### D.	User Instructions:
#### Exploring Dashboard: 
**Passing Matrix:** Each cube in the matrix represents a pass from one player to another.
**Pass Cluster:** This visualization illustrates the spatial distribution and frequency of passes on the pitch. Exploring these clusters can help you discern common patterns of play, identify key areas of passing activity, and understand the spatial strategies adopted during a match.
When a cube is selected in the Passing Matrix, the corresponding pass is visualised on the Pass Cluster. This allows users to understand not only the outcome of the pass but also its location on the pitch. You can see where the ball was passed during the match, offering a spatial understanding of player collaboration.
**Analyse Average Player Pass Position:** This visual showcases the average positions from which each player passes the ball by selecting each dot in the playground access. It requires players to have made at least 10 passes in a match to be included. Use this information to gain insights into player positioning and their passing tendencies.
**Explore the Shot Analyser:** The Shot Analyser details the location from where shots were taken and their respective outcomes. Analyse the shot locations by selecting any figure in the dashboard to understand where players are most successful in scoring. Use this information to inform attacking strategies and shot selection.
**Gain Insights from Pass Success % by Zone:** This visual analysis of the success percentage of passes in different zones on the pitch. It can be controlled by using a player filter or directly from Average Player Position visual. Use this information to assess passing efficiency and identify areas of strength or improvement.

### The Match Analyser Dashboard is a powerful tool that can help you unlock key insights from football matches. By understanding the details of each match, you can make informed decisions and create successful strategies.

## Player Finder
### A.	Dashboard Overview
**1.	Scatter Plots (6 visuals):** All visuals in the dashboard are interactive scatter plots. Hovering over a data point highlights that player across all scatter plots, allowing for easy comparison of player performance across multiple KPIs. The scatter plots will change based on the position selected in the 'Scout By Position' filter: For instance, selecting 'Forward' might display scatter plots for 'Above/below expected goals', 'Non-penalty Expected goals P90', 'Shot Creation Action 90', 'Shot on Target %', 'Goal Scored P90', and 'Key Passes'.
**2.	Playground Feature:** This allows users to access a hidden dashboard and select their own KPIs for the X-axis and Y-axis. This feature provides flexibility to analyse other KPIs beyond the predefined ones.

### B.	Filters
**1.	Scout By Position:** This filter lets users select the position of the player they are scouting and changes the pre-defined KPIs on the dashboard based on the selection. The options include ‘Forward’ 'Midfielder', 'Defender', 'Goalkeeper' and 'Others'.
**2.	League:** Users can select one of the Big 5 European leagues, all leagues, or a combination.
**3.	Age:** Set age criteria for scouting.
**4.	Player:** Search for a specific player.
**5.	Position:** Select the player’s positions.
**6.	Matches Played:** Filter players based on the number of matches played.
**7.	Playing Minutes:** Filter players based on the minutes played.
**8.	Annual Wages:** Set income criteria for scouting.
**9.	X & Y axis:** Select from the available KPIs to analyse players according to custom requirements. Only available in the Playground Mode

### C.	Insights
The dashboard can offer insights into several aspects of player performance, including:
**1.	Player Comparison:** The scatter plots allow for direct comparison of players, making it easier to identify high-performing individuals or those who perform well in specific areas.
**2.	Position-Specific Metrics:** By changing the 'Scout By Position' filter, users can focus on KPIs that are most relevant to specific player positions.
**3.	Customised Analysis:** The 'Playground' feature offers flexibility in analysis, enabling users to select KPIs that best suit their specific needs and interests.
**4.	Detailed Player Search:** The range of filters allows users to perform a detailed search for players based on factors such as age, number of matches played, and wages, in addition to performance metrics.
**5.	Scouting Efficiency:** By providing a comprehensive view of a player’s performance metrics across different KPIs in a single dashboard, scouting becomes more efficient and effective.

### D.	User Instructions:
#### Selection of the Filters: 
**1.	Scout by Position:** Select the position of the player you want to scout, such as 'Forward', 'Midfielder', 'Defender', 'Goalkeeper', or 'Others'. It will change the pre-defined KPIs on the dashboard according to the selection.
**2.	League:** Choose one of the Big 5 European leagues, select all leagues, or combine specific leagues for your analysis.
**3.	Age:** Set age criteria to narrow down your search to specific age ranges.
**4.	Player:** Use the search function to find a specific player by name. 
**5.	Position:** Select specific player positions to further refine your search. 
**6.	Matches Played:** Filter players based on the number of matches they have played. 
**7.	Playing Minutes:** Filter players based on the total minutes they have played. 
**8.	Annual Wages:** Set income criteria to focus on players within a specific wage range.

#### Click on the Playground button to navigate to Playground Area where users could choose the x and y axis’s KPIs to utilize the full potential of the player finder dashboard.

#### Explore the Scatter Plots: 
**1.**	Depending on the position selected in the 'Scout By Position' filter, the scatter plots will display relevant performance metrics for that position. Click on a data point in any scatter plot to highlight that player across all scatter plots, allowing for easy comparison of their performance across multiple KPIs.
**2.**	Analyse the scatter plots to identify high-performing players or those who excel in specific areas based on the selected KPIs.The Scouting Dashboard is a powerful tool that can help you identify and compare players based on a wide range of performance metrics. This comprehensive analysis can inform recruitment strategies and decision-making processes in football management. 

#### The Player Finder Dashboard is a powerful tool that can help you identify and compare players based on a wide range of performance metrics. This comprehensive analysis can inform recruitment strategies and decision-making processes in football management. 

## Player Profile
### A.	Dashboard Overview:
**1.	Player Basic Details:** The section showcases basic information about the selected player, including their name, nationality, age, position, and current team. This information helps in identifying the player and provides context for their performance analysis.
**2.	Attack Metrics:** Table 1 presents metrics related to the player's attacking performance. The metrics included are goals, shots taken, shots on target, shot success ratio, goal conversion ratio, and assists. These metrics provide insights into the player's effectiveness in scoring goals and assisting in the attack.
**3.	Build-up Metrics:** Table 2 displays metrics associated with the player's build-up play. The metrics included in this table are total passes, pass success ratio, and crosses. These metrics help evaluate the player's passing ability, accuracy, and involvement in creating opportunities through crosses.
**4.	Defence Metrics:** Table 3 exhibits metrics related to the player's defensive capabilities. The metrics included in this table are blocks, tackles, interceptions, yellow cards, red cards, and fouls committed. These metrics offer insights into the player's defensive contributions and disciplinary record.
**5.	Performance Over Time:** The dashboard includes eight bar charts that depict the player's performance over the last five consecutive years. Each bar chart represents a specific metric, including crosses, GCA (Goal Creating Actions), passes, goals, assists, shots on target, touches, and fouls. The Y-axis represents the performance level, and the X-axis represents the corresponding year. An average line is included in each chart to provide analytics and a benchmark for comparison.

### B.	Filters:
**1.	Player:** Users can use this filter to search and select a specific player. 

### C.	Insights:
The dashboard can offer insights into several aspects of player performance, including:
**1.	Performance Comparison:** Compare a player's performance across different metrics over time to identify trends, improvements, or declines in specific areas.
**2.	Strengths and Weaknesses:** Analyse the metrics in each table to determine the player's strengths and weaknesses. Assess their attacking prowess, passing accuracy, defensive contributions, and disciplinary record.
**3.	Consistency:** Evaluate the player's consistency by observing the performance line in each bar chart. Consistent performance above or below the average line indicates reliability in specific metrics.
**4.	Yearly Progression:** Track the changes in performance levels from year to year to identify the player's progression or regression in specific areas of their game.
**5.	Comparison with Average:** Compare the player's performance with the average line in each bar chart. Consistently outperforming the average line suggests a higher level of performance, while consistently falling below indicates room for improvement.

### D.	User Instructions:
**1.**	Use the "Player Name" filter to search and select a specific player.
**2.**	Review the player's profile details for identification and context.
**3.**	Analyse the attack, build-up, and defence metrics in their respective tables.
**4.**	Examine the bar charts to understand the player's performance over the last five years.
**5.**	Compare metrics, observe trends, and assess strengths, weaknesses, and consistency.
**6.**	Pay attention to the average lines to gauge performance relative to benchmarks.
**7.**	Use the insights gained from the dashboard to evaluate the player's overall profile and contributions.

#### The Player Profile Dashboard is a powerful tool for comprehensive player performance evaluation. Accessing key performance metrics, trend analysis, and comparative features, it enables an in-depth understanding of a player's strengths, weaknesses, and contributions over time. It aids in making data-driven decisions, crafting effective strategies, and identifying potential talent with precision.

## Customisation
The ScoutGenie can be customised to suit your specific needs:
**1.	Team Overview Dashboard:** The dashboard offers several customisation options using filters. The Year filter lets users select the specific year of data they want to analyse. The Club filter allows for the comparison of up to two clubs at a time, giving users the flexibility to choose which teams they want to compare. The Team Comparison Style filter enables users to select different styles for comparison, allowing for a more tailored analysis of team performance and style.
**2.	Match Analyser Dashboard:** Users can customise their analysis by selecting their preferred filters: Match Date, Fixture, Team, and Player. This allows them to analyse performance by match, team, or individual player to meet their specific needs.
**3.	Scouting Dashboard:** The 'Playground' feature is a powerful customisation tool. It lets users pick their own KPIs for the X and Y axes of the scatter plots to tailor the analysis according to their scouting interests. In addition, the filters for age, matches played, playing minutes, and annual wages can all be adjusted to fit specific scouting criteria.
**4.	Player Profile Dashboard:** Primarily, the 'Player' filter allows you to select a specific player whose performance and contribution you wish to evaluate. Based on your interests or needs, you can focus on different performance aspects: attack, build-up, or defence, each represented in a separate table with relevant metrics. Across all four dashboards, users can generally customise their experience by selecting and adjusting a wide range of filters to meet their unique analysis needs. The ability to select different KPIs, match parameters, player criteria, or team comparisons ensures the dashboards remain flexible and adaptable tools for detailed football analysis.

## Best Practices
To maximise the effectiveness of the ScoutGenie, it is recommended to adhere to the following improved best practices:
**1.	Data Accuracy and Timeliness:** Ensure that the data you are utilising is both accurate and current. Outdated or inaccurate data can lead to misinterpretation and flawed conclusions.
**2.	Data Cleaning and Preprocessing:** Prior to loading your data into the dashboard, conduct a thorough cleaning and preprocessing. This entails the removal of duplicates and irrelevant information, and handling missing values, ultimately improving data quality for more precise insights.
**3.	Effective Filter Utilisation:** Make the most of the filtering options available in Tableau. Apply relevant filters to focus on pertinent dimensions and time periods. This will allow for a more targeted data analysis and visualisation, aiding in the extraction of useful insights.
**4.	Diversified Visualisation and Analysis:** Do not hesitate to experiment with a variety of visualisation and analytical techniques. By varying your methods, you could potentially uncover unique insights that may otherwise go unnoticed.
**5.	Findings Validation:** After extracting insights, validate your findings with established domain knowledge. This ensures that your results are plausible and grounded. If necessary, do not shy away from conducting further research to corroborate your findings.

## Conclusion
Bravo on successfully navigating through the ScoutGenie user manual! Our aspiration is that this documentation has served as a thorough and accessible roadmap to the installation, configuration, and application of the software.
Now that you are well-equipped with the necessary knowledge, immerse yourself in the sophisticated dashboards, delve into the intricacies of football data analytics, and leverage this robust tool to foster enhanced performance and scouting.
Remember, every interaction with ScoutGenie brings you one step closer to a more data-informed approach to football strategy. Enjoy the journey and let ScoutGenie be your trusted ally on this path to success.
