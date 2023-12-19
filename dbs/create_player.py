from dbs.models import Session,engine

players=[
    {
        "firstname":"Oleksandr ",
        "lastname":"Zinchenko",
        "nationality":"Ukrainian",
        "position":"Defender",
    },
    {
        "firstname":"Oleksandr ",
        "lastname":"Mudryk",
        "nationality":"Ukrainian",
        "position":'Midfielder'
    },
    {
        "firstname":"Kylian ",
        "lastname":"Mbappe",
        "nationality":"France",
        "position":'Attacker'
    },
]

local_session = Session(bind=engine)

# new_player=Player(firstname="Messi",nationality="Argentina")
#
# local_session.add(new_player)
# local_session.commit()

for u in players:
    new_player=Player(firstname=u["firstname"],lastname=u["lastname"],nationality=u["nationality"],
                      position=u["position"])
    print(new_player)

    local_session.add(new_player)

    local_session.commit()

    print(f"Added {u['firstname']}")