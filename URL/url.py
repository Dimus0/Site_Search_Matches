from flask import Blueprint
from .views import (homepage, search_match, search_match_page,
                    admin_page,delete_matches,get_info,update_match,add_match)

my_blueprint = Blueprint('my_blueprint', __name__)

my_blueprint.add_url_rule('/', view_func=homepage, methods=['GET'])
# my_blueprint.add_url_rule('/api/v1/hello-world-<name>', view_func=function_hello_world_name, methods=['GET'])
my_blueprint.add_url_rule('/search_match', view_func=search_match_page, methods=['get'])

my_blueprint.add_url_rule('/api/search-matchers', view_func=search_match, methods=['POST'])


# my_blueprint.add_url_rule('/search-team', view_func=search_team_page, methods=['get'])
# my_blueprint.add_url_rule('/api/search-team-result', view_func=search_team, methods=['post'])

my_blueprint.add_url_rule('/admin', view_func=admin_page, methods=['get'])
# my_blueprint.add_url_rule('/admin/add_matches', view_func=add_matches, methods=['post'])
my_blueprint.add_url_rule('/update_match_info',  view_func=update_match, methods=['POST'])
my_blueprint.add_url_rule('/admin/delete_matches', view_func=delete_matches, methods=['post'])
my_blueprint.add_url_rule('/info', view_func=get_info, methods=['post'])

my_blueprint.add_url_rule('/add_match', view_func=add_match, methods=['POST'])
