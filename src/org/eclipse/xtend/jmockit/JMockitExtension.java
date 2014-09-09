/*
The MIT License (MIT)

Copyright (c) <year> <copyright holders>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
*/

/* or */

/*******************************************************************************
 * Copyright (c) 2012 Boris Brodski.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * which accompanies this distribution, and is available at
 * http://www.eclipse.org/legal/epl-v10.html
 *
 * Contributors:
 *     Boris Brodski - initial API and implementation
 ******************************************************************************/

package org.eclipse.xtend.jmockit;

import mockit.Expectations;
import mockit.ExpectationsDelegate;
import mockit.NonStrictExpectations;

public class JMockitExtension {
    public static abstract class XtendNonStrictExpectations extends NonStrictExpectations {
        public abstract void apply(ExpectationsDelegate delegate);
    }

    public static abstract class XtendExpectations extends Expectations {
        public abstract void apply(ExpectationsDelegate delegate);
    }

    public static void stub(final XtendNonStrictExpectations e) {
        new NonStrictExpectations() {{
            e.apply(new ExpectationsDelegate(this));
        }};
    }
    public static void stub(Object partiallyMocked1, final XtendNonStrictExpectations e) {
        new NonStrictExpectations(partiallyMocked1) {{
            e.apply(new ExpectationsDelegate(this));
        }};
    }
    public static void stub(Object partiallyMocked1,
                            Object partiallyMocked2, final XtendNonStrictExpectations e) {
        new NonStrictExpectations(partiallyMocked1, partiallyMocked2) {{
            e.apply(new ExpectationsDelegate(this));
        }};
    }
    public static void stub(Object partiallyMocked1,
                            Object partiallyMocked2,
                            Object partiallyMocked3, final XtendNonStrictExpectations e) {
        new NonStrictExpectations(partiallyMocked1, partiallyMocked2, partiallyMocked3) {{
            e.apply(new ExpectationsDelegate(this));
        }};
    }
    public static void stub(Object partiallyMocked1,
                            Object partiallyMocked2,
                            Object partiallyMocked3,
                            Object partiallyMocked4, final XtendNonStrictExpectations e) {
        new NonStrictExpectations(partiallyMocked1, partiallyMocked2, partiallyMocked3, partiallyMocked4) {{
            e.apply(new ExpectationsDelegate(this));
        }};
    }
    public static void stub(Object partiallyMocked1,
                            Object partiallyMocked2,
                            Object partiallyMocked3,
                            Object partiallyMocked4,
                            Object partiallyMocked5, final XtendNonStrictExpectations e) {
        new NonStrictExpectations(partiallyMocked1, partiallyMocked2, partiallyMocked3, partiallyMocked4, partiallyMocked5) {{
            e.apply(new ExpectationsDelegate(this));
        }};
    }
    public static void stub(final XtendNonStrictExpectations e, Object ... partiallyMockeds) {
    	new NonStrictExpectations(partiallyMockeds) {{
    		e.apply(new ExpectationsDelegate(this));
    	}};
    }

    public static void stub(Integer numberOfIterations, final XtendNonStrictExpectations e) {
        new NonStrictExpectations(numberOfIterations) {{
            e.apply(new ExpectationsDelegate(this));
        }};
    }
    public static void stub(Integer numberOfIterations,
    						Object partiallyMocked1, final XtendNonStrictExpectations e) {
    	new NonStrictExpectations(numberOfIterations, partiallyMocked1) {{
    		e.apply(new ExpectationsDelegate(this));
    	}};
    }
    public static void stub(Integer numberOfIterations,
    						Object partiallyMocked1,
    						Object partiallyMocked2, final XtendNonStrictExpectations e) {
    	new NonStrictExpectations(numberOfIterations, partiallyMocked1, partiallyMocked2) {{
    		e.apply(new ExpectationsDelegate(this));
    	}};
    }
    public static void stub(Integer numberOfIterations,
    		Object partiallyMocked1,
    		Object partiallyMocked2,
    		Object partiallyMocked3, final XtendNonStrictExpectations e) {
    	new NonStrictExpectations(numberOfIterations, partiallyMocked1, partiallyMocked2, partiallyMocked3) {{
    		e.apply(new ExpectationsDelegate(this));
    	}};
    }
    public static void stub(Integer numberOfIterations,
    		Object partiallyMocked1,
    		Object partiallyMocked2,
    		Object partiallyMocked3,
    		Object partiallyMocked4, final XtendNonStrictExpectations e) {
    	new NonStrictExpectations(numberOfIterations, partiallyMocked1, partiallyMocked2, partiallyMocked3, partiallyMocked4) {{
    		e.apply(new ExpectationsDelegate(this));
    	}};
    }
    public static void stub(Integer numberOfIterations,
    		Object partiallyMocked1,
    		Object partiallyMocked2,
    		Object partiallyMocked3,
    		Object partiallyMocked4,
    		Object partiallyMocked5, final XtendNonStrictExpectations e) {
    	new NonStrictExpectations(numberOfIterations, partiallyMocked1, partiallyMocked2, partiallyMocked3, partiallyMocked4, partiallyMocked5) {{
    		e.apply(new ExpectationsDelegate(this));
    	}};
    }

    public static void stub(final XtendNonStrictExpectations e, Integer numberOfIterations, Object ... partiallyMockeds) {
    	new NonStrictExpectations(numberOfIterations, partiallyMockeds) {{
    		e.apply(new ExpectationsDelegate(this));
    	}};
    }

    public static void mock(final XtendExpectations e) {
        new Expectations() {{
            e.apply(new ExpectationsDelegate(this));
        }};
    }
    public static void mock(Object partiallyMocked1, final XtendExpectations e) {
        new Expectations(partiallyMocked1) {{
            e.apply(new ExpectationsDelegate(this));
        }};
    }
    public static void mock(Object partiallyMocked1,
                            Object partiallyMocked2, final XtendExpectations e) {
        new Expectations(partiallyMocked1, partiallyMocked2) {{
            e.apply(new ExpectationsDelegate(this));
        }};
    }
    public static void mock(Object partiallyMocked1,
                            Object partiallyMocked2,
                            Object partiallyMocked3, final XtendExpectations e) {
        new Expectations(partiallyMocked1, partiallyMocked2, partiallyMocked3) {{
            e.apply(new ExpectationsDelegate(this));
        }};
    }
    public static void mock(Object partiallyMocked1,
                            Object partiallyMocked2,
                            Object partiallyMocked3,
                            Object partiallyMocked4, final XtendExpectations e) {
        new Expectations(partiallyMocked1, partiallyMocked2, partiallyMocked3, partiallyMocked4) {{
            e.apply(new ExpectationsDelegate(this));
        }};
    }
    public static void mock(Object partiallyMocked1,
                            Object partiallyMocked2,
                            Object partiallyMocked3,
                            Object partiallyMocked4,
                            Object partiallyMocked5, final XtendExpectations e) {
        new Expectations(partiallyMocked1, partiallyMocked2, partiallyMocked3, partiallyMocked4, partiallyMocked5) {{
            e.apply(new ExpectationsDelegate(this));
        }};
    }
    public static void mock(final XtendExpectations e, Object ... partiallyMockeds) {
    	new Expectations(partiallyMockeds) {{
    		e.apply(new ExpectationsDelegate(this));
    	}};
    }

    public static void mock(Integer numberOfIterations, final XtendExpectations e) {
        new Expectations(numberOfIterations) {{
            e.apply(new ExpectationsDelegate(this));
        }};
    }
    public static void mock(Integer numberOfIterations,
    						Object partiallyMocked1, final XtendExpectations e) {
    	new Expectations(numberOfIterations, partiallyMocked1) {{
    		e.apply(new ExpectationsDelegate(this));
    	}};
    }
    public static void mock(Integer numberOfIterations,
    						Object partiallyMocked1,
    						Object partiallyMocked2, final XtendExpectations e) {
    	new Expectations(numberOfIterations, partiallyMocked1, partiallyMocked2) {{
    		e.apply(new ExpectationsDelegate(this));
    	}};
    }
    public static void mock(Integer numberOfIterations,
    		Object partiallyMocked1,
    		Object partiallyMocked2,
    		Object partiallyMocked3, final XtendExpectations e) {
    	new Expectations(numberOfIterations, partiallyMocked1, partiallyMocked2, partiallyMocked3) {{
    		e.apply(new ExpectationsDelegate(this));
    	}};
    }
    public static void mock(Integer numberOfIterations,
    		Object partiallyMocked1,
    		Object partiallyMocked2,
    		Object partiallyMocked3,
    		Object partiallyMocked4, final XtendExpectations e) {
    	new Expectations(numberOfIterations, partiallyMocked1, partiallyMocked2, partiallyMocked3, partiallyMocked4) {{
    		e.apply(new ExpectationsDelegate(this));
    	}};
    }
    public static void mock(Integer numberOfIterations,
    		Object partiallyMocked1,
    		Object partiallyMocked2,
    		Object partiallyMocked3,
    		Object partiallyMocked4,
    		Object partiallyMocked5, final XtendExpectations e) {
    	new Expectations(numberOfIterations, partiallyMocked1, partiallyMocked2, partiallyMocked3, partiallyMocked4, partiallyMocked5) {{
    		e.apply(new ExpectationsDelegate(this));
    	}};
    }

    public static void mock(final XtendExpectations e, Integer numberOfIterations, Object ... partiallyMockeds) {
    	new Expectations(numberOfIterations, partiallyMockeds) {{
    		e.apply(new ExpectationsDelegate(this));
    	}};
    }




//    @SuppressWarnings("unchecked")
//	public static < T > T invoke(Expectations expectations, Object objectWithMethod, String methodName,
//                                 Object... methodArgs) {
//        return (T) MethodReflection.invoke(objectWithMethod.getClass(), objectWithMethod, methodName, methodArgs);
//    }
//
//    /**
//     * Specifies an expectation for a {@code static} method, with a given list of arguments.
//     * <p/>
//     * This is useful when a method is not accessible from the test (it's {@code private}, for example), and therefore
//     * cannot be called normally. It should not be used to call accessible methods.
//     * <p/>
//     * Additionally, this can also be used to directly test private methods, when there is no other way to do so, or it
//     * would be too difficult by indirect means. Note that in such a case the target class would not be mocked.
//     *
//     * @param methodOwner the class on which the invocation is to be done; must not be null
//     * @param methodName the name of the expected static method
//     * @param methodArgs zero or more non-null expected parameter values for the expectation;
//     *            if a null value needs to be passed, the {@code Class} object for the parameter type must be passed
//     *            instead
//     * @return the return value from the invoked method, wrapped if primitive
//     * @throws IllegalArgumentException if a null reference was provided for a parameter
//     */
//    // TODO Test
//    @SuppressWarnings("unchecked")
//    public static < T > T invoke(Expectations expectations, Class< ? > methodOwner, String methodName,
//                                 Object... methodArgs) {
//        return (T) MethodReflection.invoke(methodOwner, null, methodName, methodArgs);
//    }
//
//    /**
//     * Specifies an expectation for a constructor of a given class.
//     * <p/>
//     * This is useful for invoking non-accessible constructors ({@code private} ones, for example) from the test, which
//     * otherwise could not be called normally. It should not be used for accessible constructors.
//     * <p/>
//     * <a href="http://jmockit.googlecode.com/svn/trunk/www/tutorial/BehaviorBasedTesting.html#deencapsulation">In the
//     * Tutorial</a>
//     *
//     * @param className the fully qualified name of the desired class
//     * @param parameterTypes the formal parameter types for the desired constructor, possibly empty
//     * @param initArgs the invocation arguments for the constructor, which must be consistent with the specified
//     *            parameter types
//     * @param <T> interface or super-class type to which the returned instance should be assignable
//     * @return a newly created instance of the specified class, initialized with the specified constructor and arguments
//     * @see #newInstance(String, Object...)
//     * @see #newInnerInstance(String, Object, Object...)
//     */
//    // TODO Test
//    @SuppressWarnings("unchecked")
//    public static < T > T newInstance(Expectations expectations, String className, Class< ? >[] parameterTypes,
//                                      Object... initArgs) {
//        return (T) ConstructorReflection.newInstance(className, parameterTypes, initArgs);
//    }
//
//    /**
//     * The same as {@link #newInstance(String, Class[], Object...)}, but inferring parameter types from non-null
//     * argument
//     * values.
//     * If a given parameter needs to match {@code null} during replay, then the corresponding {@code Class} literal must
//     * be passed instead of {@code null}.
//     *
//     * @param nonNullInitArgs zero or more non-null expected parameter values for the expectation;
//     *            if a null value needs to be passed, the {@code Class} object for the parameter type must be passed
//     *            instead
//     * @throws IllegalArgumentException if one of the given arguments is {@code null}
//     */
//    // TODO Test
//    @SuppressWarnings("unchecked")
//    public static < T > T newInstance(Expectations expectations, String className, Object... nonNullInitArgs) {
//        return (T) ConstructorReflection.newInstance(className, nonNullInitArgs);
//    }
//
//    /**
//     * The same as {@link #newInstance(String, Class[], Object...)}, but for instantiating an inner non-accessible class
//     * of some other class, and where all other (if any) initialization arguments are known to be non null.
//     *
//     * @param innerClassSimpleName simple name of the inner class, that is, the part after the "$" character in its full
//     *            name
//     * @param outerClassInstance the outer class instance to which the inner class instance will belong
//     * @param nonNullInitArgs zero or more non-null expected parameter values for the expectation;
//     *            if a null value needs to be passed, the {@code Class} object for the parameter type must be passed
//     *            instead
//     */
//    // TODO Test
//    @SuppressWarnings("unchecked")
//    public static < T > T newInnerInstance(Expectations expectations, String innerClassSimpleName,
//                                           Object outerClassInstance, Object... nonNullInitArgs) {
//        return (T) ConstructorReflection.newInnerInstance(innerClassSimpleName, outerClassInstance, nonNullInitArgs);
//    }
}
