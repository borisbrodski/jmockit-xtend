package org.eclipse.xtend.jmockit.test.expectations

import mockit.Mocked
import static extension org.eclipse.xtend.jmockit.JMockitExtension.*
import mockit.internal.UnexpectedInvocation

describe "returns() returns values, including Exception objects" {
	@Mocked
	ExpectationsAPI expectationsAPI
	 
	fact "Using returns() (type: String)" {
		mock [
			expectationsAPI.returnString
			returns("My String")
		]
		
		expectationsAPI.returnString => "My String"
	}
	
	fact "Using multiple returns() (type: String)" {
		mock [
			expectationsAPI.returnString
			returns("My String 1")
			returns(null, "My String 2")
			returns("My String 3", null, "My String 4")
		]
		
		expectationsAPI.returnString => "My String 1"
		expectationsAPI.returnString => null
		expectationsAPI.returnString => "My String 2"
		expectationsAPI.returnString => "My String 3"
		expectationsAPI.returnString => null
		expectationsAPI.returnString => "My String 4"
		expectationsAPI.returnString throws UnexpectedInvocation
	}
	fact "Using multiple returns()(type: ExpectationsAPI)" {
		val api1 = new ExpectationsAPI
		val api2 = new ExpectationsAPI
		val api3 = new ExpectationsAPI
		val api4 = new ExpectationsAPI
		mock [
			expectationsAPI.returnSelf
			returns(api1)
			returns(api2, api3)
			returns(null, null, api4)
		]
		
		expectationsAPI.returnSelf => api1
		expectationsAPI.returnSelf => api2
		expectationsAPI.returnSelf => api3
		expectationsAPI.returnSelf => null
		expectationsAPI.returnSelf => null
		expectationsAPI.returnSelf => api4
		expectationsAPI.returnSelf throws UnexpectedInvocation
	}
	
	fact "Using multiple returns() (type: int)" {
		mock [
			expectationsAPI.returnInt
			returns(321)
			returns(4321, 54321)
			returns(654321, 7654321, 87654321)
		]
		
		expectationsAPI.returnInt => 321
		expectationsAPI.returnInt => 4321
		expectationsAPI.returnInt => 54321
		expectationsAPI.returnInt => 654321
		expectationsAPI.returnInt => 7654321
		expectationsAPI.returnInt => 87654321
		expectationsAPI.returnInt throws UnexpectedInvocation
	}
	
	fact "Using multiple returnsInt() (type: int)" {
		mock [
			expectationsAPI.returnInt
			returnsInt(321)
			returnsInt(4321, 54321)
			returnsInt(654321, 7654321, 87654321)
		]
		
		expectationsAPI.returnInt => 321
		expectationsAPI.returnInt => 4321
		expectationsAPI.returnInt => 54321
		expectationsAPI.returnInt => 654321
		expectationsAPI.returnInt => 7654321
		expectationsAPI.returnInt => 87654321
		expectationsAPI.returnInt throws UnexpectedInvocation
	}
	
	fact "Using multiple returns() (type: long)" {
		mock [
			expectationsAPI.returnLong
			returns(321L)
			returns(4321L, 54321L)
			returns(654321L, 7654321L, 87654321L)
		]
		
		expectationsAPI.returnLong => 321L
		expectationsAPI.returnLong => 4321L
		expectationsAPI.returnLong => 54321L
		expectationsAPI.returnLong => 654321L
		expectationsAPI.returnLong => 7654321L
		expectationsAPI.returnLong => 87654321L
		expectationsAPI.returnLong throws UnexpectedInvocation
	}
	
	fact "Using multiple returnsLong() (type: long)" {
		mock [
			expectationsAPI.returnLong
			returnsLong(321)
			returnsLong(4321, 54321)
			returnsLong(654321, 7654321, 87654321)
		]
		
		expectationsAPI.returnLong => 321L
		expectationsAPI.returnLong => 4321L
		expectationsAPI.returnLong => 54321L
		expectationsAPI.returnLong => 654321L
		expectationsAPI.returnLong => 7654321L
		expectationsAPI.returnLong => 87654321L
		expectationsAPI.returnLong throws UnexpectedInvocation
	}

	fact "Using multiple returns() (type: short)" {
		mock [
			expectationsAPI.returnShort
			returns(1 as short)
			returns(2 as short, 3as short)
			returns(4 as short, 5 as short, 6 as short)
		]
		
		expectationsAPI.returnShort => 1 as short
		expectationsAPI.returnShort => 2 as short
		expectationsAPI.returnShort => 3 as short
		expectationsAPI.returnShort => 4 as short
		expectationsAPI.returnShort => 5 as short
		expectationsAPI.returnShort => 6 as short
		expectationsAPI.returnShort throws UnexpectedInvocation
	}
	
	fact "Using multiple returns() (type: byte)" {
		mock [
			expectationsAPI.returnByte
			returns(1 as byte)
			returns(2 as byte, 3 as byte)
			returns(4 as byte, 5 as byte, 6 as byte)
		]
		
		expectationsAPI.returnByte => 1 as byte
		expectationsAPI.returnByte => 2 as byte
		expectationsAPI.returnByte => 3 as byte
		expectationsAPI.returnByte => 4 as byte
		expectationsAPI.returnByte => 5 as byte
		expectationsAPI.returnByte => 6 as byte
		expectationsAPI.returnByte throws UnexpectedInvocation
	}
	
	fact "Using multiple returns() (type: float)" {
		mock [
			expectationsAPI.returnFloat
			returns(1 as float)
			returns(1.1 as float, 3 as float)
			returns(4.5 as float, 4.6 as float, 6 as float)
		]
		
		expectationsAPI.returnFloat => 1 as float
		expectationsAPI.returnFloat => 1.1 as float
		expectationsAPI.returnFloat => 3 as float
		expectationsAPI.returnFloat => 4.5 as float
		expectationsAPI.returnFloat => 4.6 as float
		expectationsAPI.returnFloat => 6 as float
		expectationsAPI.returnFloat throws UnexpectedInvocation
	}
	
	
	/*
	fact "Using multiple result= (type: short)" {
		mock [
			expectationsAPI.returnShort
			result = 321 as short
			result = new IllegalAccessError
		]
		
		expectationsAPI.returnShort => 321 as short
		expectationsAPI.returnShort throws IllegalAccessError
		expectationsAPI.returnShort throws UnexpectedInvocation
	}
	
	fact "Using multiple result= (type: byte)" {
		mock [
			expectationsAPI.returnByte
			result = 42 as byte
			result = new IllegalAccessError
		]
		
		expectationsAPI.returnByte => 42 as byte
		expectationsAPI.returnByte throws IllegalAccessError
		expectationsAPI.returnByte throws UnexpectedInvocation
	}
	
	fact "Using multiple result= (type: float)" {
		mock [
			expectationsAPI.returnFloat
			result = 31.443f
			result = new IllegalAccessError
		]
		
		expectationsAPI.returnFloat => 31.443f
		expectationsAPI.returnFloat throws IllegalAccessError
		expectationsAPI.returnFloat throws UnexpectedInvocation
	}
	
	fact "Using multiple result= (type: double)" {
		mock [
			expectationsAPI.returnDouble
			result = 321.332
			result = new IllegalAccessError
		]
		
		expectationsAPI.returnDouble => 321.332
		expectationsAPI.returnDouble throws IllegalAccessError
		expectationsAPI.returnDouble throws UnexpectedInvocation
	}
	
	fact "Using multiple result= (type: boolean)" {
		mock [
			expectationsAPI.returnBoolean
			result = true
			result = new IllegalAccessError
		]
		
		expectationsAPI.returnBoolean => true
		expectationsAPI.returnBoolean throws IllegalAccessError
		expectationsAPI.returnBoolean throws UnexpectedInvocation
	}
	
	fact "Using multiple result= (type: char)" {
		mock [
			expectationsAPI.returnCharacter
			result = 'x'.charAt(0)
			result = new IllegalAccessError
		]
		
		expectationsAPI.returnCharacter.toString => 'x'
		expectationsAPI.returnCharacter throws IllegalAccessError
		expectationsAPI.returnCharacter throws UnexpectedInvocation
	}
	*/
}