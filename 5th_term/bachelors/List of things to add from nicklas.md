- Spies
https://stackoverflow.com/questions/12827580/mocking-vs-spying-in-mocking-frameworks
Instead of mocking the entire class, i.e have fake methods for all of the class. We can decide to use a `spy` where we can _stub_ only certain methods.
- Mocking of classes
Right now in the framework only `interfaces` are allowed to be mocked. it may provide more flexibility of how your code looks if you can also mock classes. Even tho it may not be as `clean` as only being able to mock interfaces.
- Fake data generation
?
- Improved type safety
Improving type safety in your unit tests can help catch errors at compile time rather than runtime.