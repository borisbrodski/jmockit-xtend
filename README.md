# Xtend-JMockit

Collection of the Xtend extension methods adding JMockit support

## Introduction

Xtend-JMockit contains a single file (upon tests) with the collection
of the Xtend extension methods and a couple of entry methods, like `mock` and `stub`.

## Usage

```xtend
import mockit.Mocked
import org.junit.Test
import static org.junit.Assert.*
import static org.hamcrest.core.Is.*

class MyTest {
	@Test
	def void myTest(MyService service) {
		mock [
			service.doGreeting
			result = "Hello World"
		]
		
		assertThat(service.doGreeting, is("Hello World"))
	}
```

