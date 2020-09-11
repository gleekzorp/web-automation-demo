Feature: Add two numbers and return the sum

  Scenario: Adding two even numbers returns an even number
    Given x=2
    And y=2
    When I add them together
    Then the sum should be 4
    And be even


  Scenario: Adding two negative numbers returns a negative number
    Given x=-2
    And y=-2
    When  I add them together
    Then  The sum should be -4
    And a negative number


  Scenario: Adding a number and a string it returns a number
    Given x='1'
    And y=1
    When I add them together
    Then The sum should be 2
    And be a number


  Scenario: Adding a number and a string in Javascript returns a string
    Given x='1'
    And y=1
    When I add them together
    Then The sum should be '11'
    And be a string