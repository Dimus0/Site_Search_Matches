import unittest
from unittest.mock import patch, MagicMock,Mock
from datetime import date, datetime
from URL.views import add_match,delete_match,get_info,delete_matches,local_session  # replace 'your_module' with the actual module where add_match is defined
from flask import Flask, request, jsonify, render_template,g
from dbs.models import Match
from main import app

class TestAddMatchFunction(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
    @patch('URL.views.local_session')
    def test_delete_match_success(self, mock_local_session):
        mock_match = MagicMock()
        mock_local_session.query.return_value.filter.return_value.first.return_value = mock_match

        result = delete_match(match_id="123")
        mock_local_session.delete.assert_called_once_with(mock_match)
        mock_local_session.commit.assert_called_once()
        self.assertTrue(result)

    @patch('URL.views.local_session')
    def test_delete_match_not_found(self, mock_local_session):
        mock_local_session.query.return_value.filter.return_value.first.return_value = None

        result = delete_match(match_id="456")

        mock_local_session.delete.assert_not_called()
        mock_local_session.commit.assert_not_called()
        self.assertFalse(result)

    # def test_homepage(self):
    #     tester = app.test_client(self)
    #     responce = tester.get("/")
    #     statuscode = responce.status_code
    #     self.assertEqual(statuscode, 400)
    def test_search(self):
        tester = app.test_client(self)
        responce = tester.get("/search_match")
        statuscode = responce.status_code
        self.assertEqual(statuscode,200)

    def test_admin_page(self):
        tester = app.test_client(self)
        responce = tester.get("/admin")
        statuscode = responce.status_code
        self.assertEqual(statuscode,200)

    def test_search_match(self):
        tester = app.test_client(self)
        responce = tester.get("/api/search-matchers")
        statuscode = responce.status_code
        self.assertEqual(statuscode, 405)

if __name__ == '__main__':
    unittest.main()
