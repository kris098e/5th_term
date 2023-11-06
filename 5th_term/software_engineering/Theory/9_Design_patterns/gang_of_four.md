- Design patterns in code
**Have to be able to know all of the design categories. And now 1 in each.**
- Can see the different examples
https://www.blackwasp.co.uk/gofpatterns.aspx
# Singleton
hard to test as we have global state
**considered an antipattern today**
# Facade
# Proxy
a layer on top of existing implementation. Fx can have a proxy on top of person, which will cache some of the subject.
Can also have some security on top, when the user touches something, it goes through the proxy
# Creational prototype
It is creating a cloned instantiation of another instance, it can either do this shallowly or deeply. 
## Shallow
all of the variables are just copied, i.e referenced are also copied such that they point to the same object
## Deep
means that the original instance is copied and all of its references are also copied.
## Used when
Making a new instance is inefficient. If we fx want to use an object that is already setup, and we want a new object which only needs 2 out of 10 fields changed, then it may be using less code and also time
# Builder pattern
when you have to build the instance in a specific sequential way. Fx have to build the basement before we can put something inside.
## Cons
have a lot of boiler plate
# Observers
The class has to publish some event whenever something happens, which can be subscribed to.
## Cons
can lead to memory leaks in lower level languages
# Flyweight
reduce memory usage, when having a lot of similar objects. Only in very specific scenarios. Fx if we have 100 instances with the same 10 variables, but only 1 different, we can just store the 10 once in the same object, and then for the different variables they are stored
# Visitor
- The visitor pattern is used to separate a relatively complex set of structured data classes from the functionality that may be performed upon the data that they hold.
