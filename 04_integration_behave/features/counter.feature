Feature: Hit Counter

  As a user
  I want a hit counter
  So that I can keep track of how many times I clicked

  Scenario: The counter goes up when the button is clicked
    Given the counter is reset
    When a user clicks the "Hit" button
    Then the counter should be at 1
    When a user clicks the "Hit" button
    Then the counter should be at 2

  Scenario: The counter resets to zero when the reset button is clicked
    Given the counter is reset
    When a user clicks the "Hit" button
    When a user clicks the "Hit" button
    When a user clicks the "Reset" button
    Then the counter should be at 0