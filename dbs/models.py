from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
import os

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

connection_string = "sqlite:///" + os.path.join(BASE_DIR, '../db.sqlite3')

Base = declarative_base()

engine = create_engine(connection_string, echo=True)

Session = sessionmaker(bind=engine)

class Team(Base):
    __tablename__ = 'team'
    id = Column(Integer(), primary_key=True)
    team_name = Column(String(50))
    country = Column(String(50))
    coach = Column(String(50))
    stadium = Column(String(50))
    # home_matches = relationship("Match", back_populates="home_team", foreign_keys="[Match.home_team_id]")
    # away_matches = relationship("Match", back_populates="away_team", foreign_keys="[Match.away_team_id]")

    def __repr__(self):
        return (f"<Team name={self.team_name} Country={self.country} "
                f"Coach={self.coach} Stadium={self.stadium}>")

class Match(Base):
    __tablename__ = 'match'
    id = Column(Integer(), primary_key=True)
    date = Column(DateTime())
    home_team_id = Column(String(50))
    away_team_id = Column(String(50))
    goal_score_home_team = Column(Integer())
    goal_score_away_team = Column(Integer())
    referee = Column(String(50))
    # ForeignKey('team.id')
    # home_team = relationship("Team", foreign_keys=[home_team_id], back_populates="home_matches")
    # away_team = relationship("Team", foreign_keys=[away_team_id], back_populates="away_matches")

    def __repr__(self):
        return (f"<Match date='{self.date}' Teams: {self.home_team.team_name} VS {self.away_team.team_name} "
                f"Result: {self.goal_score_home_team}:{self.goal_score_away_team} Referee- {self.referee}>")

# Base.metadata.create_all(engine)
