from flask import Blueprint
from URL.views import (homepage, search_match, search_match_page,
                       admin_page, delete_matches,get_info, update_match, add_match)

my_blueprint = Blueprint('my_blueprint', __name__)

my_blueprint.add_url_rule('/', view_func=homepage, methods=['GET'])
my_blueprint.add_url_rule('/search_match', view_func=search_match_page, methods=['get'])
my_blueprint.add_url_rule('/admin', view_func=admin_page, methods=['get'])


my_blueprint.add_url_rule('/api/search-matchers', view_func=search_match, methods=['POST'])
my_blueprint.add_url_rule('/update_match_info',  view_func=update_match, methods=['POST','ADD'])
my_blueprint.add_url_rule('/admin/delete_matches', view_func=delete_matches, methods=['POST','DELETE'])
my_blueprint.add_url_rule('/info', view_func=get_info, methods=['post'])

my_blueprint.add_url_rule('/add_match', view_func=add_match, methods=['POST','PUT'])
