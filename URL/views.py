from datetime import date, datetime

from flask import render_template, request, jsonify
from dbs.models import Match,Session,engine

local_session = Session(bind=engine)

def homepage():
    return render_template('homepage.html'),200

def admin_page():
    return render_template('admin_page.html'),200

def search_match_page():
    return render_template('searchsmatch.html'),200

def delete_match(match_id):
    try:
        match = local_session.query(Match).filter(Match.id == match_id).first()
        if not match:
            raise Exception("Match not found")

        local_session.delete(match)
        local_session.commit()
        return True
    except Exception as e:
        print(e)
        local_session.rollback()
        return False

def delete_matches():
    match_id = request.form['match_id']
    success = delete_match(match_id)

    if success:
        return render_template('admin_page.html', delete_message="Match deleted successfully")
    else:
        return render_template('admin_page.html', delete_message="Match not found"), 404


def update_match():
    new_info = request.form.to_dict()
    match_id = new_info.get("id")

    # Validate required fields
    if not match_id or not all(field in new_info for field in ["home_team", "away_team", "hscore", "ascore"]):
        return jsonify({"error": "Missing required fields"})

    # Validate date format
    # Find the match by ID
    try:
        match = local_session.query(Match).filter(Match.id == match_id).first()
    except Exception as e:
        return jsonify({"error": "Error fetching match information"})

    if not match:
        return jsonify({"error": "Match not found"})

    # Update match information
    for key, value in new_info.items():
        if key in ["home_team", "away_team", "hscore", "ascore", "referee"]:
            setattr(match, key, value)

    # Commit changes to the database
    try:
        local_session.add(match)
        local_session.commit()
    except Exception as e:
        print(e)
        local_session.rollback()
        return jsonify({"error": "Error updating match information"})

    # Return success message
    return render_template('admin_page.html',
                           success_message="Match updated successfully. Updated fields: {}"
                           .format(", ".join(new_info.keys())))

def add_match():
    match_data = {
        "id": request.form.get("id"),
        "date": request.form.get("date"),
        "home_team": request.form.get("home_team"),
        "away_team": request.form.get("away_team"),
        "hscore": request.form.get("hscore"),
        "ascore": request.form.get("ascore"),
        "referee": request.form.get("referee"),
    }
    required_fields = ["id","date", "home_team", "away_team", "hscore","ascore", "referee"]
    if not all(field in match_data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400

    id = local_session.query(Match).filter(Match.id == match_data["id"]).first()
    if id:
        return jsonify({"error": "Match with the same ID already exists"}), 400

    try:
        current_date = datetime.today()
        new_match = Match(
            id=match_data["id"],
            date=current_date,
            home_team_id=match_data["home_team"],
            away_team_id=match_data["away_team"],
            goal_score_home_team=match_data["hscore"],
            goal_score_away_team=match_data["ascore"],
            referee=match_data["referee"]
        )
        local_session.add(new_match)
        local_session.commit()

        return render_template('admin_page.html', success_message="Match added successfully")
    except Exception as e:
        print(e)
        local_session.rollback()
        return jsonify({"error": "An error occurred while adding match(es). Please try again."}), 500


def search_match():
    home_team = request.form['ht']
    away_team = request.form['at']

    if not home_team or not away_team:
        return jsonify({"error": "Both home_team and away_team are required"}), 400

    match = local_session.query(Match).filter(
        (Match.home_team_id == home_team) &
        (Match.away_team_id == away_team)
    ).first()
    if match:
        return render_template('searchmatchresult.html', match=match, ht=home_team, at=away_team)
    else:
        return jsonify({"error": "Match not found"}), 404

def get_info():
    match_id = request.form['id']

    try:
        match = local_session.query(Match).filter(Match.id == match_id).first()
    except Exception as e:
        return jsonify({"error": {"message": "Error fetching match information", "status_code": 500}}), 500

    if match:
        return render_template('infomatch.html', match=match)
    else:
        return jsonify({"error": {"message": "Match not found", "status_code": 404}}), 404
