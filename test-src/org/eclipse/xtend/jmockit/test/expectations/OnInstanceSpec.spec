package org.eclipse.xtend.jmockit.test.expectations

import mockit.Mocked
import mockit.internal.UnexpectedInvocation

import static org.eclipse.xtend.jmockit.JMockitExtension.*

describe "onInstance extension allows differentiate between single instances" {
	@Mocked
	ExpectationsAPI expectationsAPI1

	@Mocked
	ExpectationsAPI expectationsAPI2

	fact "Call the mocked instance" {
		mock [
			onInstance(expectationsAPI1).returnString
			result = "onInstance used"
		]

		expectationsAPI2.returnString => null
		expectationsAPI1.returnString => "onInstance used"
		expectationsAPI1.returnString throws UnexpectedInvocation

	}

	fact "Mock two instances differently" {
		mock [
			onInstance(expectationsAPI1).returnString
			returns("1", "2")
			onInstance(expectationsAPI2).returnString
			returns("-1", "-2")
		]

		expectationsAPI1.returnString => "1"
		expectationsAPI2.returnString => "-1"
		expectationsAPI2.returnString => "-2"
		expectationsAPI1.returnString throws UnexpectedInvocation
		expectationsAPI2.returnString throws UnexpectedInvocation
	}
}