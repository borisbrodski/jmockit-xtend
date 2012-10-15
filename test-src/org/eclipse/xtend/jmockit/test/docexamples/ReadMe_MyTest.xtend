package org.eclipse.xtend.jmockit.test.docexamples

import org.junit.Test

import static org.hamcrest.core.Is.*
import static org.junit.Assert.*

import static extension org.eclipse.xtend.jmockit.JMockitExtension.*

class MyService {
	def doGreeting() {
		return "";
	}
}

class MyTest {
	@Test
	def void myTest(MyService service) {
		mock [
			service.doGreeting
			result = "Hello World"
		]
		
		assertThat(service.doGreeting, is("Hello World"))
	}
}
