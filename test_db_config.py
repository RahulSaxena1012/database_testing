# test_db_config.py
import pytest
from unittest.mock import patch, MagicMock
from db_config import get_db_connection

# Mock the create_engine method in SQLAlchemy
@patch('db_config.create_engine')
def test_get_db_connection(mock_create_engine):
    # Arrange: Set up the mock connection object
    mock_engine = MagicMock()
    mock_connection = MagicMock()
    mock_engine.connect.return_value = mock_connection
    mock_create_engine.return_value = mock_engine

    # Act: Call the function to get the DB connection
    connection = get_db_connection()

    # Assert: Ensure the engine and connection were created and returned correctly
    mock_create_engine.assert_called_once_with('mysql+pymysql://root:mysecretpassword@localhost:3306/testdb')
    mock_engine.connect.assert_called_once()
    assert connection == mock_connection
