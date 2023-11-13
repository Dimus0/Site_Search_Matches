from datetime import datetime

from flask import Flask, redirect, url_for,render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import declarative_base,sessionmaker
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Date, ForeignKey
from sqlalchemy.orm import sessionmaker,relationship,Mapped
import os

BASE_DIR=os.path.dirname(os.path.realpath(__file__))

connection_string="sqlite:///"+os.path.join(BASE_DIR,'dbtest.sqlite3')

Base=declarative_base()

engine=create_engine(connection_string,echo=True)

Session=sessionmaker()
class Player(Base):
    __tablename__ = 'player'
    id = Column(Integer(), primary_key=True)
    firstname = Column(String(50))
    lastname = Column(String(50))
    nationality = Column(String(50))
    position = Column(String(50))

    match_id = Column(Integer, ForeignKey('match.id'))
    match = relationship("Match", back_populates="players")
    def __repr__(self):
        return (f"<Player name={self.firstname} {self.lastname} nationality={self.nationality}"
                f"Position-{self.position}>")

class Team(Base):
    __tablename__ = 'team'
    id = Column(Integer(), primary_key=True)
    team_name = Column(String(50))
    country = Column(String(50))
    coach = Column(String(50))
    stadium = Column(String(50))
    def __repr__(self):
        return (f"<Team name={self.team_name} Country={self.country}"
                f"Coach={self.coach} Stadium={self.stadium}>")
class Match(Base):
    __tablename__ = 'match'
    id = Column(Integer(), primary_key=True)
    date = Column(DateTime())
    home_team = Column(String(50),ForeignKey('team.team_name'))
    away_team = Column(String(50),ForeignKey('team.team_name'))
    GoalScoreHomeTeam = Column(Integer())
    GoalScoreAwayTeam = Column(Integer())
    Referee = Column(String(50))
    players = relationship("Player", back_populates="match")
    def __repr__(self):
        return (f"<Match date='{self.date}' Teams: {self.home_team} VS {self.away_team}"
                f"Result: {self.GoalScoreHomeTeam}:{self.GoalScoreAwayTeam} Referee- {self.Referee}>")

# new_player = Player(id=2,firstname="Ronaldo",nationality="Portugalian")
# print(new_player)

