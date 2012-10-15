package org.eclipse.xtend.jmockit;

import java.lang.reflect.Method;
import java.lang.reflect.ParameterizedType;
import java.lang.reflect.Type;
import java.util.Arrays;
import java.util.Collections;

import mockit.Delegate;
import mockit.Expectations;
import mockit.Invocation;
import mockit.NonStrictExpectations;
import mockit.internal.expectations.RecordPhase;
import mockit.internal.expectations.argumentMatching.AlwaysTrueMatcher;
import mockit.internal.expectations.argumentMatching.ArgumentMatcher;
import mockit.internal.expectations.argumentMatching.EqualityMatcher;
import mockit.internal.expectations.argumentMatching.HamcrestAdapter;
import mockit.internal.expectations.argumentMatching.ReflectiveMatcher;
import mockit.internal.expectations.transformation.ActiveInvocations;
import mockit.internal.util.DefaultValues;

import org.eclipse.xtext.xbase.lib.IntegerExtensions;
import org.eclipse.xtext.xbase.lib.Functions.Function0;
import org.eclipse.xtext.xbase.lib.Functions.Function1;
import org.eclipse.xtext.xbase.lib.Functions.Function2;
import org.eclipse.xtext.xbase.lib.Functions.Function3;
import org.eclipse.xtext.xbase.lib.Functions.Function4;
import org.eclipse.xtext.xbase.lib.Functions.Function5;
import org.eclipse.xtext.xbase.lib.Functions.Function6;
import org.eclipse.xtext.xbase.lib.IterableExtensions;
import org.eclipse.xtext.xbase.lib.Procedures.Procedure1;

public class JMockitExtension {
    public static void mock(final Procedure1< Expectations > proc) {
        new Expectations() {

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
	public static <T> T with(Expectations expectations, Delegate<T> delegateObjectWithInvocationHandlerMethod)
    {
       return (T)invokeOnInvocation(expectations, "with", new Class<?>[] {Delegate.class}, delegateObjectWithInvocationHandlerMethod);
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

}
