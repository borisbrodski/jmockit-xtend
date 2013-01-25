package org.eclipse.xtend.jmockit;

import java.lang.reflect.Method;
import java.util.regex.Pattern;

import mockit.Delegate;
import mockit.Expectations;
import mockit.NonStrictExpectations;
import mockit.internal.expectations.RecordPhase;
import mockit.internal.expectations.argumentMatching.AlwaysTrueMatcher;
import mockit.internal.expectations.argumentMatching.ArgumentMatcher;
import mockit.internal.expectations.argumentMatching.ClassMatcher;
import mockit.internal.expectations.argumentMatching.EqualityMatcher;
import mockit.internal.expectations.argumentMatching.HamcrestAdapter;
import mockit.internal.expectations.argumentMatching.InequalityMatcher;
import mockit.internal.expectations.argumentMatching.NonNullityMatcher;
import mockit.internal.expectations.argumentMatching.NullityMatcher;
import mockit.internal.expectations.argumentMatching.NumericEqualityMatcher;
import mockit.internal.expectations.argumentMatching.PatternMatcher;
import mockit.internal.expectations.argumentMatching.SamenessMatcher;
import mockit.internal.expectations.argumentMatching.StringContainmentMatcher;
import mockit.internal.expectations.argumentMatching.StringPrefixMatcher;
import mockit.internal.expectations.argumentMatching.StringSuffixMatcher;
import mockit.internal.expectations.transformation.ActiveInvocations;
import mockit.internal.util.MethodReflection;

import org.eclipse.xtext.xbase.lib.Functions.Function0;
import org.eclipse.xtext.xbase.lib.Functions.Function1;
import org.eclipse.xtext.xbase.lib.Functions.Function2;
import org.eclipse.xtext.xbase.lib.Functions.Function3;
import org.eclipse.xtext.xbase.lib.Functions.Function4;
import org.eclipse.xtext.xbase.lib.Functions.Function5;
import org.eclipse.xtext.xbase.lib.Functions.Function6;
import org.eclipse.xtext.xbase.lib.Procedures.Procedure1;

public class JMockitExtension {
    public static void mock(final Procedure1< Expectations > proc) {
        new Expectations() {

            {
                proc.apply(this);
            }
        };
    }

    public static void mock(Class< ? > clazz, final Procedure1< Expectations > proc) {
        new Expectations(clazz) {

            {
                proc.apply(this);
            }
        };
    }

    public static void stub(final Procedure1< NonStrictExpectations > proc) {
    	new NonStrictExpectations() {

    		{
    			proc.apply(this);
    		}
    	};
    }

    public static void stub(Class< ? > clazz, final Procedure1< NonStrictExpectations > proc) {
        new NonStrictExpectations(clazz) {

            {
                proc.apply(this);
            }
        };
    }

//    public static <T, T1> void setResult(Expectations expectations, final Function1<T1, T> fnc) throws Exception {
//    	ActiveInvocations.addResult(new Delegate<T>() {
//    		T method(T1 p1) {
//    			return fnc.apply(p1);
//    		}
//    	});
//    }

    @SuppressWarnings({ "rawtypes", "unused", "unchecked" })
    public static void setResult(Expectations expectations, final Object result) throws Exception {
    	if (result instanceof Function0<?>) {
    		ActiveInvocations.addResult(new Delegate<Object>() {
				Object method() {
            		return ((Function0) result).apply();
            	}
    		});
    		return;
    	}
    	if (result instanceof Function1) {
    		ActiveInvocations.addResult(new Delegate<Object>() {
    			Object method(Object p1) {
    				return ((Function1) result).apply(p1);
    			}
    		});
    		return;
    	}
    	if (result instanceof Function2) {
    		ActiveInvocations.addResult(new Delegate<Object>() {
    			Object method(Object p1, Object p2) {
    				return ((Function2) result).apply(p1, p2);
    			}
    		});
    		return;
    	}
    	if (result instanceof Function3) {
    		ActiveInvocations.addResult(new Delegate<Object>() {
    			Object method(Object p1, Object p2, Object p3) {
    				return ((Function3) result).apply(p1, p2, p3);
    			}
    		});
    		return;
    	}
    	if (result instanceof Function4) {
    		ActiveInvocations.addResult(new Delegate<Object>() {
    			Object method(Object p1, Object p2, Object p3, Object p4) {
    				return ((Function4) result).apply(p1, p2, p3, p4);
    			}
    		});
    		return;
    	}
    	if (result instanceof Function5) {
    		ActiveInvocations.addResult(new Delegate<Object>() {
    			Object method(Object p1, Object p2, Object p3, Object p4, Object p5) {
    				return ((Function5) result).apply(p1, p2, p3, p4, p5);
    			}
    		});
    		return;
    	}
    	if (result instanceof Function6) {
    		ActiveInvocations.addResult(new Delegate<Object>() {
    			Object method(Object p1, Object p2, Object p3, Object p4, Object p5, Object p6) {
    				return ((Function6) result).apply(p1, p2, p3, p4, p5, p6);
    			}
    		});
    		return;
    	}
    	ActiveInvocations.addResult(result);
    }

    public static void setResultInt(Expectations expectations, int result) throws Exception {
    	setResult(expectations, result);
    }

    public static void setResultLong(Expectations expectations, long result) throws Exception {
    	setResult(expectations, result);
    }

    public static void setResultShort(Expectations expectations, short result) throws Exception {
    	setResult(expectations, result);
    }

    public static void setResultByte(Expectations expectations, byte result) throws Exception {
    	setResult(expectations, result);
    }

    public static void setResultFloat(Expectations expectations, float result) throws Exception {
    	setResult(expectations, result);
    }

    public static void setResultDouble(Expectations expectations, double result) throws Exception {
    	setResult(expectations, result);
    }

    public static void setResultBoolean(Expectations expectations, boolean result) throws Exception {
    	setResult(expectations, result);
    }

    public static void setResultChar(Expectations expectations, char result) throws Exception {
    	setResult(expectations, result);
    }

    public static void returns(Expectations expectations, Object result) throws Exception {
        Method method = Expectations.class.getDeclaredMethod("returns", Object.class);
        method.setAccessible(true);
        method.invoke(expectations, result);
    }

    public static void returns(Expectations expectations, Object result, Object ... results) throws Exception {
    	Method method = Expectations.class.getDeclaredMethod("returns", Object.class, Object[].class);
    	method.setAccessible(true);
    	method.invoke(expectations, result, results);
    }

    public static void returnsInt(Expectations expectations, int result) throws Exception {
    	Method method = Expectations.class.getDeclaredMethod("returns", Object.class);
    	method.setAccessible(true);
    	method.invoke(expectations, result);
    }

    public static void returnsInt(Expectations expectations, int result, int ... results) throws Exception {
    	returns(expectations, result, toObjectArray(results));
    }

	public static void returnsLong(Expectations expectations, long result) throws Exception {
    	returns(expectations, result);
    }

    public static void returnsLong(Expectations expectations, long result, long ... results) throws Exception {
    	returns(expectations, result, toObjectArray(results));
    }

    public static void returnsShort(Expectations expectations, short result) throws Exception {
    	returns(expectations, result);
    }

    public static void returnsShort(Expectations expectations, short result, short ... results) throws Exception {
    	returns(expectations, result, toObjectArray(results));
    }

    public static void returnsByte(Expectations expectations, byte result) throws Exception {
    	returns(expectations, result);
    }

    public static void returnsByte(Expectations expectations, byte result, byte ... results) throws Exception {
    	returns(expectations, result, toObjectArray(results));
    }

    public static void returnsFloat(Expectations expectations, float result) throws Exception {
    	returns(expectations, result);
    }

    public static void returnsFloat(Expectations expectations, float result, float ... results) throws Exception {
    	returns(expectations, result, toObjectArray(results));
    }

    public static void returnsDouble(Expectations expectations, double result) throws Exception {
    	returns(expectations, result);
    }

    public static void returnsDouble(Expectations expectations, double result, double ... results) throws Exception {
    	returns(expectations, result, toObjectArray(results));
    }

    public static void returnsBoolean(Expectations expectations, boolean result) throws Exception {
    	returns(expectations, result);
    }

    public static void returnsBoolean(Expectations expectations, boolean result, boolean ... results) throws Exception {
    	returns(expectations, result, toObjectArray(results));
    }

    public static void returnsChar(Expectations expectations, char result) throws Exception {
    	returns(expectations, result);
    }

    public static void returnsChar(Expectations expectations, char result, char ... results) throws Exception {
    	returns(expectations, result, toObjectArray(results));
    }

    @SuppressWarnings("unchecked")
	public static < T > T onInstance(Expectations expectations, T mockedInstance) throws Exception {
        Method method = Expectations.class.getSuperclass().getDeclaredMethod("onInstance", Object.class);
        method.setAccessible(true);
        return (T) method.invoke(expectations, mockedInstance);
    }

    public static < T > T any(Expectations expectations) throws Exception {
        ActiveInvocations.addArgMatcher();
        return null;
    }

    public static int anyInt(Expectations expectations) throws Exception {
    	ActiveInvocations.addArgMatcher();
    	return 0;
    }

    public static long anyLong(Expectations expectations) throws Exception {
    	ActiveInvocations.addArgMatcher();
    	return 0;
    }

    public static short anyShort(Expectations expectations) throws Exception {
    	ActiveInvocations.addArgMatcher();
    	return 0;
    }

    public static byte anyByte(Expectations expectations) throws Exception {
    	ActiveInvocations.addArgMatcher();
    	return 0;
    }

    public static float anyFloat(Expectations expectations) throws Exception {
    	ActiveInvocations.addArgMatcher();
    	return 0;
    }

    public static double anyDouble(Expectations expectations) throws Exception {
    	ActiveInvocations.addArgMatcher();
    	return 0;
    }

    public static char anyChar(Expectations expectations) throws Exception {
    	ActiveInvocations.addArgMatcher();
    	return 0;
    }

    public static boolean anyBoolean(Expectations expectations) throws Exception {
    	ActiveInvocations.addArgMatcher();
    	return false;
    }

    @SuppressWarnings("unchecked")
	public static <T> T withDelegate(Expectations expectations, Delegate<T> delegateObjectWithInvocationHandlerMethod) throws Exception {
    	if (delegateObjectWithInvocationHandlerMethod == null) {
    		addExpectationArgumentMatcher(expectations, new EqualityMatcher(null));
    		return null;
    	}
        return (T)invokeOnInvocation(expectations, "with", new Class<?>[] {Delegate.class}, delegateObjectWithInvocationHandlerMethod);
    }

    @SuppressWarnings("unchecked")
    public static <T> T with(Expectations expectations, final Function1<T, Boolean> lambdaMatcher) throws Exception {
    	if (lambdaMatcher == null) {
    		addExpectationArgumentMatcher(expectations, new EqualityMatcher(null));
    		return null;
    	}
    	return (T)invokeOnInvocation(expectations, "with", new Class<?>[] {Delegate.class},
    			new Delegate<T>() {
    		@SuppressWarnings("unused")
			public boolean match(T t) {
    			return lambdaMatcher.apply(t);
    		}
    	});
    }

    public static int withInt(Expectations expectations, final Function1<Integer, Boolean> lambdaMatcher) throws Exception {
    	if (lambdaMatcher == null) {
    		addExpectationArgumentMatcher(expectations, new EqualityMatcher(null));
    	} else {
	    	invokeOnInvocation(expectations, "with", new Class<?>[] {Delegate.class},
	    			new Delegate<Integer>() {
	    		@SuppressWarnings("unused")
	    		public boolean match(int t) {
	    			return lambdaMatcher.apply(t);
	    		}
	    	});
    	}
    	return 0;
    }

    public static long withLong(Expectations expectations, final Function1<Long, Boolean> lambdaMatcher) throws Exception {
    	if (lambdaMatcher == null) {
    		addExpectationArgumentMatcher(expectations, new EqualityMatcher(null));
    	} else {
    		invokeOnInvocation(expectations, "with", new Class<?>[] {Delegate.class},
    				new Delegate<Long>() {
    			@SuppressWarnings("unused")
    			public boolean match(long t) {
    				return lambdaMatcher.apply(t);
    			}
    		});
    	}
    	return 0;
    }

    public static short withShort(Expectations expectations, final Function1<Short, Boolean> lambdaMatcher) throws Exception {
    	if (lambdaMatcher == null) {
    		addExpectationArgumentMatcher(expectations, new EqualityMatcher(null));
    	} else {
    		invokeOnInvocation(expectations, "with", new Class<?>[] {Delegate.class},
    				new Delegate<Short>() {
    			@SuppressWarnings("unused")
    			public boolean match(short t) {
    				return lambdaMatcher.apply(t);
    			}
    		});
    	}
    	return 0;
    }
    public static byte withByte(Expectations expectations, final Function1<Byte, Boolean> lambdaMatcher) throws Exception {
    	if (lambdaMatcher == null) {
    		addExpectationArgumentMatcher(expectations, new EqualityMatcher(null));
    	} else {
    		invokeOnInvocation(expectations, "with", new Class<?>[] {Delegate.class},
    				new Delegate<Byte>() {
    			@SuppressWarnings("unused")
    			public boolean match(byte t) {
    				return lambdaMatcher.apply(t);
    			}
    		});
    	}
    	return 0;
    }
    public static double withDouble(Expectations expectations, final Function1<Double, Boolean> lambdaMatcher) throws Exception {
    	if (lambdaMatcher == null) {
    		addExpectationArgumentMatcher(expectations, new EqualityMatcher(null));
    	} else {
    		invokeOnInvocation(expectations, "with", new Class<?>[] {Delegate.class},
    				new Delegate<Double>() {
    			@SuppressWarnings("unused")
    			public boolean match(double t) {
    				return lambdaMatcher.apply(t);
    			}
    		});
    	}
    	return 0;
    }
    public static float withFloat(Expectations expectations, final Function1<Float, Boolean> lambdaMatcher) throws Exception {
    	if (lambdaMatcher == null) {
    		addExpectationArgumentMatcher(expectations, new EqualityMatcher(null));
    	} else {
    		invokeOnInvocation(expectations, "with", new Class<?>[] {Delegate.class},
    				new Delegate<Float>() {
    			@SuppressWarnings("unused")
    			public boolean match(float t) {
    				return lambdaMatcher.apply(t);
    			}
    		});
    	}
    	return 0;
    }
    public static char withChar(Expectations expectations, final Function1<Character, Boolean> lambdaMatcher) throws Exception {
    	if (lambdaMatcher == null) {
    		addExpectationArgumentMatcher(expectations, new EqualityMatcher(null));
    	} else {
    		invokeOnInvocation(expectations, "with", new Class<?>[] {Delegate.class},
    				new Delegate<Character>() {
    			@SuppressWarnings("unused")
    			public boolean match(char t) {
    				return lambdaMatcher.apply(t);
    			}
    		});
    	}
    	return 0;
    }
    public static boolean withBoolean(Expectations expectations, final Function1<Boolean, Boolean> lambdaMatcher) throws Exception {
    	if (lambdaMatcher == null) {
    		addExpectationArgumentMatcher(expectations, new EqualityMatcher(null));
    	} else {
    		invokeOnInvocation(expectations, "with", new Class<?>[] {Delegate.class},
    				new Delegate<Boolean>() {
    			@SuppressWarnings("unused")
    			public boolean match(boolean t) {
    				return lambdaMatcher.apply(t);
    			}
    		});
    	}
    	return false;
    }

    public static < T > T with(Expectations expectations, T t) throws Exception {
        addExpectationArgumentMatcher(expectations, new EqualityMatcher(t));
        return t;
    }

    public static int withInt(Expectations expectations, int t) throws Exception {
    	addExpectationArgumentMatcher(expectations, new EqualityMatcher(t));
    	return 0;
    }

    public static long withLong(Expectations expectations, long t) throws Exception {
    	addExpectationArgumentMatcher(expectations, new EqualityMatcher(t));
    	return 0;
    }
    public static short withShort(Expectations expectations, short t) throws Exception {
    	addExpectationArgumentMatcher(expectations, new EqualityMatcher(t));
    	return 0;
    }
    public static byte withByte(Expectations expectations, byte t) throws Exception {
    	addExpectationArgumentMatcher(expectations, new EqualityMatcher(t));
    	return 0;
    }
    public static float withFloat(Expectations expectations, float t) throws Exception {
    	addExpectationArgumentMatcher(expectations, new EqualityMatcher(t));
    	return 0;
    }
    public static double withDouble(Expectations expectations, double t) throws Exception {
    	addExpectationArgumentMatcher(expectations, new EqualityMatcher(t));
    	return 0;
    }
    public static char withChar(Expectations expectations, char t) throws Exception {
    	addExpectationArgumentMatcher(expectations, new EqualityMatcher(t));
    	return 0;
    }
    public static boolean withBoolean(Expectations expectations, boolean t) throws Exception {
    	addExpectationArgumentMatcher(expectations, new EqualityMatcher(t));
    	return false;
    }

    public static <T> T with(Expectations expectations, T argValue, Object argumentMatcher) throws Exception {
    	addExpectationHamcrestMatcher(expectations, argumentMatcher);
        return argValue;
    }

    private static Object invokeOnInvocation(Expectations expectations, String name, Class<?>[] types, Object ... parameters) {
    	Class<? super Expectations> invocationsClass = Expectations.class.getSuperclass();
    	try {
			Method method = invocationsClass.getDeclaredMethod(name, types);
	    	method.setAccessible(true);
	    	return method.invoke(expectations, parameters);
    	} catch (Exception exception) {
    		StringBuilder stringBuilder = new StringBuilder();
    		for (Class<?> type : types) {
				if (stringBuilder.length() > 0) {
					stringBuilder.append(", ");
				}
				stringBuilder.append(type.getCanonicalName());
			}
    		throw new RuntimeException("Error invoking method " +  invocationsClass.getCanonicalName() + "." + name + "(" + stringBuilder + ")", exception);
    	}
    }

    public static <T> T withAny(Expectations expectations, T arg) throws Exception {
       getCurrectExpectationsPhase(expectations).addArgMatcher(AlwaysTrueMatcher.INSTANCE);
       return arg;
    }

    /**
     * When passed as argument for an expectation, creates a new matcher that will check if the given value is
     * {@link Object#equals(Object) equal} to the corresponding argument received by a matching invocation.
     * <p/>
     * The matcher is added to the end of the list of argument matchers for the invocation being recorded/verified.
     * It cannot be reused for a different parameter.
     * <p/>
     * Usually, this particular method should <em>not</em> be used. Instead, simply pass the desired argument value
     * directly, without any matcher.
     * Only when specifying values for a <em>varargs</em> method it's useful, and even then only when some other argument
     * matcher is also used.
     * <p/>
     * <a href="http://jmockit.googlecode.com/svn/trunk/www/tutorial/BehaviorBasedTesting.html#argumentMatching">In the
     * Tutorial</a>
     *
     * @param arg the expected argument value
     *
     * @return the given argument
     */
    public static < T > T withEqual(Expectations expectations, T arg) throws Exception {
    	addExpectationArgumentMatcher(expectations, new EqualityMatcher(arg));
        return arg;
    }

    /**
     * Same as {@link #withEqual(Expectations, Object)}, but checking that a numeric invocation argument in the replay phase is
     * sufficiently close to the given value.
     *
     * @param value the center value for range comparison
     * @param delta the tolerance around the center value, for a range of [value - delta, value + delta]
     *
     * @return the given {@code value}
     */
    public static double withEqual(Expectations expectations, double value, double delta) throws Exception {
    	addExpectationArgumentMatcher(expectations, new NumericEqualityMatcher(value, delta));
    	return value;
    }

    /**
     * Same as {@link #withEqual(Expectations, Object)}, but checking that a numeric invocation argument in the replay phase is
     * sufficiently close to the given value.
     *
     * @param value the center value for range comparison
     * @param delta the tolerance around the center value, for a range of [value - delta, value + delta]
     *
     * @return the given {@code value}
     */
    public static float withEqual(Expectations expectations, float value, double delta) throws Exception {
    	addExpectationArgumentMatcher(expectations, new NumericEqualityMatcher(value, delta));
        return value;
    }

    /**
     * Same as {@link #withEqual(Expectations, Object)}, but checking that an invocation argument in the replay phase is an instance of
     * the same class as the given object.
     * <p/>
     * Equivalent to a <code>withInstanceOf(object.getClass())</code> call, except that it returns {@code object} instead
     * of {@code null}.
     *
     * @param object an instance of the desired class
     *
     * @return the given instance
     */
    public static <T> T withInstanceLike(Expectations expectations, T object) throws Exception {
    	addExpectationArgumentMatcher(expectations, new ClassMatcher(object.getClass()));
        return object;
    }

    /**
     * Same as {@link #withEqual(Expectations, Object)}, but checking that an invocation argument in the replay phase is an instance of
     * the given class.
     *
     * @param argClass the desired class
     *
     * @return always {@code null}; if you need a specific return value, use {@link #withInstanceLike(Object)}
     */
    public static <T> T withInstanceOf(Expectations expectations, Class<T> argClass) throws Exception {
    	addExpectationArgumentMatcher(expectations, new ClassMatcher(argClass));
        return null;
    }

    /**
     * Same as {@link #withEqual(Expectations, Object)}, but checking that a textual invocation argument in the replay phase matches
     * the given {@link Pattern regular expression}.
     * <p/>
     * Note that this can be used for any string comparison, including case insensitive ones (with {@code "(?i)"} in the
     * regex).
     *
     * @param regex an arbitrary (non-null) regular expression against which textual argument values will be matched
     *
     * @return the given regex
     *
     * @see Pattern#compile(String, int)
     */
    public static <T extends CharSequence> T withMatch(Expectations expectations, T regex) throws Exception {
    	addExpectationArgumentMatcher(expectations, new PatternMatcher(regex.toString()));
        return regex;
    }

    /**
     * Same as {@link #withEqual(Expectations, Object)}, but checking that the invocation argument in the replay phase is different
     * from the given value.
     *
     * @param arg an arbitrary value, but different from the ones expected to occur during replay
     *
     * @return the given argument value
     */
    public static <T> T withNotEqual(Expectations expectations, T arg) throws Exception {
    	addExpectationArgumentMatcher(expectations, new InequalityMatcher(arg));
        return arg;
    }

    /**
     * Same as {@link #withEqual(Expectations, Object)}, but checking that an invocation argument in the replay phase is not
     * {@code null}.
     *
     * @return always {@code null}
     */
    public static <T> T withNotNull(Expectations expectations) throws Exception {
    	addExpectationArgumentMatcher(expectations, NonNullityMatcher.INSTANCE);
        return null;
    }

    /**
     * Same as {@link #withEqual(Object)}, but checking that an invocation argument in the replay phase is {@code null}.
     *
     * @return always {@code null}
     */
    public static <T> T withNull(Expectations expectations) throws Exception {
    	addExpectationArgumentMatcher(expectations, NullityMatcher.INSTANCE);
        return null;
    }

    /**
     * Same as {@link #withEqual(Expectations, Object)}, but checking that a textual invocation argument in the replay phase starts
     * with the given text.
     *
     * @param text an arbitrary non-null textual value
     *
     * @return the given text
     */
    public static <T extends CharSequence> T withPrefix(Expectations expectations, T text) throws Exception {
    	addExpectationArgumentMatcher(expectations, new StringPrefixMatcher(text));
        return text;
    }

    /**
     * Same as {@link #withEqual(Expectations, Object)}, but checking that an invocation argument in the replay phase is the exact same
     * instance as the one in the recorded/verified invocation.
     *
     * @param object the desired instance

     * @return the given object
     */
    public static <T> T withSameInstance(Expectations expectations, T object) throws Exception {
    	addExpectationArgumentMatcher(expectations, new SamenessMatcher(object));
        return object;
    }

    /**
     * Same as {@link #withEqual(Object)}, but checking that a textual invocation argument in the replay phase contains
     * the given text as a substring.
     *
     * @param text an arbitrary non-null textual value
     *
     * @return the given text
     */
    public static <T extends CharSequence> T withSubstring(Expectations expectations, T text) throws Exception {
    	addExpectationArgumentMatcher(expectations, new StringContainmentMatcher(text));
        return text;
    }

    /**
     * Same as {@link #withEqual(Object)}, but checking that a textual invocation argument in the replay phase ends with
     * the given text.
     *
     * @param text an arbitrary non-null textual value
     *
     * @return the given text
     */
    public static <T extends CharSequence> T withSuffix(Expectations expectations, T text) throws Exception {
    	addExpectationArgumentMatcher(expectations, new StringSuffixMatcher(text));
        return text;
    }

    private static < T > void addExpectationArgumentMatcher(Expectations expectations, ArgumentMatcher matcher) throws Exception {
        getCurrectExpectationsPhase(expectations).addArgMatcher(matcher);
    }

    private static < T > void addExpectationHamcrestMatcher(Expectations expectations, Object matcher) throws Exception {
    	getCurrectExpectationsPhase(expectations).addArgMatcher(HamcrestAdapter.create(matcher));
    }

    private static RecordPhase getCurrectExpectationsPhase(Expectations expectations) throws Exception {
        Method method = Expectations.class.getDeclaredMethod("getCurrentPhase");
        method.setAccessible(true);
        return (RecordPhase) method.invoke(expectations);
    }

    private static Object[] toObjectArray(int[] values) {
    	if (values == null) {
    		return null;
    	}
    	Object[] objectArray = new Object[values.length];
    	for (int i = 0; i < values.length; i++) {
			objectArray[i] = values[i];
		}
		return objectArray;
	}
    private static Object[] toObjectArray(long[] values) {
    	if (values == null) {
    		return null;
    	}
    	Object[] objectArray = new Object[values.length];
    	for (int i = 0; i < values.length; i++) {
    		objectArray[i] = values[i];
    	}
    	return objectArray;
    }
    private static Object[] toObjectArray(short[] values) {
    	if (values == null) {
    		return null;
    	}
    	Object[] objectArray = new Object[values.length];
    	for (int i = 0; i < values.length; i++) {
    		objectArray[i] = values[i];
    	}
    	return objectArray;
    }
    private static Object[] toObjectArray(byte[] values) {
    	if (values == null) {
    		return null;
    	}
    	Object[] objectArray = new Object[values.length];
    	for (int i = 0; i < values.length; i++) {
    		objectArray[i] = values[i];
    	}
    	return objectArray;
    }
    private static Object[] toObjectArray(float[] values) {
    	if (values == null) {
    		return null;
    	}
    	Object[] objectArray = new Object[values.length];
    	for (int i = 0; i < values.length; i++) {
    		objectArray[i] = values[i];
    	}
    	return objectArray;
    }
    private static Object[] toObjectArray(double[] values) {
    	if (values == null) {
    		return null;
    	}
    	Object[] objectArray = new Object[values.length];
    	for (int i = 0; i < values.length; i++) {
    		objectArray[i] = values[i];
    	}
    	return objectArray;
    }

    private static Object[] toObjectArray(boolean[] values) {
    	if (values == null) {
    		return null;
    	}
    	Object[] objectArray = new Object[values.length];
    	for (int i = 0; i < values.length; i++) {
    		objectArray[i] = values[i];
    	}
    	return objectArray;
    }
    private static Object[] toObjectArray(char[] values) {
    	if (values == null) {
    		return null;
    	}
    	Object[] objectArray = new Object[values.length];
    	for (int i = 0; i < values.length; i++) {
    		objectArray[i] = values[i];
    	}
    	return objectArray;
    }

    public static void setTimes(Expectations expectations, int times) throws Exception {
        ActiveInvocations.times(times);
    }

    public static void setMaxTimes(Expectations expectations, int maxTimes) throws Exception {
        ActiveInvocations.maxTimes(maxTimes);
    }
    public static void setMinTimes(Expectations expectations, int minTimes) throws Exception {
    	ActiveInvocations.minTimes(minTimes);
    }
    @SuppressWarnings("unchecked")
	public static < T > T invoke(Expectations expectations, Object objectWithMethod, String methodName,
                                 Object... methodArgs) {
        return (T) MethodReflection.invoke(objectWithMethod.getClass(), objectWithMethod, methodName, methodArgs);
    }

    /**
     * Specifies an expectation for a {@code static} method, with a given list of arguments.
     * <p/>
     * This is useful when a method is not accessible from the test (it's {@code private}, for example), and therefore
     * cannot be called normally. It should not be used to call accessible methods.
     * <p/>
     * Additionally, this can also be used to directly test private methods, when there is no other way to do so, or it
     * would be too difficult by indirect means. Note that in such a case the target class would not be mocked.
     *
     * @param methodOwner the class on which the invocation is to be done; must not be null
     * @param methodName the name of the expected static method
     * @param methodArgs zero or more non-null expected parameter values for the expectation;
     *            if a null value needs to be passed, the {@code Class} object for the parameter type must be passed
     *            instead
     * @return the return value from the invoked method, wrapped if primitive
     * @throws IllegalArgumentException if a null reference was provided for a parameter
     */
    // TODO Test
    public static < T > T invoke(Expectations expectations, Class< ? > methodOwner, String methodName,
                                 Object... methodArgs) {
        return (T) MethodReflection.invoke(methodOwner, null, methodName, methodArgs);
    }

    /**
     * Specifies an expectation for a constructor of a given class.
     * <p/>
     * This is useful for invoking non-accessible constructors ({@code private} ones, for example) from the test, which
     * otherwise could not be called normally. It should not be used for accessible constructors.
     * <p/>
     * <a href="http://jmockit.googlecode.com/svn/trunk/www/tutorial/BehaviorBasedTesting.html#deencapsulation">In the
     * Tutorial</a>
     *
     * @param className the fully qualified name of the desired class
     * @param parameterTypes the formal parameter types for the desired constructor, possibly empty
     * @param initArgs the invocation arguments for the constructor, which must be consistent with the specified
     *            parameter types
     * @param <T> interface or super-class type to which the returned instance should be assignable
     * @return a newly created instance of the specified class, initialized with the specified constructor and arguments
     * @see #newInstance(String, Object...)
     * @see #newInnerInstance(String, Object, Object...)
     */
    // TODO Test
    public static < T > T newInstance(Expectations expectations, String className, Class< ? >[] parameterTypes,
                                      Object... initArgs) {
        return (T) ConstructorReflection.newInstance(className, parameterTypes, initArgs);
    }

    /**
     * The same as {@link #newInstance(String, Class[], Object...)}, but inferring parameter types from non-null
     * argument
     * values.
     * If a given parameter needs to match {@code null} during replay, then the corresponding {@code Class} literal must
     * be passed instead of {@code null}.
     *
     * @param nonNullInitArgs zero or more non-null expected parameter values for the expectation;
     *            if a null value needs to be passed, the {@code Class} object for the parameter type must be passed
     *            instead
     * @throws IllegalArgumentException if one of the given arguments is {@code null}
     */
    // TODO Test
    public static < T > T newInstance(Expectations expectations, String className, Object... nonNullInitArgs) {
        return (T) ConstructorReflection.newInstance(className, nonNullInitArgs);
    }

    /**
     * The same as {@link #newInstance(String, Class[], Object...)}, but for instantiating an inner non-accessible class
     * of some other class, and where all other (if any) initialization arguments are known to be non null.
     *
     * @param innerClassSimpleName simple name of the inner class, that is, the part after the "$" character in its full
     *            name
     * @param outerClassInstance the outer class instance to which the inner class instance will belong
     * @param nonNullInitArgs zero or more non-null expected parameter values for the expectation;
     *            if a null value needs to be passed, the {@code Class} object for the parameter type must be passed
     *            instead
     */
    // TODO Test
    public static < T > T newInnerInstance(Expectations expectations, String innerClassSimpleName,
                                           Object outerClassInstance, Object... nonNullInitArgs) {
        return (T) ConstructorReflection.newInnerInstance(innerClassSimpleName, outerClassInstance, nonNullInitArgs);
    }
}
