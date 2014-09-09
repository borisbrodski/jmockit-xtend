package org.eclipse.xtend.jmockit.test.expectations

import mockit.Mocked

describe "Reflect helper methods work" {

	@Mocked("paramsPrivateString")
	ExpectationsAPI expectationsAPI

    // TODO Add and test reflection helper methods
	fact "invoke() calls and mocks private methods"
//	 {
//		stub [
//			invoke(expectationsAPI, "paramsPrivateString", "xxx")
//			result = "My string"
//		]
//
//		expectationsAPI.callParamsPrivateString("aaa") => null
//		expectationsAPI.callParamsPrivateString("xxx") => "My string"
//		expectationsAPI.callParamsPrivateString("aaa") => null
//	}
}