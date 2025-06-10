# Created by sasha at 6/7/25
Feature: Check cart status on target.com

  Scenario: User sees "Your cart is empty" message
    Given I open target.com
    When I click on cart icon
    Then I should see "Your cart is empty" message