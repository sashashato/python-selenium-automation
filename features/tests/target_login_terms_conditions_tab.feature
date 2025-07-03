# Created by sasha at 6/28/25
Feature: Test for Target login page

  Scenario: User can open and close Terms and Conditions from login page
    Given Open login page
    When Store original window
    And Click on Target terms and conditions link
    And Switch to the newly opened window
    Then Verify Terms and Conditions page is opened
    And User can close new window and switch back to original
