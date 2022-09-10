from backend.services.main_services import main_services
from backend.entities.team_information_entity import team_information_entity
from backend.entities.team_entity import team_entity

def test_start_game():
    test_obj = main_services()  
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

    all_teams_dict = test_obj.start_game(team_information)
    correct_result = "{'1': {'teamA': Group Ranking Obj: {teamA, goals: 0, wins: 0, draws: 0, losts: 0}, 'teamB': Group Ranking Obj: {teamB, goals: 0, wins: 0, draws: 0, losts: 0}, 'teamC': Group Ranking Obj: {teamC, goals: 0, wins: 0, draws: 0, losts: 0}, 'teamD': Group Ranking Obj: {teamD, goals: 0, wins: 0, draws: 0, losts: 0}, 'teamE': Group Ranking Obj: {teamE, goals: 0, wins: 0, draws: 0, losts: 0}, 'teamF': Group Ranking Obj: {teamF, goals: 0, wins: 0, draws: 0, losts: 0}}, '2': {'teamG': Group Ranking Obj: {teamG, goals: 0, wins: 0, draws: 0, losts: 0}, 'teamH': Group Ranking Obj: {teamH, goals: 0, wins: 0, draws: 0, losts: 0}, 'teamI': Group Ranking Obj: {teamI, goals: 0, wins: 0, draws: 0, losts: 0}, 'teamJ': Group Ranking Obj: {teamJ, goals: 0, wins: 0, draws: 0, losts: 0}, 'teamK': Group Ranking Obj: {teamK, goals: 0, wins: 0, draws: 0, losts: 0}, 'teamL': Group Ranking Obj: {teamL, goals: 0, wins: 0, draws: 0, losts: 0}}}"
    assert str(all_teams_dict) == correct_result

def test_enter_result():
    all_teams_dict = dict()
    group1_dict = dict()
    group1_dict["teamA"] = team_information_entity(team_entity("teamA", "01/04", "1"))
    group1_dict["teamB"] = team_information_entity(team_entity("teamB", "01/01", "1"))
    all_teams_dict = {"1": group1_dict}
    
    match_result = "teamA teamB 0 1"

    test_obj = main_services()  
    all_teams_dict = test_obj.enter_result(all_teams_dict, match_result)

    correct_result = "{'1': {'teamA': Group Ranking Obj: {teamA, goals: 0, wins: 0, draws: 0, losts: 1}, 'teamB': Group Ranking Obj: {teamB, goals: 1, wins: 1, draws: 0, losts: 0}}}"
    assert str(all_teams_dict) == correct_result

def test_tabulate_points():
    all_teams_dict = dict()
    group1_dict = dict()
    group1_dict["teamA"] = team_information_entity(team_entity("teamA", "01/04", "1"))
    group1_dict["teamB"] = team_information_entity(team_entity("teamB", "01/01", "1"))
    all_teams_dict = {"1": group1_dict}
    
    match_result = "teamA teamB 0 1"

    test_obj = main_services()  
    all_teams_dict = test_obj.enter_result(all_teams_dict, match_result)
    points_by_group = test_obj.tabulate_points(all_teams_dict)
    correct_result = "{'1': {0: ['teamA'], 3: ['teamB']}}"
    assert str(points_by_group) == correct_result
