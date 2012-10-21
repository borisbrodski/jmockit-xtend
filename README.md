# JMockit-Xtend

Collection of the extension methods adding [JMockit](http://jmockit.googlecode.com/)
support to the [Xtend](http://www.eclipse.org/xtend/).


## Screencast about JMockit-Xtend

If you have 12 minutes to spare, you can watch the new screen cast on the [XtextCasts.org](http://xtextcasts.org/):
- http://xtextcasts.org/episodes/13-jmockit-xtend

## Content ##

- [Introduction](#Introduction)
- [Download](#Download)
- [New cool Xtend-driven API enhancements](#NewCoolXtendAPI)
 - [Simple mock definitions](#SimpleMockDefinitions)
 - [`any` without cast](#AnyWithoutCast)
 - [Dynamic parameter matching](#DynamicParameterMatching)
 - [Dynamic return value](#DynamicReturnValue)
- [Differences to the original JMockit API](#DifferencesToJMockitAPI)
- [Usage](#Usage)
 - [Expectations](#Expectations)
  - [Expectations using `mock []`](#StrictExpectationsUsingMock)
  - [Non strict expectations using `stub []`](#NonStrictExpectationsWithStub)
 - [Using `result=`](#UsingResult)
 - [Xtend-style dynamic result using `result= []`](#XtendStyleDynamicResult)
 - [Using `returns()`](#UsingReturns)
 - [Using `onInstance()`](#UsingOnInstance)
 - [Using `times=`](#UsingTimes)
 - [Using `maxTimes=`](#UsingMaxTimes)
 - [Simple parameter matching with `any()` and `with()`](#SimpleParameterMatchingWithAnyAndWith)
 - [Parameter matching with JMockit with\*() methods](#ParameterMatchingWithWithXXX)
 - [Xtend-style dynamic parameter matching using `with []`](#XtendStyleParameterMatching)
- [TODO](#TODO)

<a name="Introduction"></a>
## Introduction

JMockit-Xtend provides a collection of the extension and helper methods
to integrate the popular java mocking framework
[JMockit](http://jmockit.googlecode.com/) with the new
[Xtend](http://www.eclipse.org/xtend/) language.
The goal is not only to provide [almost complete](#DifferencesToJMockitAPI "Differences to the original JMockit API")
original JMockit API to the Xtend but also [enhance the API](#NewCoolXtendAPI) using the power of the Xtend.

The optimal use of the JMockit-Xtend can to achieved together with [Jnario](http://jnario.org/).

JMockit-Xtend consists of a single java file [JMockitExtension.java](https://raw.github.com/borisbrodski/jmockit-xtend/master/src/org/eclipse/xtend/jmockit/JMockitExtension.java),
and [Jnario](http://jnario.org/) tests.

<a href="#top">&#8593; top</a>

<a name="Download"></a>
## Download

You can download the JMockitExtension.java from the master branch
[here](https://raw.github.com/borisbrodski/jmockit-xtend/master/src/org/eclipse/xtend/jmockit/JMockitExtension.java) 
and then simply add the downloaded file to your java project.

<a href="#top">&#8593; top</a>

<a name="NewCoolXtendAPI"></a>
## New cool Xtend-driven API enhancements

Cool things first. Here is a brief overview of the new cool Xtend-powered API

<a href="#top">&#8593; top</a>

<a name="SimpleMockDefinitions"></a>
### Simple mock definitions

JMockit-Xtend provides a set of convenient methods to define the mock configurations:

- `mock []` defines the [strict mock expectations](http://jmockit.googlecode.com/svn/trunk/www/tutorial/BehaviorBasedTesting.html#strictness)
- `stub []` defines the [non-strict mock expectations](http://jmockit.googlecode.com/svn/trunk/www/tutorial/BehaviorBasedTesting.html#strictness)

Example:

```java
stub [
    permissionHelper.allowToSend       // non-strict expectations 
    result = true
]

mock [
    permissionHelper.prepareOperation       // strict expectations
    permissionHelper.performOperation       // strict expectations 
]
```

<a href="#top">&#8593; top</a>

<a name="AnyWithoutCast"></a>
### `any` without cast

Thanks to the generic method definition is itn't necessary to cast the `any` to the
expected type. You can do it though to enforce the type, if you want.

**Warning**: The `any` method can be used only with the non primitive type. For all
primitive types the corresponding `anyInt`, `anyLong`, ... methods should be used.
The violators will be punished with the NullPointerException.

```java
stub [
    service.acceptString(any, any, any)
    stringBuilder.append(<String>any)    // Force to type to call the right method
    Math::max(any, any)                  // NullPointerException, use anyInt instead
]
```

For more information see [Simple parameter matching with `any()` and `with()`](#SimpleParameterMatchingWithAnyAndWith)

<a href="#top">&#8593; top</a>

<a name="DynamicParameterMatching"></a>
### Dynamic parameter matching

It's very easy to match the parameter using [Xtend-Lambda Expressions](http://www.eclipse.org/xtend/documentation.html#lambdas):

```java
stub [
    service.acceptString(with [ length > 5 ])
]
``` 

<a href="#top">&#8593; top</a>

<a name="DynamicReturnValue"></a>
### Dynamic return value

It's also very easy to calculate a return value of the mocked method on the fly:

```java
stub [
    service.generateEMail(any, any, any)
    result = [ String to, String subject, String body |
        '''
            To: «to»
            Subject: «subject»
            «body»
        '''.toString
    ]
]
``` 

<a href="#top">&#8593; top</a>

<a name="DifferencesToJMockitAPI"></a>
## Differences to the original JMockit API

*TODO* describe:
- Using `with(T)` matcher, if at least one matcher used
- Using `withDelegate(Delegate)` instead of `with(Delegate)`

<a href="#top">&#8593; top</a>

<a name="Usage"></a>
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


<a href="#top">&#8593; top</a>

<a name="Expectations"></a>
### Expectations

<a name="StrictExpectationsUsingMock"></a>
#### Expectations using `mock []`

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

<a href="#top">&#8593; top</a>

<a name="NonStrictExpectationsWithStub"></a>
#### Non strict expectations using `stub []`

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

<a href="#top">&#8593; top</a>

<a name="UsingResult"></a>
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

<a href="#top">&#8593; top</a>

<a name="XtendStyleDynamicResult"></a>
### Xtend-style dynamic result using `result= []`

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

<a href="#top">&#8593; top</a>

<a name="UsingReturns"></a>
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

<a href="#top">&#8593; top</a>

<a name="UsingOnInstance"></a>
### Using `onInstance()`

The `onInstance` method can be used to restrict an extected call to a single instance of a mocked class.

```java
mock [
    instance2.callAcceptedOnAllInstances()
    onInstance(instance2).callAcceptedOnlyOnInstance2()
]
```

Tutorial: http://jmockit.googlecode.com/svn/trunk/www/tutorial/BehaviorBasedTesting.html#onInstance

<a href="#top">&#8593; top</a>

<a name="UsingTimes"></a>
### Using `times=`

The `times=` (or setTimes()) setter specifies the number of the expected calls to the mocked method.

```java
mock [
    service.sendEmail()
    times = 3
]
``` 

JMockit Tutorial: http://jmockit.googlecode.com/svn/trunk/www/tutorial/BehaviorBasedTesting.html#constraints

<a href="#top">&#8593; top</a>

<a name="UsingMaxTimes"></a>
### Using `maxTimes=`

The `maxTimes=` (or setMaxTimes()) setter specifies the maximal number of the expected calls to the mocked method.

```java
mock [
    service.sendEmail()
    maxTimes = 5
]
``` 

JMockit Tutorial: http://jmockit.googlecode.com/svn/trunk/www/tutorial/BehaviorBasedTesting.html#constraints

<a href="#top">&#8593; top</a>

<a name="SimpleParameterMatchingWithAnyAndWith"></a>
### Simple parameter matching with `any()` and `with()`

The `any()`, `anyInt()`, `anyLong()`, ... and `with()`, `withInt()`, `withLong()`, ... extension methods are used to
statically match the parameter of the mocked method.

**WARNING**: Unlike JMockit API, you have to wrap the concrete values within `with\*()` for every invocation,
where one of the `any\*()' methods are used.

```java
stub [
    service.max(1, 2)               // ok    - no use of any()
    service.max(anyInt, with(3))    // ok    - using with() for the values
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

<a href="#top">&#8593; top</a>

<a name="ParameterMatchingWithWithXXX"></a>
### Parameter matching with JMockit with\*() methods

Following JMockit `with\*()` methods are supported within "expectations" and "verification" blocks:

- `with(Object)`
- `with(T, Object)`
- `withAny(T)`
- `withEqual(double, double)`
- `withEqual(float, double)`
- `withEqual(T)`
- `withInstanceLike(T)`
- `withInstanceOf(Class) Doesn't work with primitive types`
- `withMatch(T)`
- `withNotEqual(T)`
- `withNotNull()`
- `withNull()`
- `withPrefix(T)`
- `withSameInstance(T)`
- `withSubstring(T)`
- `withSuffix(T)`

The JMockit `with(Delegate)` is renamed to `withDelegate(Delegate)` allowing the Xtend-lambda expression to be used with the simple `with []` syntax 

Following JMockit `with\*()` methods are supported only within the "verifications" block:

- `withCapture()`
- `withCapture(Object)`

<a href="#top">&#8593; top</a>

<a name="XtendStyleParameterMatching"></a>
### Xtend-style dynamic parameter matching using `with []`

The dynamic parameter matching can be accomplished using Xtend-lambda expression using the `with []`
extension method for the `Object` types and `withInt []`, `withLong []`, ... extension method for
all primitive types.

```java
stub [
    service.processString(with [ length > 5 ])
    service.processString(with [ it?.length > 5 ]) // Prevents NullPointerException if it==null
                                                   // If it==null then (it?.length) evaluates to 0 
    service.processInt(withInt [ it > 0 ])

    service.processInt(with [ it > 0 ])  // NullPointerException: withInt should be used
]
```

<a href="#top">&#8593; top</a>

<a name="TODO"></a>
## TODO

- Add minTimes
- README - summarize differences to the JMockit API
- Specifying default results
- Iterated expectations
- Explicit verification
- Accessing private fields, methods and constructors
- Dynamic partial mocking
- Cascading mocks
- Capturing internal instances of mocked types
- Automatic instantiation and injection of tested classes
- Reusing expectation and verification blocks
- State-based testing with JMockit
- forEachInvocation (see InvocationBlockModifier.java) 

<a href="#top">&#8593; top</a>
