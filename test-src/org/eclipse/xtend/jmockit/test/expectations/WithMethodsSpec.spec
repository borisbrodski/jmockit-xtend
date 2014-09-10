package org.eclipse.xtend.jmockit.test.expectations

import mockit.Mocked
import static extension org.eclipse.xtend.jmockit.JMockitExtension.*
import mockit.Delegate
import mockit.Deencapsulation

describe "with*() methods work as expected" {
	@Mocked
	ExpectationsAPI expectationsAPI

	fact "with(<lambda>) works (type: String)" {
		stub [
			expectationsAPI.paramsString(with [ (it ?: "").length > 3 ])
			result = "match1"
		]
		expectationsAPI.paramsString("aBc") => null
		expectationsAPI.paramsString("abcd") => "match1"
		expectationsAPI.paramsString("abcde") => "match1"
		expectationsAPI.paramsString("") => null
		expectationsAPI.paramsString(null) => null
	}

	fact "with(<lambda>) works (type: Int)" {
		stub [
			expectationsAPI.paramsInt(withInt[ it > 10])
			result = "match1"
		]


		expectationsAPI.paramsInt(9) => null
		expectationsAPI.paramsInt(10) => null
		expectationsAPI.paramsInt(11) => "match1"
		expectationsAPI.paramsInt(12) => "match1"
	}

	fact "with(<lambda>) works (type: Long)" {
		stub [
			expectationsAPI.paramsLong(withLong [ it > 10])
			result = "match1"
		]


		expectationsAPI.paramsLong(9) => null
		expectationsAPI.paramsLong(10) => null
		expectationsAPI.paramsLong(11) => "match1"
		expectationsAPI.paramsLong(12) => "match1"
	}

	fact "with(<lambda>) works (type: Short)" {
		stub [
			expectationsAPI.paramsShort(withShort [ it > 10])
			result = "match1"
		]

		expectationsAPI.paramsShort(9 as short) => null
		expectationsAPI.paramsShort(10 as short) => null
		expectationsAPI.paramsShort(11 as short) => "match1"
		expectationsAPI.paramsShort(12 as short) => "match1"
	}

	fact "with(<lambda>) works (type: Byte)" {
		stub [
			expectationsAPI.paramsByte(withByte [ it > 10])
			result = "match1"
		]


		expectationsAPI.paramsByte(9 as byte) => null
		expectationsAPI.paramsByte(10 as byte) => null
		expectationsAPI.paramsByte(11 as byte) => "match1"
		expectationsAPI.paramsByte(12 as byte) => "match1"
	}
	fact "with(<lambda>) works (type: Double)" {
		stub [
			expectationsAPI.paramsDouble(withDouble [ it > 10.3 ])
			result = "match1"
		]


		expectationsAPI.paramsDouble(9.5) => null
		expectationsAPI.paramsDouble(10.2) => null
		expectationsAPI.paramsDouble(10.4) => "match1"
		expectationsAPI.paramsDouble(11) => "match1"
	}
	fact "with(<lambda>) works (type: Float)" {
		stub [
			expectationsAPI.paramsFloat(withFloat [ it > 10.3 ])
			result = "match1"
		]


		expectationsAPI.paramsFloat(9.5 as float) => null
		expectationsAPI.paramsFloat(10.2 as float) => null
		expectationsAPI.paramsFloat(10.4 as float) => "match1"
		expectationsAPI.paramsFloat(11) => "match1"
	}

	fact "with(<lambda>) works (type: Char)" {
		stub [
			expectationsAPI.paramsChar(withChar [ Character::isDigit(it) ])
			result = "match1"
		]


		expectationsAPI.paramsChar("a".charAt(0)) => null
		expectationsAPI.paramsChar("1".charAt(0)) => "match1"
		expectationsAPI.paramsChar("4".charAt(0)) => "match1"
		expectationsAPI.paramsChar("X".charAt(0)) => null
	}

	fact "with(<lambda>) works (type: Boolean)" {
		stub [
			expectationsAPI.paramsBoolean(withBoolean [ !it ])
			result = "match1"
		]

		expectationsAPI.paramsBoolean(true) => null
		expectationsAPI.paramsBoolean(false) => "match1"
	}

	fact "withAny(T) works" {
		stub [
		    Deencapsulation.invoke(expectationsAPI, "paramsLong", withAny(1L))
			result = "match1"

		    Deencapsulation.invoke(expectationsAPI, "paramsString", withAny(""))
			result = "match2"
		]

		expectationsAPI.paramsLong(4) => "match1"
		expectationsAPI.paramsLong(-1) => "match1"

		expectationsAPI.paramsString(null) => "match2"
		expectationsAPI.paramsString("123") => "match2"
	}

	fact "with(T, Object) works" {
		stub [
			expectationsAPI.paramsLong(with(1L, 101L))
			result = "match1"
		]

		expectationsAPI.paramsLong(101L) => "match1"
		expectationsAPI.paramsLong(102L) => null
		expectationsAPI.paramsLong(100L) => null
	}

	fact "with(Delegate) works" {
		stub [
			val Delegate<Long> a = new MoreThat100
			expectationsAPI.paramsLong(withDelegate(a))
			result = "match1"
		]

		expectationsAPI.paramsLong(101L) => "match1"
		expectationsAPI.paramsLong(102L) => "match1"
		expectationsAPI.paramsLong(100L) => null
		expectationsAPI.paramsLong(99L) => null
	}

	fact "with(T, Delegate) works" {
		stub [
			val Delegate<Long> a = new MoreThat100
			expectationsAPI.paramsLong(withDelegate(1L, a))
			result = "match1"
		]

		expectationsAPI.paramsLong(101L) => "match1"
		expectationsAPI.paramsLong(102L) => "match1"
		expectationsAPI.paramsLong(100L) => null
		expectationsAPI.paramsLong(99L) => null
	}

	fact "withEqual(Object) works" {
		stub [
			expectationsAPI.paramsLong(withEqual(101L))
			result = "match1"
		]

		expectationsAPI.paramsLong(100L) => null
		expectationsAPI.paramsLong(101L) => "match1"
		expectationsAPI.paramsLong(102L) => null
		expectationsAPI.paramsLong(99L) => null
	}

	fact "withEqual(double, double) works" {
		stub [
			expectationsAPI.paramsDouble(withEqual(1.0, 0.001))
			result = "match1"
		]

		expectationsAPI.paramsDouble(1.0) => "match1"
		expectationsAPI.paramsDouble(1.0005) => "match1"
		expectationsAPI.paramsDouble(1.005) => null
		expectationsAPI.paramsDouble(0.9995) => "match1"
		expectationsAPI.paramsDouble(0.995) => null
	}

	fact "withEqual(float, double) works" {
		stub [
			expectationsAPI.paramsFloat(withEqual(1.0 as float, 0.001))
			result = "match1"
		]

		expectationsAPI.paramsFloat(1.0 as float) => "match1"
		expectationsAPI.paramsFloat(1.0005 as float) => "match1"
		expectationsAPI.paramsFloat(1.005 as float) => null
		expectationsAPI.paramsFloat(0.9995 as float) => "match1"
		expectationsAPI.paramsFloat(0.995 as float) => null
	}

	fact "withInstanceLike(Object) works" {
		stub [
			expectationsAPI.paramsObject(withInstanceLike(""))
			result = "match1"
		]

		expectationsAPI.paramsObject(1.0) => null
		expectationsAPI.paramsObject("test") => "match1"
		expectationsAPI.paramsObject(null) => null
	}

	fact "withInstanceOf(Class) works" {
		stub [
			expectationsAPI.paramsObject(withInstanceOf(String))
			result = "match1"
		]

		expectationsAPI.paramsObject(1.0) => null
		expectationsAPI.paramsObject("test") => "match1"
		expectationsAPI.paramsObject(null) => null
	}

	fact "withMatch(CharSequence) works" {
		stub [
			expectationsAPI.paramsString(withMatch("[a-z]+"))
			result = "match1"
		]

		expectationsAPI.paramsString("") => null
		expectationsAPI.paramsString("awwf") => "match1"
		expectationsAPI.paramsString("Acsw") => null
	}
	fact "withNotEqual(Object) works" {
		stub [
			expectationsAPI.paramsString(withNotEqual("test"))
			result = "match1"
		]

		expectationsAPI.paramsString("TEST") => "match1"
		expectationsAPI.paramsString("test") => null
		expectationsAPI.paramsString("") => "match1"
	}
	fact "withNotNull() works" {
		stub [
			expectationsAPI.paramsString(withNotNull)
			result = "match1"
		]

		expectationsAPI.paramsString("TEST") => "match1"
		expectationsAPI.paramsString(null) => null
		expectationsAPI.paramsString("") => "match1"
	}
	fact "withNull() works" {
		stub [
			expectationsAPI.paramsString(withNull)
			result = "match1"
		]

		expectationsAPI.paramsString("TEST") => null
		expectationsAPI.paramsString(null) => "match1"
		expectationsAPI.paramsString("") => null
	}
	fact "withPrefix(CharSequence) works" {
		stub [
			expectationsAPI.paramsString(withPrefix("abc"))
			result = "match1"
		]

		expectationsAPI.paramsString("abc") => "match1"
		expectationsAPI.paramsString("abcdef") => "match1"
		expectationsAPI.paramsString(null) => null
		expectationsAPI.paramsString("aBcdef") => null
	}
	fact "withSameInstance(Object) works" {
		val v1 = new String("1")
		val v2 = new String("1")
		stub [
			expectationsAPI.paramsString(withSameInstance(v1))
			result = "match1"
		]

		expectationsAPI.paramsString(v1) => "match1"
		expectationsAPI.paramsString(v2) => null
		expectationsAPI.paramsString("1") => null
		expectationsAPI.paramsString(null) => null
	}
	fact "withSubstring(CharSequence) works" {
		stub [
			expectationsAPI.paramsString(withSubstring("abc"))
			result = "match1"
		]

		expectationsAPI.paramsString("abc") => "match1"
		expectationsAPI.paramsString("Xabc") => "match1"
		expectationsAPI.paramsString("abcX") => "match1"
		expectationsAPI.paramsString("$abc$") => "match1"
		expectationsAPI.paramsString("def") => null
		expectationsAPI.paramsString("aBc") => null
		expectationsAPI.paramsString("") => null
		expectationsAPI.paramsString(null) => null
	}
	fact "withSuffix(CharSequence) works" {
		stub [
			expectationsAPI.paramsString(withSuffix("abc"))
			result = "match1"
		]

		expectationsAPI.paramsString("abc") => "match1"
		expectationsAPI.paramsString("Xabc") => "match1"
		expectationsAPI.paramsString("abcX") => null
		expectationsAPI.paramsString("$abc$") => null
		expectationsAPI.paramsString("def") => null
		expectationsAPI.paramsString("aBc") => null
		expectationsAPI.paramsString("") => null
		expectationsAPI.paramsString(null) => null
	}
}