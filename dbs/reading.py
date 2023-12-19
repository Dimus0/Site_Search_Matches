from models import Match,Session,engine

local_session = Session(bind=engine)
match_id =12
matches=local_session.query(Match).filter(Match.id == 12).first()
print(matches)