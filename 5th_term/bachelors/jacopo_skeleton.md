## Unit testing in Kotlin and its coupling to the JVM
### Motivation & Goal
Unit testing is a crucial part of software development for several reasons. Firstly, it helps in identifying and fixing bugs early in the development process, which can save time and resources. By writing tests for individual units of code, developers can ensure that each part of the system works as expected. This can lead to more reliable and robust software
Secondly, unit tests serve as documentation. They provide clear examples of how different parts of the system are supposed to work, which can be helpful for new team members or for developers who need to revisit the code in the future. This makes the codebase easier to maintain and understand. Lastly, unit tests help in refactoring. When you have a suite of unit tests, you can confidently refactor your code knowing that you have tests in place to catch any regressions. This makes the process of improving the design and structure of your code safer and more efficient.

The motivation behind this thesis comes from the need to understand how unit-testing is performed in Kotlin and JVM-based languages. In particular, annotation processors can help to reduce boilerplate code and catch errors at compile time, which can lead to more robust and reliable software. Annotation processors are also used by `KAPT and KSP`, to generate code at compile time:
	- `KAPT` can be used used to generate code for only Kotlin/JVM since it relies on the java compiler. This means that, when using the compiler plugin `KAPT` with Kotlin, you will end up with java-bytecode, meaning your program can be used with other languages that compile to java-bytecode.
	- `KSP` can be used to generate code for the Kotlin Multiplatform targets: Kotlin/JVM, Kotlin/JS, Kotlin/iOS, Kotlin/Native, and more. Compared to `KAPT` this is a **kotlin-first-approach**, where none of the code is being translated to java before compiling the code. `KSP` runs up to twice as fast as `KAPT`, which can make a big difference when doing multiple builds, for instance when testing your code multiple times. This is primarily due to the overhead that `KAPT` has, when generating java stubs for the Kotlin code. The output of the compiler is a binary executable, which can run on the platform which it was compiled for. This means that your system does not need to run the JVM in order to run your kotlin code, and you have faster build times.

Most of the testing frameworks for Kotlin (i.e., `Mockito and MockK`) use `KAPT`, meaning that you cannot test your Kotlin code if you target other platforms in the Kotlin Multiplatform suite, than Kotlin/JVM. To overcome this limitation, testing frameworks like `Mockative` have been created which use `KSP` to handle the annotation processing.

However, the `Mockative` framework is a project in the early stage of development and has a limited set of features. For instance, as of now, the users are only allowed to mock `interfaces`, which puts constraints on code structure, such that the classes tested, have to implement the interface which are mocked in the tests. To relieve this constraint, the project will contain an implementation of mocking classes in Kotlin. In addition, `spies` will also be implemented. These will enable users to interact with the spied class, utilizing all its features except for those methods designated as mocked. This approach allows us to emulate specific functionalities, which aids in testing other aspects of the class

### Plan of activities

* State-of-the-art survey. We will start to consult the following online and book materials to survey the state of the art in unit testing.
	- [why we should be unit-testing, good points about when using SCRUM/agile/XP. Expensive not to do it](https://en.wikipedia.org/wiki/Unit_testing)
	- [Unit Testing Principles, Practices, and Patterns](https://sd.blackball.lv/library/unit_testing_(2020).pdf)
	- [# Learning Test-Driven Development: A Polyglot Guide to Writing Uncluttered Code](https://www.amazon.com/Learning-Test-Driven-Development-Polyglot-Uncluttered/dp/1098106474)
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

* Development and research phase
	- Extend the `Mockative` framework with mocking of classes and spies, using the APIs provided by `KSP` and `KotlinPoet`, providing unit-tests showcasing it behaves as expected.
	- If time allows, look into implementations of generics in the Mockative, MockK, Mockatio and other advanced features,  `fakes, spies, error messages, interface mocking, coroutines, relaxed, ...`,  asserting, in regards to Kotlin, how hard it is to implement, if the different frameworks succeeded.

* Experiments.
	- Test if the implemented features of mocking classes and spies into the `Mockative`  framework are working, witnessing that `KSP and KotlinPoet` will behave as expected, and the test cases are successfull.
	- Implement some different tests (e.g., a function which calls another mocked function 100,000 times) and get numbers on the speed differences using the different frameworks.

* Finalizing the report/thesis following the academic conventions

### Tentative time plan

- Februrary
	* Research of why we should use unit test, barriers, bad testing, will take 1-2 weeks
	* Research of `java kotlin annotation processors` with examples will take 2 weeks.
	* Research of `KAPT, KSP, KotlinPoet` & understanding the `Mockative framework` will take 2 weeks.
- March till mid April
	- Implement mocking classes in Mockative and spies.
- mid April to start May
	* Research of specifics regarding `Mockito, MockK` and their coupling with the JVM, use of `type erasure, byte-buddy` will take 2 weeks
- May
	* Comparing speeds of the different testing frameworks, will take 1 week
		
### Risk evaluation
  * A possible risk is having unexpected difficulties in developing the features in `Mockative`.
    If this happens, we will get an understanding of the difficulties and provide explanation of the barriers to develop or use such features.

### Outcome. At the end of the project, the outcomes of the project will be
  * Thesis reporting the state of the art, implementation details and experiment results written following the standard academic conventions 
  * The code & data for the implementation of mocking of classes and spies in `Mockative`, the different examples of annotation processors in java and kotlin, the tests used for comparing the test-frameworks.
