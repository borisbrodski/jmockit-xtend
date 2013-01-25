package org.eclipse.xtend.jmockit.test.expectations

import mockit.Mocked
import static extension org.eclipse.xtend.jmockit.JMockitExtension.*

describe "Reflect helper methods work" {
	
	@Mocked(methods = "callParamsPrivateString", inverse = true)
	ExpectationsAPI expectationsAPI
	
	fact "invoke() calls and mocks private methods" {
		stub [
			invoke(expectationsAPI, "paramsPrivateString", "xxx")
			result = "My string"
		]

		expectationsAPI.callParamsPrivateString("aaa") => null
		expectationsAPI.callParamsPrivateString("xxx") => "My string"
		expectationsAPI.callParamsPrivateString("aaa") => null
	}
}