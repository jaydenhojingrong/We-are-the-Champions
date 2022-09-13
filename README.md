# TAP 2023 GDS ACE Tech Assessment

Name: Ho Jing Rong (Jayden)
Linkedin: https://www.linkedin.com/in/jayden-ho/ 

## What is this?
First round football championship tracker where 12 teams, split into 2 groups of 6 where each team will play a match against every other team within the same group. Upon adding in team information and match results, the app will display the top 4 teams of each group will then qualify for the next round.

## How to access this?
https://we-are-the-champions.herokuapp.com/

## How do I run this via localhost?
You will have to comment some codes and run two things seperately:
* Frontend
* Backend

### Simple changes + Running Frontend (port 3000)
* Open \frontend\src\components\TeamInformation.js in a text editor
* Comment out line 12 & uncomment line 13
* Next, open \frontend\src\components\MatchInformation.js in a text editor
* Comment out line 13 & uncomment line 14
* Open the root folder in a terminal 
* `cd .\frontend\ `
* `npm install`
* `npm start`

### Running Backend (port 5000)
* Open the root folder in a terminal 
* `pip install requirements.txt`
* `cd .\backend\`
* `python -m backend.controllers.app`

#### Running simple unit test cases
* Open the root folder in a terminal 
* `python -m pytest`

## Demo and screenshots
[![Watch the video](https://img.youtube.com/vi/aEORRe-aXss/maxresdefault.jpg)](https://youtu.be/aEORRe-aXss)

## High level walk-through of tech architecture
### Backend
* Technologies used: 
    * Flask + Python 
    * pytest (https://docs.pytest.org/en/7.1.x/)
* Built using layered architecture (Entities, Services, Controllers) and OOP
    * Benefits:
        * Modularity, thus easier to scale in the future
        * Testability and ease of troubleshooting
        * Encourages code reuse
        * Tidy organization of dev files
### Frontend
* Technologies used: 
    * ReactJS + JavaScript
    * Material UI (https://mui.com/)
    
### Cloud Deployment
* Technologies used: 
    * Heroku (https://heroku.com/)
        * Has various built-in security features:
            * SSL
            * Firewalls
            * DDOS
            * Full details here: https://www.heroku.com/policy/security
        * Triggered by Git Push, making it convenient for deployment
        
## Assumptions
* Users should not input any empty lines for team information or match results
* Users should not go directly into rankings page or enter_results page via URL
    * They should follow the process of team_information page > enter_results > rankings page
* Duplicate team names within the same group will be overwritten
## High-level features
* Entering team information
* Entering match results
* Computing round results based on multi-tiered logic (different scoring system based on events)
* Displaying rankings and identifying teams that passed
* Validating user inputs
    * Team information
    * Match results
## What can be improved?
* Modularity of frontend
    * Reusing components by passing in props to show/process different data
* UI/UX design
    * May include success status update when team_information or match_result is keyed in correctly   
* Absence of database to allow persistent data across system reboots
    * Possibility of using NoSQL DB since the only data that needs to be stored (and is already available) is JSON format
* Simple redirecting to the index page when user lands directly on to the match_result page or rankings page 
# THANK YOU 
Hope you have enjoyed using this application :)
