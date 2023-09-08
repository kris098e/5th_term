# general model
Sequential model

like a waterfall, the next phase cannot begin before the previous step has been complete.
As an analogy it is like waterfalls, you have to fill up a part before water starts flowing into the next

Specialists at each phase
Visibility hiding based on the time spent on the project.
Need to pass down the document to the next team before going further. This means that the approach is document driven
Quality control: software may end up being outdated as the previous phases can take too much time 
Rigorous planning: Yes, but if one phase does not meet the deadline, that will cause chaos on the next phase, I.e have to change plans

Good when having people with a lot of experience, when having the ability to do the work in small steps. Fx. building a house, first floors, then walls, then plumbing ...

Does not have an official definition, but is just a pair of guidelines

**Waterfall is particularly useful for large, complex projects** with very specific and unchanging requirements. Development teams will be less resistant to detailed product requirements documents and design specifications since that's what's expected.
![[Pasted image 20230903155037.png]]

# 6 phases
### 1. Feasibility Study
The main goal of this phase is to determine whether it would be financially and technically feasible to develop the software.   
The feasibility study involves understanding the problem and then determining the various possible strategies to solve the problem. These different identified solutions are analyzed based on their benefits and drawbacks, The best solution is chosen and all the other phases are carried out as per this solution strategy. 

### 2. Requirements Analysis and Specification

The aim of the requirement analysis and specification phase is to understand the exact requirements of the customer and document them properly. This phase consists of two different activities. 

- **Requirement gathering and analysis:** Firstly all the requirements regarding the software are gathered from the customer and then the gathered requirements are analyzed. The goal of the analysis part is to remove incompleteness (an incomplete requirement is one in which some parts of the actual requirements have been omitted) and inconsistencies (an inconsistent requirement is one in which some part of the requirement contradicts some other part).
- **Requirement specification:** These analyzed requirements are documented in a software requirement specification (SRS) document. SRS document serves as a contract between the development team and customers. Any future dispute between the customers and the developers can be settled by examining the SRS document.

#### Own notes
Many requirements may be given, but not all may be met. Use priority model, fx **moscow-model**

functional vs non-functional requirements. **non-functional** are harder to add, functional can be seen and more clearly be specified

**functional:** it should do what it is required to do
**non-functional:** fx that it has to be able to do it all the time, fx the server for the provided service actually have to be up >90% of the time

some requirement may be both functional and non-functional, as it may need implementation
### 3. System Design

The goal of this phase is to convert the requirements acquired in the SRS into a format that can be coded in a programming language. It includes high-level and detailed design as well as the overall software architecture. A [Software Design Document](https://www.geeksforgeeks.org/design-documentation-in-software-engineering/) is used to document all of this effort (SDD)

#### Own notes
Architecture design, does not implement it -> diagrams
### 4. Coding and Unit Testing

In the coding phase software design is translated into source code using any suitable programming language. Thus each designed module is coded. The aim of the unit testing phase is to check whether each module is working properly or not. 

### 5. Integration and System testing

Integration of different modules is undertaken soon after they have been coded and unit tested. Integration of various modules is carried out incrementally over a number of steps. During each integration step, previously planned modules are added to the partially integrated system and the resultant system is tested. Finally, after all the modules have been successfully integrated and tested, the full working system is obtained and system testing is carried out on this.   
System testing consists of three different kinds of testing activities as described below.

- **Alpha testing:** Alpha testing is the system testing performed by the development team.
- **Beta testing:** Beta testing is the system testing performed by a friendly set of customers.
- **Acceptance testing:** After the software has been delivered, the customer performed acceptance testing to determine whether to accept the delivered software or reject it.

### 6. deployment
put into production
### 7. Maintenance

Maintenance is the most important phase of a software life cycle. The effort spent on maintenance is 60% of the total effort spent to develop a full software. There are basically three types of maintenance.

- **Corrective Maintenance:** This type of maintenance is carried out to correct errors that were not discovered during the product development phase.
- **Perfective Maintenance:** This type of maintenance is carried out to enhance the functionalities of the system based on the customer’s request.
- **Adaptive Maintenance:** Adaptive maintenance is usually required for porting the software to work in a new environment such as working on a new computer platform or with a new operating system.