package org.eclipse.xtend.jmockit.test.docexamples

import org.junit.Test

import static org.hamcrest.core.Is.*
import static org.junit.Assert.*

import static extension org.eclipse.xtend.jmockit.JMockitExtension.*
import mockit.Mocked

class MyService {
	def doGreeting() {
		return "";
	}
}

class MyTest {
	@Mocked
	MyService service

	@Test
	def void myTest() {
		mock [
			service.doGreeting
			result = "Hello World"
		]

		assertThat(service.doGreeting, is("Hello World"))
	}
}
