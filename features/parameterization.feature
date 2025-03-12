Feature: Parameterization Testing

    Scenario Outline: Fetch user details with different IDs
    Given the API endpoint is "/<user_id>"
    When I send a GET request
    Then the response status code should be <status_code>
    And the response should contain "<expected_name>"

    Examples:
      | user_id | status_code | expected_name   |
      | 1       | 200        | Leanne Graham  |
      | 2       | 200        | Ervin Howell   |

