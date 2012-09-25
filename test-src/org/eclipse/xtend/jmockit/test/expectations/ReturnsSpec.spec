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
			returns(2 as short, 3 as short)
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
	
	fact "Using multiple returnsShort() (type: short)" {
		mock [
			expectationsAPI.returnShort
			returnsShort(1 as short)
			returnsShort(2 as short, 3 as short)
			returnsShort(4 as short, 5 as short, 6 as short)
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
	
	fact "Using multiple returnsByte() (type: byte)" {
		mock [
			expectationsAPI.returnByte
			returnsByte(1 as byte)
			returnsByte(2 as byte, 3 as byte)
			returnsByte(4 as byte, 5 as byte, 6 as byte)
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
			returns(1f)
			returns(1.1f, 3f)
			returns(4.5f, 4.6f, 6f)
		]
		
		expectationsAPI.returnFloat => 1f
		expectationsAPI.returnFloat => 1.1f
		expectationsAPI.returnFloat => 3f
		expectationsAPI.returnFloat => 4.5f
		expectationsAPI.returnFloat => 4.6f
		expectationsAPI.returnFloat => 6f
		expectationsAPI.returnFloat throws UnexpectedInvocation
	}
	
	fact "Using multiple returnsFloat() (type: float)" {
		mock [
			expectationsAPI.returnFloat
			returnsFloat(1)
			returnsFloat(1.1f, 3)
			returnsFloat(4.5f, 4.6f, 6)
		]
		
		expectationsAPI.returnFloat => 1f
		expectationsAPI.returnFloat => 1.1f
		expectationsAPI.returnFloat => 3f
		expectationsAPI.returnFloat => 4.5f
		expectationsAPI.returnFloat => 4.6f
		expectationsAPI.returnFloat => 6f
		expectationsAPI.returnFloat throws UnexpectedInvocation
	}
	
	fact "Using multiple returns() (type: double)" {
		mock [
			expectationsAPI.returnDouble
			returns(1d)
			returns(1.1, 3d)
			returns(4.5, 4.6, 6d)
		]
		
		expectationsAPI.returnDouble => 1d
		expectationsAPI.returnDouble => 1.1
		expectationsAPI.returnDouble => 3d
		expectationsAPI.returnDouble => 4.5
		expectationsAPI.returnDouble => 4.6
		expectationsAPI.returnDouble => 6d
		expectationsAPI.returnDouble throws UnexpectedInvocation
	}
	
	fact "Using multiple returnsDouble() (type: double)" {
		mock [
			expectationsAPI.returnDouble
			returnsDouble(1)
			returnsDouble(1.1, 3)
			returnsDouble(4.5, 4.6, 6)
		]
		
		expectationsAPI.returnDouble => 1d
		expectationsAPI.returnDouble => 1.1
		expectationsAPI.returnDouble => 3d
		expectationsAPI.returnDouble => 4.5
		expectationsAPI.returnDouble => 4.6
		expectationsAPI.returnDouble => 6d
		expectationsAPI.returnDouble throws UnexpectedInvocation
	}
	
	fact "Using multiple returns() (type: boolean)" {
		mock [
			expectationsAPI.returnBoolean
			returns(true)
			returns(true, false)
			returns(false, true, false)
		]
		
		expectationsAPI.returnBoolean => true
		expectationsAPI.returnBoolean => true
		expectationsAPI.returnBoolean => false
		expectationsAPI.returnBoolean => false
		expectationsAPI.returnBoolean => true
		expectationsAPI.returnBoolean => false
		expectationsAPI.returnBoolean throws UnexpectedInvocation
	}
	
	fact "Using multiple returnsBoolean() (type: boolean)" {
		mock [
			expectationsAPI.returnBoolean
			returnsBoolean(true)
			returnsBoolean(false, true)
			returnsBoolean(true, false, true)
		]
		
		expectationsAPI.returnBoolean => true
		expectationsAPI.returnBoolean => false
		expectationsAPI.returnBoolean => true
		expectationsAPI.returnBoolean => true
		expectationsAPI.returnBoolean => false
		expectationsAPI.returnBoolean => true
		expectationsAPI.returnBoolean throws UnexpectedInvocation
	}
	
	fact "Using multiple returns() (type: char)" {
		mock [
			expectationsAPI.returnCharacter
			returns('a'.charAt(0))
			returns('b'.charAt(0), 'c'.charAt(0))
			returns('d'.charAt(0), 'e'.charAt(0), 'f'.charAt(0))
		]
		
		expectationsAPI.returnCharacter => 'a'.charAt(0)
		expectationsAPI.returnCharacter => 'b'.charAt(0)
		expectationsAPI.returnCharacter => 'c'.charAt(0)
		expectationsAPI.returnCharacter => 'd'.charAt(0)
		expectationsAPI.returnCharacter => 'e'.charAt(0)
		expectationsAPI.returnCharacter => 'f'.charAt(0)
		expectationsAPI.returnCharacter throws UnexpectedInvocation
	}
	
	fact "Using multiple returnsCharacter() (type: char)" {
		mock [
			expectationsAPI.returnCharacter
			returnsChar('a'.charAt(0))
			returnsChar('b'.charAt(0), 'c'.charAt(0))
			returnsChar('d'.charAt(0), 'e'.charAt(0), 'f'.charAt(0))
		]
		
		expectationsAPI.returnCharacter => 'a'.charAt(0)
		expectationsAPI.returnCharacter => 'b'.charAt(0)
		expectationsAPI.returnCharacter => 'c'.charAt(0)
		expectationsAPI.returnCharacter => 'd'.charAt(0)
		expectationsAPI.returnCharacter => 'e'.charAt(0)
		expectationsAPI.returnCharacter => 'f'.charAt(0)
		expectationsAPI.returnCharacter throws UnexpectedInvocation
	}
}