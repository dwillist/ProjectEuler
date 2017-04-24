#!/usr/bin/python2.7

# here we just have a function for calculating the current predicted runtime
# of New.py if n = 350
# we will use this to make a decision about weather or not re-writing this program in C
# is a worthwhile task and could potentially give us a runtime of approximately 1 minute.

# the below is the model information from R

    #Call:
#lm(formula = y ~ poly(x, 3, raw = TRUE))
#Coefficients:
#                          Estimate Std. Error t value Pr(>|t|)
#(Intercept)             -6.906e-01  1.208e-01  -5.715 1.26e-07 ***
#poly(x, 3, raw = TRUE)1  1.173e-01  1.033e-02  11.350  < 2e-16 ***
#poly(x, 3, raw = TRUE)2 -4.275e-03  2.378e-04 -17.974  < 2e-16 ***
#poly(x, 3, raw = TRUE)3  4.370e-05  1.554e-06  28.112  < 2e-16 ***

#Residual standard error: 0.2906 on 95 degrees of freedom
#Multiple R-squared:  0.9913,	Adjusted R-squared:  0.9911
#F-statistic:  3622 on 3 and 95 DF,  p-value: < 2.2e-16

def predict(n):
    intercept = -6.906e-01
    c1 = 1.173e-01
    c2 = -4.275e-03
    c3 = 4.370e-05
    return intercept + c1*n + c2*n**2 + c3*n**3

def main():
    user_input = int(raw_input("enter n: "))
    print "---Runtime Estimate---"
    print predict(user_input)

main()
