package org.eclipse.xtend.jmockit;

import java.lang.reflect.Method;

import mockit.Expectations;
import mockit.internal.expectations.transformation.ActiveInvocations;

import org.eclipse.xtext.xbase.lib.Procedures.Procedure1;

public class JMockitExtension {
    public static void mock(final Procedure1< Expectations > proc) {
        new Expectations() {

            {
                proc.apply(this);
            }
        };
    }

    public static void setResult(Expectations expectations, Object result) throws Exception {
        ActiveInvocations.addResult(result);
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
    	Method method = Expectations.class.getDeclaredMethod("returns", Object.class, Object[].class);
    	method.setAccessible(true);
    	method.invoke(expectations, result, toObjectArray(results));
    }
    
	public static void returnsLong(Expectations expectations, long result) throws Exception {
    	Method method = Expectations.class.getDeclaredMethod("returns", Object.class);
    	method.setAccessible(true);
    	method.invoke(expectations, result);
    }
    
    public static void returnsLong(Expectations expectations, long result, long ... results) throws Exception {
    	Method method = Expectations.class.getDeclaredMethod("returns", Object.class, Object[].class);
    	method.setAccessible(true);
    	method.invoke(expectations, result, toObjectArray(results));
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

}
