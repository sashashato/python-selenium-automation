# Created by sasha at 6/19/25
Feature: Verify color selection on Target product page

  Scenario: User can select each color and see it activated
    Given Open the Target product page "https://www.target.com/p/women-s-low-rise-cargo-camp-denim-shorts-wild-fable/-/A-93592886?preselect=93028563#lnk=sametab"
    Then Verify user can click through colors