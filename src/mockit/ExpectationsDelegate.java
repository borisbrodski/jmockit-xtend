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

package mockit;

import java.util.HashMap;

import mockit.internal.expectations.argumentMatching.LenientEqualityMatcher;
import mockit.internal.expectations.argumentMatching.NullityMatcher;
import mockit.internal.expectations.transformation.ActiveInvocations;

import org.eclipse.xtext.xbase.lib.Functions.Function0;
import org.eclipse.xtext.xbase.lib.Functions.Function1;
import org.eclipse.xtext.xbase.lib.Functions.Function2;
import org.eclipse.xtext.xbase.lib.Functions.Function3;
import org.eclipse.xtext.xbase.lib.Functions.Function4;
import org.eclipse.xtext.xbase.lib.Functions.Function5;
import org.eclipse.xtext.xbase.lib.Functions.Function6;


public final class ExpectationsDelegate {
    private Expectations expectations;

    public ExpectationsDelegate(Expectations expectations) {
        this.expectations = expectations;
    }

    @SuppressWarnings({"unused", "unchecked"})
    public void setResult(final Object object) {
      	if (object instanceof Function0<?>) {
      		ActiveInvocations.addResult(new Delegate<Object>() {
				Object method() {
					return ((Function0<?>) object).apply();
              	}
      		});
      		return;
      	}
      	if (object instanceof Function1) {
      		ActiveInvocations.addResult(new Delegate<Object>() {
      			Object method(Object p1) {
      				return ((Function1<Object, ?>) object).apply(p1);
      			}
      		});
      		return;
      	}
      	if (object instanceof Function2) {
      		ActiveInvocations.addResult(new Delegate<Object>() {
      			Object method(Object p1, Object p2) {
      				return ((Function2<Object, Object, ?>) object).apply(p1, p2);
      			}
      		});
      		return;
      	}
      	if (object instanceof Function3) {
      		ActiveInvocations.addResult(new Delegate<Object>() {
      			Object method(Object p1, Object p2, Object p3) {
      				return ((Function3<Object, Object, Object, ?>) object).apply(p1, p2, p3);
      			}
      		});
      		return;
      	}
      	if (object instanceof Function4) {
      		ActiveInvocations.addResult(new Delegate<Object>() {
      			Object method(Object p1, Object p2, Object p3, Object p4) {
      				return ((Function4<Object, Object, Object, Object, ?>) object).apply(p1, p2, p3, p4);
      			}
      		});
      		return;
      	}
      	if (object instanceof Function5) {
      		ActiveInvocations.addResult(new Delegate<Object>() {
      			Object method(Object p1, Object p2, Object p3, Object p4, Object p5) {
      				return ((Function5<Object, Object, Object, Object, Object, ?>) object).apply(p1, p2, p3, p4, p5);
      			}
      		});
      		return;
      	}
      	if (object instanceof Function6) {
      		ActiveInvocations.addResult(new Delegate<Object>() {
      			Object method(Object p1, Object p2, Object p3, Object p4, Object p5, Object p6) {
      				return ((Function6<Object, Object, Object, Object, Object, Object, ?>) object).apply(p1, p2, p3, p4, p5, p6);
      			}
      		});
      		return;
      	}
    	ActiveInvocations.addResult(object);
    }
    public void setResultInt(int intValue) {
        setResult(intValue);
    }
    public void setResultLong(long longValue) {
        setResult(longValue);
    }
    public void setResultShort(short shortValue) {
        setResult(shortValue);
    }
    public void setResultByte(byte byteValue) {
        setResult(byteValue);
    }
    public void setResultFloat(float floatValue) {
        setResult(floatValue);
    }
    public void setResultDouble(double doubleValue) {
        setResult(doubleValue);
    }
    public void setResultBoolean(boolean booleanValue) {
        setResult(booleanValue);
    }
    public void setResultChar(char charValue) {
        setResult(charValue);
    }

    public void returns(Object firstValue, Object... remainingValues) {
        expectations.returns(firstValue, remainingValues);
    }
    public void returnsInt(int firstValue, int... remainingValues) {
        expectations.returns(firstValue, toObjectArray(remainingValues));
    }
    public void returnsLong(long firstValue, long... remainingValues) {
        expectations.returns(firstValue, toObjectArray(remainingValues));
    }
    public void returnsShort(short firstValue, short... remainingValues) {
        expectations.returns(firstValue, toObjectArray(remainingValues));
    }
    public void returnsByte(byte firstValue, byte... remainingValues) {
        expectations.returns(firstValue, toObjectArray(remainingValues));
    }
    public void returnsFloat(float firstValue, float... remainingValues) {
        expectations.returns(firstValue, toObjectArray(remainingValues));
    }
    public void returnsDouble(double firstValue, double... remainingValues) {
        expectations.returns(firstValue, toObjectArray(remainingValues));
    }
    public void returnsBoolean(boolean firstValue, boolean... remainingValues) {
        expectations.returns(firstValue, toObjectArray(remainingValues));
    }
    public void returnsChar(char firstValue, char... remainingValues) {
        expectations.returns(firstValue, toObjectArray(remainingValues));
    }

    public void setMaxTimes(int value) {
        ActiveInvocations.maxTimes(value);
    }

    public void setMinTimes(int value) {
        ActiveInvocations.minTimes(value);
    }

    public void setTimes(int value) {
        ActiveInvocations.times(value);
    }

    public <T> T any() {
        ActiveInvocations.addArgMatcher();
        return null;
    }
    public int anyInt() {
        ActiveInvocations.addArgMatcher();
        return 0;
    }
    public long anyLong() {
        ActiveInvocations.addArgMatcher();
        return 0;
    }
    public short anyShort() {
        ActiveInvocations.addArgMatcher();
        return 0;
    }
    public byte anyByte() {
        ActiveInvocations.addArgMatcher();
        return 0;
    }
    public float anyFloat() {
        ActiveInvocations.addArgMatcher();
        return 0;
    }
    public double anyDouble() {
        ActiveInvocations.addArgMatcher();
        return 0;
    }
    public boolean anyBoolean() {
        ActiveInvocations.addArgMatcher();
        return false;
    }
    public char anyChar() {
        ActiveInvocations.addArgMatcher();
        return 'c';
    }

    public <T> T with(T value) {
        return with(value, value);
    }
    public <T> T with(final Function1<T, Boolean> lambdaMatcher) throws Exception {
        if (lambdaMatcher == null) {
            expectations.getCurrentPhase().addArgMatcher(NullityMatcher.INSTANCE);
            return null;
        }
        return expectations.with(new Delegate<T>() {
                    @SuppressWarnings("unused")
                    public boolean match(T t) {
                        return lambdaMatcher.apply(t);
                    }
                });
    }
    public int withInt(int argumentMatcher) {
        with(argumentMatcher);
        return 0;
    }
    public int withInt(final Function1<Integer, Boolean> lambdaMatcher) throws Exception {
        expectations.with(new Delegate<Integer>() {
                    @SuppressWarnings("unused")
                    public boolean match(Integer i) {
                        return lambdaMatcher.apply(i);
                    }
                });
        return 0;
    }
    public long withLong(long argumentMatcher) {
        with(argumentMatcher);
        return 0;
    }
    public long withLong(final Function1<Long, Boolean> lambdaMatcher) throws Exception {
        expectations.with(new Delegate<Long>() {
                    @SuppressWarnings("unused")
                    public boolean match(Long i) {
                        return lambdaMatcher.apply(i);
                    }
                });
        return 0;
    }
    public short withShort(short argumentMatcher) {
        with(argumentMatcher);
        return 0;
    }
    public short withShort(final Function1<Short, Boolean> lambdaMatcher) throws Exception {
        expectations.with(new Delegate<Short>() {
                    @SuppressWarnings("unused")
                    public boolean match(Short i) {
                        return lambdaMatcher.apply(i);
                    }
                });
        return 0;
    }
    public byte withByte(byte argumentMatcher) {
        with(argumentMatcher);
        return 0;
    }
    public byte withByte(final Function1<Byte, Boolean> lambdaMatcher) throws Exception {
        expectations.with(new Delegate<Byte>() {
                    @SuppressWarnings("unused")
                    public boolean match(Byte i) {
                        return lambdaMatcher.apply(i);
                    }
                });
        return 0;
    }
    public float withFloat(float argumentMatcher) {
        with(argumentMatcher);
        return 0;
    }
    public float withFloat(final Function1<Float, Boolean> lambdaMatcher) throws Exception {
        expectations.with(new Delegate<Float>() {
                    @SuppressWarnings("unused")
                    public boolean match(Float i) {
                        return lambdaMatcher.apply(i);
                    }
                });
        return 0;
    }
    public double withDouble(double argumentMatcher) {
        with(argumentMatcher);
        return 0;
    }
    public double withDouble(final Function1<Double, Boolean> lambdaMatcher) throws Exception {
        expectations.with(new Delegate<Double>() {
                    @SuppressWarnings("unused")
                    public boolean match(Double i) {
                        return lambdaMatcher.apply(i);
                    }
                });
        return 0;
    }
    public boolean withBoolean(boolean argumentMatcher) {
        with(argumentMatcher);
        return false;
    }
    public boolean withBoolean(final Function1<Boolean, Boolean> lambdaMatcher) throws Exception {
        expectations.with(new Delegate<Boolean>() {
                    @SuppressWarnings("unused")
                    public boolean match(Boolean i) {
                        return lambdaMatcher.apply(i);
                    }
                });
        return false;
    }
    public char withChar(char argumentMatcher) {
        with(argumentMatcher);
        return 'c';
    }
    public char withChar(final Function1<Character, Boolean> lambdaMatcher) throws Exception {
        expectations.with(new Delegate<Character>() {
                    @SuppressWarnings("unused")
                    public boolean match(Character i) {
                        return lambdaMatcher.apply(i);
                    }
                });
        return 'c';
    }

    public <T> T with(T argValue, Object value) {
        expectations.getCurrentPhase().addArgMatcher(new LenientEqualityMatcher(value, new HashMap<Object, Object>()));
        return argValue;
    }

    public <T> T withDelegate(Delegate<T> delegateObjectWithInvocationHandlerMethod) {
        return expectations.with(delegateObjectWithInvocationHandlerMethod);
    }

    public <T> T withDelegate(T arg, Delegate<T> delegateObjectWithInvocationHandlerMethod) {
    	expectations.with(delegateObjectWithInvocationHandlerMethod);
    	return arg;
    }

    public <T> T withAny(T t) {
        return expectations.withAny(t);
    }

    public <T> T withEqual(T value) {
    	return expectations.withEqual(value);
    }

    public float withEqual(float value, double delta) {
    	return expectations.withEqual(value, delta);
    }

    public double withEqual(double value, double delta) {
    	return expectations.withEqual(value, delta);
    }

    public <T> T withInstanceLike(T value) {
    	return expectations.withInstanceLike(value);
    }

    public <T> T withInstanceOf(Class<T> value) {
    	return expectations.withInstanceOf(value);
    }

    public <T extends CharSequence> T withMatch(T regex) {
    	return expectations.withMatch(regex);
    }

    public <T> T withNotEqual(T value) {
    	return expectations.withNotEqual(value);
    }

    public <T> T withNotNull() {
    	return expectations.withNotNull();
    }

    public <T> T withNull() {
    	return expectations.withNull();
    }

    public <T extends CharSequence> T withPrefix(T value) {
    	return expectations.withPrefix(value);
    }

    public <T> T withSameInstance(T value) {
    	return expectations.withSameInstance(value);
    }

    public <T extends CharSequence> T withSubstring(T value) {
    	return expectations.withSubstring(value);
    }

    public <T extends CharSequence> T withSuffix(T value) {
    	return expectations.withSuffix(value);
    }

    public <T> T onInstance(T mockedInstance) {
    	return expectations.onInstance(mockedInstance);
    }

    private Object[] toObjectArray(int[] array) {
        Object[] objects = new Object[array.length];
        for (int i = 0; i < objects.length; i++) {
            objects[i] = array[i];
        }
        return objects;
    }
    private Object[] toObjectArray(long[] array) {
        Object[] objects = new Object[array.length];
        for (int i = 0; i < objects.length; i++) {
            objects[i] = array[i];
        }
        return objects;
    }
    private Object[] toObjectArray(short[] array) {
        Object[] objects = new Object[array.length];
        for (int i = 0; i < objects.length; i++) {
            objects[i] = array[i];
        }
        return objects;
    }
    private Object[] toObjectArray(byte[] array) {
        Object[] objects = new Object[array.length];
        for (int i = 0; i < objects.length; i++) {
            objects[i] = array[i];
        }
        return objects;
    }
    private Object[] toObjectArray(float[] array) {
        Object[] objects = new Object[array.length];
        for (int i = 0; i < objects.length; i++) {
            objects[i] = array[i];
        }
        return objects;
    }
    private Object[] toObjectArray(double[] array) {
        Object[] objects = new Object[array.length];
        for (int i = 0; i < objects.length; i++) {
            objects[i] = array[i];
        }
        return objects;
    }
    private Object[] toObjectArray(boolean[] array) {
        Object[] objects = new Object[array.length];
        for (int i = 0; i < objects.length; i++) {
            objects[i] = array[i];
        }
        return objects;
    }
    private Object[] toObjectArray(char[] array) {
        Object[] objects = new Object[array.length];
        for (int i = 0; i < objects.length; i++) {
            objects[i] = array[i];
        }
        return objects;
    }
}
