package org.eclipse.xtend.jmockit.test.expectations

import java.lang.reflect.InvocationTargetException
import java.util.List

describe "ExpectationsAPI without mock" {
	fact "All methods throw RuntimeException" {
		for (method : typeof(ExpectationsAPI).declaredMethods) {
			try {
				var parameters = buildParameters(method.parameterTypes)
				method.invoke(new ExpectationsAPI, parameters.toArray)
			} catch (InvocationTargetException e) {
				(e.cause instanceof RuntimeException) => true
			}
		}
	}

	def private buildParameters(List<Class<?>> parameterTypes) {
		parameterTypes.map [
			switch (it) {
				case typeof(int):
				    0
				case typeof(long):
				    0L
				case typeof(byte):
				    0 as byte
			    case typeof(short):
			        0 as short
			    case typeof(float):
			        0.0 as float
			    case typeof(double):
			    	0.0
			    case typeof(char):
			    	" ".charAt(0)
			    case typeof(boolean):
			    	false
			    default:
					null
			}
		] as List<Object>
	}
}