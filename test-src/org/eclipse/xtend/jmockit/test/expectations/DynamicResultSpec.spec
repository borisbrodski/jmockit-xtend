package org.eclipse.xtend.jmockit.test.expectations

import mockit.Mocked

import static org.eclipse.xtend.jmockit.JMockitExtension.*

describe "Result of the method calls can be specified with a dynamic result setter" {
	@Mocked
	ExpectationsAPI expectationsAPI

	int counter

	fact "Using result= (no parameter)" {
		stub [
			expectationsAPI.returnInt
			result=[| counter=counter + 1 ]
		]

		expectationsAPI.returnInt => 1
		expectationsAPI.returnInt => 2
		expectationsAPI.returnInt => 3
		expectationsAPI.returnInt => 4
	}

	fact "Using result= (1 parameter)" {
		stub [
			expectationsAPI.paramsInt(anyInt)
			result=[ int p1 |
				"p1=" + p1
			]
		]

		expectationsAPI.paramsInt(2) => "p1=2"
		expectationsAPI.paramsInt(3) => "p1=3"
	}

	fact "Using result= (2 parameter)" {
		stub [
			expectationsAPI.paramsIntInt(anyInt, anyInt)
			result=[ int p1, int p2 |
				"p1=" + p1 + ", p2=" + p2
			]
		]

		expectationsAPI.paramsIntInt(6, -5) => "p1=6, p2=-5"
		expectationsAPI.paramsIntInt(1, 10) => "p1=1, p2=10"
	}

	fact "Using result= (3 parameter)" {
		stub [
			expectationsAPI.paramsIntIntInt(anyInt, anyInt, anyInt)
			result=[ int p1, int p2, int p3 |
				"p1=" + p1 + ", p2=" + p2 + ", p3=" + p3
			]
		]

		expectationsAPI.paramsIntIntInt(97, -43, 2) => "p1=97, p2=-43, p3=2"
		expectationsAPI.paramsIntIntInt(12, -42, -21) => "p1=12, p2=-42, p3=-21"
	}

	fact "Using result= (4 parameter)" {
		stub [
			expectationsAPI.paramsIntIntIntInt(anyInt, anyInt, anyInt, anyInt)
			result=[ int p1, int p2, int p3, int p4 |
				"p1=" + p1 + ", p2=" + p2 + ", p3=" + p3 + ", p4=" + p4
			]
		]

		expectationsAPI.paramsIntIntIntInt(53, -1, 532, 3) => "p1=53, p2=-1, p3=532, p4=3"
		expectationsAPI.paramsIntIntIntInt(9, -23, 8, 6) => "p1=9, p2=-23, p3=8, p4=6"
	}

	fact "Using result= (5 parameter)" {
		stub [
			expectationsAPI.paramsIntIntIntIntInt(anyInt, anyInt, anyInt, anyInt, anyInt)
			result=[ int p1, int p2, int p3, int p4, int p5 |
				"p1=" + p1 + ", p2=" + p2 + ", p3=" + p3 + ", p4=" + p4 + ", p5=" + p5
			]
		]

		expectationsAPI.paramsIntIntIntIntInt(7, 82, -23, -74, 32) => "p1=7, p2=82, p3=-23, p4=-74, p5=32"
		expectationsAPI.paramsIntIntIntIntInt(23, 49, 0, -89, 54) => "p1=23, p2=49, p3=0, p4=-89, p5=54"
	}

	fact "Using result= (6 parameter)" {
		stub [
			expectationsAPI.paramsIntIntIntIntIntInt(anyInt, anyInt, anyInt, anyInt, anyInt, anyInt)
			result=[ int p1, int p2, int p3, int p4, int p5, int p6 |
				"p1=" + p1 + ", p2=" + p2 + ", p3=" + p3 + ", p4=" + p4 + ", p5=" + p5 + ", p6=" + p6
			]
		]

		expectationsAPI.paramsIntIntIntIntIntInt(48,-741,2,84,93,-89) => "p1=48, p2=-741, p3=2, p4=84, p5=93, p6=-89"
		expectationsAPI.paramsIntIntIntIntIntInt(3,4,903,-4,89,-7) => "p1=3, p2=4, p3=903, p4=-4, p5=89, p6=-7"
	}
	fact "Using result= (combined types)" {
		stub [
			expectationsAPI.paramsStringBLongBoolean(any, any, anyBoolean)
			result=[ String string, Long number, boolean bool |
				string + ", " + number + ", " + bool
			]
		]

		expectationsAPI.paramsStringBLongBoolean("HelloWorld", 12221L, true) => "HelloWorld, 12221, true"
		expectationsAPI.paramsStringBLongBoolean("ByeBye", -84372L, false) => "ByeBye, -84372, false"
	}
}