# Xtend-JMockit

Collection of the Xtend extension methods adding JMockit support

## Introduction

Xtend-JMockit contains a single file (upon tests) with the collection
of the Xtend extension methods and a couple of entry methods, like `mock` and `stub`.

## Usage

```java
import mockit.Mocked
import org.junit.Test
import static org.junit.Assert.*
import static org.hamcrest.core.Is.*

class MyTest {
	@Test
	def void myTest(MyService service) {
		mock [
			service.doGreeting
			result = "Hello World"
		]
		
		assertThat(service.doGreeting, is("Hello World"))
	}
```

### Using `mock []`

The `mock []` method is an alias to the JMockit `new `[Expectations](http://jmockit.googlecode.com/svn/trunk/www/javadoc/mockit/Expectations.html)()`{{ ... }}`
block, which is a strict by default.

```java
mock [
    // Strict expectations
    // - default: times = 1
    // - order is important
	service.call1
	service.call2("x")
	service.call3(1, 2)
]
```

JMockit Tutorial: http://jmockit.googlecode.com/svn/trunk/www/tutorial/BehaviorBasedTesting.html#strictness

### Using `stub []`

The `stub []` method is an alias to the JMockit `new `[NonStrictExpectations](http://jmockit.googlecode.com/svn/trunk/www/javadoc/mockit/NonStrictExpectations.html)()`{{ ... }}`
block, which is a non-strict by default.

```java
stub [
    // Non-strict expectations
    // - default: times = infinity
    // - order is't important
	service.call1
	service.call2("x")
	service.call3(1, 2)
]
```

JMockit Tutorial: http://jmockit.googlecode.com/svn/trunk/www/tutorial/BehaviorBasedTesting.html#strictness

### Using `result=`

The `result=` setter can be used to set one or more results
or to throw an exception as a result of the mocked method call.

```java
mock [
	service.methodReturningString
	result = "Hello World!"
	result = new NoMoreGreetingsException
	result = "Ok, the last one"
]

assertThat(service.methodReturningString, is("Hello World!"))
try {
	service.methodReturningString
	fail("Exception expected")
} catch (NoMoreGreetingsException e) {}
assertThat(service.methodReturningString, is("Ok, the last one"))
```

There are `resultInt=`, `resultLong=`, `resultShort=`, ... methods available to enforce the type casting
and reduce the chance of the ClassCastException:

```java
mock [
	service.methodReturningLong
	result = 1L      // With postfix 'L'
	resultLong = 1   // Without postfix 'L'
]
```

JMockit Tutorial: http://jmockit.googlecode.com/svn/trunk/www/tutorial/BehaviorBasedTesting.html#results

### Dynamic `results=`

The `result=` setter can be also used to pass a lambda expression instead of a constant result.
The lambda expression will be evaluated each time the mocked method is invoked.

```java
mock [
	service.getUniqueId
	result = [| id = id + 1 ]
	
	service.calculateSum(anyInt, anyInt)
	result = [ int a, int b | a + b ]
]
```


### Using `returns()`

The `returns` method can be also used to set one or more results
but can't be used to throw an exception as a result of the mocked method call.
For further information consult the JMockit documentation. (e. g. http://jmockit.googlecode.com/svn/trunk/www/tutorial/BehaviorBasedTesting.html) 

```java
mock [
	service.methodReturningString
	returns("Hello", "World!")
	returns("Ok, the last one")
]

assertThat(service.methodReturningString, is("Hello"))
assertThat(service.methodReturningString, is("World!"))
assertThat(service.methodReturningString, is("Ok, the last one"))
```

There are also `returnsInt=`, `returnsLong=`, `returnsShort=`, ... methods available to enforce the type casting
and reduce the chance of the ClassCastException:

```java
mock [
	service.methodReturningLong
	returns(1L)    // With postfix 'L'
	returns(1)     // Without postfix 'L'
]
```

JMockit Tutorial: http://jmockit.googlecode.com/svn/trunk/www/tutorial/BehaviorBasedTesting.html#results

### Using `onInstance()`

The `onInstance` method can be used to restrict an extected call to a single instance of a mocked class.

```java
mock [
	instance2.callAcceptedOnAllInstances()
	onInstance(instance2).callAcceptedOnlyOnInstance2()
]
```

Tutorial: http://jmockit.googlecode.com/svn/trunk/www/tutorial/BehaviorBasedTesting.html#onInstance


### Using `times=`

The `times=` (or setTimes()) setter specifies the number of the expected calls to the mocked method.

```java
mock [
	service.sendEmail()
	times = 3
]
``` 

JMockit Tutorial: http://jmockit.googlecode.com/svn/trunk/www/tutorial/BehaviorBasedTesting.html#constraints


### Using `maxTimes=`

The `maxTimes=` (or setMaxTimes()) setter specifies the maximal number of the expected calls to the mocked method.

```java
mock [
	service.sendEmail()
	maxTimes = 5
]
``` 

JMockit Tutorial: http://jmockit.googlecode.com/svn/trunk/www/tutorial/BehaviorBasedTesting.html#constraints

### Simple parameter matching with `any()` and `with()`

The `any()`, `anyInt()`, `anyLong()`, ... and `with()`, `withInt()`, `withLong()`, ... extension methods are used to
statically match the parameter of the mocked method.

**WARNING**: Unlike JMockit API, you have to wrap the concrete values within `with*()` for every invocation,
where one of the `any*()' methods are used.

```java
stub [
	service.max(1, 2)            // ok    - no use of any()
	service.max(anyInt, with(3)) // ok    - using with() for the values
	service.max(anyInt, 3)          // ERROR - any() used, but the values without with()
	
	stringBuilder.append(anyChar)        // Match java.lang.StringBuilder.append(char) 
	stringBuilder.append(with(3.3))      // Match java.lang.StringBuilder.append(double) 
	stringBuilder.append(withFloat(3.3)) // Match java.lang.StringBuilder.append(float) 
]
``` 

**WARNING**: Unlike JMockit API, there are `any()` extension methods, that has the generic definition:
```java
public static < T > T any(Expectations expectations) throws Exception {
    ...
    return null;
}
```

As a result, the `any()` extension method can be used for all kind of parameters without casting. The down side of
this method is, that it produces a NullPointerException each time it used with primitive type.

```java
stub [
	service.max(withInt(1), any)            // NullPointerException: Xtend call any.intValue() where any == null
	service.max(withInt(1), anyInt)         // ok: anyInt == (int)0
]
```

### Static parameter matching with with*() methods

All JMockit with*() methods are supported:

* [x] with(Object)
* [x] with(Delegate<T>)  Only with explicit casting
* [x] with(T, Object)
* [x] withAny(T)
* [ ] withCapture()
* [ ] withCapture(List<T>)
* [ ] withEqual(double, double)
* [ ] withEqual(float, double)
* [ ] withEqual(T)
* [ ] withInstanceLike(T)
* [ ] withInstanceOf(Class<T>)
* [ ] withMatch(T)
* [ ] withNotEqual(T)
* [ ] withNotNull()
* [ ] withNull()
* [ ] withPrefix(T)
* [ ] withSameInstance(T)
* [ ] withSubstring(T)
* [ ] withSuffix(T)

### Dynamic parameter matching with `matching*()`



### TODO

* README - summarize differences to the JMockit API

* Specifying default results
* Iterated expectations

* Explicit verification
* Accessing private fields, methods and constructors
* Dynamic partial mocking
* Cascading mocks
* Capturing internal instances of mocked types
* Automatic instantiation and injection of tested classes
* Reusing expectation and verification blocks
* State-based testing with JMockit
