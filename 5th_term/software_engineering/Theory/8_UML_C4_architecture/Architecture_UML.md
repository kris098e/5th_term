# Noun analysis
see slides
# Architects / architecture
- structuring the layout of the infrastructure
	- In the code, packaging, layers (controller, services, repo, ...)
	- Diagrams
- may be lead developers
	- has much experience, knows what can go wrong more intuitively
## Architecture
- components
- interfaces
may be sketched out in diagrams, fx `UML`
### Code rot
**see slides**
architecture prevents code rot
- software taht is hard to maintain
- fragile components
	- unrelated changes will destroy certain functionality in some components / modules
	- have a lot of unused code
- cannot use functions for multiple things
#### Examples
**see slides**
### Coupling
(IMPORTANT)want low coupling
- if we have two boxes in an UML-diagram, which has many arrows to eachother, then we have high coupling.
	- we cannot change the one class, without changing much in the 2nd class aswel
		- code is hard to maintain
### Cohesion
(IMPORTANT)want high cohesion
- how well does code belong together
	- often inside classes
- **does the logic for the class only do logic for the class, and does it belong here**
### Stack overflow
https://stackoverflow.com/questions/3085285/difference-between-cohesion-and-coupling
**Cohesion** refers to what the class (or module) can do. Low cohesion would mean that the class does a great variety of actions - it is broad, unfocused on what it should do. High cohesion means that the class is focused on what it should be doing, i.e. only methods relating to the intention of the class.

Example of Low Cohesion:

```
-------------------
| Staff           |
-------------------
| checkEmail()    |
| sendEmail()     |
| emailValidate() |
| PrintLetter()   |
-------------------
```
Example of High Cohesion:
```
----------------------------
| Staff                   |
----------------------------
| -salary                 |
| -emailAddr              |
----------------------------
| setSalary(newSalary)    |
| getSalary()             |
| setEmailAddr(newEmail)  |
| getEmailAddr()          |
----------------------------
```
As for **coupling**, it refers to how related or dependent two classes/modules are toward each other. For low coupled classes, changing something major in one class should not affect the other. High coupling would make it difficult to change and maintain your code; since classes are closely knit together, making a change could require an entire system revamp.

Good software design has **high cohesion** and **low coupling**.
### Encapsulation
**see slides**
- expose specification
	- not implementation
	- private
# Layered architecture approach
**slides**
- reduce complexity
- different models
	- Model
		- of the system
	- View
	- Controller
![[Pasted image 20231102104228.png]]
If we have no distribution pattern, then the entire application will be a single file
## example on how to implement the layered approach
**slides**
- user interface
- business logic
- database mangement
![[Pasted image 20231102102451.png]]
### direct example
**slides**
### notes to example on common service
- dialog control
	- light handling of the interraction, if we dont have to interract with the backend
- business logic
	- the backend controllers
- database management
	- database access
If we have no distribution pattern, then the entire application will be a single file
