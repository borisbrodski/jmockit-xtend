package org.eclipse.xtend.jmockit.test.expectations

import mockit.Mocked
import static extension org.eclipse.xtend.jmockit.JMockitExtension.*
import mockit.internal.UnexpectedInvocation
import static org.junit.Assert.*

describe "mock behaves like Expectations" {

    context "Non-partial mocking" {
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

    }

    fact "Partially mocking" {
        mock(ExpectationsAPI)

        mock [
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

    fact "Dynamic partial mock" {
        mock(ExpectationsAPI) [
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

    fact "Dynamic partial mock (2 parameters)" {
        val o1 = new Object
        val o2 = new Object
        mock(o1, o2) [
            o1.toString
            result = "(o1)"

            o2.toString
            result = "(o2)"
        ]
        o1.toString => "(o1)"
        o2.toString => "(o2)"
    }

    fact "Dynamic partial mock (3 parameters)" {
        val o1 = new Object
        val o2 = new Object
        val o3 = new Object
        mock(o1, o2, o3) [
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

    fact "Dynamic partial mock (4 parameters)" {
        val o1 = new Object
        val o2 = new Object
        val o3 = new Object
        val o4 = new Object
        mock(o1, o2, o3, o4) [
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

    fact "Dynamic partial mock (5 parameters)" {
        val o1 = new Object
        val o2 = new Object
        val o3 = new Object
        val o4 = new Object
        val o5 = new Object
        mock(o1, o2, o3, o4, o5) [
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

    fact "Dynamic partial mock (X parameters)" {
        val o1 = new Object
        val o2 = new Object
        val o3 = new Object
        val o4 = new Object
        val o5 = new Object
        val o6 = new Object
        mock([
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

    fact "mock with iterations and partial mockbing (1 parameters)" {
        val o1 = new Object
        mock(o1) [
            o1.toString
            result = "(o1)"
        ]
        o1.toString => "(o1)"
    }

    fact "mock with iterations and partial mockbing (2 parameters)" {
        val o1 = new Object
        val o2 = new Object
        mock(2, o1, o2) [
            o1.toString
            result = "(o1)"

            o2.toString
            result = "(o2)"
        ]
        o1.toString => "(o1)"
        o2.toString => "(o2)"
    }

    fact "mock with iterations and partial mockbing (3 parameters)" {
        val o1 = new Object
        val o2 = new Object
        val o3 = new Object
        mock(2, o1, o2, o3) [
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

    fact "mock with iterations and partial mockbing (4 parameters)" {
        val o1 = new Object
        val o2 = new Object
        val o3 = new Object
        val o4 = new Object
        mock(2, o1, o2, o3, o4) [
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

    fact "mock with iterations and partial mockbing (5 parameters)" {
        val o1 = new Object
        val o2 = new Object
        val o3 = new Object
        val o4 = new Object
        val o5 = new Object
        mock(2, o1, o2, o3, o4, o5) [
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

    fact "mock with iterations and partial mockbing (X parameters)" {
        val o1 = new Object
        val o2 = new Object
        val o3 = new Object
        val o4 = new Object
        val o5 = new Object
        val o6 = new Object
        mock([
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
