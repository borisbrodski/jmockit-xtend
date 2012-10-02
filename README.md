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

### Using result=

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

### Using returns()

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

### Using onInstance()

The `onInstance` method can be used to restrict an extected call to a single instance of a mocked class.

```java
mock [
	instance2.callAcceptedOnAllInstances()
	onInstance(instance2).callAcceptedOnlyOnInstance2()
]
```

Tutorial: http://jmockit.googlecode.com/svn/trunk/www/tutorial/BehaviorBasedTesting.html#onInstance


### Using times=

The `times=` (or setTimes()) setter specifies the number of the expected calls to the mocked method.

```java
mock [
	service.sendEmail()
	times = 3
]
``` 

JMockit Tutorial: http://jmockit.googlecode.com/svn/trunk/www/tutorial/BehaviorBasedTesting.html#constraints


### Using maxTimes=

The `maxTimes=` (or setMaxTimes()) setter specifies the maximal number of the expected calls to the mocked method.

```java
mock [
	service.sendEmail()
	maxTimes = 5
]
``` 

JMockit Tutorial: http://jmockit.googlecode.com/svn/trunk/www/tutorial/BehaviorBasedTesting.html#constraints

