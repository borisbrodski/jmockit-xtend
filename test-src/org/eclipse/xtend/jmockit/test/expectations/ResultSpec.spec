package org.eclipse.xtend.jmockit.test.expectations

import mockit.Mocked

import static extension org.eclipse.xtend.jmockit.JMockitExtension.*
import mockit.internal.UnexpectedInvocation

describe "Result of the method calls can be specified" {
	@Mocked
	ExpectationsAPI expectationsAPI
	 
	fact "Using result= (type: String)" {
		mock [
			expectationsAPI.returnString
			result = "My String"
		]
		
		expectationsAPI.returnString => "My String"
	}
	
	fact "Using multiple result= (type: String)" {
		mock [
			expectationsAPI.returnString
			result = "My String 1"
			result = new IllegalAccessError
			result = null
			result = new IllegalStateException
			result = "My String 2"
		]
		
		expectationsAPI.returnString => "My String 1"
		expectationsAPI.returnString throws IllegalAccessError
		expectationsAPI.returnString => null
		expectationsAPI.returnString throws IllegalStateException
		expectationsAPI.returnString => "My String 2"
		expectationsAPI.returnString throws UnexpectedInvocation
	}
	
	fact "Using multiple result= (type: ExpectationsAPI)" {
		val api = new ExpectationsAPI
		mock [
			expectationsAPI.returnSelf
			result = api
			result = null
			result = new IllegalAccessError
		]
		
		expectationsAPI.returnSelf => api
		expectationsAPI.returnSelf => null
		expectationsAPI.returnSelf throws IllegalAccessError
		expectationsAPI.returnSelf throws UnexpectedInvocation
	}
	
	fact "Using multiple result= (type: int)" {
		mock [
			expectationsAPI.returnInt
			result = 321
			result = new IllegalAccessError
		]
		
		expectationsAPI.returnInt => 321
		expectationsAPI.returnInt throws IllegalAccessError
		expectationsAPI.returnInt throws UnexpectedInvocation
	}
	
	fact "Using multiple resultInt= (type: int)" {
		mock [
			expectationsAPI.returnInt
			resultInt = 321
			result = new IllegalAccessError
		]
		
		expectationsAPI.returnInt => 321
		expectationsAPI.returnInt throws IllegalAccessError
		expectationsAPI.returnInt throws UnexpectedInvocation
	}
	
	fact "Using multiple result= (type: long)" {
		mock [
			expectationsAPI.returnLong
			result = 321L
			result = new IllegalAccessError
		]
		
		expectationsAPI.returnLong => 321L
		expectationsAPI.returnLong throws IllegalAccessError
		expectationsAPI.returnLong throws UnexpectedInvocation
	}
	
	fact "Using multiple resultLong= (type: long)" {
		mock [
			expectationsAPI.returnLong
			resultLong = 321
			result = new IllegalAccessError
		]
		
		expectationsAPI.returnLong => 321L
		expectationsAPI.returnLong throws IllegalAccessError
		expectationsAPI.returnLong throws UnexpectedInvocation
	}
	
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
	
	fact "Using multiple resultShort= (type: short)" {
		mock [
			expectationsAPI.returnShort
			resultShort = 321 as short
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
	
	fact "Using multiple resultByte= (type: byte)" {
		mock [
			expectationsAPI.returnByte
			resultByte = 42 as byte
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
			result = 32f
			result = new IllegalAccessError
		]
		
		expectationsAPI.returnFloat => 31.443f
		expectationsAPI.returnFloat => 32f
		expectationsAPI.returnFloat throws IllegalAccessError
		expectationsAPI.returnFloat throws UnexpectedInvocation
	}
	
	fact "Using multiple resultFloat= (type: float)" {
		mock [
			expectationsAPI.returnFloat
			resultFloat = 31.443f
			resultFloat = 32
			result = new IllegalAccessError
		]
		
		expectationsAPI.returnFloat => 31.443f
		expectationsAPI.returnFloat => 32f
		expectationsAPI.returnFloat throws IllegalAccessError
		expectationsAPI.returnFloat throws UnexpectedInvocation
	}
	
	fact "Using multiple result= (type: double)" {
		mock [
			expectationsAPI.returnDouble
			result = 321.332
			result = 2.0
			result = new IllegalAccessError
		]
		
		expectationsAPI.returnDouble => 321.332
		expectationsAPI.returnDouble => 2.0
		expectationsAPI.returnDouble throws IllegalAccessError
		expectationsAPI.returnDouble throws UnexpectedInvocation
	}
	
	fact "Using multiple resultDouble= (type: double)" {
		mock [
			expectationsAPI.returnDouble
			resultDouble = 321.332
			resultDouble = 2
			result = new IllegalAccessError
		]
		
		expectationsAPI.returnDouble => 321.332
		expectationsAPI.returnDouble => 2.0
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
	
	fact "Using multiple resultBoolean= (type: boolean)" {
		mock [
			expectationsAPI.returnBoolean
			resultBoolean = true
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
	
	fact "Using multiple resultChar= (type: char)" {
		mock [
			expectationsAPI.returnCharacter
			resultChar = 'x'.charAt(0)
			result = new IllegalAccessError
		]
		
		expectationsAPI.returnCharacter.toString => 'x'
		expectationsAPI.returnCharacter throws IllegalAccessError
		expectationsAPI.returnCharacter throws UnexpectedInvocation
	}
	

}