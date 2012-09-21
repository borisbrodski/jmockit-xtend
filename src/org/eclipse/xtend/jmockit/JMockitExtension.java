package org.eclipse.xtend.jmockit;

import mockit.Expectations;
import mockit.internal.expectations.transformation.ActiveInvocations;

import org.eclipse.xtext.xbase.lib.Procedures.Procedure1;

public class JMockitExtension {
    public static void mock(final Procedure1< Expectations > proc) {
        new Expectations() {

            {
                proc.apply(this);
            }
        };
    }

    public static void setResult(Expectations expectations, Object result) throws Exception {
        ActiveInvocations.addResult(result);
    }
    
}
