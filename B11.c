#include <jni.h>
#include <stdio.h>
#include "B11.h"

JNIEXPORT void JNICALL Java_B11_add1(JNIEnv *env, jobject obj, jint a, jint b)
{
    printf("\n%d + %d = %d\n", a, b, (a + b));
}

JNIEXPORT void JNICALL Java_B11_sub1(JNIEnv *env, jobject obj, jint a, jint b)
{
    printf("\n%d - %d = %d\n", a, b, (a - b));
}

JNIEXPORT void JNICALL Java_B11_mult1(JNIEnv *env, jobject obj, jint a, jint b)
{
    printf("\n%d * %d = %d\n", a, b, (a * b));
}

JNIEXPORT void JNICALL Java_B11_div1(JNIEnv *env, jobject obj, jint a, jint b)
{
    if (b == 0)
        printf("\nDivision by zero is not allowed!\n");
    else
        printf("\n%d / %d = %d\n", a, b, (a / b));
}
