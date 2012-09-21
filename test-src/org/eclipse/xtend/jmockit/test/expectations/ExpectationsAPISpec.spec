package org.eclipse.xtend.jmockit.test.expectations

import java.lang.reflect.InvocationTargetException

describe "ExpectationsAPI without mock" {
	fact "All methods throw RuntimeException" {
		for (method : typeof(ExpectationsAPI).declaredMethods) {
			try {
				method.invoke(new ExpectationsAPI)
			} catch (InvocationTargetException e) {
				(e.cause instanceof RuntimeException) => true
			} 
		}
	}
}