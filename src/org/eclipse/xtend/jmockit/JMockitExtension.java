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
import mockit.internal.util.ConstructorReflection;

public class JMockitExtension {
    public static abstract class XtendNonStrictExpectations extends NonStrictExpectations {
        public abstract void apply(ExpectationsDelegate delegate);
    }
    public static abstract class XtendNonStrictExpectations1<T1> extends NonStrictExpectations {
        public abstract void apply(ExpectationsDelegate delegate, T1 i1);
    }
    public static abstract class XtendNonStrictExpectations2<T1, T2> extends NonStrictExpectations {
    	public abstract void apply(ExpectationsDelegate delegate, T1 i1, T2 i2);
    }
    public static abstract class XtendNonStrictExpectations3<T1, T2, T3> extends NonStrictExpectations {
    	public abstract void apply(ExpectationsDelegate delegate, T1 i1, T2 i2, T3 i3);
    }
    public static abstract class XtendNonStrictExpectations4<T1, T2, T3, T4> extends NonStrictExpectations {
    	public abstract void apply(ExpectationsDelegate delegate, T1 i1, T2 i2, T3 i3, T4 i4);
    }
    public static abstract class XtendNonStrictExpectations5<T1, T2, T3, T4, T5> extends NonStrictExpectations {
    	public abstract void apply(ExpectationsDelegate delegate, T1 i1, T2 i2, T3 i3, T4 i4, T5 i5);
    }

    public static abstract class XtendExpectations extends Expectations {
        public abstract void apply(ExpectationsDelegate delegate);
    }
    public static abstract class XtendExpectations1<T1> extends Expectations {
        public abstract void apply(ExpectationsDelegate delegate, T1 i1);
    }
    public static abstract class XtendExpectations2<T1, T2> extends Expectations {
    	public abstract void apply(ExpectationsDelegate delegate, T1 i1, T2 i2);
    }
    public static abstract class XtendExpectations3<T1, T2, T3> extends Expectations {
    	public abstract void apply(ExpectationsDelegate delegate, T1 i1, T2 i2, T3 i3);
    }
    public static abstract class XtendExpectations4<T1, T2, T3, T4> extends Expectations {
    	public abstract void apply(ExpectationsDelegate delegate, T1 i1, T2 i2, T3 i3, T4 i4);
    }
    public static abstract class XtendExpectations5<T1, T2, T3, T4, T5> extends Expectations {
    	public abstract void apply(ExpectationsDelegate delegate, T1 i1, T2 i2, T3 i3, T4 i4, T5 i5);
    }

    public static void stub(final XtendNonStrictExpectations e) {
        new NonStrictExpectations() {{
            e.apply(new ExpectationsDelegate(this));
        }};
    }
    public static <T> T stub(Class<T> singleClass) {
    	new NonStrictExpectations(singleClass) {{
    	}};
    	return ins(singleClass);
    }
    public static void stub(Class<?> ... partiallyMockedClasses) {
        new NonStrictExpectations((Object[])partiallyMockedClasses) {{
        }};
    }
    public static void stub(int iterations, final XtendNonStrictExpectations e) {
        new NonStrictExpectations(iterations) {{
            e.apply(new ExpectationsDelegate(this));
        }};
    }
    public static <T1> void stub(final Class<T1> partiallyMockedClass1, final XtendNonStrictExpectations1<T1> e) {
        new NonStrictExpectations(partiallyMockedClass1) {{
            e.apply(new ExpectationsDelegate(this), ins(partiallyMockedClass1));
        }};
    }
    public static void stub(Object partiallyMocked1, final XtendNonStrictExpectations e) {
        new NonStrictExpectations(partiallyMocked1) {{
            e.apply(new ExpectationsDelegate(this));
        }};
    }
    public static <T1> void stub(int iterations, final Class<T1> partiallyMockedClass1, final XtendNonStrictExpectations1<T1> e) {
    	new NonStrictExpectations(iterations, partiallyMockedClass1) {{
    		e.apply(new ExpectationsDelegate(this), ins(partiallyMockedClass1));
    	}};
    }
    public static void stub(int iterations, Object partiallyMocked1, final XtendNonStrictExpectations e) {
        new NonStrictExpectations(iterations, partiallyMocked1) {{
            e.apply(new ExpectationsDelegate(this));
        }};
    }
    public static <T1, T2>
    	void stub(final Class<T1> partiallyMocked1,
    			  final Class<T2> partiallyMocked2, final XtendNonStrictExpectations2<T1, T2> e) {
    	new NonStrictExpectations(partiallyMocked1, partiallyMocked2) {{
    		e.apply(new ExpectationsDelegate(this), ins(partiallyMocked1), ins(partiallyMocked2));
    	}};
    }
    public static void stub(Object partiallyMocked1,
    						Object partiallyMocked2, final XtendNonStrictExpectations e) {
    	new NonStrictExpectations(partiallyMocked1, partiallyMocked2) {{
    		e.apply(new ExpectationsDelegate(this));
    	}};
    }
    public static <T1, T2>
	    void stub(int iterations,
	    		  final Class<T1> partiallyMocked1,
				  final Class<T2> partiallyMocked2, final XtendNonStrictExpectations2<T1, T2> e) {
		new NonStrictExpectations(iterations, partiallyMocked1, partiallyMocked2) {{
			e.apply(new ExpectationsDelegate(this), ins(partiallyMocked1), ins(partiallyMocked2));
		}};
	}
    public static void stub(int iterations,
				            Object partiallyMocked1,
				            Object partiallyMocked2, final XtendNonStrictExpectations e) {
		new NonStrictExpectations(iterations, partiallyMocked1, partiallyMocked2) {{
			e.apply(new ExpectationsDelegate(this));
		}};
	}
    public static <T1, T2, T3>
    	void stub(final Class<T1> partiallyMocked1,
    			  final Class<T2> partiallyMocked2,
    			  final Class<T3> partiallyMocked3, final XtendNonStrictExpectations3<T1, T2, T3> e) {
    	new NonStrictExpectations(partiallyMocked1, partiallyMocked2, partiallyMocked3) {{
    		e.apply(new ExpectationsDelegate(this), ins(partiallyMocked1), ins(partiallyMocked2), ins(partiallyMocked3));
    	}};
    }
    public static void stub(Object partiallyMocked1,
    						Object partiallyMocked2,
    						Object partiallyMocked3, final XtendNonStrictExpectations e) {
    	new NonStrictExpectations(partiallyMocked1, partiallyMocked2, partiallyMocked3) {{
    		e.apply(new ExpectationsDelegate(this));
    	}};
    }
    public static <T1, T2, T3>
		void stub(int iterations,
				  final Class<T1> partiallyMocked1,
				  final Class<T2> partiallyMocked2,
				  final Class<T3> partiallyMocked3, final XtendNonStrictExpectations3<T1, T2, T3> e) {
		new NonStrictExpectations(iterations, partiallyMocked1, partiallyMocked2, partiallyMocked3) {{
			e.apply(new ExpectationsDelegate(this), ins(partiallyMocked1), ins(partiallyMocked2), ins(partiallyMocked3));
		}};
	}
    public static void stub(int iterations,
				            Object partiallyMocked1,
				            Object partiallyMocked2,
				            Object partiallyMocked3, final XtendNonStrictExpectations e) {
        new NonStrictExpectations(iterations, partiallyMocked1, partiallyMocked2, partiallyMocked3) {{
            e.apply(new ExpectationsDelegate(this));
        }};
    }
    public static <T1, T2, T3, T4>
		void stub(final Class<T1> partiallyMocked1,
				  final Class<T2> partiallyMocked2,
				  final Class<T3> partiallyMocked3,
				  final Class<T4> partiallyMocked4, final XtendNonStrictExpectations4<T1, T2, T3, T4> e) {
		new NonStrictExpectations(partiallyMocked1, partiallyMocked2, partiallyMocked3, partiallyMocked4) {{
			e.apply(new ExpectationsDelegate(this), ins(partiallyMocked1), ins(partiallyMocked2), ins(partiallyMocked3), ins(partiallyMocked4));
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
    public static <T1, T2, T3, T4>
		void stub(int iterations,
				  final Class<T1> partiallyMocked1,
				  final Class<T2> partiallyMocked2,
				  final Class<T3> partiallyMocked3,
				  final Class<T4> partiallyMocked4, final XtendNonStrictExpectations4<T1, T2, T3, T4> e) {
		new NonStrictExpectations(iterations, partiallyMocked1, partiallyMocked2, partiallyMocked3, partiallyMocked4) {{
			e.apply(new ExpectationsDelegate(this), ins(partiallyMocked1), ins(partiallyMocked2), ins(partiallyMocked3), ins(partiallyMocked4));
		}};
	}
    public static void stub(int iterations,
				            Object partiallyMocked1,
				            Object partiallyMocked2,
				            Object partiallyMocked3,
				            Object partiallyMocked4, final XtendNonStrictExpectations e) {
        new NonStrictExpectations(iterations, partiallyMocked1, partiallyMocked2, partiallyMocked3, partiallyMocked4) {{
            e.apply(new ExpectationsDelegate(this));
        }};
    }

    public static <T1, T2, T3, T4, T5>
		void stub(final Class<T1> partiallyMocked1,
				  final Class<T2> partiallyMocked2,
				  final Class<T3> partiallyMocked3,
				  final Class<T4> partiallyMocked4,
				  final Class<T5> partiallyMocked5, final XtendNonStrictExpectations5<T1, T2, T3, T4, T5> e) {
		new NonStrictExpectations(partiallyMocked1, partiallyMocked2, partiallyMocked3, partiallyMocked4, partiallyMocked5) {{
			e.apply(new ExpectationsDelegate(this), ins(partiallyMocked1), ins(partiallyMocked2), ins(partiallyMocked3), ins(partiallyMocked4), ins(partiallyMocked5));
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

    public static <T1, T2, T3, T4, T5>
		void stub(int iterations,
				  final Class<T1> partiallyMocked1,
				  final Class<T2> partiallyMocked2,
				  final Class<T3> partiallyMocked3,
				  final Class<T4> partiallyMocked4,
				  final Class<T5> partiallyMocked5, final XtendNonStrictExpectations5<T1, T2, T3, T4, T5> e) {
		new NonStrictExpectations(iterations, partiallyMocked1, partiallyMocked2, partiallyMocked3, partiallyMocked4, partiallyMocked5) {{
			e.apply(new ExpectationsDelegate(this), ins(partiallyMocked1), ins(partiallyMocked2), ins(partiallyMocked3), ins(partiallyMocked4), ins(partiallyMocked5));
		}};
	}

    public static void stub(int iterations,
    		Object partiallyMocked1,
    		Object partiallyMocked2,
    		Object partiallyMocked3,
    		Object partiallyMocked4,
    		Object partiallyMocked5, final XtendNonStrictExpectations e) {
    	new NonStrictExpectations(iterations, partiallyMocked1, partiallyMocked2, partiallyMocked3, partiallyMocked4, partiallyMocked5) {{
    		e.apply(new ExpectationsDelegate(this));
    	}};
    }

    public static void stub(final XtendNonStrictExpectations e, Object ... partiallyMockeds) {
    	new NonStrictExpectations(partiallyMockeds) {{
    		e.apply(new ExpectationsDelegate(this));
    	}};
    }

    public static void stub(int iterations, final XtendNonStrictExpectations e, Object ... partiallyMockeds) {
        new NonStrictExpectations(iterations, partiallyMockeds) {{
            e.apply(new ExpectationsDelegate(this));
        }};
    }


    public static void mock(final XtendExpectations e) {
        new Expectations() {{
            e.apply(new ExpectationsDelegate(this));
        }};
    }
    public static <T> T mock(Class<T> singleClass) {
    	new NonStrictExpectations(singleClass) {{
    	}};
    	return ins(singleClass);
    }
    public static void mock(Class<?> ... partiallyMockedClasses) {
        new Expectations((Object[])partiallyMockedClasses) {{
        }};
    }
    public static void mock(int iterations, final XtendExpectations e) {
        new Expectations(iterations) {{
            e.apply(new ExpectationsDelegate(this));
        }};
    }
    public static <T1> void mock(final Class<T1> partiallyMockedClass1, final XtendExpectations1<T1> e) {
        new Expectations(partiallyMockedClass1) {{
            e.apply(new ExpectationsDelegate(this), ins(partiallyMockedClass1));
        }};
    }
    public static void mock(Object partiallyMocked1, final XtendExpectations e) {
        new Expectations(partiallyMocked1) {{
            e.apply(new ExpectationsDelegate(this));
        }};
    }
    public static <T1> void mock(int iterations, final Class<T1> partiallyMockedClass1, final XtendExpectations1<T1> e) {
    	new Expectations(iterations, partiallyMockedClass1) {{
    		e.apply(new ExpectationsDelegate(this), ins(partiallyMockedClass1));
    	}};
    }
    public static void mock(int iterations, Object partiallyMocked1, final XtendExpectations e) {
        new Expectations(iterations, partiallyMocked1) {{
            e.apply(new ExpectationsDelegate(this));
        }};
    }
    public static <T1, T2>
    	void mock(final Class<T1> partiallyMocked1,
    			  final Class<T2> partiallyMocked2, final XtendExpectations2<T1, T2> e) {
    	new Expectations(partiallyMocked1, partiallyMocked2) {{
    		e.apply(new ExpectationsDelegate(this), ins(partiallyMocked1), ins(partiallyMocked2));
    	}};
    }
    public static void mock(Object partiallyMocked1,
    						Object partiallyMocked2, final XtendExpectations e) {
    	new Expectations(partiallyMocked1, partiallyMocked2) {{
    		e.apply(new ExpectationsDelegate(this));
    	}};
    }
    public static <T1, T2>
	    void mock(int iterations,
	    		  final Class<T1> partiallyMocked1,
				  final Class<T2> partiallyMocked2, final XtendExpectations2<T1, T2> e) {
		new Expectations(iterations, partiallyMocked1, partiallyMocked2) {{
			e.apply(new ExpectationsDelegate(this), ins(partiallyMocked1), ins(partiallyMocked2));
		}};
	}
    public static void mock(int iterations,
				            Object partiallyMocked1,
				            Object partiallyMocked2, final XtendExpectations e) {
		new Expectations(iterations, partiallyMocked1, partiallyMocked2) {{
			e.apply(new ExpectationsDelegate(this));
		}};
	}
    public static <T1, T2, T3>
    	void mock(final Class<T1> partiallyMocked1,
    			  final Class<T2> partiallyMocked2,
    			  final Class<T3> partiallyMocked3, final XtendExpectations3<T1, T2, T3> e) {
    	new Expectations(partiallyMocked1, partiallyMocked2, partiallyMocked3) {{
    		e.apply(new ExpectationsDelegate(this), ins(partiallyMocked1), ins(partiallyMocked2), ins(partiallyMocked3));
    	}};
    }
    public static void mock(Object partiallyMocked1,
    						Object partiallyMocked2,
    						Object partiallyMocked3, final XtendExpectations e) {
    	new Expectations(partiallyMocked1, partiallyMocked2, partiallyMocked3) {{
    		e.apply(new ExpectationsDelegate(this));
    	}};
    }
    public static <T1, T2, T3>
		void mock(int iterations,
				  final Class<T1> partiallyMocked1,
				  final Class<T2> partiallyMocked2,
				  final Class<T3> partiallyMocked3, final XtendExpectations3<T1, T2, T3> e) {
		new Expectations(iterations, partiallyMocked1, partiallyMocked2, partiallyMocked3) {{
			e.apply(new ExpectationsDelegate(this), ins(partiallyMocked1), ins(partiallyMocked2), ins(partiallyMocked3));
		}};
	}
    public static void mock(int iterations,
				            Object partiallyMocked1,
				            Object partiallyMocked2,
				            Object partiallyMocked3, final XtendExpectations e) {
        new Expectations(iterations, partiallyMocked1, partiallyMocked2, partiallyMocked3) {{
            e.apply(new ExpectationsDelegate(this));
        }};
    }
    public static <T1, T2, T3, T4>
		void mock(final Class<T1> partiallyMocked1,
				  final Class<T2> partiallyMocked2,
				  final Class<T3> partiallyMocked3,
				  final Class<T4> partiallyMocked4, final XtendExpectations4<T1, T2, T3, T4> e) {
		new Expectations(partiallyMocked1, partiallyMocked2, partiallyMocked3, partiallyMocked4) {{
			e.apply(new ExpectationsDelegate(this), ins(partiallyMocked1), ins(partiallyMocked2), ins(partiallyMocked3), ins(partiallyMocked4));
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
    public static <T1, T2, T3, T4>
		void mock(int iterations,
				  final Class<T1> partiallyMocked1,
				  final Class<T2> partiallyMocked2,
				  final Class<T3> partiallyMocked3,
				  final Class<T4> partiallyMocked4, final XtendExpectations4<T1, T2, T3, T4> e) {
		new Expectations(iterations, partiallyMocked1, partiallyMocked2, partiallyMocked3, partiallyMocked4) {{
			e.apply(new ExpectationsDelegate(this), ins(partiallyMocked1), ins(partiallyMocked2), ins(partiallyMocked3), ins(partiallyMocked4));
		}};
	}
    public static void mock(int iterations,
				            Object partiallyMocked1,
				            Object partiallyMocked2,
				            Object partiallyMocked3,
				            Object partiallyMocked4, final XtendExpectations e) {
        new Expectations(iterations, partiallyMocked1, partiallyMocked2, partiallyMocked3, partiallyMocked4) {{
            e.apply(new ExpectationsDelegate(this));
        }};
    }

    public static <T1, T2, T3, T4, T5>
		void mock(final Class<T1> partiallyMocked1,
				  final Class<T2> partiallyMocked2,
				  final Class<T3> partiallyMocked3,
				  final Class<T4> partiallyMocked4,
				  final Class<T5> partiallyMocked5, final XtendExpectations5<T1, T2, T3, T4, T5> e) {
		new Expectations(partiallyMocked1, partiallyMocked2, partiallyMocked3, partiallyMocked4, partiallyMocked5) {{
			e.apply(new ExpectationsDelegate(this), ins(partiallyMocked1), ins(partiallyMocked2), ins(partiallyMocked3), ins(partiallyMocked4), ins(partiallyMocked5));
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

    public static <T1, T2, T3, T4, T5>
		void mock(int iterations,
				  final Class<T1> partiallyMocked1,
				  final Class<T2> partiallyMocked2,
				  final Class<T3> partiallyMocked3,
				  final Class<T4> partiallyMocked4,
				  final Class<T5> partiallyMocked5, final XtendExpectations5<T1, T2, T3, T4, T5> e) {
		new Expectations(iterations, partiallyMocked1, partiallyMocked2, partiallyMocked3, partiallyMocked4, partiallyMocked5) {{
			e.apply(new ExpectationsDelegate(this), ins(partiallyMocked1), ins(partiallyMocked2), ins(partiallyMocked3), ins(partiallyMocked4), ins(partiallyMocked5));
		}};
	}

    public static void mock(int iterations,
    		Object partiallyMocked1,
    		Object partiallyMocked2,
    		Object partiallyMocked3,
    		Object partiallyMocked4,
    		Object partiallyMocked5, final XtendExpectations e) {
    	new Expectations(iterations, partiallyMocked1, partiallyMocked2, partiallyMocked3, partiallyMocked4, partiallyMocked5) {{
    		e.apply(new ExpectationsDelegate(this));
    	}};
    }

    public static void mock(final XtendExpectations e, Object ... partiallyMockeds) {
    	new Expectations(partiallyMockeds) {{
    		e.apply(new ExpectationsDelegate(this));
    	}};
    }

    public static void mock(int iterations, final XtendExpectations e, Object ... partiallyMockeds) {
        new Expectations(iterations, partiallyMockeds) {{
            e.apply(new ExpectationsDelegate(this));
        }};
    }




    public static <T> T ins(Class<T> clazz) {
    	return ConstructorReflection.newUninitializedInstance(clazz);
    }
}
