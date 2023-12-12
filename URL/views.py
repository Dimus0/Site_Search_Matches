from flask import render_template, request, jsonify, redirect, url_for
from db import Player,Team,Match

match_inform = [
    {"id": "5","home_team": "Шахтар", "away_team": "Динамо", "score": "2-1", "stadium": "Stadium X"},
    {"id": "12","home_team": "Барса", "away_team": "Аль-Насар", "score": "0-0", "stadium": "Stadium Y"}
]
team_inform = [
    {'team_name': "Шахтар"}
]
def homepage():
    return render_template('homepage.html')

def search_team_page():
    return render_template('search-team.html')
def admin_page():
    return render_template('admin_page.html')
def search_match_page():
    return render_template('searchsmatch.html')

def find_match(home_team, away_team):
    for match in match_inform:
        if match["home_team"] == home_team and match["away_team"] == away_team:
            return match
    return None

def find_match_by_id(match_id):
    for match in match_inform:
        if match["id"] == match_id:
            return match
    return None

def delete_matches():
    match_id = request.form['match_id']

    m_ID = find_match_by_id(match_id)

    if m_ID:
        match_inform.remove(m_ID)
        return render_template('admin_page.html', delete_message="Match deleted successfully")
    else:
        return render_template('admin_page.html', delete_message="Match not found"), 404

def get_info():
    match_id = request.form['id']

    m_ID = find_match_by_id(match_id)
    if m_ID:
        return render_template('infomatch.html', match=m_ID)
    else:
        return jsonify({"error": "Match not found"}), 404


def search_match():
    home_team = request.form['ht']
    away_team = request.form['at']

    if not home_team or not away_team:
        return jsonify({"error": "Both home_team and away_team are required"}), 400

    match = find_match(home_team, away_team)

    if match:
        return render_template('searchmatchresult.html', match=match, ht=home_team, at=away_team)
    else:
        return jsonify({"error": "Match not found"}), 404


def update_match_in_list(match_inform, match_id, new_match):
    for index, match in enumerate(match_inform):
        if match["id"] == match_id:
            match_inform[index] = new_match
            return True

    return False

def update_match():
    new_info = request.form.to_dict()
    match_id = new_info.get("id")

    # Validate required fields
    if not match_id:
        return jsonify({"error": "Missing required field: `id`"})

    if not all(field in new_info for field in ["home_team", "away_team", "score", "stadium"]):
        return jsonify({"error": "Missing required fields"})

    # Find the match by ID
    match = find_match_by_id(match_id)
    if not match:
        return jsonify({"error": "Match not found"})

    # Update the match information
    for key, value in new_info.items():
        if key in ["home_team", "away_team", "score", "stadium"]:
            match[key] = value

    # Update the match in match_inform
    update_match_in_list(match_inform, match_id, match)

    # Return success message
    return render_template('admin_page.html', success_message="Match update successfully")



def add_match():
    new_match_data = request.form.to_dict()
    required_fields = ["id", "home_team", "away_team", "score", "stadium"]
    if not all(field in new_match_data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400

    if find_match_by_id(new_match_data["id"]):
        return jsonify({"error": "Match with the same ID already exists"}), 400
    else:
        match_inform.append(new_match_data)

    added_match = find_match_by_id(new_match_data["id"])

    if added_match:
        return render_template('admin_page.html', success_message="Match added successfully")
    else:
        return jsonify({"error": "Match could not be added. Please try again."}), 500



