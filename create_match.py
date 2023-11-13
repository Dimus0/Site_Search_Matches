from datetime import datetime

from db import Match,Session,engine
specific_date = datetime(2023, 11, 13)
specific_date2 = datetime(2022, 11, 13)
specific_date3 = datetime(2021, 11, 13)
matches=[
    {
        'date':specific_date,
        'home_team':'Arsenal',
        'away_team':'PSG',
        'GoalScoreHomeTeam':3,
        'GoalScoreAwayTeam':4,
        'Referee':'Artem Matok'
    },
    {
        'date':specific_date2,
        'home_team':'Chelsea',
        'away_team':'PSG',
        'GoalScoreHomeTeam':1,
        'GoalScoreAwayTeam':2,
        'Referee':'Vadim Matok'
    },
    {
        'date':specific_date3,
        'home_team':'Arsenal',
        'away_team':'Chelsea',
        'GoalScoreHomeTeam':0,
        'GoalScoreAwayTeam':0,
        'Referee':'Vlad Ortovox'
    },
]

local_session = Session(bind=engine)

for u in matches:
    new_matches=Match(date=u['date'],home_team=u['home_team'],away_team=u['away_team'],GoalScoreHomeTeam=u['GoalScoreHomeTeam'],
                      GoalScoreAwayTeam=u['GoalScoreAwayTeam'],Referee=u['Referee'])
    print(new_matches)

    local_session.add(new_matches)

    local_session.commit()

    print(f"Added {u['date']}")