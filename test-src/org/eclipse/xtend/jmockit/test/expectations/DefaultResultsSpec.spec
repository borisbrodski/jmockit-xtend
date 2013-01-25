package org.eclipse.xtend.jmockit.test.expectations

import mockit.Mocked
import mockit.Input
import static extension org.eclipse.xtend.jmockit.JMockitExtension.*
import java.io.IOException
import java.io.InputStream

describe "Default results can be specified" {
	context "Default int value" {
		@Mocked
		ExpectationsAPI api
		
		@Input
		int a = 3
		
		fact "All int returning methods should return 3" {
			api.returnInt => 3
		} 
	}
	
	context "Default checked exception" {
		@Mocked
		InputStream inputStream
		
		@Input
		IOException ioException;
		
		fact "Default checked exception get thrown" {
			inputStream.read throws IOException
		}
	}
	
}