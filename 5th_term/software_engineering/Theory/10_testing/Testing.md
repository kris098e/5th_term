# Stubs and mocks
## Stubs
Stubs will always return the same value when called with certain parameters.
A stub may look look like
```kotlin
interface Car {
	fun turnOn(times: Int): Boolean
}

val carStub = mockk<Car>()
@Test
fun `turn on`() {
	every { carStub.turnOn(2) } returns false
}
```
## Mocks
Mocks may use stubs to finish out the operation, but wont always return the same. 
```kotlin
class Service(car: Car) {
	fun helloCar(): String {
		if (time.now.minutes == 2) return Car.turnOn(2).toString()
		else return "not 2!"
	}
}
val carStub = mockk<Car>()
val Service = Service(carStub)

@Test
fun `test Service`() {
	every { carStub.turnOn(2) } returns false
	assert(exactly = 1) { carStub.turnOn(2) }
}
```
This example the mock may behave differently, but the stub can only return the same value.
# Levels of testing
**Look at the slides for image of the types of tests**
## Acceptance Testing

Acceptance testing is the final and one of the most important levels of testing. Upon successful completion, the application is released to production. The primary aim of acceptance testing is to ensure that the product meets the specified business requirements within the defined standard of quality [artoftesting.com](https://artoftesting.com/levels-of-software-testing).

There are two kinds of acceptance testing: alpha testing and beta testing. Alpha testing is carried out by testers or some other internal employees of the organization at the developer’s site. User acceptance testing done by end-users at the end-user’s site is called beta testing [artoftesting.com](https://artoftesting.com/levels-of-software-testing).
## Stress Tests
Stress testing is not explicitly mentioned in the provided sources. However, generally, stress testing is a type of performance testing that is used to determine the behavior of a system under extreme workload. The main purpose of stress testing is to check the system's stability and reliability under high load.
## End-to-End Tests
End-to-end testing validates an application's workflow from start to finish from the user's perspective, ensuring all integrated components and dependencies function as intended. This testing aims to identify defects during the interaction of different application parts, ensuring overall functionality, reliability, and performance [lambdatest.com](https://www.lambdatest.com/learning-hub/end-to-end-testing).

End-to-end testing is usually done infrequently and is the last stage of testing. It is time-consuming, requires more infrastructure than unit testing and integration testing, and it is relatively difficult to pinpoint exact breakage with this methodology [lambdatest.com](https://www.lambdatest.com/learning-hub/end-to-end-testing).
## Integration Tests
Integration testing is the second level of testing in which we test a group of related modules. It aims at finding interfacing issues between the modules i.e. if the individual units can be integrated into a sub-system correctly [artoftesting.com](https://artoftesting.com/levels-of-software-testing).

Integration testing is of four types – Big-bang, top-down, bottom-up, and Hybrid. In big bang integration, all the modules are first required to be completed and then integrated. After integration, testing is carried out on the integrated unit as a whole [artoftesting.com](https://artoftesting.com/levels-of-software-testing).
## Unit Tests
Unit testing is the first level of software testing where individual components of a software are tested. The purpose is to validate that each unit of the software performs as designed. A unit is the smallest testable part of any software [cultivate.software](https://cultivate.software/unit-vs-integration-vs-acceptance-test/).

Unit tests are designed to test individual components in isolation. They are typically written and run by developers to ensure that code meets its design and behaves as expected [cultivate.software](https://cultivate.software/unit-vs-integration-vs-acceptance-test/).


# Equivalence Partitions
# Unit tests examples
## Example 1
Carsten means
- test on each side of the less than sign
	- 29, 30, 15, 42, max int, negative numbers, floats, strings
Depends on the specific language you use. Whether it is strictly typed
## Example 2
...
- input
	- just test each branch of the code
	- edge cases
- output
	- the given possible output, "member", "owner", "new"
## Example 3
- test edge cases
- 

# Code coverage
slides
- should not obsess about it
	- may end up making more tests than what is needed to increase test coverage
## Quotes from Carsten
![[Pasted image 20231113164614.png]]


# Property Based Testing
- have some software which generates data. Fx can have some library which generates random strings for a function.
- Often combined with randomness
# Test Driven Development (TDD)
- Write the tests beforehand
	- The test should fail before we have implemented the methods
- Make sure to run the test before we implement the function
	- Assert that it fails
- At first, only implement the necessary part of the program to make the test pass.
- Add other functionality
	- Write the test first
		- Assert it fails
	- implement further
- This will also help you not over-engineer code, since you write out what is the basic.
## When done
- Refactor the code
- Test the code again
# Triple A
- Arrange / Given
- Act / When
- Assert / Then
