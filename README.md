# JMockit-Xtend

Collection of the extension methods adding [JMockit](http://jmockit.googlecode.com/)
support to the [Xtend](http://www.eclipse.org/xtend/).

Current release: ([more info](#VersionInfo))
- JMockit-Xtend: 0.2
  - Xtend: 2.6.0
  - JMockit: 1.10-1.11

## Screencast about JMockit-Xtend

If you have 12 minutes to spare, you can watch the new screen cast on the [XtextCasts.org](http://xtextcasts.org/):
- http://xtextcasts.org/episodes/13-jmockit-xtend

## Content ##

- [Introduction](#Introduction)
- [Download](#Download)
- [Version info](#VersionInfo)
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
  - [Dynamic partial mocking using `mock(class) []`](#DynamicPartialMockingWithMock)
  - [Dynamic partial mocking using `stub(class) []`](#DynamicPartialMockingWithStub)
  - [Specifying count of iterations for `mock`/`stub` expectations](#CountOfIterationWithMockAndStub)
 - [Creating fake instances using `ins(class)`](#CreateFakeInstance)
 - [Using `result=`](#UsingResult)
 - [Xtend-style dynamic result using `result= []`](#XtendStyleDynamicResult)
 - [Using `returns()`](#UsingReturns)
 - [Using `onInstance()`](#UsingOnInstance)
 - [Using `times=`](#UsingTimes)
 - [Using `maxTimes=`](#UsingMaxTimes)
 - [Using `minTimes=`](#UsingMinTimes)
 - [Simple parameter matching with `any()` and `with()`](#SimpleParameterMatchingWithAnyAndWith)
 - [Parameter matching with JMockit with*() methods](#ParameterMatchingWithWithXXX)
 - [Xtend-style dynamic parameter matching using `with []`](#XtendStyleParameterMatching)
 - [Mocking private methods](#MockingPrivateMethods)
- [Specifying default results](#DefaultResults)
- [TODO](#TODO)*
- [License](#License)

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

<a name="VersionInfo"></a>
## Version info

| Date       | Version | JMockit versions | Xtend versions |
| ---------- | ------- |:-----------------| -------------- |
| 09/22/2014 | 0.2     | [1.10,1.11]      | 2.6.0          |

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

<a name="DynamicPartialMockingWithMock"></a>
#### Dynamic partial mocking using `mock(class) []`

The `mock(classOrObject) []` method can be used for the partial mocking.

```java
mock(MyClass) [
    new MyClass().call1
]
```

You can also grab a mocked instance of the partial mocked class using closure parameter(s):

```java
mock(Api1, Api2) [it, api1, api2 |
    api1.call
    api2.call
]
```

You may pass up to 5 classes or objects like this: `mock(obj1, Class2, obj3, obj4, Class5)`. If you need to pass more
parameters you should use more verbose syntax specifying the closure first:

```java
mock([
    obj1.toString
    result = "obj1"
], obj1, Class2, obj3, obj4, Class5, Class6, obj7, obj8)
```

`mock(class)` or `stub(class)` methods can also be used to initiate a partial mocking:

```java
mock(Class1, Class2)
```

Expectations about `Class1` and `Class2` may be specified later on:

```java
mock [
	new Class1().method1
	ins(Class2).method2
]
```

Defining single partial mock can be combined with creation of an instance of the partial mocked class:

```java
val obj = mock(Class1)

mock [
	obj.method1
]
```

JMockit Tutorial: http://jmockit.googlecode.com/svn/trunk/www/tutorial/BehaviorBasedTesting.html#partial

<a href="#top">&#8593; top</a>

<a name="DynamicPartialMockingWithStub"></a>
#### Dynamic partial mocking using `stub(classOrObject) []`

The `stub(classOrObject) []` method can be used for non-strict the partial mocking.

```java
stub(MyClass) [
    service.call1
]
```

You can also grab a mocked instance of the partial stubbed class using closure parameter(s):

```java
stub(Api1, Api2) [it, api1, api2 |
    api1.call
    api2.call
]
```

You may pass up to 5 classes or objects like this: `stub(obj1, Class2, obj3, obj4, Class5)`. If you need to pass more
parameters you should use more verbose syntax specifying the closure first:

```java
stub([
    obj1.toString
    result = "obj1"
], obj1, Class2, obj3, obj4, Class5, Class6, obj7, obj8)
```

`stub(class)` or `mock(class)` methods can also be used to initiate a partial mocking:

```java
stub(Class1, Class2)
```

Expectations about `Class1` and `Class2` may be specified later on:

```java
stub [
	new Class1().method1
	ins(Class2).method2
]
```

Defining single partial stub can be combined with creation of an instance of the partial mocked class:

```java
val obj = stub(Class1)

stub [
	obj.method1
]
```

JMockit Tutorial: http://jmockit.googlecode.com/svn/trunk/www/tutorial/BehaviorBasedTesting.html#partial

<a href="#top">&#8593; top</a>

<a name="CountOfIterationWithMockAndStub"></a>
#### Specifying count of iterations for `mock`/`stub` expectations

You can specify the count of iterations as a first int parameter of the `mock`/`stub` expectation block:

```java
stub(10) [
    service.call1
    returns(1, 2, 3)
]
```

You can also specify the count of iterations and dynamic partial mocking objects at the same time:

```java
stub(10, Class1, obj2) [
    service.call1
    returns(1, 2, 3)
]
```

or for that 5 partial mocking parameters:

```java
stub([
    service.call1
    returns(1, 2, 3)
], 10, Class1, obj2, Class3, obj4, obj5, obj6, obj7, Class8)
```

<a href="#top">&#8593; top</a>

<a name="CreateFakeInstance"></a>
### Creating fake instances using `ins(class)`

In `mock[...]` and `stub[...]` expectations blocks you can get a fake instance of any object
using `ins(class)` method. This is particularly useful for partially mocking a class without handy constructor:

```java
stub(ClassWithoutSuitableConstructor) [
	ins(ClassWithoutSuitableConstructor).method
	result = 1
]
```

Alternatively, you can use closure parameters as described in "Dynamic partial mocking" section:

```java
stub(ClassWithoutSuitableConstructor) [it, instance|
	instance.method
	result = 1
]
```

*Please note:* instances created with `ins(class)` method are not initialized. Calling non-mocked methods
on such instances my cause unexpected behavior!

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

<a name="UsingMinTimes"></a>
### Using `minTimes=`

The `minTimes=` (or setMinTimes()) setter specifies the minimal number of the expected calls to the mocked method.

```java
mock [
	service.sendEmail()
	minTimes = 2
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

<a name="MockingPrivateMethods"></a>
### Mocking private methods

Private method mocking can be accomplished using one of overloaded `invoke()` extension methods:

```java
stub [
    invoke(object, "methodName", param1, param2)
    result = "result"


]
```

JMockit Tutorial: http://jmockit.googlecode.com/svn/trunk/www/tutorial/BehaviorBasedTesting.html#deencapsulation

<a href="#top">&#8593; top</a>

<a name="DefaultResults"></a>
## Specifying default results

Other that in the JMockit the default results can be specified within the test class.

```java
class MyTest {
    @Mocked
    MyAPI api

    @Input
    int a = -1 // Return -1 for all methods returning "int"

    @Input
    IOException e // Throw IOException for all methods declaring IOException

    def void myTest() {
        assertThat(api.getInt(), is(-1))
    }
}
```

JMockit Tutorial: http://jmockit.googlecode.com/svn/trunk/www/tutorial/BehaviorBasedTesting.html#defaultResults


<a href="#top">&#8593; top</a>

<a name="TODO"></a>
## TODO

- README - summarize differences to the JMockit API
- Iterated expectations
- Explicit verification
- Accessing private fields, methods and constructors
- Cascading mocks
- Capturing internal instances of mocked types
- Automatic instantiation and injection of tested classes
- Reusing expectation and verification blocks
- State-based testing with JMockit
- forEachInvocation (see InvocationBlockModifier.java)
- Add withNull(T) method to allow null parameter matching with invoke()

<a href="#top">&#8593; top</a>

<a name="License"></a>
## License

JMockit-Xtend is dual-licensed (available under either MIT or EPL licenses):
- [MIT License](http://opensource.org/licenses/mit-license.php)
- [EPL](http://www.eclipse.org/org/documents/epl-v10.php)
