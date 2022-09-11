from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from backend.services.main_services import main_services, dict_with_obj_to_json, json_to_dict_with_obj 

app = Flask(__name__ ,static_folder='../../frontend/build',static_url_path='')
CORS(app)

@app.route('/health_check')
def health_check():
    return '200'

@app.route('/start_game', methods=['POST'])
@cross_origin()
def start_game():
    
    team_information_output = dict()
    main_services_obj = main_services()
    data = request.get_json()
    team_information = data["team_information"]

    all_teams_dict = main_services_obj.start_game(team_information)

    team_information_output = dict_with_obj_to_json(all_teams_dict)

    return jsonify(
            {
                "code": 200,
                "data": {
                    "team_information": team_information_output
                }
            }
        )

@app.route('/enter_result', methods=['POST'])
def enter_result():
    main_services_obj = main_services()
    points_by_group = dict()
    ranking_by_group = dict()

    data = request.get_json()
    match_results = data["match_results"]
    all_teams_dict = data["team_information"]

    all_teams_dict = json_to_dict_with_obj(all_teams_dict)

    all_teams_dict = main_services_obj.enter_result(all_teams_dict, match_results)
    points_by_group = main_services_obj.tabulate_points(all_teams_dict)
    ranking_by_group = main_services_obj.get_rankings(all_teams_dict, points_by_group)

    return jsonify(
        {
            "code": 200,
            "data": {
                "ranking_by_group": ranking_by_group
            }
        }
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

