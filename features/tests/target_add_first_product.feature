# Created by sasha at 6/12/25
Feature: Add first product to cart

  Scenario: User adds first product from homepage to cart
    Given I open target.com
    When I add first product from homepage to cart
    And I confirm adding product in the side menu
    And I open the cart page
    Then I should see product in the cart