package org.eclipse.xtend.jmockit.test.expectations

import mockit.Mocked
import mockit.internal.UnexpectedInvocation

import static extension org.eclipse.xtend.jmockit.JMockitExtension.*

describe "SetTimes sets the count of the method invocations" {
	@Mocked
	ExpectationsAPI expectationsAPI

	fact "Set times to 1 (default)" {
		mock [
			expectationsAPI.returnString
			result = "1"
			result = "2"
			times = 1
		]
		expectationsAPI.returnString => "1"
		expectationsAPI.returnString throws UnexpectedInvocation
	}

	fact "Set times to 3" {
		mock [
			expectationsAPI.returnString
			result = "1"
			times = 3
		]
		expectationsAPI.returnString => "1"
		expectationsAPI.returnString => "1"
		expectationsAPI.returnString => "1"
		expectationsAPI.returnString throws UnexpectedInvocation
	}
}