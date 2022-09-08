from backend.entities.team_entity import team_entity
from backend.entities.group_ranking_entity import group_ranking_entity
from backend.services.date_service import get_excel_date_serial_value

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
                all_teams_dict[team_obj.group][group_ranking_obj.team.name] = group_ranking_obj
            else:
                all_teams_dict[team_obj.group] = dict()
                all_teams_dict[team_obj.group][group_ranking_obj.team.name] = group_ranking_obj
            
        return all_teams_dict

    def enter_result(self, all_teams_dict, match_results):
        # similarly.. split match result into array
        # each array into match details array
        # arr[0] = team1, arr[1] = team2, arr[2] = goal1, arr[3] = goal2, 
        # compare goals to see who won?
        # go to new function for logic on point allocation -> returns with tuple (points_for_team_1, points_for_team_2)
        # update the all_teams_dict on the points + goals scored
        result_data = list()
        winner = str()
        match_results_arr = match_results.split("\n")
        for result in match_results_arr:
            result_data = result.split()
            record_match(all_teams_dict, result_data)
        return all_teams_dict

    def tabulate_points(self, all_teams_dict, win_points, draw_points, lose__points):
        
        # create a new dict to store group as keys and points as value in an array
        # for each key in all_teams_dict
        # accumulate points.. wins = points + 3 etc

        points_by_group = dict()
        for group in all_teams_dict:
            for team_record in all_teams_dict[group]:
                points = int()
                
                points += (all_teams_dict[group][team_record].wins * win_points)
                points += (all_teams_dict[group][team_record].draws * draw_points)
                points += (all_teams_dict[group][team_record].losts * lose__points)
            
                if group in points_by_group:
                    if points in points_by_group[group]:
                        points_by_group[all_teams_dict[group][team_record].team.group][points].append(all_teams_dict[group][team_record].team.name)
                    else:
                        points_by_group[all_teams_dict[group][team_record].team.group][points] = list()
                        points_by_group[all_teams_dict[group][team_record].team.group][points].append(all_teams_dict[group][team_record].team.name)
                else:
                    points_by_group[group] = dict()
                    points_by_group[group][points] = list()
                    points_by_group[group][points].append(all_teams_dict[group][team_record].team.name)
        # print(points_by_group)
        return points_by_group
                
    def get_rankings(self, all_teams_dict, points_by_group):

        # put inside a dict where key is the group, value is the sorted list by ranking (desc)
        ranking_by_group = dict()
        
        for group in points_by_group:
            for points, team_names in sorted(points_by_group[group].items(), reverse=True):
                if len(team_names) > 1:
                    team_names = handle_teams_with_same_points(all_teams_dict, team_names, group)

                if group in ranking_by_group:
                    ranking_by_group[group].extend(team_names)
                else:
                    ranking_by_group[group] = list()
                    ranking_by_group[group].extend(team_names)
        
        return ranking_by_group


def handle_teams_with_same_points(all_teams_dict, team_names, group):
    # compare goals
    all_goals = dict()
    new_rankings = list()
    for team in team_names:
        if all_teams_dict[group][team].goals in all_goals:
            all_goals[all_teams_dict[group][team].goals].append(team)
        else:
            all_goals[all_teams_dict[group][team].goals] = list()
            all_goals[all_teams_dict[group][team].goals].append(team)

    for goals, team_names in sorted(all_goals.items(), reverse=True):
        if len(team_names) > 1:
            team_names = handle_teams_with_same_points_and_goals(all_teams_dict, team_names, group)

        new_rankings.extend(team_names)
    return new_rankings

def handle_teams_with_same_points_and_goals(all_teams_dict, team_names, group):
    # compare recalculated score
    new_all_teams_dict = dict(all_teams_dict)
    new_rankings = list()
    teams_by_new_points = dict()
    service_obj = main_services()

    # change point system
    points_by_group = service_obj.tabulate_points(new_all_teams_dict, 5, 3, 1)

    # extract only the teams that we are interested in
    for interested_team in team_names:
        for points, new_team_names in points_by_group[group].items():
            for new_team in new_team_names:
                if new_team == interested_team:
                    if points in teams_by_new_points:
                        teams_by_new_points[points].append(interested_team)
                    else:
                        teams_by_new_points[points] = list()
                        teams_by_new_points[points].append(interested_team)
    
    for points, team_names in sorted(teams_by_new_points.items(), reverse=True):
        if len(team_names) > 1:
            # pass
            team_names = handle_teams_with_same_points_and_goals_and_new_points(all_teams_dict, team_names, group)
        new_rankings.extend(team_names)

    return new_rankings

def handle_teams_with_same_points_and_goals_and_new_points(all_teams_dict, team_names, group):
    # compare register date
    
    # extract team reg date in all_teams_dict
    # convert into a int to represent their date value and put them in a dict like: {2332341: ["teamA"], 33434234: ["teamC"]}
    # sort them into a list
    # return the list
    new_rankings = list()
    teams_by_registered_date = dict()
    for interested_team in team_names:
        date_registered = (all_teams_dict[group][interested_team].team.date_registered)
        date_value = get_excel_date_serial_value(date_registered)

        if date_value in teams_by_registered_date:
            teams_by_registered_date[date_value].append(interested_team)
        else:
            teams_by_registered_date[date_value] = list()
            teams_by_registered_date[date_value].append(interested_team)
    
    for date_value, team_names in sorted(teams_by_registered_date.items()):
        new_rankings.extend(team_names)
    
    return new_rankings

def record_match(all_teams_dict, result_data):
    team1 = result_data[0]
    team2 = result_data[1]
    goal1 = result_data[2]
    goal2 = result_data[3]
    winner = tuple()
    loser = tuple() 
    is_draw = bool()

    # if winner/loser tuple empty.. means it is a draw
    if goal1 > goal2:
        winner = (team1, goal1)
        loser = (team2, goal2)
    elif goal1 < goal2:
        winner = (team2, goal2)
        loser = (team1, goal1)
    else:
        is_draw = True
        winner = (team1, goal1)
        loser = (team2, goal2)
    
    # update match in all_teams_dict
    # for each participant..
    # for each group.. is the participant inside?
    # if inside.. update the wins/draws/losts field

    winner_name = winner[0]
    winner_goals = int(winner[1])
    loser_name = loser[0]
    loser_goals = int(loser[1])

    for group in all_teams_dict:
        if winner_name in all_teams_dict[group]:
            
            # accmulate goals scored
            all_teams_dict[group][winner_name].goals += winner_goals
            all_teams_dict[group][loser_name].goals += loser_goals

            #check if it is a draw
            if is_draw:
                all_teams_dict[group][winner_name].draws += 1
                all_teams_dict[group][loser_name].draws += 1
            else:
                #add win/lose/draw record
                all_teams_dict[group][winner_name].wins += 1
                all_teams_dict[group][loser_name].losts += 1


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

    all_teams_dict = obj1.start_game(team_information)
    
    match_result = """teamA teamB 0 1
teamA teamC 1 3
teamA teamD 2 2
teamA teamE 2 4
teamA teamF 3 3
teamB teamC 0 1
teamB teamD 2 2
teamB teamE 4 0
teamB teamF 0 0
teamC teamD 2 0
teamC teamE 0 0
teamC teamF 1 0
teamD teamE 0 3
teamD teamF 2 1
teamE teamF 3 4
teamG teamH 3 2
teamG teamI 0 4
teamG teamJ 1 0
teamG teamK 1 4
teamG teamL 1 4
teamH teamI 2 0
teamH teamJ 3 0
teamH teamK 3 4
teamH teamL 0 1
teamI teamJ 2 1
teamI teamK 3 0
teamI teamL 1 3
teamJ teamK 1 4
teamJ teamL 0 3
teamK teamL 0 0"""
    all_teams_dict = obj1.enter_result(all_teams_dict, match_result)

    points_by_group = obj1.tabulate_points(all_teams_dict, 3, 1, 0)
    ranking_by_group = obj1.get_rankings(all_teams_dict, points_by_group)
    print(ranking_by_group)

    # testing edge case where same points and goals, thus need to compare by recalculating points and also registered_date
    print(handle_teams_with_same_points_and_goals(all_teams_dict, ["teamG", "teamH", "teamI", "teamJ"], "2"))

    