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
    correct_result = "{'1': {'teamA': Team Information Obj: {teamA, goals: 0, wins: 0, draws: 0, losts: 0}, 'teamB': Team Information Obj: {teamB, goals: 0, wins: 0, draws: 0, losts: 0}, 'teamC': Team Information Obj: {teamC, goals: 0, wins: 0, draws: 0, losts: 0}, 'teamD': Team Information Obj: {teamD, goals: 0, wins: 0, draws: 0, losts: 0}, 'teamE': Team Information Obj: {teamE, goals: 0, wins: 0, draws: 0, losts: 0}, 'teamF': Team Information Obj: {teamF, goals: 0, wins: 0, draws: 0, losts: 0}}, '2': {'teamG': Team Information Obj: {teamG, goals: 0, wins: 0, draws: 0, losts: 0}, 'teamH': Team Information Obj: {teamH, goals: 0, wins: 0, draws: 0, losts: 0}, 'teamI': Team Information Obj: {teamI, goals: 0, wins: 0, draws: 0, losts: 0}, 'teamJ': Team Information Obj: {teamJ, goals: 0, wins: 0, draws: 0, losts: 0}, 'teamK': Team Information Obj: {teamK, goals: 0, wins: 0, draws: 0, losts: 0}, 'teamL': Team Information Obj: {teamL, goals: 0, wins: 0, draws: 0, losts: 0}}}"
    assert str(all_teams_dict) == correct_result

def test_enter_result():
    all_teams_dict = dict()
    group1_dict = dict()
    group2_dict = dict()
    group1_dict["teamA"] = team_information_entity(team_entity("teamA", "01/04", "1"))
    group1_dict["teamB"] = team_information_entity(team_entity("teamB", "02/05", "1"))
    group1_dict["teamC"] = team_information_entity(team_entity("teamC", "03/06", "1"))
    group1_dict["teamD"] = team_information_entity(team_entity("teamD", "04/06", "1"))
    group1_dict["teamE"] = team_information_entity(team_entity("teamE", "05/06", "1"))
    group1_dict["teamF"] = team_information_entity(team_entity("teamF", "05/06", "1"))
    group2_dict["teamG"] = team_information_entity(team_entity("teamG", "14/06", "2"))
    group2_dict["teamH"] = team_information_entity(team_entity("teamH", "13/06", "2"))
    group2_dict["teamI"] = team_information_entity(team_entity("teamI", "12/06", "2"))
    group2_dict["teamJ"] = team_information_entity(team_entity("teamJ", "11/06", "2"))
    group2_dict["teamK"] = team_information_entity(team_entity("teamK", "10/06", "2"))
    group2_dict["teamL"] = team_information_entity(team_entity("teamL", "27/06", "2"))
    all_teams_dict = {"1": group1_dict, "2": group2_dict}
    
    match_result = "teamA teamB 0 1\nteamA teamC 1 3\nteamA teamD 2 2\nteamA teamE 2 4\nteamA teamF 3 3\nteamB teamC 0 1\nteamB teamD 2 2\nteamB teamE 4 0\nteamB teamF 0 0\nteamC teamD 2 0\nteamC teamE 0 0\nteamC teamF 1 0\nteamD teamE 0 3\nteamD teamF 2 1\nteamE teamF 3 4\nteamG teamH 3 2\nteamG teamI 0 4\nteamG teamJ 1 0\nteamG teamK 1 4\nteamG teamL 1 4\nteamH teamI 2 0\nteamH teamJ 3 0\nteamH teamK 3 4\nteamH teamL 0 1\nteamI teamJ 2 1\nteamI teamK 3 0\nteamI teamL 1 3\nteamJ teamK 1 4\nteamJ teamL 0 3\nteamK teamL 0 0"

    test_obj = main_services()  
    all_teams_dict = test_obj.enter_result(all_teams_dict, match_result)

    correct_result = "{'1': {'teamA': Team Information Obj: {teamA, goals: 8, wins: 0, draws: 2, losts: 3}, 'teamB': Team Information Obj: {teamB, goals: 7, wins: 2, draws: 2, losts: 1}, 'teamC': Team Information Obj: {teamC, goals: 7, wins: 4, draws: 1, losts: 0}, 'teamD': Team Information Obj: {teamD, goals: 6, wins: 1, draws: 2, losts: 2}, 'teamE': Team Information Obj: {teamE, goals: 10, wins: 2, draws: 1, losts: 2}, 'teamF': Team Information Obj: {teamF, goals: 8, wins: 1, draws: 2, losts: 2}}, '2': {'teamG': Team Information Obj: {teamG, goals: 6, wins: 2, draws: 0, losts: 3}, 'teamH': Team Information Obj: {teamH, goals: 10, wins: 2, draws: 0, losts: 3}, 'teamI': Team Information Obj: {teamI, goals: 10, wins: 3, draws: 0, losts: 2}, 'teamJ': Team Information Obj: {teamJ, goals: 2, wins: 0, draws: 0, losts: 5}, 'teamK': Team Information Obj: {teamK, goals: 12, wins: 3, draws: 1, losts: 1}, 'teamL': Team Information Obj: {teamL, goals: 11, wins: 4, draws: 1, losts: 0}}}"
    assert str(all_teams_dict) == correct_result

def test_tabulate_points():
    all_teams_dict = dict()
    group1_dict = dict()
    group2_dict = dict()
    group1_dict["teamA"] = team_information_entity(team_entity("teamA", "01/04", "1"))
    group1_dict["teamB"] = team_information_entity(team_entity("teamB", "02/05", "1"))
    group1_dict["teamC"] = team_information_entity(team_entity("teamC", "03/06", "1"))
    group1_dict["teamD"] = team_information_entity(team_entity("teamD", "04/06", "1"))
    group1_dict["teamE"] = team_information_entity(team_entity("teamE", "05/06", "1"))
    group1_dict["teamF"] = team_information_entity(team_entity("teamF", "05/06", "1"))
    group2_dict["teamG"] = team_information_entity(team_entity("teamG", "14/06", "2"))
    group2_dict["teamH"] = team_information_entity(team_entity("teamH", "13/06", "2"))
    group2_dict["teamI"] = team_information_entity(team_entity("teamI", "12/06", "2"))
    group2_dict["teamJ"] = team_information_entity(team_entity("teamJ", "11/06", "2"))
    group2_dict["teamK"] = team_information_entity(team_entity("teamK", "10/06", "2"))
    group2_dict["teamL"] = team_information_entity(team_entity("teamL", "27/06", "2"))

    all_teams_dict = {"1": group1_dict, "2": group2_dict}
    
    match_result = "teamA teamB 0 1\nteamA teamC 1 3\nteamA teamD 2 2\nteamA teamE 2 4\nteamA teamF 3 3\nteamB teamC 0 1\nteamB teamD 2 2\nteamB teamE 4 0\nteamB teamF 0 0\nteamC teamD 2 0\nteamC teamE 0 0\nteamC teamF 1 0\nteamD teamE 0 3\nteamD teamF 2 1\nteamE teamF 3 4\nteamG teamH 3 2\nteamG teamI 0 4\nteamG teamJ 1 0\nteamG teamK 1 4\nteamG teamL 1 4\nteamH teamI 2 0\nteamH teamJ 3 0\nteamH teamK 3 4\nteamH teamL 0 1\nteamI teamJ 2 1\nteamI teamK 3 0\nteamI teamL 1 3\nteamJ teamK 1 4\nteamJ teamL 0 3\nteamK teamL 0 0"

    test_obj = main_services()  
    all_teams_dict = test_obj.enter_result(all_teams_dict, match_result)
    points_by_group = test_obj.tabulate_points(all_teams_dict)
    correct_result = "{'1': {2: ['teamA'], 8: ['teamB'], 13: ['teamC'], 5: ['teamD', 'teamF'], 7: ['teamE']}, '2': {6: ['teamG', 'teamH'], 9: ['teamI'], 0: ['teamJ'], 10: ['teamK'], 13: ['teamL']}}"
    
    assert str(points_by_group) == correct_result
