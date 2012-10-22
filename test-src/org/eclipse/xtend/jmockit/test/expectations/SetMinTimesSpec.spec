package org.eclipse.xtend.jmockit.test.expectations

import mockit.Mocked
import mockit.internal.UnexpectedInvocation

import static extension org.eclipse.xtend.jmockit.JMockitExtension.*

describe "SetMinTimes sets the minimal count of the method invocations" {
	@Mocked
	ExpectationsAPI expectationsAPI

	fact "Set min times to 1 with one call" {
		mock [
			expectationsAPI.returnString
			result = "1"
			minTimes = 1
		]
		expectationsAPI.returnString => "1"
	}

	fact "Set min times to 3 call 1 time" {
		mock [
			expectationsAPI.returnString
			result = "1"
			minTimes = 3
		]
		expectationsAPI.returnString => "1"
		expectationsAPI.returnString => "1"
		expectationsAPI.returnString => "1"
		expectationsAPI.returnString => "1"
		expectationsAPI.returnString => "1"
		expectationsAPI.returnString => "1"
		expectationsAPI.returnString => "1"
	}

	fact "Set min times to 3 call 3 times" {
		mock [
			expectationsAPI.returnString
			result = "1"
			minTimes = 3
		]
		expectationsAPI.returnString => "1"
		expectationsAPI.returnString => "1"
		expectationsAPI.returnString => "1"
	}
}