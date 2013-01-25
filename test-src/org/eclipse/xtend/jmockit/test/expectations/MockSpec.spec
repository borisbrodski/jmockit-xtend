package org.eclipse.xtend.jmockit.test.expectations

import mockit.Mocked
import static extension org.eclipse.xtend.jmockit.JMockitExtension.*
import mockit.internal.UnexpectedInvocation

describe "mock behaves like Expectations" {
	
	@Mocked
	ExpectationsAPI expectationsAPI
	
	fact "The order and number of call is important" {
		mock [
			expectationsAPI.returnString
			result = "My string"
			
			expectationsAPI.returnInt
			result = 12345
		]
		
		expectationsAPI.returnString => "My string"
		expectationsAPI.returnInt => 12345
		expectationsAPI.returnString throws UnexpectedInvocation
		expectationsAPI.returnInt throws UnexpectedInvocation
		expectationsAPI.returnString throws UnexpectedInvocation
		expectationsAPI.returnSelf throws UnexpectedInvocation
	}
	
	fact "Dynamic partial stub" {
		mock(typeof(ExpectationsAPI)) [
			(new ExpectationsAPI).returnString
			result = "My string 1"
		]

		(new ExpectationsAPI).returnString => "My string 1" 
		try {
			(new ExpectationsAPI).returnVoid
			fail
		} catch (RuntimeException exception) {
			exception.message => "Not implemented"
		}
		try {
			(new ExpectationsAPI).returnString
			fail
		} catch (RuntimeException exception) {
			exception.message => "Not implemented"
		}
	}
}