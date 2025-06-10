# Created by sasha at 6/10/25
Feature: Verify Sign In for logged out users

  Scenario: Logged out user can navigate to Sign In
    Given I open target.com
    When I click on Account
    And I click on Sign in or create account from side navigation
    Then I should see the "Enter your email or mobile number to continue" message