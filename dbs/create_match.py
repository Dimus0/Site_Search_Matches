from datetime import datetime

from dbs.models import Match,Session,engine
specific_date = datetime(2023, 11, 13)
specific_date2 = datetime(2022, 11, 13)
specific_date3 = datetime(2021, 11, 13)
# matches=[
#     {
#         'id':123,
#         'date':specific_date,
#         'home_team':'Arsenal',
#         'away_team':'PSG',
#         'GoalScoreHomeTeam':3,
#         'GoalScoreAwayTeam':4,
#         'Referee':'Artem Matok'
#     },
#     {
#         'id':23,
#         'date':specific_date2,
#         'home_team':'Chelsea',
#         'away_team':'PSG',
#         'GoalScoreHomeTeam':1,
#         'GoalScoreAwayTeam':2,
#         'Referee':'Vadim Matok'
#     },
#     {
#         'id':3,
#         'date':specific_date3,
#         'home_team':'Arsenal',
#         'away_team':'Chelsea',
#         'GoalScoreHomeTeam':0,
#         'GoalScoreAwayTeam':0,
#         'Referee':'Vlad Ortovox'
#     },
# ]

local_session = Session(bind=engine)


new_matches = Match(id=12,date=specific_date2,home_team_id="Шахтар",away_team_id="Динама",
                    goal_score_home_team= 2,goal_score_away_team = 2,referee ="Руль")
local_session.add(new_matches)

local_session.commit()