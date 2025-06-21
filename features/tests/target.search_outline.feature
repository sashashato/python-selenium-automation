# Created by sasha at 6/12/25
Feature: Target product search


  Scenario Outline: Search for product and verify results
    Given I open target.com
    When I search for "<product>"
    Then I should see results related "<product>"

    Examples:
      |product      |
      |transformer  |
      |salt         |
      |clay         |