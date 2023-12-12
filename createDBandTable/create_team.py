from db import Team,Session,engine

teams=[
    {
        "team_name": "Arsenal",
        "country":"England",
        "coach":"Mikel Arteta",
        "stadium":"Emirates"
    },
    {
        "team_name": "Chelsea",
        "country":"England",
        "coach":"Mauricio Pochettino",
        "stadium":"Stamford Bridge"
    },
    {
        "team_name": "PSG",
        "country":"France",
        "coach":"Luis Enrique",
        "stadium":"Park de Prince"
    },
]

local_session = Session(bind=engine)

# new_player=Player(firstname="Messi",nationality="Argentina")
#
# local_session.add(new_player)
# local_session.commit()

for u in teams:
    new_teams=Team(team_name=u["team_name"],country=u["country"],coach=u["coach"],stadium=u["stadium"])
    print(new_teams)

    local_session.add(new_teams)

    local_session.commit()

    print(f"Added {u['team_name']}")
