![[Pasted image 20230908102700.png]]

# Step 2, document the design
Documentation is key to software development
Keeps up the designers from having verbal agreements, preventing them for month after month saying they are 90% done
during the early phase of software development the documentation _is_ the specification and _is_ the design. 

Documentation is key during every phase

**during test phase** without good documentation every mistake no matter the size will have to be done by the guy implementing it, as no others can do it in a good enough time-span
**Following the operations phase** if the software has to be changed even slightly, it may need for writing the whole code again if no proper documentation is provided

# Step 3, attempt to do it twice
Do a simulation first, which should be done in fx $\frac{1}{4}$ of the times. This implementation has just be the bare minimum. If it went well, you can use the same processes again
![[Pasted image 20230908105135.png]]

# step 4, plan, control and monitor the test phase
All steps before has been leading up to minimizing the failures in the test phase, as if this fails we have to go back some steps which is very costly

1. without documentation, we cannot use specialist in tests as they cannot know what to test and the guys who build it has to be the ones testing.
2. visual detection of errors are most common
3. Test every logical path in code

# Step 5, involve the customer