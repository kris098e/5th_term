* Title 
	* Unit testing in Kotlin and its coupling to the JVM
* Motivation & Goal
	* The motivation and goal of this analysis would be to understand and compare the different aspects of Java annotation processors, Kotlin multiplatform and native, and testing frameworks in the context of software development. This analysis aims to provide a comprehensive understanding of these concepts, their applications, and how they interact with each other.
	- The motivation behind this analysis comes from the need to understand how these tools and concepts can improve the efficiency and effectiveness of software development. Annotation processors can help to reduce boilerplate code and catch errors at compile time, which can lead to more robust and reliable software. Kotlin multiplatform and native, on the other hand, can help to share code across different platforms and compile code to binary executables, which can lead to more efficient and versatile software. Testing frameworks can help to ensure that the software is functioning as expected, which can lead to higher quality software and fewer bugs.
	- The goal of this analysis is to provide a detailed comparison of these tools and concepts, including their advantages, disadvantages, and specific use cases. This comparison will help to identify the best tools and concepts for different types of software development projects. It will also help to understand the limitations of these tools and concepts, and how to overcome these limitations.
	- In addition, this analysis aims to understand the challenges and issues that can arise when using these tools and concepts. For example, certain Kotlin-specific functionalities are not supported by KAPT, which can lead to difficulties when testing Kotlin code with most used frameworks that rely on the JVM. By understanding these challenges and issues, developers can make more informed decisions about when and how to use these tools and concepts.
	- In conclusion, the motivation and goal of this analysis is to provide a comprehensive understanding of Java annotation processors, Kotlin multiplatform and native, and testing frameworks in the context of software development. This understanding will help to improve the efficiency and effectiveness of software development, and to make more informed decisions about which tools and concepts to use.

* Plan of activities
	* Start with survey of the art and list references to signal that you know
	  where to start looking (references should be books, articles or online
	  material)
		- [why we should be unit-testing, good points about when using SCRUM/agile/XP. Expensive not to do it](https://en.wikipedia.org/wiki/Unit_testing)
		- [KSP source with useful links in README](https://github.com/google/ksp/tree/main)
			- [official explanations from kotlin lang](https://kotlinlang.org/docs/ksp-overview.html#supported-libraries)
		- [KotlinPoet](https://square.github.io/kotlinpoet/)
		- [MockK open source project](https://github.com/mockk/mockk)
			- Important to note that there are a lot of in depth articles explaining the ins and outs of the MockK framework.
			- contains article about how it works under the hood
		- [Mockito source](https://github.com/mockito/mockito)
			- [Mockito javadoc](https://javadoc.io/doc/org.mockito/mockito-core/latest/org/mockito/Mockito.html)
			- [how it works under the hood](https://medium.com/@gorali/how-mockito-works-7d3a2c77da71)
		- [Mockative source](https://github.com/mockative/mockative)
			- self explanitory that I will be doing much implementation therefore I will go in depth with the implementation. However as `KAPT` and `KSP and KotlinPoet` is also gonna be explained, which is what is used, the implementation specifics wont be as long.
		- [byte-buddy, how Mockito and MockK handles mocking](https://github.com/raphw/byte-buddy)
		- [type erasure used by Mockito](https://www.baeldung.com/java-type-erasure)
	* Development or research phase. Describe in general terms what you are going
	  to do and how.
		- research annotation processors in java and kotlin, providing different examples of why it is used and how powerful it is. How it is used in `KSP, KAPT`, and elsewhere to reduce boiler plate, provide easy made documentation, reduce errors at runtime ...
		- when to use kotlin multiplatform and when to use kotlin/native, the difference factors to take into consideration such as performance boosts and limitations.
		- I am going to research which `APIs` KSP and KotlinPoet provides, and how the `Mockative` framework is build around these tools. Then implement mocking of classes and spies into the framework, test them using the same testing framework inside the project.
		- I will research how `KAPT` is used with `Mockito and MockK` going into the specifics about how they are coupled to the JVM limiting the features it can use, compared to code which is kotlin native.
		- shortly visit good testing vs bad testing. For instance mocking too much, the use of `any`-matcher, testing single fields
		- research on test barriers (primarily ease of use), and why most developers hate testing.
	* Experiments. Describe to the the best you can what kind of experiments you
	  would like to run to answer your research question
		- Implementing the features of mocking classes and spies into the `Mockative`  framework, seeing that `KSP and KotlinPoet` will behave as expected, and the test cases are successfull
			- can mock a class in `Mockative`
			- can mock only certain functions using spies
		- I will implement some different tests, could fx be a function which calls another mocked function 100,000 times, and get numbers on the speed difference. Look into generics in the different frameworks, ease of use, advanced features `fakes, spies, error messages, interface mocking, coroutines, relaxed, ...`
	* Analysis + additional time to rerun experiments if needed
	* Finalizing the report/thesis following the academic conventions
* Tentative time plan (e.g., an item every 2 weeks/1 month)
	* Research of why we should unit test, barriers, bad testing, will take 1-2 weeks
	* Research of `java kotlin annotation processors` with examples will take 2 weeks.
	* Research of `KAPT, KSP, KotlinPoet` & understanding the `Mockative framework` will take 2 weeks.
		* sets up the next phase of implementation using the tools nicely
	* expect to have implemented mocking of classes during the first month, spies in the next 2 weeks. The testing phase will not be long for these features. Only need to show the generated source file, and see they are as expected for both of the implementations. 
		* the unit tests for these will not take long. For mocking of classes, just need to make a class which is not implementing some abstract class or interface, which has some methods we can verify certain behaviours on. Spies will be a matter of seeing that we can use existing implementation of a function, and mock another function.
	* Research of specifics regarding `Mockito, MockK` and their coupling with the JVM, use of `erasure, byte-buddy` will take 2 weeks
		* fx how they handles the mocking of objects, method invocations, fakes. See the list of (advanced)features
	* Comparing speeds of the different testing frameworks, ease of use, will take 1-2 weeks
* Risk evaluation
  * What are the risks involved in the project?
	  * not getting the features implemented
    What are possible remedies?
	- Explain what is going wrong, and what would fix it. Possibly a different approach
* Outcome. At the end of the project, the outcomes of the project will be
  * A report written in English and following the standard academic writing
    conventions containing ... (two line description of what the reprot should talk about)
	- Why unit testing is important, with examples of which frameworks are available to you in Kotlin and other JVM based languages. This will contain an explanation of the tools used to create the frameworks, with explanation of kotlin/native and kotlin multiplatform, and additionally what these tools imposes of limitations to the framework. With a comparison of the different features available to you, a speed comparison between the 3 test-frameworks and their ease of use. 
  * The code & data for the implementation of mocking of classes and spies in `Mockative`, the different examples of annotation processors in java and kotlin, the tests used for comparing the test-frameworks.
* Bibliography

---
The entry that can be cited for the standard acdemic writing convention
and a good book to have a loot at is 

@book{writing_conventions,
author = {Zobel, Justin},
title = {Writing for Computer Science},
year = {2015},
isbn = {1447166388},
publisher = {Springer Publishing Company, Incorporated},
edition = {3rd}
}
 
 
--------
 And remember :)
 
 "A good dissertation is a done dissertation. A great dissertation is a 
 published dissertation. A perfect dissertation is neither."
