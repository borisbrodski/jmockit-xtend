package org.eclipse.xtend.jmockit.test.expectations

import mockit.Mocked
import mockit.internal.UnexpectedInvocation

import static extension org.eclipse.xtend.jmockit.JMockitExtension.*
import org.hamcrest.Matchers

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

        fact "mock with iterations" {
            mock(2) [
                expectationsAPI.returnString
                returns("a", "b")

                expectationsAPI.returnInt
                result = 1
                maxTimes = 2
            ]

            expectationsAPI.returnString => "a"
            expectationsAPI.returnString => "b"

            expectationsAPI.returnInt => 1
            expectationsAPI.returnInt => 1
            expectationsAPI.returnString => "b"
            expectationsAPI.returnString => "b"
            expectationsAPI.returnInt => 1
            expectationsAPI.returnInt => 1
            expectationsAPI.returnString throws UnexpectedInvocation
            expectationsAPI.returnInt throws UnexpectedInvocation
            expectationsAPI.returnSelf throws UnexpectedInvocation
        }

		fact "Get faked instance of any class" {
			mock [
				ins(ClassWithNoSuitableConstructor) => Matchers.instanceOf(ClassWithNoSuitableConstructor)
			]
		}
    }

    fact "Partially mocking" {
        mock(ExpectationsAPI)

        mock [
            (new ExpectationsAPI).returnString
            result = "My string 1"
        ]

        (new ExpectationsAPI).returnString => "My string 1"
        (new ExpectationsAPI).returnVoid throws NotMocked
        (new ExpectationsAPI).returnString => "My string 1"
    }

    fact "Partially mock single class returns instance of the class" {
        val api = mock(ExpectationsAPI)

        mock [
            api.returnString
            result = "My string 1"
        ]

        api.returnString => "My string 1"
        api.returnVoid throws NotMocked
        api.returnString => "My string 1"
    }

    fact "Dynamic partial mock (1 parameters)" {
        mock(ExpectationsAPI) [
            (new ExpectationsAPI).returnString
            result = "My string 1"
        ]

        (new ExpectationsAPI).returnString => "My string 1"
        (new ExpectationsAPI).returnVoid throws NotMocked
        (new ExpectationsAPI).returnString throws NotMocked
    }

    fact "Dynamic partial mock with instance parameters (1 parameters)" {
        mock(ExpectationsAPI) [ it, api |
            api.returnString
            result = "My string 1"
        ]

        (new ExpectationsAPI).returnString => "My string 1"
        (new ExpectationsAPI).returnVoid throws NotMocked
        (new ExpectationsAPI).returnString throws NotMocked
    }

    fact "Dynamic partial mock instances (1 parameters)" {
    	val api = new ExpectationsAPI()
        mock(api) [
            api.returnString
            result = "My string 1"
        ]

        api.returnString => "My string 1"
        api.returnString throws NotMocked
        (new ExpectationsAPI).returnString throws NotMocked
        (new ExpectationsAPI).returnVoid throws NotMocked
    }

    fact "Dynamic partial mock with iterations (1 parameters)" {
        mock(2, ExpectationsAPI) [
            (new ExpectationsAPI).returnString
            result = "My string 1"
        ]

        (new ExpectationsAPI).returnString => "My string 1"
        (new ExpectationsAPI).returnString => "My string 1"
        (new ExpectationsAPI).returnVoid throws NotMocked
        (new ExpectationsAPI).returnString throws NotMocked
    }

    fact "Dynamic partial mock with instance parameters with iterations (1 parameters)" {
        mock(2, ExpectationsAPI) [ it, api |
            api.returnString
            result = "My string 1"
        ]

        (new ExpectationsAPI).returnString => "My string 1"
        (new ExpectationsAPI).returnString => "My string 1"
        (new ExpectationsAPI).returnVoid throws NotMocked
        (new ExpectationsAPI).returnString throws NotMocked
    }

    fact "Dynamic partial mock instances with iterations (1 parameters)" {
        val o1 = new PartialMock1API
        mock(2, o1) [
            o1.toBeMocked
            result = "(o1)"
        ]
        o1.toBeMocked => "(o1)"
        o1.toBeMocked => "(o1)"
        o1.toBeMocked throws NotMocked
    }

    fact "Dynamic partial mock (2 parameters)" {
        mock(PartialMock1API, PartialMock2API) [
            new PartialMock1API().toBeMocked
            result = "(o1)"

            new PartialMock2API().toBeMocked
            result = "(o2)"
        ]

        new PartialMock1API().toBeMocked => "(o1)"
        new PartialMock2API().toBeMocked => "(o2)"
        new PartialMock1API().notToBeMocked throws NotMocked
        new PartialMock2API().notToBeMocked throws NotMocked
    }

    fact "Dynamic partial mock with instance parameters (2 parameters)" {
        mock(PartialMock1API, PartialMock2API) [it, api1, api2 |
            api1.toBeMocked
            result = "(o1)"

            api2.toBeMocked
            result = "(o2)"
        ]
        new PartialMock1API().toBeMocked => "(o1)"
        new PartialMock2API().toBeMocked => "(o2)"
        new PartialMock1API().notToBeMocked throws NotMocked
        new PartialMock2API().notToBeMocked throws NotMocked
    }

    fact "Dynamic partial mock instances (2 parameters)" {
        val o1 = new PartialMock1API
        val o2 = new PartialMock1API
        mock(o1, o2) [
            o1.toBeMocked
            result = "(o1)"

            o2.toBeMocked
            result = "(o2)"
        ]
        o1.toBeMocked => "(o1)"
        o2.toBeMocked => "(o2)"
    }

    fact "Dynamic partial mock with iterations (2 parameters)" {
        mock(2, PartialMock1API, PartialMock2API) [
            new PartialMock1API().toBeMocked
            result = "(o1)"

            new PartialMock2API().toBeMocked
            result = "(o2)"
        ]

        new PartialMock1API().toBeMocked => "(o1)"
        new PartialMock2API().toBeMocked => "(o2)"
        new PartialMock1API().toBeMocked => "(o1)"
        new PartialMock2API().toBeMocked => "(o2)"
        new PartialMock1API().notToBeMocked throws NotMocked
        new PartialMock2API().notToBeMocked throws NotMocked
        new PartialMock2API().toBeMocked throws NotMocked
    }

    fact "Dynamic partial mock with instance parameters with iterations (2 parameters)" {
        mock(2, PartialMock1API, PartialMock2API) [it, api1, api2 |
            api1.toBeMocked
            result = "(o1)"

            api2.toBeMocked
            result = "(o2)"
        ]
        new PartialMock1API().toBeMocked => "(o1)"
        new PartialMock2API().toBeMocked => "(o2)"
        new PartialMock1API().toBeMocked => "(o1)"
        new PartialMock2API().toBeMocked => "(o2)"
        new PartialMock1API().notToBeMocked throws NotMocked
        new PartialMock2API().notToBeMocked throws NotMocked
        new PartialMock2API().toBeMocked throws NotMocked
    }

    fact "Dynamic partial mock instances with iterations (2 parameters)" {
        val o1 = new PartialMock1API
        val o2 = new PartialMock1API
        mock(2, o1, o2) [
            o1.toBeMocked
            result = "(o1)"

            o2.toBeMocked
            result = "(o2)"
        ]
        o1.toBeMocked => "(o1)"
        o2.toBeMocked => "(o2)"
        o1.toBeMocked => "(o1)"
        o2.toBeMocked => "(o2)"

        new PartialMock1API().notToBeMocked throws NotMocked
        new PartialMock2API().notToBeMocked throws NotMocked
    }

    fact "Dynamic partial mock (3 parameters)" {
        mock(PartialMock1API, PartialMock2API, PartialMock3API) [
            new PartialMock1API().toBeMocked
            result = "(o1)"

            new PartialMock2API().toBeMocked
            result = "(o2)"

            new PartialMock3API().toBeMocked
            result = "(o3)"
        ]

        new PartialMock1API().toBeMocked => "(o1)"
        new PartialMock2API().toBeMocked => "(o2)"
        new PartialMock3API().toBeMocked => "(o3)"
        new PartialMock1API().notToBeMocked throws NotMocked
        new PartialMock2API().notToBeMocked throws NotMocked
        new PartialMock3API().notToBeMocked throws NotMocked
    }

    fact "Dynamic partial mock with instance parameters (3 parameters)" {
        mock(PartialMock1API, PartialMock2API, PartialMock3API) [it, api1, api2, api3 |
            api1.toBeMocked
            result = "(o1)"

            api2.toBeMocked
            result = "(o2)"

            api3.toBeMocked
            result = "(o3)"
        ]
        new PartialMock1API().toBeMocked => "(o1)"
        new PartialMock2API().toBeMocked => "(o2)"
        new PartialMock3API().toBeMocked => "(o3)"
        new PartialMock1API().notToBeMocked throws NotMocked
        new PartialMock2API().notToBeMocked throws NotMocked
        new PartialMock3API().notToBeMocked throws NotMocked
    }

    fact "Dynamic partial mock instances (3 parameters)" {
        val o1 = new PartialMock1API
        val o2 = new PartialMock1API
        val o3 = new PartialMock1API
        mock(o1, o2, o3) [
            o1.toBeMocked
            result = "(o1)"

            o2.toBeMocked
            result = "(o2)"

            o3.toBeMocked
            result = "(o3)"
        ]
        o1.toBeMocked => "(o1)"
        o2.toBeMocked => "(o2)"
        o3.toBeMocked => "(o3)"

        new PartialMock1API().toBeMocked throws NotMocked
        new PartialMock2API().toBeMocked throws NotMocked
        new PartialMock3API().toBeMocked throws NotMocked
    }


    fact "Dynamic partial mock with iterations (3 parameters)" {
        mock(2, PartialMock1API, PartialMock2API, PartialMock3API) [
            new PartialMock1API().toBeMocked
            result = "(o1)"

            new PartialMock2API().toBeMocked
            result = "(o2)"

            new PartialMock3API().toBeMocked
            result = "(o3)"
        ]

        new PartialMock1API().toBeMocked => "(o1)"
        new PartialMock2API().toBeMocked => "(o2)"
        new PartialMock3API().toBeMocked => "(o3)"
        new PartialMock1API().toBeMocked => "(o1)"
        new PartialMock2API().toBeMocked => "(o2)"
        new PartialMock3API().toBeMocked => "(o3)"
        new PartialMock1API().notToBeMocked throws NotMocked
        new PartialMock2API().notToBeMocked throws NotMocked
        new PartialMock3API().notToBeMocked throws NotMocked
        new PartialMock1API().toBeMocked throws NotMocked
        new PartialMock2API().toBeMocked throws NotMocked
        new PartialMock3API().toBeMocked throws NotMocked
    }

    fact "Dynamic partial mock with instance parameters with iterations (3 parameters)" {
        mock(2, PartialMock1API, PartialMock2API, PartialMock3API) [it, api1, api2, api3 |
            api1.toBeMocked
            result = "(o1)"

            api2.toBeMocked
            result = "(o2)"

            api3.toBeMocked
            result = "(o3)"
        ]
        new PartialMock1API().toBeMocked => "(o1)"
        new PartialMock2API().toBeMocked => "(o2)"
        new PartialMock3API().toBeMocked => "(o3)"
        new PartialMock1API().toBeMocked => "(o1)"
        new PartialMock2API().toBeMocked => "(o2)"
        new PartialMock3API().toBeMocked => "(o3)"
        new PartialMock1API().notToBeMocked throws NotMocked
        new PartialMock2API().notToBeMocked throws NotMocked
        new PartialMock3API().notToBeMocked throws NotMocked
    }

    fact "Dynamic partial mock instances with iterations (3 parameters)" {
        val o1 = new PartialMock1API
        val o2 = new PartialMock1API
        val o3 = new PartialMock1API
        mock(2, o1, o2, o3) [
            o1.toBeMocked
            result = "(o1)"

            o2.toBeMocked
            result = "(o2)"

            o3.toBeMocked
            result = "(o3)"
        ]
        o1.toBeMocked => "(o1)"
        o2.toBeMocked => "(o2)"
        o3.toBeMocked => "(o3)"
        o1.toBeMocked => "(o1)"
        o2.toBeMocked => "(o2)"
        o3.toBeMocked => "(o3)"
        o1.toBeMocked throws NotMocked
        o2.toBeMocked throws NotMocked
        o3.toBeMocked throws NotMocked
    }

    fact "Dynamic partial mock (4 parameters)" {
        mock(PartialMock1API, PartialMock2API, PartialMock3API, PartialMock4API) [
            new PartialMock1API().toBeMocked
            result = "(o1)"

            new PartialMock2API().toBeMocked
            result = "(o2)"

            new PartialMock3API().toBeMocked
            result = "(o3)"

            new PartialMock4API().toBeMocked
            result = "(o4)"
        ]
        new PartialMock1API().toBeMocked => "(o1)"
        new PartialMock2API().toBeMocked => "(o2)"
        new PartialMock3API().toBeMocked => "(o3)"
        new PartialMock4API().toBeMocked => "(o4)"
        new PartialMock1API().notToBeMocked throws NotMocked
        new PartialMock2API().notToBeMocked throws NotMocked
        new PartialMock3API().notToBeMocked throws NotMocked
        new PartialMock4API().notToBeMocked throws NotMocked
    }

    fact "Dynamic partial mock with instance parameters (4 parameters)" {
        mock(PartialMock1API, PartialMock2API, PartialMock3API, PartialMock4API) [it, api1, api2, api3, api4 |
            api1.toBeMocked
            result = "(o1)"

            api2.toBeMocked
            result = "(o2)"

            api3.toBeMocked
            result = "(o3)"

            api4.toBeMocked
            result = "(o4)"
        ]
        new PartialMock1API().toBeMocked => "(o1)"
        new PartialMock2API().toBeMocked => "(o2)"
        new PartialMock3API().toBeMocked => "(o3)"
        new PartialMock4API().toBeMocked => "(o4)"
        new PartialMock1API().notToBeMocked throws NotMocked
        new PartialMock2API().notToBeMocked throws NotMocked
        new PartialMock3API().notToBeMocked throws NotMocked
        new PartialMock4API().notToBeMocked throws NotMocked
    }

    fact "Dynamic partial mock instances (4 parameters)" {
        val o1 = new PartialMock1API
        val o2 = new PartialMock1API
        val o3 = new PartialMock1API
        val o4 = new PartialMock1API
        mock(o1, o2, o3, o4) [
            o1.toBeMocked
            result = "(o1)"

            o2.toBeMocked
            result = "(o2)"

            o3.toBeMocked
            result = "(o3)"

            o4.toBeMocked
            result = "(o4)"
        ]
        o1.toBeMocked => "(o1)"
        o2.toBeMocked => "(o2)"
        o3.toBeMocked => "(o3)"
        o4.toBeMocked => "(o4)"
    }


    fact "Dynamic partial mock with iterations (4 parameters)" {
        mock(2, PartialMock1API, PartialMock2API, PartialMock3API, PartialMock4API) [
            new PartialMock1API().toBeMocked
            result = "(o1)"

            new PartialMock2API().toBeMocked
            result = "(o2)"

            new PartialMock3API().toBeMocked
            result = "(o3)"

            new PartialMock4API().toBeMocked
            result = "(o4)"
        ]
        new PartialMock1API().toBeMocked => "(o1)"
        new PartialMock2API().toBeMocked => "(o2)"
        new PartialMock3API().toBeMocked => "(o3)"
        new PartialMock4API().toBeMocked => "(o4)"
        new PartialMock1API().toBeMocked => "(o1)"
        new PartialMock2API().toBeMocked => "(o2)"
        new PartialMock3API().toBeMocked => "(o3)"
        new PartialMock4API().toBeMocked => "(o4)"
        new PartialMock1API().notToBeMocked throws NotMocked
        new PartialMock2API().notToBeMocked throws NotMocked
        new PartialMock3API().notToBeMocked throws NotMocked
        new PartialMock4API().notToBeMocked throws NotMocked
    }

    fact "Dynamic partial mock with instance parameters with iterations (4 parameters)" {
        mock(2, PartialMock1API, PartialMock2API, PartialMock3API, PartialMock4API) [it, api1, api2, api3, api4 |
            api1.toBeMocked
            result = "(o1)"

            api2.toBeMocked
            result = "(o2)"

            api3.toBeMocked
            result = "(o3)"

            api4.toBeMocked
            result = "(o4)"
        ]
        new PartialMock1API().toBeMocked => "(o1)"
        new PartialMock2API().toBeMocked => "(o2)"
        new PartialMock3API().toBeMocked => "(o3)"
        new PartialMock4API().toBeMocked => "(o4)"
        new PartialMock1API().toBeMocked => "(o1)"
        new PartialMock2API().toBeMocked => "(o2)"
        new PartialMock3API().toBeMocked => "(o3)"
        new PartialMock4API().toBeMocked => "(o4)"
        new PartialMock1API().notToBeMocked throws NotMocked
        new PartialMock2API().notToBeMocked throws NotMocked
        new PartialMock3API().notToBeMocked throws NotMocked
        new PartialMock4API().notToBeMocked throws NotMocked
    }

    fact "Dynamic partial mock instances with iterations (4 parameters)" {
        val o1 = new PartialMock1API
        val o2 = new PartialMock1API
        val o3 = new PartialMock1API
        val o4 = new PartialMock1API
        mock(2, o1, o2, o3, o4) [
            o1.toBeMocked
            result = "(o1)"

            o2.toBeMocked
            result = "(o2)"

            o3.toBeMocked
            result = "(o3)"

            o4.toBeMocked
            result = "(o4)"
        ]
        o1.toBeMocked => "(o1)"
        o2.toBeMocked => "(o2)"
        o3.toBeMocked => "(o3)"
        o4.toBeMocked => "(o4)"
        o1.toBeMocked => "(o1)"
        o2.toBeMocked => "(o2)"
        o3.toBeMocked => "(o3)"
        o4.toBeMocked => "(o4)"
        o1.toBeMocked throws NotMocked
        o2.toBeMocked throws NotMocked
        o3.toBeMocked throws NotMocked
        o4.toBeMocked throws NotMocked
    }

    fact "Dynamic partial mock (5 parameters)" {
        mock(PartialMock1API, PartialMock2API, PartialMock3API, PartialMock4API, PartialMock5API) [
            new PartialMock1API().toBeMocked
            result = "(o1)"

            new PartialMock2API().toBeMocked
            result = "(o2)"

            new PartialMock3API().toBeMocked
            result = "(o3)"

            new PartialMock4API().toBeMocked
            result = "(o4)"

            new PartialMock5API().toBeMocked
            result = "(o5)"
        ]
        new PartialMock1API().toBeMocked => "(o1)"
        new PartialMock2API().toBeMocked => "(o2)"
        new PartialMock3API().toBeMocked => "(o3)"
        new PartialMock4API().toBeMocked => "(o4)"
        new PartialMock5API().toBeMocked => "(o5)"
        new PartialMock1API().notToBeMocked throws NotMocked
        new PartialMock2API().notToBeMocked throws NotMocked
        new PartialMock3API().notToBeMocked throws NotMocked
        new PartialMock4API().notToBeMocked throws NotMocked
        new PartialMock5API().notToBeMocked throws NotMocked
    }

    fact "Dynamic partial mock with instance parameters (5 parameters)" {
        mock(PartialMock1API, PartialMock2API, PartialMock3API, PartialMock4API, PartialMock5API) [it, api1, api2, api3, api4, api5 |
            api1.toBeMocked
            result = "(o1)"

            api2.toBeMocked
            result = "(o2)"

            api3.toBeMocked
            result = "(o3)"

            api4.toBeMocked
            result = "(o4)"

            api5.toBeMocked
            result = "(o5)"
        ]
        new PartialMock1API().toBeMocked => "(o1)"
        new PartialMock2API().toBeMocked => "(o2)"
        new PartialMock3API().toBeMocked => "(o3)"
        new PartialMock4API().toBeMocked => "(o4)"
        new PartialMock5API().toBeMocked => "(o5)"
        new PartialMock1API().notToBeMocked throws NotMocked
        new PartialMock2API().notToBeMocked throws NotMocked
        new PartialMock3API().notToBeMocked throws NotMocked
        new PartialMock4API().notToBeMocked throws NotMocked
        new PartialMock5API().notToBeMocked throws NotMocked
    }

    fact "Dynamic partial mock instances (5 parameters)" {
        val o1 = new PartialMock1API
        val o2 = new PartialMock1API
        val o3 = new PartialMock1API
        val o4 = new PartialMock1API
        val o5 = new PartialMock1API
        mock(o1, o2, o3, o4, o5) [
            o1.toBeMocked
            result = "(o1)"

            o2.toBeMocked
            result = "(o2)"

            o3.toBeMocked
            result = "(o3)"

            o4.toBeMocked
            result = "(o4)"

            o5.toBeMocked
            result = "(o5)"
        ]
        o1.toBeMocked => "(o1)"
        o2.toBeMocked => "(o2)"
        o3.toBeMocked => "(o3)"
        o4.toBeMocked => "(o4)"
        o5.toBeMocked => "(o5)"
    }

   fact "Dynamic partial mock with iterations (5 parameters)" {
        mock(2, PartialMock1API, PartialMock2API, PartialMock3API, PartialMock4API, PartialMock5API) [
            new PartialMock1API().toBeMocked
            result = "(o1)"

            new PartialMock2API().toBeMocked
            result = "(o2)"

            new PartialMock3API().toBeMocked
            result = "(o3)"

            new PartialMock4API().toBeMocked
            result = "(o4)"

            new PartialMock5API().toBeMocked
            result = "(o5)"
        ]
        new PartialMock1API().toBeMocked => "(o1)"
        new PartialMock2API().toBeMocked => "(o2)"
        new PartialMock3API().toBeMocked => "(o3)"
        new PartialMock4API().toBeMocked => "(o4)"
        new PartialMock5API().toBeMocked => "(o5)"
        new PartialMock1API().toBeMocked => "(o1)"
        new PartialMock2API().toBeMocked => "(o2)"
        new PartialMock3API().toBeMocked => "(o3)"
        new PartialMock4API().toBeMocked => "(o4)"
        new PartialMock5API().toBeMocked => "(o5)"
        new PartialMock1API().notToBeMocked throws NotMocked
        new PartialMock2API().notToBeMocked throws NotMocked
        new PartialMock3API().notToBeMocked throws NotMocked
        new PartialMock4API().notToBeMocked throws NotMocked
        new PartialMock5API().notToBeMocked throws NotMocked
    }

    fact "Dynamic partial mock with instance parameters with iterations (5 parameters)" {
        mock(2, PartialMock1API, PartialMock2API, PartialMock3API, PartialMock4API, PartialMock5API) [it, api1, api2, api3, api4, api5 |
            api1.toBeMocked
            result = "(o1)"

            api2.toBeMocked
            result = "(o2)"

            api3.toBeMocked
            result = "(o3)"

            api4.toBeMocked
            result = "(o4)"

            api5.toBeMocked
            result = "(o5)"
        ]
        new PartialMock1API().toBeMocked => "(o1)"
        new PartialMock2API().toBeMocked => "(o2)"
        new PartialMock3API().toBeMocked => "(o3)"
        new PartialMock4API().toBeMocked => "(o4)"
        new PartialMock5API().toBeMocked => "(o5)"
        new PartialMock1API().toBeMocked => "(o1)"
        new PartialMock2API().toBeMocked => "(o2)"
        new PartialMock3API().toBeMocked => "(o3)"
        new PartialMock4API().toBeMocked => "(o4)"
        new PartialMock5API().toBeMocked => "(o5)"
        new PartialMock1API().notToBeMocked throws NotMocked
        new PartialMock2API().notToBeMocked throws NotMocked
        new PartialMock3API().notToBeMocked throws NotMocked
        new PartialMock4API().notToBeMocked throws NotMocked
        new PartialMock5API().notToBeMocked throws NotMocked
    }

    fact "Dynamic partial mock instances with iterations (5 parameters)" {
        val o1 = new PartialMock1API
        val o2 = new PartialMock1API
        val o3 = new PartialMock1API
        val o4 = new PartialMock1API
        val o5 = new PartialMock1API
        mock(2, o1, o2, o3, o4, o5) [
            o1.toBeMocked
            result = "(o1)"

            o2.toBeMocked
            result = "(o2)"

            o3.toBeMocked
            result = "(o3)"

            o4.toBeMocked
            result = "(o4)"

            o5.toBeMocked
            result = "(o5)"
        ]
        o1.toBeMocked => "(o1)"
        o2.toBeMocked => "(o2)"
        o3.toBeMocked => "(o3)"
        o4.toBeMocked => "(o4)"
        o5.toBeMocked => "(o5)"
        o1.toBeMocked => "(o1)"
        o2.toBeMocked => "(o2)"
        o3.toBeMocked => "(o3)"
        o4.toBeMocked => "(o4)"
        o5.toBeMocked => "(o5)"
        o1.toBeMocked throws NotMocked
        o2.toBeMocked throws NotMocked
        o3.toBeMocked throws NotMocked
        o4.toBeMocked throws NotMocked
        o5.toBeMocked throws NotMocked
    }

    fact "Dynamic partial mock instances (X parameters)" {
        val o1 = new PartialMock1API
        val o2 = new PartialMock1API
        val o3 = new PartialMock1API
        val o4 = new PartialMock1API
        val o5 = new PartialMock1API
        val o6 = new PartialMock1API
        mock([
            o1.toBeMocked
            result = "(o1)"

            o2.toBeMocked
            result = "(o2)"

            o3.toBeMocked
            result = "(o3)"

            o4.toBeMocked
            result = "(o4)"

            o5.toBeMocked
            result = "(o5)"

            o6.toBeMocked
            result = "(o6)"
        ], o1, o2, o3, o4, o5, o6)
        o1.toBeMocked => "(o1)"
        o2.toBeMocked => "(o2)"
        o3.toBeMocked => "(o3)"
        o4.toBeMocked => "(o4)"
        o5.toBeMocked => "(o5)"
        o6.toBeMocked => "(o6)"
    }

    fact "Dynamic partial mock instances with iterations (X parameters)" {
        val o1 = new PartialMock1API
        val o2 = new PartialMock1API
        val o3 = new PartialMock1API
        val o4 = new PartialMock1API
        val o5 = new PartialMock1API
        val o6 = new PartialMock1API
        mock(2, [
            o1.toBeMocked
            result = "(o1)"

            o2.toBeMocked
            result = "(o2)"

            o3.toBeMocked
            result = "(o3)"

            o4.toBeMocked
            result = "(o4)"

            o5.toBeMocked
            result = "(o5)"

            o6.toBeMocked
            result = "(o6)"
        ], o1, o2, o3, o4, o5, o6)
        o1.toBeMocked => "(o1)"
        o2.toBeMocked => "(o2)"
        o3.toBeMocked => "(o3)"
        o4.toBeMocked => "(o4)"
        o5.toBeMocked => "(o5)"
        o6.toBeMocked => "(o6)"
        o1.toBeMocked => "(o1)"
        o2.toBeMocked => "(o2)"
        o3.toBeMocked => "(o3)"
        o4.toBeMocked => "(o4)"
        o5.toBeMocked => "(o5)"
        o6.toBeMocked => "(o6)"
        o1.toBeMocked throws NotMocked
        o2.toBeMocked throws NotMocked
        o3.toBeMocked throws NotMocked
        o4.toBeMocked throws NotMocked
        o5.toBeMocked throws NotMocked
        o6.toBeMocked throws NotMocked
    }
}
