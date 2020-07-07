def karatsuba(x: str,y: str):
    if len(x)>len(y):
        y = y.zfill(len(x))
    elif len(y)>len(x):
        x = x.zfill(len(y))
    
    if len(x) > 1:
        n_half = len(x)//2
        left_x = x[:n_half]
        right_x = x[n_half:]
        left_y = y[:n_half]
        right_y = y[n_half:]

        step_one = karatsuba(left_x, left_y)
        step_two = karatsuba(right_x, right_y)
        step_three = karatsuba(str(int(left_x) + int(right_x)), str(int(left_y) + int(right_y)))
        step_four = step_three - step_one - step_two
        result = step_one * (10**(n_half*2)) + step_two + step_four * (10**n_half)

        return result
    else:
        return int(x)*int(y)

if __name__ == '__main__':
    print(karatsuba('3141592653589793238462643383279502884197169399375105820974944592','2718281828459045235360287471352662497757247093699959574966967627'))