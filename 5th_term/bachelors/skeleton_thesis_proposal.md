* Title 
	* Unit testing in Kotlin and its coupling to the JVM
* Motivation & Goal
	* The motivation and goal of this analysis would be to understand and compare the different aspects of Java annotation processors, Kotlin multiplatform and native, and testing frameworks in the context of software development. This analysis aims to provide a comprehensive understanding of these concepts, their applications, and how they interact with each other.
	* Unit testing is a crucial part of software development for several reasons. Firstly, it helps in identifying and fixing bugs early in the development process, which can save time and resources. By writing tests for individual units of code, developers can ensure that each part of the system works as expected. This can lead to more reliable and robust software
	  Secondly, unit tests serve as documentation. They provide clear examples of how different parts of the system are supposed to work, which can be helpful for new team members or for developers who need to revisit the code in the future. This makes the codebase easier to maintain and understand. Lastly, unit tests help in refactoring. When you have a suite of unit tests, you can confidently refactor your code knowing that you have tests in place to catch any regressions. This makes the process of improving the design and structure of your code safer and more efficient
	- The motivation behind this analysis comes from the need to understand how these tools and concepts can improve the efficiency and effectiveness of software development, due to their usage in unit-testing in Kotlin and JVM-based languages. Annotation processors can help to reduce boilerplate code and catch errors at compile time, which can lead to more robust and reliable software. Annotation processors are also used by `KAPT and KSP`, to generate code at compile time.
	- `KAPT` is used to generate code for Kotlin multiplatform since it relies on the java compiler. This means that, when using the compiler plugin `KAPT` with Kotlin, you will end up with java-bytecode, meaning your program can be used with other languages that compile to java-bytecode. However, as Kotlin has functionalities which is time intensive and hard to generate java stubs for, and the fact that the generated java-bytecode may be slower than expected, another tool arises.
	- `KSP` is used to generate code for Kotlin Native, meaning it relies on the `kotlinc-native` compiler. Compared to `KAPT` this is a **kotlin-first-approach**, where none of the code is being translated to java before compiling the code. `KSP` runs up to twice as fast as `KAPT`, which can make a big difference when doing multiple builds, for instance when testing your code multiple times. The output of the compiler is a binary executable, which can run on the platform which it was compiled for. This means that your system does not need to run the JVM in order to run your kotlin code, and you have faster build times.
	- The challenge is then that most of the testing frameworks for Kotlin, where the biggest ones are `Mockito and MockK`, use `KAPT` meaning you cannot test your kotlin code, if you use the Kotlin Native compiler. This is a very big problem, forcing you to use `KAPT` as the annotation processor for your code and rely on the JVM. Therefore, testing frameworks like `Mockative` have been created which use `KSP` to handle the annotation processing.
	- The goal of this analysis is to provide a detailed comparison of these tools and concepts, including their advantages, disadvantages, and specific use cases. This comparison will help to identify the best tools and concepts for different types of software development projects. It will also help to understand the limitations of these tools and concepts, and how to overcome these limitations.

* Plan of activities
	- [why we should be unit-testing, good points about when using SCRUM/agile/XP. Expensive not to do it](https://en.wikipedia.org/wiki/Unit_testing)
	- [Unit Testing Principles, Practices, and Patterns](https://sd.blackball.lv/library/unit_testing_(2020).pdf)
	- [MockK open source project](https://github.com/mockk/mockk)
		- Important to note that there are a lot of in depth articles explaining the ins and outs of the MockK framework.
		- contains an article about how it works under the hood
	- [Mockito source](https://github.com/mockito/mockito)
		- [Mockito javadoc](https://javadoc.io/doc/org.mockito/mockito-core/latest/org/mockito/Mockito.html)
		- [how it works under the hood](https://medium.com/@gorali/how-mockito-works-7d3a2c77da71)
	- [Mockative source](https://github.com/mockative/mockative)
		- self explanitory that I will be doing much implementation therefore I will go in depth with the implementation. However as `KAPT` and `KSP and KotlinPoet` is also gonna be explained, which is what is used, the implementation specifics wont be as long.
	- [byte-buddy, how Mockito and MockK handles mocking](https://github.com/raphw/byte-buddy)
	- [type erasure used by Mockito](https://www.baeldung.com/java-type-erasure)
	- [KSP source with useful links in README](https://github.com/google/ksp/tree/main)
		- [official explanations from kotlin lang](https://kotlinlang.org/docs/ksp-overview.html#supported-libraries)
	- [KotlinPoet](https://square.github.io/kotlinpoet/)


	* Development or research phase. Describe in general terms what you are going
	  to do and how.
		-  I will research how `KAPT` is used with `Mockito and MockK` going into the specifics about how they are coupled to the JVM limiting build time for the Kotlin code and hard to implemented features.
		- I will research the best practises of testing, different methods of testing, with the primary focus on unit testing
		- research annotation processors in java and kotlin, providing different examples of why it is used and how powerful it is. How it is used in `KSP, KAPT`, and elsewhere to reduce boiler plate, provide easy made documentation, reduce errors at runtime ...
		- when to use kotlin multiplatform and when to use kotlin/native, the difference factors to take into consideration such as performance boosts and limitations.
		- I am going to extend the `Mockative` framework with mocking of classes and spies, using the APIs provided by `KSP` and `KotlinPoet`, providing unit-tests showcasing it behaves as expected.
			- If time allows, I will look into implementations of generics in the Mockative, MockK, Mockatio and other advanced features,  `fakes, spies, error messages, interface mocking, coroutines, relaxed, ...`,  asserting, in regards to Kotlin, how hard it is to implement, if the different frameworks succeeded, and provide examples of how it looks like in Kotlin. 
	* Experiments. Describe to the the best you can what kind of experiments you
	  would like to run to answer your research question
		- Implementing the features of mocking classes and spies into the `Mockative`  framework, seeing that `KSP and KotlinPoet` will behave as expected, and the test cases are successfull
			- can mock a class in `Mockative`
			- can mock only certain functions using spies
		- I will implement some different tests, could fx be a function which calls another mocked function 100,000 times, and get numbers on the speed differences using the different frameworks.
	* Analysis + additional time to rerun experiments if needed
	* Finalizing the report/thesis following the academic conventions
* Tentative time plan
	- Februrary
		* Research of why we should unit test, barriers, bad testing, will take 1-2 weeks
		* Research of `java kotlin annotation processors` with examples will take 2 weeks.
		* Research of `KAPT, KSP, KotlinPoet` & understanding the `Mockative framework` will take 2 weeks.
	- March till mid april
		- Implement mocking classes in Mockative and spies.
	- mid april to start may
		* Research of specifics regarding `Mockito, MockK` and their coupling with the JVM, use of `type erasure, byte-buddy` will take 2 weeks
	* start may to mid may
		* Comparing speeds of the different testing frameworks, will take 1 week
* Risk evaluation
  * What are the risks involved in the project?
	  * not getting the features implemented
    What are possible remedies?
	- Explain what is going wrong, and what would fix it.
* Outcome. At the end of the project, the outcomes of the project will be
	- Why unit testing is important, with examples of which state of the art frameworks are available to you in Kotlin and other JVM based languages. An extension of `Mockative` has been added, providing functionality for mocking classes and spies. This will contain an explanation of the tools used to create the frameworks, with explanation of kotlin/native and kotlin multiplatform, and additionally what these tools imposes of limitations to the framework. With a comparison of the different features available to you, a speed comparison between the 3 test-frameworks and their ease of use. 
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
