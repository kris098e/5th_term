# Dynamic or static
## Class
The class view is `static`
## Instance of class
The instance is `dynamic`
## class diagram
Is a `static`, since it should not change
## Sequence diagram
can only see when it is started, so it is `dynamic`
## User stories
`dynamic`, they are not set and stone. But can also argue that it is `static`
# UML
https://medium.com/@smagid_allThings/uml-class-diagrams-tutorial-step-by-step-520fd83b300b
keep it simple with the arrows and lines, dont have to use them all

**slides**
Writing them up before may indicate a `simple state` in the cynefin-model. But in `complex` we may not have such a good idea
## Class diagram
Write em up before we start implementing or afterwards. 
- May be less error prone to implement them before 
- May be faster, and more dynamic to them after we are done
## Arrow heads matter
different arrow heads signals different things
- fx filled head means waiting for return
- non filled may mean we do it asynchronously
## Lines
- striped line is a lifeline, of how long the instance live.
- non-striped line means it is always alive
## keywords
- `alt` is like an `if`
	- alternative
