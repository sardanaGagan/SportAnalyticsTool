import sys
print("If you want to make changes to the files:")
print("Go to the each file and make the necessary changes such as updating the urls, chaning logics etc")

input_data = input("Do you wish to continue (Type yes to continue else anything to exit): ")
if input_data.lower() == 'yes':
	print("Downloading Event Data")
	exec(open('Sports_Tool_Data_Extraction_Event_Data_Preparation.py').read())
	print("Event Data Downloaded")

	print("Downloading Player Data For Scouting")
	exec(open('Sports_Tool_Data Extraction_Player_Data_Preparation_Scouting_Data.py').read())
	print("Player Data For Scouting Downloaded")

	print("Downloading Team Data")
	exec(open('Sports_Tool_Data_Extraction_Team_Data_Preparation.py').read())
	print("Team Data Downloaded")

	print("Downloading Team Wages Data")
	exec(open('Sports_Tool_Data_Extraction_Team_Wages_Data_Preparation.py').read())
	print("Team Wages Data Downloaded")

	print("Data Download completed")
else:
	print("Thanks for using our tool")
	sys.exit()





