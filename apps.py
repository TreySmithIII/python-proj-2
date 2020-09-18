import constants

team_copy = constants.TEAMS
players_copy = constants.PLAYERS
height=[]
def clean_data():
    for player in players_copy:
        player['height']=int(player['height'][0:2])
        
        
        if player['experience'] == 'YES':
            player['experience'] == True
            
        elif player['experience'] == 'NO':
            player['experience'] == False
            


clean_data()
