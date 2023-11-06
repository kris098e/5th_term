# Chatten / SOLID
The SOLID principles are a set of five principles that were introduced by Robert C. Martin (also known as Uncle Bob) to make software designs more understandable, flexible, and maintainable. SOLID is an acronym that stands for:

Single-Responsibility Principle (SRP): A class should have only one reason to change, meaning that a class should have only one job. This principle makes the system easier to manage, understand, and modify digitalocean.com, baeldung.com.
class Square
```php
{
   public $length;
   public function construct($length)
   {
       $this->length = $length;
   }
}
```
Open-Closed Principle (OCP): Software entities (classes, modules, functions, etc.) should be open for extension but closed for modification. This means that you should be able to add new functionality or behaviors without changing existing code.
Liskov Substitution Principle (LSP): Subtypes must be substitutable for their base types. This principle ensures that a derived class can always be used in place of its base class without affecting the correctness of the program digitalocean.com, freecodecamp.org.
class VolumeCalculator extends AreaCalculator
```php
{
   public function construct($shapes = [])
   {
       parent::construct($shapes);
   }
   public function sum()
   {
       // logic to calculate the volumes and then return an array of output
       return [$summedData];
   }
}
```
Interface Segregation Principle (ISP): Clients should not be forced to depend on interfaces they do not use. This principle promotes the use of multiple, smaller, more specific interfaces over a single, large, general interface.
Dependency Inversion Principle (DIP): High-level modules should not depend on low-level modules. Both should depend on abstractions. Additionally, abstractions should not depend on details; details should depend on abstractions. This principle makes the system more flexible and easier to refactor digitalocean.com.
class MySQLConnection implements DBConnectionInterface
```java
{
   public function connect()
   {
       // handle the database connection
       return 'Database connection';
   }
}
```
class PasswordReminder
```php

{
   private $dbConnection;
   public function __construct(DBConnectionInterface $dbConnection)
   {
       $this->dbConnection = $dbConnection;
   }
}
```
Adhering to the SOLID principles can lead to software that is easier to maintain, understand, and extend. However, it's important to note that these principles are guidelines, not hard rules. They should be applied judiciously and in context, keeping in mind the specific needs and constraints of your project

# (S)single responsibility principle (SRP)
**see slides**
- but dont overdo it.
	- Dont make a class for each method, and break down methods into classes that will become too small
- However it does become more easy to test
	- can mock what each of the class methods return, if they are tested elsewhere
# (O)Open close principle
- code should be open for extension, but closed for modification
- what do we put as `public, protected, private, open, abstract, interface`
	- could also think about injection, of which behaviour to use. `@singleton, @bean`
		- fx for `validators, loggers, web, ...`
## Chatten
The Open-Closed Principle (OCP) is a key concept in object-oriented programming and is one of the five principles that make up the SOLID design principles. The OCP states that "software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification" stackify.com, en.wikipedia.org.

In other words, you should be able to add new functionality or behaviors to a software entity without changing its existing code. This principle helps to make your code more maintainable, scalable, and less prone to bugs, as changes to the existing code can introduce new bugs or break existing functionality stackify.com, freecodecamp.org.

The OCP can be achieved by using abstract classes or interfaces. When you define a class or an interface, you specify a contract that the class or any class implementing the interface must adhere to. This allows you to add new functionality by creating new classes or implementations that adhere to the same contract, without modifying the existing classes or interfaces stackify.com, baeldung.com.

Here's a simple example in Java:

``` java
public interface Shape {
   double area();
}

public class Circle implements Shape {
   private double radius;

   public Circle(double radius) {
       this.radius = radius;
   }

   @Override
   public double area() {
       return Math.PI * Math.pow(radius, 2);
   }
}

public class Rectangle implements Shape {
   private double length;
   private double width;

   public Rectangle(double length, double width) {
       this.length = length;
       this.width = width;
   }

   @Override
   public double area() {
       return length * width;
   }
}
```
In this example, the Shape interface is open for extension (you can create new classes like Circle and Rectangle that implement the Shape interface) but closed for modification (you don't need to change the Shape interface to add new shapes). This is a simple example, but the principle can be applied to more complex systems geeksforgeeks.org.

Remember, the Open-Closed Principle is a guideline, not a strict rule. It's important to consider the specific needs and constraints of your project when deciding how to structure your code freecodecamp.org.

# (L)Liskov Substitution Principle
- extending classes and providing different implementation, should still deliver the correct result
	- fx the parent gives the shortes route in the graph
		- the children should then also return the shortest route. Not fx a longer graph
![[Pasted image 20231102095223.png]]
# (I)Interface Segregation Principle
- Only depend on the method you use
	- should not have to implement other functionality that you do not have to use
- should not have interface where you are required to implement functions you do not use, for the specific implementer.
	- should segregate them
![[Pasted image 20231102095952.png]]
# (D)Dependency Inversion Principle
**see slides**
- dependency injection
	- depend on interfaces, not on implementations
## chatten
The Dependency Inversion Principle (DIP) is a key concept in object-oriented programming and is part of the SOLID principles. The DIP states that high-level modules should not depend on low-level modules, and both should depend on abstractions. Additionally, abstractions should not depend on details, but details should depend on abstractions stackify.com, baeldung.com.

In other words, the DIP encourages the use of interfaces or abstract classes to decouple high-level and low-level modules. This makes your code more flexible and easier to modify, as changes to the low-level modules won't affect the high-level modules and vice versa stackify.com, baeldung.com.

Here's a simple example in Java:

``` java
public interface Light {
   void turnOn();
   void turnOff();
}

public class BedroomLight implements Light {
   public void turnOn() {
       System.out.println("Bedroom light turned on");
   }

   public void turnOff() {
       System.out.println("Bedroom light turned off");
   }
}

public class Bedroom {
   private Light light;

   public Bedroom(Light light) {
       this.light = light;
   }

   public void turnOnLight() {
       light.turnOn();
   }

   public void turnOffLight() {
       light.turnOff();
   }
}
```
In this example, the Bedroom class (a high-level module) depends on the Light interface (an abstraction), not on the BedroomLight class (a low-level module). This means you can change the type of light used in the bedroom without modifying the Bedroom class, as long as the new light class implements the Light interface baeldung.com.

Remember, the Dependency Inversion Principle is a guideline, not a strict rule. It's important to consider the specific needs and constraints of your project when deciding how to structure your code stackify.com.

