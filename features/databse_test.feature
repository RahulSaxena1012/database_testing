Feature: Test database interactions

  Scenario: Fetch users from the database
    Given the database is connected
    When I fetch all users from the "users" table
    Then I should see following users
        | username | email          |
        | John Doe      | john@example.com |
        | Jane Doe      | jane@example.com |
