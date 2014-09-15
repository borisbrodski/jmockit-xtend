package org.eclipse.xtend.jmockit.test.expectations;

public class PartialMock5API {
	public String toBeMocked() {
		throw new NotMocked();
	}
	public void notToBeMocked() {
		throw new NotMocked();
	}
}
