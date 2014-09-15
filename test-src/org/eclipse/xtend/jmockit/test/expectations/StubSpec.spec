package org.eclipse.xtend.jmockit.test.expectations

import mockit.Mocked
import mockit.internal.UnexpectedInvocation
import org.hamcrest.Matchers

import static org.eclipse.xtend.jmockit.JMockitExtension.*

describe "stub behaves like NonStrictExpectations" {

    context "Non-partial mocking with stub" {
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

        fact "stub with iterations" {
            stub(2) [
                expectationsAPI.returnString
                result = "a"
                maxTimes = 2 // Get multiplied by iteration count (2)
            ]

            expectationsAPI.returnString => "a"
            expectationsAPI.returnString => "a"
            expectationsAPI.returnString => "a"
            expectationsAPI.returnString => "a"
        	expectationsAPI.returnString throws UnexpectedInvocation
            expectationsAPI.returnSelf throws UnexpectedInvocation // TODO See JMockit issue #66
        }

		fact "Get faked instance of any class" {
			stub [
				ins(ClassWithNoSuitableConstructor) => Matchers.instanceOf(ClassWithNoSuitableConstructor)
			]
		}
    }

    fact "Partially stubbing" {
        stub(ExpectationsAPI)

        stub [
            (new ExpectationsAPI).returnString
            result = "My string 1"
        ]

        (new ExpectationsAPI).returnString => "My string 1"
        (new ExpectationsAPI).returnVoid throws NotMocked
        (new ExpectationsAPI).returnString => "My string 1"
    }

    fact "Partially stub single class returns instance of the class" {
        val api = stub(ExpectationsAPI)

        stub [
            api.returnString
            result = "My string 1"
        ]

        api.returnString => "My string 1"
        api.returnVoid throws NotMocked
        api.returnString => "My string 1"
    }

    fact "Dynamic partial stub (1 parameters)" {
        stub(ExpectationsAPI) [
            (new ExpectationsAPI).returnString
            result = "My string 1"
        ]

        (new ExpectationsAPI).returnString => "My string 1"
        (new ExpectationsAPI).returnVoid throws NotMocked
        (new ExpectationsAPI).returnString => "My string 1"
    }

    fact "Dynamic partial stub with instance parameters (1 parameters)" {
        stub(ExpectationsAPI) [ it, api |
            api.returnString
            result = "My string 1"
        ]

        (new ExpectationsAPI).returnString => "My string 1"
        (new ExpectationsAPI).returnVoid throws NotMocked
        (new ExpectationsAPI).returnString => "My string 1"
    }

    fact "Dynamic partial stub instances (1 parameters)" {
    	val api = new ExpectationsAPI()
        stub(api) [
            api.returnString
            result = "My string 1"
        ]

        api.returnString => "My string 1"
        (new ExpectationsAPI).returnString throws NotMocked
        (new ExpectationsAPI).returnVoid throws NotMocked
    }


    fact "Dynamic partial stub with iterations (1 parameters)" {
        stub(2, ExpectationsAPI) [
            (new ExpectationsAPI).returnString
            maxTimes = 2
            result = "My string 1"
        ]

        (new ExpectationsAPI).returnString => "My string 1"
        (new ExpectationsAPI).returnString => "My string 1"
        (new ExpectationsAPI).returnString => "My string 1"
        (new ExpectationsAPI).returnString => "My string 1"
        (new ExpectationsAPI).returnVoid throws NotMocked
        (new ExpectationsAPI).returnString throws UnexpectedInvocation
    }

    fact "Dynamic partial stub with instance parameters with iterations (1 parameters)" {
        stub(2, ExpectationsAPI) [ it, api |
            api.returnString
            maxTimes = 2
            result = "My string 1"
        ]

        (new ExpectationsAPI).returnString => "My string 1"
        (new ExpectationsAPI).returnString => "My string 1"
        (new ExpectationsAPI).returnString => "My string 1"
        (new ExpectationsAPI).returnString => "My string 1"
        (new ExpectationsAPI).returnVoid throws NotMocked
        (new ExpectationsAPI).returnString throws UnexpectedInvocation
    }

    fact "Dynamic partial stub instances with iterations (1 parameters)" {
        val o1 = new PartialMock1API
        stub(2, o1) [
            o1.toBeMocked
            maxTimes = 2
            result = "(o1)"
        ]
        o1.toBeMocked => "(o1)"
        o1.toBeMocked => "(o1)"
        o1.toBeMocked => "(o1)"
        o1.toBeMocked => "(o1)"
        o1.toBeMocked throws UnexpectedInvocation
    }

    fact "Dynamic partial stub (2 parameters)" {
        stub(PartialMock1API, PartialMock2API) [
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

    fact "Dynamic partial stub with instance parameters (2 parameters)" {
        stub(PartialMock1API, PartialMock2API) [it, api1, api2 |
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

    fact "Dynamic partial stub instances (2 parameters)" {
        val o1 = new PartialMock1API
        val o2 = new PartialMock1API
        stub(o1, o2) [
            o1.toBeMocked
            result = "(o1)"

            o2.toBeMocked
            result = "(o2)"
        ]
        o1.toBeMocked => "(o1)"
        o2.toBeMocked => "(o2)"
    }

    fact "Dynamic partial stub with iterations (2 parameters)" {
        stub(2, PartialMock1API, PartialMock2API) [
            new PartialMock1API().toBeMocked
            result = "(o1)"

            new PartialMock2API().toBeMocked
            maxTimes = 2
            result = "(o2)"
        ]

        new PartialMock1API().toBeMocked => "(o1)"
        new PartialMock2API().toBeMocked => "(o2)"
        new PartialMock2API().toBeMocked => "(o2)"
        new PartialMock2API().toBeMocked => "(o2)"
        new PartialMock2API().toBeMocked => "(o2)"
        new PartialMock1API().notToBeMocked throws NotMocked
        new PartialMock2API().notToBeMocked throws NotMocked
        new PartialMock2API().toBeMocked throws UnexpectedInvocation
    }

    fact "Dynamic partial stub with instance parameters with iterations (2 parameters)" {
        stub(2, PartialMock1API, PartialMock2API) [it, api1, api2 |
            api1.toBeMocked
            result = "(o1)"

            api2.toBeMocked
            maxTimes = 2
            result = "(o2)"
        ]
        new PartialMock1API().toBeMocked => "(o1)"
        new PartialMock2API().toBeMocked => "(o2)"
        new PartialMock2API().toBeMocked => "(o2)"
        new PartialMock2API().toBeMocked => "(o2)"
        new PartialMock2API().toBeMocked => "(o2)"
        new PartialMock1API().notToBeMocked throws NotMocked
        new PartialMock2API().notToBeMocked throws NotMocked
        new PartialMock2API().toBeMocked throws UnexpectedInvocation
    }

    fact "Dynamic partial stub instances with iterations (2 parameters)" {
        val o1 = new PartialMock1API
        val o2 = new PartialMock1API
        stub(2, o1, o2) [
            o1.toBeMocked
            result = "(o1)"

            o2.toBeMocked
            result = "(o2)"
        ]
        o1.toBeMocked => "(o1)"
        o2.toBeMocked => "(o2)"
    }

    fact "Dynamic partial stub (3 parameters)" {
        stub(PartialMock1API, PartialMock2API, PartialMock3API) [
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

    fact "Dynamic partial stub with instance parameters (3 parameters)" {
        stub(PartialMock1API, PartialMock2API, PartialMock3API) [it, api1, api2, api3 |
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

    fact "Dynamic partial stub instances (3 parameters)" {
        val o1 = new PartialMock1API
        val o2 = new PartialMock1API
        val o3 = new PartialMock1API
        stub(o1, o2, o3) [
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
    }


    fact "Dynamic partial stub with iterations (3 parameters)" {
        stub(2, PartialMock1API, PartialMock2API, PartialMock3API) [
            new PartialMock1API().toBeMocked
            result = "(o1)"

            new PartialMock2API().toBeMocked
            result = "(o2)"

            new PartialMock3API().toBeMocked
            maxTimes = 2
            result = "(o3)"
        ]

        new PartialMock1API().toBeMocked => "(o1)"
        new PartialMock2API().toBeMocked => "(o2)"
        new PartialMock3API().toBeMocked => "(o3)"
        new PartialMock3API().toBeMocked => "(o3)"
        new PartialMock3API().toBeMocked => "(o3)"
        new PartialMock3API().toBeMocked => "(o3)"
        new PartialMock1API().notToBeMocked throws NotMocked
        new PartialMock2API().notToBeMocked throws NotMocked
        new PartialMock3API().notToBeMocked throws NotMocked
        new PartialMock3API().toBeMocked throws UnexpectedInvocation
    }

    fact "Dynamic partial stub with instance parameters with iterations (3 parameters)" {
        stub(2, PartialMock1API, PartialMock2API, PartialMock3API) [it, api1, api2, api3 |
            api1.toBeMocked
            result = "(o1)"

            api2.toBeMocked
            result = "(o2)"

            api3.toBeMocked
            result = "(o3)"
            maxTimes = 2
        ]
        new PartialMock1API().toBeMocked => "(o1)"
        new PartialMock2API().toBeMocked => "(o2)"
        new PartialMock3API().toBeMocked => "(o3)"
        new PartialMock3API().toBeMocked => "(o3)"
        new PartialMock3API().toBeMocked => "(o3)"
        new PartialMock3API().toBeMocked => "(o3)"
        new PartialMock1API().notToBeMocked throws NotMocked
        new PartialMock2API().notToBeMocked throws NotMocked
        new PartialMock3API().notToBeMocked throws NotMocked
        new PartialMock3API().toBeMocked throws UnexpectedInvocation
    }

    fact "Dynamic partial stub instances with iterations (3 parameters)" {
        val o1 = new PartialMock1API
        val o2 = new PartialMock1API
        val o3 = new PartialMock1API
        stub(2, o1, o2, o3) [
            o1.toBeMocked
            result = "(o1)"

            o2.toBeMocked
            result = "(o2)"

            o3.toBeMocked
            maxTimes = 2
            result = "(o3)"
        ]
        o1.toBeMocked => "(o1)"
        o2.toBeMocked => "(o2)"
        o3.toBeMocked => "(o3)"
        o3.toBeMocked => "(o3)"
        o3.toBeMocked => "(o3)"
        o3.toBeMocked => "(o3)"
        o3.toBeMocked throws UnexpectedInvocation
    }

    fact "Dynamic partial stub (4 parameters)" {
        stub(PartialMock1API, PartialMock2API, PartialMock3API, PartialMock4API) [
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

    fact "Dynamic partial stub with instance parameters (4 parameters)" {
        stub(PartialMock1API, PartialMock2API, PartialMock3API, PartialMock4API) [it, api1, api2, api3, api4 |
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

    fact "Dynamic partial stub instances (4 parameters)" {
        val o1 = new PartialMock1API
        val o2 = new PartialMock1API
        val o3 = new PartialMock1API
        val o4 = new PartialMock1API
        stub(o1, o2, o3, o4) [
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


    fact "Dynamic partial stub with iterations (4 parameters)" {
        stub(2, PartialMock1API, PartialMock2API, PartialMock3API, PartialMock4API) [
            new PartialMock1API().toBeMocked
            result = "(o1)"

            new PartialMock2API().toBeMocked
            result = "(o2)"

            new PartialMock3API().toBeMocked
            result = "(o3)"

            new PartialMock4API().toBeMocked
            result = "(o4)"
            maxTimes = 2
        ]
        new PartialMock1API().toBeMocked => "(o1)"
        new PartialMock2API().toBeMocked => "(o2)"
        new PartialMock3API().toBeMocked => "(o3)"
        new PartialMock4API().toBeMocked => "(o4)"
        new PartialMock4API().toBeMocked => "(o4)"
        new PartialMock4API().toBeMocked => "(o4)"
        new PartialMock4API().toBeMocked => "(o4)"
        new PartialMock1API().notToBeMocked throws NotMocked
        new PartialMock2API().notToBeMocked throws NotMocked
        new PartialMock3API().notToBeMocked throws NotMocked
        new PartialMock4API().notToBeMocked throws NotMocked
        new PartialMock4API().toBeMocked throws UnexpectedInvocation
    }

    fact "Dynamic partial stub with instance parameters with iterations (4 parameters)" {
        stub(2, PartialMock1API, PartialMock2API, PartialMock3API, PartialMock4API) [it, api1, api2, api3, api4 |
            api1.toBeMocked
            result = "(o1)"

            api2.toBeMocked
            result = "(o2)"

            api3.toBeMocked
            result = "(o3)"

            api4.toBeMocked
            maxTimes = 2
            result = "(o4)"
        ]
        new PartialMock1API().toBeMocked => "(o1)"
        new PartialMock2API().toBeMocked => "(o2)"
        new PartialMock3API().toBeMocked => "(o3)"
        new PartialMock4API().toBeMocked => "(o4)"
        new PartialMock4API().toBeMocked => "(o4)"
        new PartialMock4API().toBeMocked => "(o4)"
        new PartialMock4API().toBeMocked => "(o4)"
        new PartialMock1API().notToBeMocked throws NotMocked
        new PartialMock2API().notToBeMocked throws NotMocked
        new PartialMock3API().notToBeMocked throws NotMocked
        new PartialMock4API().notToBeMocked throws NotMocked
        new PartialMock4API().toBeMocked throws UnexpectedInvocation
    }

    fact "Dynamic partial stub instances with iterations (4 parameters)" {
        val o1 = new PartialMock1API
        val o2 = new PartialMock1API
        val o3 = new PartialMock1API
        val o4 = new PartialMock1API
        stub(2, o1, o2, o3, o4) [
            o1.toBeMocked
            result = "(o1)"

            o2.toBeMocked
            result = "(o2)"

            o3.toBeMocked
            result = "(o3)"

            o4.toBeMocked
            result = "(o4)"
            maxTimes = 2
        ]
        o1.toBeMocked => "(o1)"
        o2.toBeMocked => "(o2)"
        o3.toBeMocked => "(o3)"
        o4.toBeMocked => "(o4)"
        o4.toBeMocked => "(o4)"
        o4.toBeMocked => "(o4)"
        o4.toBeMocked => "(o4)"
        o4.toBeMocked throws UnexpectedInvocation
    }

    fact "Dynamic partial stub (5 parameters)" {
        stub(PartialMock1API, PartialMock2API, PartialMock3API, PartialMock4API, PartialMock5API) [
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

    fact "Dynamic partial stub with instance parameters (5 parameters)" {
        stub(PartialMock1API, PartialMock2API, PartialMock3API, PartialMock4API, PartialMock5API) [it, api1, api2, api3, api4, api5 |
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

    fact "Dynamic partial stub instances (5 parameters)" {
        val o1 = new PartialMock1API
        val o2 = new PartialMock1API
        val o3 = new PartialMock1API
        val o4 = new PartialMock1API
        val o5 = new PartialMock1API
        stub(o1, o2, o3, o4, o5) [
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

   fact "Dynamic partial stub with iterations (5 parameters)" {
        stub(2, PartialMock1API, PartialMock2API, PartialMock3API, PartialMock4API, PartialMock5API) [
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
            maxTimes = 2
        ]
        new PartialMock1API().toBeMocked => "(o1)"
        new PartialMock2API().toBeMocked => "(o2)"
        new PartialMock3API().toBeMocked => "(o3)"
        new PartialMock4API().toBeMocked => "(o4)"
        new PartialMock5API().toBeMocked => "(o5)"
        new PartialMock5API().toBeMocked => "(o5)"
        new PartialMock5API().toBeMocked => "(o5)"
        new PartialMock5API().toBeMocked => "(o5)"
        new PartialMock1API().notToBeMocked throws NotMocked
        new PartialMock2API().notToBeMocked throws NotMocked
        new PartialMock3API().notToBeMocked throws NotMocked
        new PartialMock4API().notToBeMocked throws NotMocked
        new PartialMock5API().notToBeMocked throws NotMocked
        new PartialMock5API().toBeMocked throws UnexpectedInvocation
    }

    fact "Dynamic partial stub with instance parameters with iterations (5 parameters)" {
        stub(2, PartialMock1API, PartialMock2API, PartialMock3API, PartialMock4API, PartialMock5API) [it, api1, api2, api3, api4, api5 |
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
            maxTimes = 2
        ]
        new PartialMock1API().toBeMocked => "(o1)"
        new PartialMock2API().toBeMocked => "(o2)"
        new PartialMock3API().toBeMocked => "(o3)"
        new PartialMock4API().toBeMocked => "(o4)"
        new PartialMock5API().toBeMocked => "(o5)"
        new PartialMock5API().toBeMocked => "(o5)"
        new PartialMock5API().toBeMocked => "(o5)"
        new PartialMock5API().toBeMocked => "(o5)"
        new PartialMock1API().notToBeMocked throws NotMocked
        new PartialMock2API().notToBeMocked throws NotMocked
        new PartialMock3API().notToBeMocked throws NotMocked
        new PartialMock4API().notToBeMocked throws NotMocked
        new PartialMock5API().notToBeMocked throws NotMocked
        new PartialMock5API().toBeMocked throws UnexpectedInvocation
    }

    fact "Dynamic partial stub instances with iterations (5 parameters)" {
        val o1 = new PartialMock1API
        val o2 = new PartialMock1API
        val o3 = new PartialMock1API
        val o4 = new PartialMock1API
        val o5 = new PartialMock1API
        stub(2, o1, o2, o3, o4, o5) [
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
            maxTimes = 2 // Get multiplied by iteration count (2)
        ]
        o1.toBeMocked => "(o1)"
        o2.toBeMocked => "(o2)"
        o3.toBeMocked => "(o3)"
        o4.toBeMocked => "(o4)"
        o5.toBeMocked => "(o5)"
        o5.toBeMocked => "(o5)"
        o5.toBeMocked => "(o5)"
        o5.toBeMocked => "(o5)"
        o5.toBeMocked throws UnexpectedInvocation
    }

    fact "Dynamic partial stub instances (X parameters)" {
        val o1 = new PartialMock1API
        val o2 = new PartialMock1API
        val o3 = new PartialMock1API
        val o4 = new PartialMock1API
        val o5 = new PartialMock1API
        val o6 = new PartialMock1API
        stub([
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

    fact "Dynamic partial stub instances with iterations (X parameters)" {
        val o1 = new PartialMock1API
        val o2 = new PartialMock1API
        val o3 = new PartialMock1API
        val o4 = new PartialMock1API
        val o5 = new PartialMock1API
        val o6 = new PartialMock1API
        stub(2, [
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
            maxTimes = 2 // Get multiplied by iteration count (2)
            result = "(o6)"
        ], o1, o2, o3, o4, o5, o6)
        o1.toBeMocked => "(o1)"
        o2.toBeMocked => "(o2)"
        o3.toBeMocked => "(o3)"
        o4.toBeMocked => "(o4)"
        o5.toBeMocked => "(o5)"
        o6.toBeMocked => "(o6)"
        o6.toBeMocked => "(o6)"
        o6.toBeMocked => "(o6)"
        o6.toBeMocked => "(o6)"
        o6.toBeMocked throws UnexpectedInvocation
    }
}
