- KAPT targets JVM and java language
	- tightly coupled and have to translate into JVM specifics [kapt handling](https://kotlinlang.org/docs/ksp-why-ksp.html#comparison-to-kapt)
	- actually uses `javac` (look same section as above) 
- KSP targets kotlin directly https://kotlinlang.org/docs/ksp-why-ksp.html#comparison-to-reflection
	- faster compile time in comparrison to KAPT (2 times faster)
	- provides an API to the compiler, to keep it seperate from the deep learning of compiler and implementation of the `kotlinc-compiler`
	- should not modify code (annotation processor)
	- Not 

**!!!kapt is not supported for kotlin/native!!!** This is because it generates source code for java. This is a huge problem when considering it is faster to run natively than the JVM. And as some project uses **kotlin/native for fx mobile apps** `we need a testing framework which can handle kotlin/native` to test kotlin/native code.

Kapt (Kotlin Annotation Processing Tool) is primarily designed for JVM-based projects, including Android projects, and it's not typically used with Kotlin/Native or Kotlin/JS projects [kotlinlang.org](https://kotlinlang.org/docs/kapt.html).

Kapt generates Java stubs from Kotlin files, which Java annotation processors then process. However, Kotlin/Native and Kotlin/JS do not use the JVM, so this approach is not applicable [kotlinlang.org](https://kotlinlang.org/docs/kapt.html).

Kotlin/Native is a technology for compiling Kotlin directly to native binaries, which can run without a virtual machine. Kotlin/JS is a technology for compiling Kotlin to JavaScript, which can run in any JavaScript environment. Neither of these environments have a concept of Java annotation processors, so Kapt cannot be used with them [kotlinlang.org](https://kotlinlang.org/docs/kapt.html).

On the other hand, KSP (Kotlin Symbol Processing) is a Kotlin-first alternative to Kapt and it's designed to work with all Kotlin platforms, including Kotlin/Native and Kotlin/JS. KSP analyzes Kotlin code directly, which makes it more suitable for these platforms [developer.android.com](https://developer.android.com/build/migrate-to-ksp).

In conclusion, while Kapt is a valuable tool for annotation processing in JVM-based Kotlin projects, it's not suitable for Kotlin/Native or Kotlin/JS projects. For these platforms, KSP is the recommended tool for annotation processing.




# list of things to write about

https://www.youtube.com/watch?v=nKCsIHWircA
talk about **runtime environments?**: JUNIT5,4?, which else 

- what are `anotation processors`
	- what are annotations
		- Talk about the different scopes of the annotations, 
			- `@Target, @Retention, ...` 
			- why they are used
	- a lot of java annotation processors are available
	- where is it used, and why
		- remove boilerplate code, generate documentation, catch more errors at compile time than runtime
			- for instance `@Override` checks if a method is actually being overriden in a subclass 
	- how does it work
		- The annotation processing is done in multiple rounds. Each round starts with the compiler searching for the annotations in the source files and choosing the annotation processors suited for these annotations. Each annotation processor is called on the corresponding sources. If any files are generated during this process, another round is started with the generated files as its input. This process continues until no new files are generated during the processing stage [baeldung.com](https://www.baeldung.com/java-annotation-processing-builder).
- kotlin multiplatform and native
	- multiplatform is code that can be shared among all projects that can use the JVM
	- native is code that are compiled to binary executables, fx cannot use native to both `IOS and android`
	- `KAPT, KSP & kotlinPoet` - `based on jvm, kotlin symbol prossecor with code generation` 
		- This brings the talk to testing frameworks which relies on using `KAPT` and `KSP`
			- as KAPT is coupled to the JVM, certain kotlin specific functionalities are not supported. Therefore the struggles when testing kotlin code with most used frameworks which relies on the `JVM`.
				- which features of the kotlin framework is not supported, and why?
			- in here how `mockative` is not coupled to JVM (most of all since it uses `KSP`, but how are the features specifically implemented). Also why `Mockito and MockK` are coupled to JVM and what it does under the hood [taken from one of the sources within MockK references](https://chao2zhang.medium.com/unraveling-mockks-black-magic-e725c61ed9dd)
				- The use of `ByteBuddy` to manipulate java byte code. 
- runtime environments???
- unit testing in software development
	- Why we want to test / barriers in testing and misunderstanding in testing
		- https://insights.sei.cmu.edu/blog/common-testing-problems-pitfalls-to-prevent-and-mitigate/
		- Good error messages
		- The use of `any()`
		- Relaxed mocking
		- testing single fields
	- testing frameworks
		- comparison between `mockative, mockito, mockk`
			- Speed comparisons
			- advanced features
			- complicated features
				- generics, interfaces, abstract classes, final classes, coroutines
					- mockito https://www.waldo.com/blog/mockito-mock-generic-class
						- mockito cannot mock final classes, hard time supporting generics (type errasor), suspend functions cannot be handled
					- MockK https://chao2zhang.medium.com/unraveling-mockks-black-magic-e725c61ed9dd 
						- same problem, generics are complicated, cannot mock final classes, have to make subclasses for interfaces and abstract classes
					- Mokative
						- generics are more supported keeping the generic type at runtime
	- 

## Great sources
https://insights.sei.cmu.edu/blog/common-testing-problems-pitfalls-to-prevent-and-mitigate/
[KSP open-source github project](https://github.com/google/ksp/tree/main)
[this is just an example, but javadoc or kotlin own website](https://kotlinlang.org/docs/ksp-quickstart.html#eda56b9a)
[how MockK handles mocks under the hood](https://chao2zhang.medium.com/unraveling-mockks-black-magic-e725c61ed9dd)
### Somewhat great
https://medium.com/swlh/all-about-annotations-and-annotation-processors-4af47159f29d