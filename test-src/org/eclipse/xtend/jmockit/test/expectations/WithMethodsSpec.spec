package org.eclipse.xtend.jmockit.test.expectations

import mockit.Mocked
import static extension org.eclipse.xtend.jmockit.JMockitExtension.*
import mockit.Delegate

describe "with*() methods work as expected" {
	@Mocked
	ExpectationsAPI expectationsAPI
	
	fact "withAny(T) works" {
		stub [
			expectationsAPI.paramsLong(withAny(1L))
			result = "match1"
			
			expectationsAPI.paramsString(withAny(""))
			result = "match2"
		]
		
		expectationsAPI.paramsLong(4) => "match1"
		expectationsAPI.paramsLong(-1) => "match1"
		
		expectationsAPI.paramsString(null) => "match2"
		expectationsAPI.paramsString("123") => "match2"
	}
	
	fact "with(T, Object) works" {
		stub [
			expectationsAPI.paramsLong(with(1L, new MoreThat100))
			result = "match1"
		]
		
		expectationsAPI.paramsLong(101L) => "match1"
		expectationsAPI.paramsLong(102L) => "match1"
		expectationsAPI.paramsLong(100L) => null
		expectationsAPI.paramsLong(99L) => null
	}
	fact "with(Delegate) works" {
		stub [
			val Delegate<Long> a = new MoreThat100
			expectationsAPI.paramsLong(with(a))
			result = "match1"
		]
		
		expectationsAPI.paramsLong(101L) => "match1"
		expectationsAPI.paramsLong(102L) => "match1"
		expectationsAPI.paramsLong(100L) => null
		expectationsAPI.paramsLong(99L) => null
	}
}