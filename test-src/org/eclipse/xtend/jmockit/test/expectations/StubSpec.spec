package org.eclipse.xtend.jmockit.test.expectations

import mockit.Mocked
import static org.junit.Assert.*
import static extension org.eclipse.xtend.jmockit.JMockitExtension.*

describe "stub behaves like NonStrictExpectations" {

	@Mocked
	ExpectationsAPI expectationsAPI

	fact "The order and number of call is not important" {
		stub [
			expectationsAPI.returnString
			result = "My string"

			expectationsAPI.returnInt
			result = 12345
		]

		expectationsAPI.returnString => "My string"
		expectationsAPI.returnString => "My string"
		expectationsAPI.returnInt => 12345
		expectationsAPI.returnInt => 12345
		expectationsAPI.returnString => "My string"
		expectationsAPI.returnInt => 12345
		expectationsAPI.returnSelf => null
	}

	fact "Dynamic partial stub" {
		stub(ExpectationsAPI) [
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
		(new ExpectationsAPI).returnString => "My string 1"
	}

	fact "Dynamic partial stub (2 parameters)" {
		val o1 = new Object
		val o2 = new Object
		stub(o1, o2) [
			o1.toString
			result = "(o1)"

			o2.toString
			result = "(o2)"
		]
		o1.toString => "(o1)"
		o2.toString => "(o2)"
	}

	fact "Dynamic partial stub (3 parameters)" {
		val o1 = new Object
		val o2 = new Object
		val o3 = new Object
		stub(o1, o2, o3) [
			o1.toString
			result = "(o1)"

			o2.toString
			result = "(o2)"

			o3.toString
			result = "(o3)"
		]
		o1.toString => "(o1)"
		o2.toString => "(o2)"
		o3.toString => "(o3)"
	}

	fact "Dynamic partial stub (4 parameters)" {
		val o1 = new Object
		val o2 = new Object
		val o3 = new Object
		val o4 = new Object
		stub(o1, o2, o3, o4) [
			o1.toString
			result = "(o1)"

			o2.toString
			result = "(o2)"

			o3.toString
			result = "(o3)"

			o4.toString
			result = "(o4)"
		]
		o1.toString => "(o1)"
		o2.toString => "(o2)"
		o3.toString => "(o3)"
		o4.toString => "(o4)"
	}

	fact "Dynamic partial stub (5 parameters)" {
		val o1 = new Object
		val o2 = new Object
		val o3 = new Object
		val o4 = new Object
		val o5 = new Object
		stub(o1, o2, o3, o4, o5) [
			o1.toString
			result = "(o1)"

			o2.toString
			result = "(o2)"

			o3.toString
			result = "(o3)"

			o4.toString
			result = "(o4)"

			o5.toString
			result = "(o5)"
		]
		o1.toString => "(o1)"
		o2.toString => "(o2)"
		o3.toString => "(o3)"
		o4.toString => "(o4)"
		o5.toString => "(o5)"
	}

	fact "Dynamic partial stub (X parameters)" {
		val o1 = new Object
		val o2 = new Object
		val o3 = new Object
		val o4 = new Object
		val o5 = new Object
		val o6 = new Object
		stub([
			o1.toString
			result = "(o1)"

			o2.toString
			result = "(o2)"

			o3.toString
			result = "(o3)"

			o4.toString
			result = "(o4)"

			o5.toString
			result = "(o5)"

			o6.toString
			result = "(o6)"
		], o1, o2, o3, o4, o5, o6)
		o1.toString => "(o1)"
		o2.toString => "(o2)"
		o3.toString => "(o3)"
		o4.toString => "(o4)"
		o5.toString => "(o5)"
		o6.toString => "(o6)"
	}

    fact "stub with iterations" {
        stub(2) [
            expectationsAPI.returnString
            returns("a", "b", "c")

            expectationsAPI.returnInt
            result = 1
            result = 2
        ]

        expectationsAPI.returnString => "a"
        expectationsAPI.returnString => "b"
        expectationsAPI.returnString => "c"
        expectationsAPI.returnString => "c" // TODO Fix after issue resolved: https://github.com/jmockit/jmockit1/issues/60

        expectationsAPI.returnInt => 1
        expectationsAPI.returnInt => 2
        expectationsAPI.returnInt => 2 // TODO Fix after issue resolved: https://github.com/jmockit/jmockit1/issues/60

        expectationsAPI.returnSelf => null
    }

    fact "stub with iterations and partial stubbing (1 parameters)" {
        val o1 = new Object
        stub(2, o1) [
            o1.toString
            result = "(o1)"
        ]
        o1.toString => "(o1)"
    }

    fact "stub with iterations and partial stubbing (2 parameters)" {
        val o1 = new Object
        val o2 = new Object
        stub(2, o1, o2) [
            o1.toString
            result = "(o1)"

            o2.toString
            result = "(o2)"
        ]
        o1.toString => "(o1)"
        o2.toString => "(o2)"
    }

    fact "stub with iterations and partial stubbing (3 parameters)" {
        val o1 = new Object
        val o2 = new Object
        val o3 = new Object
        stub(2, o1, o2, o3) [
            o1.toString
            result = "(o1)"

            o2.toString
            result = "(o2)"

            o3.toString
            result = "(o3)"
        ]
        o1.toString => "(o1)"
        o2.toString => "(o2)"
        o3.toString => "(o3)"
    }

    fact "stub with iterations and partial stubbing (4 parameters)" {
        val o1 = new Object
        val o2 = new Object
        val o3 = new Object
        val o4 = new Object
        stub(2, o1, o2, o3, o4) [
            o1.toString
            result = "(o1)"

            o2.toString
            result = "(o2)"

            o3.toString
            result = "(o3)"

            o4.toString
            result = "(o4)"
        ]
        o1.toString => "(o1)"
        o2.toString => "(o2)"
        o3.toString => "(o3)"
        o4.toString => "(o4)"
    }

    fact "stub with iterations and partial stubbing (5 parameters)" {
        val o1 = new Object
        val o2 = new Object
        val o3 = new Object
        val o4 = new Object
        val o5 = new Object
        stub(2, o1, o2, o3, o4, o5) [
            o1.toString
            result = "(o1)"

            o2.toString
            result = "(o2)"

            o3.toString
            result = "(o3)"

            o4.toString
            result = "(o4)"

            o5.toString
            result = "(o5)"
        ]
        o1.toString => "(o1)"
        o2.toString => "(o2)"
        o3.toString => "(o3)"
        o4.toString => "(o4)"
        o5.toString => "(o5)"
    }

    fact "stub with iterations and partial stubbing (X parameters)" {
        val o1 = new Object
        val o2 = new Object
        val o3 = new Object
        val o4 = new Object
        val o5 = new Object
        val o6 = new Object
        stub([
            o1.toString
            result = "(o1)"

            o2.toString
            result = "(o2)"

            o3.toString
            result = "(o3)"

            o4.toString
            result = "(o4)"

            o5.toString
            result = "(o5)"

            o6.toString
            result = "(o6)"
        ], 2, o1, o2, o3, o4, o5, o6)
        o1.toString => "(o1)"
        o2.toString => "(o2)"
        o3.toString => "(o3)"
        o4.toString => "(o4)"
        o5.toString => "(o5)"
        o6.toString => "(o6)"
    }
}