package org.eclipse.xtend.jmockit.test.expectations;

import mockit.Delegate;

public class MoreThat100 implements Delegate<Long> {
    public boolean check(Long l) {
        return l != null && l > 100;
    }
}
