# Manual testing
- same work does not scale well to different settings
	- fx different platforms
		- iOS
		- Linux
		- windows
		- ...
- same tests have to be carried out multiple times 
	- better to automate
- use a platform that allows you to test on software where stuff works so you dont have to think about it. 
	- this platform should also have some integration testing for each fx phone, to test everything works
- have to test different acceptance criteria. Fx we have to center the image instead just show it on the side
	- here we would fx use image recognition
# Automated testing
need different frameworks
- cucumber
	- human-readable
	- Uses `given / when / then`
- selenium
- page objects
	- define some UI before tests
## Complexity increase
- May end up using AI, machine learning, and image recognition to get to the end-goal
# report bugs
give much information
- agree on which info to give
	- reproduction
	- severity
	- version
	- ...
## The feeling of the project
- can base the current version, how good it is, from the bugs discovered in the tests
	- This provides some baseline of the product and version
