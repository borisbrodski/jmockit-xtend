package org.eclipse.xtend.jmockit.test;

import org.eclipse.xtend.jmockit.test.docexamples.MyTest;
import org.junit.runner.RunWith;
import org.junit.runners.Suite;
import org.junit.runners.Suite.SuiteClasses;


@RunWith(Suite.class)
@SuiteClasses({ MyTest.class, AllJnarioTestsSuite.class })
public class AllTests {
}
