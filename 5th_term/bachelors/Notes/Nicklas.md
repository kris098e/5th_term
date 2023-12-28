# 2nd Intro
## Own notes after the explanation
There is generated enough code such that each invocation of a function has the correct values, and information is saved to find out which functions are stubbed.

At first we record, and since the `invoke()` function is used, while recording, that means an exception is thrown, whrere we can then record which function was used, and later add the expected behaviour on the `ResultBuilder`. When the `invoke` function is then called without being in `recording`-mode, the stub is then called, if it exists.

Have to remove the global state for each of the mocks when we want to mock classes. This is because as a class, we cannot extend 2 classes. So when we have to extend the original class, we can only extend this, and not `Mockable`. We do this by making a hashmap `Map<Any, AtomicList<Stub>`, keeping the state in the map, and the invocations. So we make all of the functions go outside of `Mockable` as fx top-level protected functions, and they can then be used by each of the generated mocks

For `spies` we can for instance, if dont find a stubbing when a function is called, just call `super.$function()` with the supplied arguments. This way we dont have to do a lot of work for `spies`. We just have to add something to the `invoke()`-function (maybe), and generate some code.
## 1st phase / compile time / K-generation
1. Annotate property with `@Mock` which we will use for generating the code needed such that we can do logic on the annotated property, as we find all the properties annotated with this to know which classes to generate code for.
2. That is, we generate the respective classes, add the properties for the class, and add the functions with the correct modifiers, arguments ...
3. We need the specific `mock(class: Kclass<T>)` function for each of mocked properties, which should be in exactly the same package for the function to work.
4. All of the generated classes should extend `Mockable` which is the class responsible for doing the logic on runtime.
## 2nd phase / runtime
- The kotlin compiler automaticly uses the generated `mock()` functions because they are more specific than the generic variant included in the core library.
- On the mock, you can use the functions provided by the `Mockable` class, for creating the expected behavior. 
- We use `every { }` and `coEvery { }` to create the expected behaviour. We create the expected behavior by recording the invocations, via exceptions, where we store the expectation matching the invocation in a list for later `match`-finding.

# Steps
# Stubbing of class types

1. Refactor code to remove dependency on `Mockable` by moving code to functions unrelated to the mock instance, e.g. by having the instance as a first parameter, and by keeping state per instance globally/statically
2. Remove support for `stubsUnitByDefault` until further notice
3. Make code generator generate code without the use of the now removed `Mockable` base class
4. Make code generator support generating code for classes with a 0 parameter constructor (Require the use of the `all-open` plugin)
5. Make code generator support recursively generating mocks for classes with non-zero parameter constructors

# First intro
## ValueOf / problems with generating the correct classes as parameters
https://github.com/mockative/mockative/blob/bc10f2a7bd6ef9ab8b8ea2c3eb643e475f21b6d5/mockative/src/jvmMain/kotlin/io/mockative/fake/ValueOf.kt#L49
- Different implementation whether it is for JVM or kotlin/native. JVM is shit and need much implementation. This is due to JVM checking parameters when function is called, both native and JVM checks on compile-time, but JVM also checks types on runtime. In native we can simply say we dont care about the cast, i.e suppress cast.
- Mockative, mockito and mockK all uses same libraries to generate classes on runtime and then instantiating these via fx `objenesis`
	- generating instantiation without calling the constructor, whenever the constructor is not accessible.
## Recording mode and execution mode
When dealing with the stubs we enter recording mode, `isRecording = true`, where we then throw the correct errors depending on the mode. We add the stubing the recording and expectation to a list, where we then can use these again.
`almost all of the runtime part of the mocking is in the Mockable-class`
- The `invoke()` and `recording` part of the mocking is the bread and butter. So we recording something first, and then we can finally invoke the function by executing it.


