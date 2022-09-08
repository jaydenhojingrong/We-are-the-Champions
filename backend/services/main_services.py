from backend.entities.team_entity import team_entity
from backend.entities.group_ranking_entity import group_ranking_entity

class main_services():
    
    def start_game(self, team_information):
        # split team_info by the nextline
        # split again by space
        # [0] = team, [1] = date, [2] = group
        all_teams_dict = dict()
        team_information_arr = team_information.split("\n")
        for team in team_information_arr:
            team_data = team.split()
            team_obj = team_entity(team_data[0], team_data[1], team_data[2])
            group_ranking_obj = group_ranking_entity(team_obj)

            if team_obj.group in all_teams_dict:
                all_teams_dict[team_obj.group].append(group_ranking_obj)
            else:
                all_teams_dict[team_obj.group] = list()
                all_teams_dict[team_obj.group].append(group_ranking_obj)
            
        print(all_teams_dict)

if __name__ == "__main__":
    obj1 = main_services()  
    team_information = """teamA 01/04 1
teamB 02/05 1
teamC 03/06 1
teamD 04/06 1
teamE 05/06 1
teamF 15/06 1
teamG 14/06 2
teamH 13/06 2
teamI 12/06 2
teamJ 11/06 2
teamK 10/06 2
teamL 27/06 2"""

    obj1.start_game(team_information)