# Cyclomatic Complexity
less that 10 complexity in a function
- each branch in the code is adding complexity
- +1 for the call to the function
- Does not have to be accurate, really opinion based - have to use the same measure everytime tho. Cannot change.

# CRAP - formula
[[Lecture 9_ Design Patterns 2.pdf#page=29]]
- penalities for not testing
- penalties for having high cyclomatic complexity
- if we have low test coverage and high complexity, then we will be penaltiest by a lot
# Code rot
 https://dibt.unimol.it/staff/fpalomba/documents/C4.pdf
- another name for technical debt
## Request Question 1
When are the code smell introduced.
what are defined as code smells
![[Pasted image 20231106173629.png]]
When refactoring, new features, enhancing?

- Looked at 2000 github repositories. Both looked at small and big ones. Looked at .5M commits.
- The last time before a major release creates more than 80% of the code smell
- when refactoring code we also get a lot of code smell, which is contraintuitive when you actually want to remove
- The ones owning the classes are the ones creating the most code smell for the code
	- the more experienced ones will introduce more code smell because they may be more happy with complex code
	- the new developers produce more spagghetti code, but introduce less spagghetti code
		- may fx be because their PRs would be more gone through
- code smell is also tied to work load
![[Pasted image 20231106175027.png]]
## Request Question 2
why are the code smell introduced
- merge code with code smell
	- can use tools to automate checks for code smells. Fx would not allow new code to be merged into the project before a certain threshold is met.
- 
