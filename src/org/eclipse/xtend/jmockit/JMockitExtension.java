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
    public static void stub(Class<?> ... partiallyMockedClasses) {
        new NonStrictExpectations((Object[])partiallyMockedClasses) {{
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
    public static void mock(Class<?> ... partiallyMockedClasses) {
        new Expectations((Object[])partiallyMockedClasses) {{
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

}
