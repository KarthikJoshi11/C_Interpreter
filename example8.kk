#include<stdio.h>
#include<math.h>

int main() {
    double x = 2.5;
    double y = 3.0;
    
    // Test basic arithmetic with math functions
    printf("Square root of %.2f is %.4f\n", x, sqrt(x));
    printf("Power %.2f raised to %.2f is %.4f\n", x, y, pow(x, y));
    
    // Test trigonometric functions
    printf("sin(%.2f) = %.4f\n", x, sin(x));
    printf("cos(%.2f) = %.4f\n", x, cos(x));
    printf("tan(%.2f) = %.4f\n", x, tan(x));
    
    // Test logarithmic and exponential functions
    printf("ln(%.2f) = %.4f\n", x, log(x));
    printf("e^%.2f = %.4f\n", x, exp(x));
    
    // Test rounding functions
    printf("floor(%.2f) = %.2f\n", x, floor(x));
    printf("ceil(%.2f) = %.2f\n", x, ceil(x));
    
    // Test absolute value
    double negx = -x;
    printf("|%.2f| = %.2f\n", negx, fabs(negx));
    
    return 0;
} 