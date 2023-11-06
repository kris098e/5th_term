# Why architecture
- creating system that are robusts, easy to change, identifying the places where it is difficult to change certain logic. 
- creating well documented and easy understood software
# Value streams
4 value streams, i.e 4 teams,
- 3 on robots
- 1 off robots

uses scrum
uses PI's (product increments)
# PI's
- What we want to do in the next 4-5 sprints
- Done in your team
	- have team outbreaks where you can talk with other teams if you have dependencies
## UR digital planning
# Software architecture
The software architecture of a system **represents the design decisions related to overall system structure and behavior**. Architecture helps stakeholders understand and analyze how the system will achieve essential qualities such as modifiability, availability, and security.
## Different levels of abstraction
- System
- application
- infrastructure
### Conways Law
_Any organization that designs a system (defined broadly) will produce a design whose structure is a copy of the organization's communication structure_
- the organization will design an architecture which is a product of what was communicated
### Organized in product teams (this is in UR)
### main points
#### application architecture
- has to be simple, maintanable, testable
- focus on things difficult to change (API's, data models)
- often classic n-layer architecture - where n <= 3
#### infrastructure (cloud) architecture
- global company / global customer base
#### System architecture
- data flows
	- how our system talks together
		- should be documented
### Example
![[Pasted image 20231023163453.png]]
# How are new applications created
## Requirements
**PMS, tech leads, stakeholders** will talk together for some time, and come up with what should happen
## what technologies could be used to solve this
make or buy (depends on if it is cheaper, or more manageable)
## application architecture - team decision
- what fits?
	- which programming language, which framework ...
- what is the expectation for the system?
## Iterative process
deliver MVPs and then do increments when we learn from the feedback
# Main purpose of documentation
- onboarding
	- makes it easier to onboard and come into the company if it properly documented
- knowledge sharing
	- 
- capturing decisions
## Primary focus
- overall system and data flow documentation / diagrams
# Tooling
- No company wide tool for diagrams
	- many different tools are used
- Use shared software, for storing the documentation, which everyone can access, fx `confluence`

