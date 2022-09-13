from backend.entities.team_entity import team_entity
from backend.entities.team_information_entity import team_information_entity
from backend.services.date_service import get_excel_date_serial_value

class main_services():

    def start_game(self, team_information):
        # split team_info by the nextline
        # split again by space
        # [0] = team, [1] = date, [2] = group
        all_teams_dict = dict()
        date_range = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", '31']
        group_check_arr = list()
        team_information_arr = team_information.split("\n")

        # check if there are 12 lines. if not? raise exception
        if len(team_information_arr) != 12:
            raise ValueError("Only 12 lines are expected.")

        for team in team_information_arr:
            team_data = team.split()

            # check if there are 3 items in each line
            if len(team_data) != 3:
                raise ValueError("Each line is expected to have 3 items seperated by space.")

            # check date_registered format
            if team_data[1][2] != "/" or not(team_data[1][:2] in date_range) or not(team_data[1][3:] in date_range[:12]):
                raise ValueError("Each date value is expected to be in MM/YY format.")

            # check group count, if more than 2 than raise exception
            if not (team_data[2] in group_check_arr):
                group_check_arr.append(team_data[2])

                if len(group_check_arr) > 2:
                    raise ValueError("Only two different groups are expected.")
                
            team_obj = team_entity(team_data[0], team_data[1], team_data[2])
            group_ranking_obj = team_information_entity(team_obj)

            if team_obj.group not in all_teams_dict:
                all_teams_dict[team_obj.group] = dict()
            all_teams_dict[team_obj.group][group_ranking_obj.team.name] = group_ranking_obj

        # check len of each group, make sure it is 6 each
        for group in group_check_arr:
            if len(all_teams_dict[group]) != 6:
                raise ValueError("Only six teams are expected in each group.")

        return all_teams_dict

    def enter_result(self, all_teams_dict, match_results):
        # similarly.. split match result into array
        # each array into match details array
        # arr[0] = team1, arr[1] = team2, arr[2] = goal1, arr[3] = goal2, 
        # compare goals to see who won?
        # go to new function for logic on point allocation -> returns with tuple (points_for_team_1, points_for_team_2)
        # update the all_teams_dict on the points + goals scored

        result_data = list()
        match_results_arr = match_results.split("\n")   

        for result in match_results_arr:
            result_data = result.split()
            # check result data before passing to record match
            if len(result_data) != 4:
                raise ValueError("Each line is expected to have 4 items seperated by spaces.")
      
            if not result_data[2].isdigit() or not result_data[3].isdigit():
                raise ValueError("Goals for each team is expected to be numeric.")
            
            # check if the teams playing with one another are from the same group
            try:
                record_match(all_teams_dict, result_data)
            except ValueError as err:
                raise err

        # loop the dict key and items
        # for each group..  
        # for each item.. does the wins + draws + lost == 5?
        for group, teams in all_teams_dict.items():
            for name, team_information in teams.items():
                if team_information.wins + team_information.draws + team_information.losts != 5:
                    raise ValueError("Each team is expected to play 5 matches.")
        return all_teams_dict

    def tabulate_points(self, all_teams_dict):

        # create a new dict to store group as keys and points as value in an array
        # for each key in all_teams_dict
        # accumulate points.. wins = points + 3 etc

        points_by_group = dict()
        for group in all_teams_dict:
            for team_record in all_teams_dict[group]:
                points = points_for_team(all_teams_dict[group][team_record])

                if group in points_by_group:
                    if points not in points_by_group[group]:
                        points_by_group[group][points] = list()
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

                if group not in ranking_by_group:
                    ranking_by_group[group] = list()
                ranking_by_group[group].extend(team_names)

        return ranking_by_group


def points_for_team(team_name, win_points = 3, draw_points = 1, lose__points = 0):
    points = int()

    points += (team_name.wins * win_points)
    points += (team_name.draws * draw_points)
    points += (team_name.losts * lose__points)

    return points

def handle_teams_with_same_points(all_teams_dict, team_names, group):
    # compare goals
    all_goals = dict()
    new_rankings = list()
    for team in team_names:
        if all_teams_dict[group][team].goals not in all_goals:
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

    # extract only the teams that we are interested in
    for interested_team in team_names:
        # calculate points for team with new point system
        points = points_for_team(all_teams_dict[group][interested_team], 5, 3, 1)

        if points not in teams_by_new_points:
            teams_by_new_points[points] = list()
        teams_by_new_points[points].append(interested_team)

    for points, team_names in sorted(teams_by_new_points.items(), reverse=True):
        if len(team_names) > 1:
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
        date_registered = all_teams_dict[group][interested_team].team.date_registered
        date_value = get_excel_date_serial_value(date_registered)

        if date_value not in teams_by_registered_date:
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
            # if error here, means name cannot be found in the group
            try:
                # accmulate goals scored
                all_teams_dict[group][winner_name].goals += winner_goals
                all_teams_dict[group][loser_name].goals += loser_goals
            except:
                raise ValueError("Teams (entered from the previous page) are expected to play only with other teams from the same group.")

            #check if it is a draw
            if is_draw:
                all_teams_dict[group][winner_name].draws += 1
                all_teams_dict[group][loser_name].draws += 1
            else:
                #add win/lose/draw record
                all_teams_dict[group][winner_name].wins += 1
                all_teams_dict[group][loser_name].losts += 1

def dict_with_obj_to_json(all_teams_dict):
    
    output = dict()
    for group, teams in all_teams_dict.items():
        output[group] = dict()
        for team in teams:
            output[group][team] = {"teams": teams[team].team.json(), "goals": teams[team].goals, "wins": teams[team].wins, "draws": teams[team].draws, "losts": teams[team].losts}
    
    return output

def json_to_dict_with_obj(all_teams_dict):
    output = dict()
    for group, teams in all_teams_dict.items():
         output[group] = dict()
         for team in teams:
            name = all_teams_dict[group][team]["teams"]["name"]
            date_registered = all_teams_dict[group][team]["teams"]["date_registered"]
            output[group][team] = team_information_entity(team_entity(name, date_registered, group))
    
    return output

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

    points_by_group = obj1.tabulate_points(all_teams_dict)
    ranking_by_group = obj1.get_rankings(all_teams_dict, points_by_group)
    print(ranking_by_group)

    # testing edge case where same points and goals, thus need to compare by recalculating points and also registered_date
    print(handle_teams_with_same_points_and_goals(all_teams_dict, ["teamG", "teamH", "teamI", "teamJ"], "2"))

    