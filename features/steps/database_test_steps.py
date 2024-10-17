# features/steps/db_steps.py
from behave import given, when, then
from db_config import get_db_connection
from sqlalchemy import text

@given('the database is connected')
def step_impl(context):
    context.connection = get_db_connection()

@when('I fetch all users from the "{table_name}" table')
def step_impl(context, table_name):
    query = text(f"SELECT name, email FROM {table_name}")
    result = context.connection.execute(query)
    context.users = result.fetchall()

@then('I should see following users')
def step_impl(context):
    expected_users = [tuple(row.cells) for row in context.table]
    actual_users = [(row[0], row[1]) for row in context.users]
    assert expected_users == actual_users, f"Expected {expected_users}, but got {actual_users}"



