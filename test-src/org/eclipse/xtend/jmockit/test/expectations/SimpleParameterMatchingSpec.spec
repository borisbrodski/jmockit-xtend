package org.eclipse.xtend.jmockit.test.expectations

import static extension org.eclipse.xtend.jmockit.JMockitExtension.*
import mockit.Mocked

describe "Simple parameter matching with any() and with()"{
	@Mocked
	ExpectationsAPI expectationsAPI

	fact "Exact single parameter matching works (String)" {
		stub [
			expectationsAPI.paramsString("Test 1")
			result = "(1)"

			expectationsAPI.paramsString("Test 2")
			result = "(2)"

			expectationsAPI.paramsString(null)
			result = "(-)"
		]

		expectationsAPI.paramsString(null) => "(-)"
		expectationsAPI.paramsString("Test 2") => "(2)"
		expectationsAPI.paramsString("Test 1") => "(1)"
		expectationsAPI.paramsString("Test 3") => null

		expectationsAPI.paramsString(null) => "(-)"
		expectationsAPI.paramsString("Test 2") => "(2)"
		expectationsAPI.paramsString("Test 1") => "(1)"
		expectationsAPI.paramsString("Test 3") => null
	}

	fact "Exact single parameter matching works (int)" {
		stub [
			expectationsAPI.paramsInt(1)
			result = "(1)"

			expectationsAPI.paramsInt(2)
			result = "(2)"

			expectationsAPI.paramsInt(-4)
			result = "(-4)"
		]

		expectationsAPI.paramsInt(0) => null
		expectationsAPI.paramsInt(-4) => "(-4)"
		expectationsAPI.paramsInt(2) => "(2)"
		expectationsAPI.paramsInt(1) => "(1)"
		expectationsAPI.paramsInt(3) => null

		expectationsAPI.paramsInt(0) => null
		expectationsAPI.paramsInt(-4) => "(-4)"
		expectationsAPI.paramsInt(2) => "(2)"
		expectationsAPI.paramsInt(1) => "(1)"
		expectationsAPI.paramsInt(3) => null
	}

	fact "Exact single parameter matching works (long)" {
		stub [
			expectationsAPI.paramsLong(1)
			result = "(1)"

			expectationsAPI.paramsLong(2)
			result = "(2)"

			expectationsAPI.paramsLong(-4)
			result = "(-4)"
		]

		expectationsAPI.paramsLong(0) => null
		expectationsAPI.paramsLong(-4) => "(-4)"
		expectationsAPI.paramsLong(2) => "(2)"
		expectationsAPI.paramsLong(1) => "(1)"
		expectationsAPI.paramsLong(3) => null

		expectationsAPI.paramsLong(0) => null
		expectationsAPI.paramsLong(-4) => "(-4)"
		expectationsAPI.paramsLong(2) => "(2)"
		expectationsAPI.paramsLong(1) => "(1)"
		expectationsAPI.paramsLong(3) => null
	}

	fact "Exact single parameter matching works (short)" {
		stub [
			expectationsAPI.paramsShort(1 as short)
			result = "(1)"

			expectationsAPI.paramsShort(2 as short)
			result = "(2)"

			expectationsAPI.paramsShort((-4) as short)
			result = "(-4)"
		]

		expectationsAPI.paramsShort(0 as short) => null
		expectationsAPI.paramsShort((-4) as short) => "(-4)"
		expectationsAPI.paramsShort(2 as short) => "(2)"
		expectationsAPI.paramsShort(1 as short) => "(1)"
		expectationsAPI.paramsShort(3 as short) => null

		expectationsAPI.paramsShort(0 as short) => null
		expectationsAPI.paramsShort((-4) as short) => "(-4)"
		expectationsAPI.paramsShort(2 as short) => "(2)"
		expectationsAPI.paramsShort(1 as short) => "(1)"
		expectationsAPI.paramsShort(3 as short) => null
	}

	fact "Exact single parameter matching works (byte)" {
		stub [
			expectationsAPI.paramsByte(1 as byte)
			result = "(1)"

			expectationsAPI.paramsByte(2 as byte)
			result = "(2)"

			expectationsAPI.paramsByte((-4) as byte)
			result = "(-4)"
		]

		expectationsAPI.paramsByte(0 as byte) => null
		expectationsAPI.paramsByte((-4) as byte) => "(-4)"
		expectationsAPI.paramsByte(2 as byte) => "(2)"
		expectationsAPI.paramsByte(1 as byte) => "(1)"
		expectationsAPI.paramsByte(3 as byte) => null

		expectationsAPI.paramsByte(0 as byte) => null
		expectationsAPI.paramsByte((-4) as byte) => "(-4)"
		expectationsAPI.paramsByte(2 as byte) => "(2)"
		expectationsAPI.paramsByte(1 as byte) => "(1)"
		expectationsAPI.paramsByte(3 as byte) => null
	}

	fact "Exact single parameter matching works (char)" {
		stub [
			expectationsAPI.paramsChar("1".charAt(0))
			result = "(1)"

			expectationsAPI.paramsChar("2".charAt(0))
			result = "(2)"

			expectationsAPI.paramsChar("x".charAt(0))
			result = "(x)"
		]

		expectationsAPI.paramsChar("0".charAt(0)) => null
		expectationsAPI.paramsChar("x".charAt(0)) => "(x)"
		expectationsAPI.paramsChar("2".charAt(0)) => "(2)"
		expectationsAPI.paramsChar("1".charAt(0)) => "(1)"
		expectationsAPI.paramsChar("3".charAt(0)) => null

		expectationsAPI.paramsChar("0".charAt(0)) => null
		expectationsAPI.paramsChar("x".charAt(0)) => "(x)"
		expectationsAPI.paramsChar("2".charAt(0)) => "(2)"
		expectationsAPI.paramsChar("1".charAt(0)) => "(1)"
		expectationsAPI.paramsChar("3".charAt(0)) => null
	}

	fact "Exact single parameter matching works (boolean)" {
		stub [
			expectationsAPI.paramsBoolean(true)
			result = "(x)"
		]

		expectationsAPI.paramsBoolean(false) => null
		expectationsAPI.paramsBoolean(true) => "(x)"
		expectationsAPI.paramsBoolean(true) => "(x)"
		expectationsAPI.paramsBoolean(false) => null
	}

	fact "Exact multiple parameter matching works" {
		stub [
			expectationsAPI.paramsIntInt(1, 2)
			result = "(1, 2)"

			expectationsAPI.paramsIntInt(3, 4)
			result = "(3, 4)"

			expectationsAPI.paramsIntIntInt(-5, 6, -7)
			result = "(-5, 6, -7)"

			expectationsAPI.paramsString(null)
			result = "(-)"
		]

		expectationsAPI.paramsIntInt(2, 1) => null
		expectationsAPI.paramsIntIntInt(-5, 6, -7) => "(-5, 6, -7)"
		expectationsAPI.paramsIntIntInt(-15, 6, -7) => null
		expectationsAPI.paramsIntIntInt(-5, 16, -7) => null
		expectationsAPI.paramsIntIntInt(-15, 6, -17) => null
		expectationsAPI.paramsIntInt(3, 4) => "(3, 4)"
		expectationsAPI.paramsIntInt(1, 1) => null
		expectationsAPI.paramsIntInt(1, 2) => "(1, 2)"
	}

	fact "Matching with any() and with() works (String)" {
		stub [
			expectationsAPI.paramsStringString(any, with("test1"))
			result = "(*, test1)"

			expectationsAPI.paramsStringString(with("test2"), any)
			result = "(test2, *)"

			expectationsAPI.paramsStringString(<String>any, any)
			result = "(*, *)"

			expectationsAPI.paramsStringStringString(with("-5"), any, with("-7"))
			result = "(-5, *, -7)"
		]

		expectationsAPI.paramsStringString("12345", "test1") =>  "(*, test1)"
		expectationsAPI.paramsStringString("test2", "test1") =>  "(*, test1)"
		expectationsAPI.paramsStringString("test2", "12345") =>  "(test2, *)"
		expectationsAPI.paramsStringString("12345", "12345") =>  "(*, *)"

		expectationsAPI.paramsStringStringString("-5", "42", "-7") => "(-5, *, -7)"
		expectationsAPI.paramsStringStringString("-6", "42", "-7") => null
		expectationsAPI.paramsStringStringString("-5", "42", "-8") => null
	}

	fact "Matching with any() and with() works (with String and nulls)" {
		stub [
			expectationsAPI.paramsStringString(with(null), with(null))
			result = "(null, null)"

			expectationsAPI.paramsStringString(any, with(null))
			result = "(*, null)"

			expectationsAPI.paramsStringString(any, null)
			result = "(*, *)"
		]

		expectationsAPI.paramsStringString("12345", null) =>  "(*, null)"
		expectationsAPI.paramsStringString(null, null) =>  "(null, null)"
		expectationsAPI.paramsStringString("12345", "12345") =>  "(*, *)"
	}

	fact "Matching with any() and with() works (Int)" {
		stub [
			expectationsAPI.paramsIntInt(anyInt, withInt(1))
			result = "(*, 1)"

			expectationsAPI.paramsIntInt(with(2), anyInt)
			result = "(2, *)"

			expectationsAPI.paramsIntInt(anyInt, anyInt)
			result = "(*, *)"

			expectationsAPI.paramsIntIntInt(with(-5), anyInt, with(-7))
			result = "(-5, *, -7)"
		]

		expectationsAPI.paramsIntInt(12345, 1) =>  "(*, 1)"
		expectationsAPI.paramsIntInt(2, 1) =>  "(*, 1)"
		expectationsAPI.paramsIntInt(2, 12345) =>  "(2, *)"
		expectationsAPI.paramsIntInt(12345, 12345) =>  "(*, *)"

		expectationsAPI.paramsIntIntInt(-5, 42, -7) => "(-5, *, -7)"
		expectationsAPI.paramsIntIntInt(-6, 42, -7) => null
		expectationsAPI.paramsIntIntInt(-5, 42, -8) => null
	}

	fact "Matching with any() and with() works (Long)" {
		stub [
			expectationsAPI.paramsLongLong(anyLong, withLong(1))
			result = "(*, 1)"

			expectationsAPI.paramsLongLong(with(2L), anyLong)
			result = "(2, *)"

			expectationsAPI.paramsLongLong(anyLong, anyLong)
			result = "(*, *)"

			expectationsAPI.paramsLongLongLong(with(-5L), anyLong, with(-7L))
			result = "(-5, *, -7)"
		]

		expectationsAPI.paramsLongLong(12345, 1) =>  "(*, 1)"
		expectationsAPI.paramsLongLong(2, 1) =>  "(*, 1)"
		expectationsAPI.paramsLongLong(2, 12345) =>  "(2, *)"
		expectationsAPI.paramsLongLong(12345, 12345) =>  "(*, *)"

		expectationsAPI.paramsLongLongLong(-5, 42, -7) => "(-5, *, -7)"
		expectationsAPI.paramsLongLongLong(-6, 42, -7) => null
		expectationsAPI.paramsLongLongLong(-5, 42, -8) => null
	}

	fact "Matching with any() and with() works (Short)" {
		stub [
			expectationsAPI.paramsShortShort(anyShort, withShort(1 as short))
			result = "(*, 1)"

			expectationsAPI.paramsShortShort(with(2 as short), anyShort)
			result = "(2, *)"

			expectationsAPI.paramsShortShort(anyShort, anyShort)
			result = "(*, *)"

			expectationsAPI.paramsShortShortShort(with((-5) as short), anyShort, with((-7) as short))
			result = "(-5, *, -7)"
		]

		expectationsAPI.paramsShortShort(12345 as short, 1 as short) =>  "(*, 1)"
		expectationsAPI.paramsShortShort(2 as short, 1 as short) =>  "(*, 1)"
		expectationsAPI.paramsShortShort(2 as short, 12345 as short) =>  "(2, *)"
		expectationsAPI.paramsShortShort(12345 as short, 12345 as short) =>  "(*, *)"

		expectationsAPI.paramsShortShortShort((-5) as short, 42 as short, (-7) as short) => "(-5, *, -7)"
		expectationsAPI.paramsShortShortShort((-6) as short, 42 as short, (-7) as short) => null
		expectationsAPI.paramsShortShortShort((-5) as short, 42 as short, (-8) as short) => null
	}
	fact "Matching with any() and with() works (Byte)" {
		stub [
			expectationsAPI.paramsByteByte(anyByte, withByte(1 as byte))
			result = "(*, 1)"

			expectationsAPI.paramsByteByte(with(2 as byte), anyByte)
			result = "(2, *)"

			expectationsAPI.paramsByteByte(anyByte, anyByte)
			result = "(*, *)"

			expectationsAPI.paramsByteByteByte(with((-5) as byte), anyByte, with((-7) as byte))
			result = "(-5, *, -7)"
		]

		expectationsAPI.paramsByteByte(123 as byte, 1 as byte) =>  "(*, 1)"
		expectationsAPI.paramsByteByte(2 as byte, 1 as byte) =>  "(*, 1)"
		expectationsAPI.paramsByteByte(2 as byte, 123 as byte) =>  "(2, *)"
		expectationsAPI.paramsByteByte(123 as byte, 123 as byte) =>  "(*, *)"

		expectationsAPI.paramsByteByteByte((-5) as byte, 42 as byte, (-7) as byte) => "(-5, *, -7)"
		expectationsAPI.paramsByteByteByte((-6) as byte, 42 as byte, (-7) as byte) => null
		expectationsAPI.paramsByteByteByte((-5) as byte, 42 as byte, (-8) as byte) => null
	}
	fact "Matching with any() and with() works (Float)" {
		stub [
			expectationsAPI.paramsFloatFloat(anyFloat, withFloat(1 as float))
			result = "(*, 1)"

			expectationsAPI.paramsFloatFloat(with(2 as float), anyFloat)
			result = "(2, *)"

			expectationsAPI.paramsFloatFloat(anyFloat, anyFloat)
			result = "(*, *)"

			expectationsAPI.paramsFloatFloatFloat(with((-5) as float), anyFloat, with((-7) as float))
			result = "(-5, *, -7)"
		]

		expectationsAPI.paramsFloatFloat(12345 as float, 1 as float) =>  "(*, 1)"
		expectationsAPI.paramsFloatFloat(2 as float, 1 as float) =>  "(*, 1)"
		expectationsAPI.paramsFloatFloat(2 as float, 12345 as float) =>  "(2, *)"
		expectationsAPI.paramsFloatFloat(12345 as float, 12345 as float) =>  "(*, *)"

		expectationsAPI.paramsFloatFloatFloat((-5) as float, 42 as float, (-7) as float) => "(-5, *, -7)"
		expectationsAPI.paramsFloatFloatFloat((-6) as float, 42 as float, (-7) as float) => null
		expectationsAPI.paramsFloatFloatFloat((-5) as float, 42 as float, (-8) as float) => null
	}
	fact "Matching with any() and with() works (Double)" {
		stub [
			expectationsAPI.paramsDoubleDouble(anyDouble, withDouble(1 as double))
			result = "(*, 1)"

			expectationsAPI.paramsDoubleDouble(with(2 as double), anyDouble)
			result = "(2, *)"

			expectationsAPI.paramsDoubleDouble(anyDouble, anyDouble)
			result = "(*, *)"

			expectationsAPI.paramsDoubleDoubleDouble(with((-5) as double), anyDouble, with((-7) as double))
			result = "(-5, *, -7)"
		]

		expectationsAPI.paramsDoubleDouble(12345 as double, 1 as double) =>  "(*, 1)"
		expectationsAPI.paramsDoubleDouble(2 as double, 1 as double) =>  "(*, 1)"
		expectationsAPI.paramsDoubleDouble(2 as double, 12345 as double) =>  "(2, *)"
		expectationsAPI.paramsDoubleDouble(12345 as double, 12345 as double) =>  "(*, *)"

		expectationsAPI.paramsDoubleDoubleDouble((-5) as double, 42 as double, (-7) as double) => "(-5, *, -7)"
		expectationsAPI.paramsDoubleDoubleDouble((-6) as double, 42 as double, (-7) as double) => null
		expectationsAPI.paramsDoubleDoubleDouble((-5) as double, 42 as double, (-8) as double) => null
	}
	fact "Matching with any() and with() works (Char)" {
		stub [
			expectationsAPI.paramsCharChar(anyChar, withChar(1 as char))
			result = "(*, 1)"

			expectationsAPI.paramsCharChar(with(2 as char), anyChar)
			result = "(2, *)"

			expectationsAPI.paramsCharChar(anyChar, anyChar)
			result = "(*, *)"

			expectationsAPI.paramsCharCharChar(with((-5) as char), anyChar, with((-7) as char))
			result = "(-5, *, -7)"
		]

		expectationsAPI.paramsCharChar(12345 as char, 1 as char) =>  "(*, 1)"
		expectationsAPI.paramsCharChar(2 as char, 1 as char) =>  "(*, 1)"
		expectationsAPI.paramsCharChar(2 as char, 12345 as char) =>  "(2, *)"
		expectationsAPI.paramsCharChar(12345 as char, 12345 as char) =>  "(*, *)"

		expectationsAPI.paramsCharCharChar((-5) as char, 42 as char, (-7) as char) => "(-5, *, -7)"
		expectationsAPI.paramsCharCharChar((-6) as char, 42 as char, (-7) as char) => null
		expectationsAPI.paramsCharCharChar((-5) as char, 42 as char, (-8) as char) => null
	}
	fact "Matching with any() and with() works (Boolean)" {
		stub [
			expectationsAPI.paramsBooleanBoolean(anyBoolean, withBoolean(true))
			result = "(*, true)"

			expectationsAPI.paramsBooleanBoolean(with(false), anyBoolean)
			result = "(false, *)"

			expectationsAPI.paramsBooleanBooleanBoolean(with(false), anyBoolean, with(true))
			result = "(false, *, true)"
		]

		expectationsAPI.paramsBooleanBoolean(false, true) =>  "(*, true)"
		expectationsAPI.paramsBooleanBoolean(true, true) =>  "(*, true)"
		expectationsAPI.paramsBooleanBoolean(false, false) =>  "(false, *)"

		expectationsAPI.paramsBooleanBooleanBoolean(false, true, true) => "(false, *, true)"
		expectationsAPI.paramsBooleanBooleanBoolean(false, false, true) => "(false, *, true)"
		expectationsAPI.paramsBooleanBooleanBoolean(false, false, false) => null
		expectationsAPI.paramsBooleanBooleanBoolean(false, true, false) => null
		expectationsAPI.paramsBooleanBooleanBoolean(true, false, true) => null
		expectationsAPI.paramsBooleanBooleanBoolean(true, true, true) => null
		expectationsAPI.paramsBooleanBooleanBoolean(true, false, false) => null
		expectationsAPI.paramsBooleanBooleanBoolean(true, true, false) => null
	}
}