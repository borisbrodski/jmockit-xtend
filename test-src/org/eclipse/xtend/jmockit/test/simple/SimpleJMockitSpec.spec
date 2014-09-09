package org.eclipse.xtend.jmockit.test.simple

import mockit.Mocked

import static extension org.eclipse.xtend.jmockit.JMockitExtension.*
import mockit.internal.UnexpectedInvocation

describe "Xtend-JMockit simple test"{
	describe "Simple API without mocking throws exceptions" {
		fact "Simple API implementation throws exceptions" {
			new SimpleAPI().returnString(null, null) throws RuntimeException
			
		}
	}
	
	describe "SimpleAPI with mocking" {
		@Mocked
		SimpleAPI api
		
		fact "mock method record expectations" {
			mock [
				api.returnString("a", "b")
			]
			
			api.returnString("a", "b")
		}
		
		fact "mock method record expectations and throw exception by wrong calls" {
			mock [
				api.returnString("a", "b")
			]
			
			api.returnString("a", "b")
			api.returnString("x", "y") throws UnexpectedInvocation
		}
	}
}

