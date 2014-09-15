package org.eclipse.xtend.jmockit.test.expectations;

import java.util.ArrayList;
import java.util.LinkedList;

public class ExpectationsAPI {
	public ExpectationsAPI returnSelf() {
		throw new NotMocked();
	}
	public void returnVoid() {
		throw new NotMocked();
	}
	public String returnString() {
		throw new NotMocked();
	}
	public Exception returnException() {
		throw new NotMocked();
	}
	public int returnInt() {
		throw new NotMocked();
	}
	public long returnLong() {
		throw new NotMocked();
	}
	public short returnShort() {
		throw new NotMocked();
	}
	public byte returnByte() {
		throw new NotMocked();
	}
	public float returnFloat() {
		throw new NotMocked();
	}
	public double returnDouble() {
		throw new NotMocked();
	}
	public boolean returnBoolean() {
		throw new NotMocked();
	}
	public char returnCharacter() {
		throw new NotMocked();
	}
	public String paramsSelf(ExpectationsAPI a) {
		throw new NotMocked();
	}
	public String paramsString(String a) {
		throw new NotMocked();
	}
	public String paramsInt(int a) {
		throw new NotMocked();
	}
	public String paramsLong(long a) {
		throw new NotMocked();
	}
	public String paramsByte(byte a) {
		throw new NotMocked();
	}
	public String paramsShort(short a) {
		throw new NotMocked();
	}
	public String paramsFloat(float a) {
		throw new NotMocked();
	}
	public String paramsDouble(double a) {
		throw new NotMocked();
	}
	public String paramsChar(char a) {
		throw new NotMocked();
	}
	public String paramsBoolean(boolean a) {
		throw new NotMocked();
	}
	public String paramsIntInt(int a, int b) {
		throw new NotMocked();
	}
	public String paramsIntIntInt(int a, int b, int c) {
		throw new NotMocked();
	}
	public String paramsIntIntIntInt(int a, int b, int c, int d) {
		throw new NotMocked();
	}
	public String paramsIntIntIntIntInt(int a, int b, int c, int d, int e) {
		throw new NotMocked();
	}
	public String paramsIntIntIntIntIntInt(int a, int b, int c, int d, int e, int f) {
		throw new NotMocked();
	}
	public String paramsLongLong(long a, long b) {
		throw new NotMocked();
	}
	public String paramsLongLongLong(long a, long b, long c) {
		throw new NotMocked();
	}
	public String paramsShortShort(short a, short b) {
		throw new NotMocked();
	}
	public String paramsShortShortShort(short a, short b, short c) {
		throw new NotMocked();
	}
	public String paramsByteByte(byte a, byte b) {
		throw new NotMocked();
	}
	public String paramsByteByteByte(byte a, byte b, byte c) {
		throw new NotMocked();
	}
	public String paramsFloatFloat(float a, float b) {
		throw new NotMocked();
	}
	public String paramsFloatFloatFloat(float a, float b, float c) {
		throw new NotMocked();
	}
	public String paramsDoubleDouble(double a, double b) {
		throw new NotMocked();
	}
	public String paramsDoubleDoubleDouble(double a, double b, double c) {
		throw new NotMocked();
	}
	public String paramsCharChar(char a, char b) {
		throw new NotMocked();
	}
	public String paramsCharCharChar(char a, char b, char c) {
		throw new NotMocked();
	}
	public String paramsBooleanBoolean(boolean a, boolean b) {
		throw new NotMocked();
	}
	public String paramsBooleanBooleanBoolean(boolean a, boolean b, boolean c) {
		throw new NotMocked();
	}
	public String paramsStringString(String a, String b) {
		throw new NotMocked();
	}
	public String paramsStringStringString(String a, String b, String c) {
		throw new NotMocked();
	}
	public String paramsStringBLongBoolean(String a, Long b, boolean c) {
		throw new NotMocked();
	}
	public String paramsObject(Object a) {
		throw new NotMocked();
	}
	public String paramsList(ArrayList<?> arrayList) {
		throw new NotMocked();
	}
	public String paramsList(LinkedList<?> arrayList) {
		throw new NotMocked();
	}
	public String paramsPrivateString(String a) {
		throw new NotMocked();
	}
	public String callParamsPrivateString(String a) {
		return paramsPrivateString(a);
	}
}
