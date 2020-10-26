'''
An implementation of the grade-school multiplication method for multi-digit integers
'''

import sys

def rotate(l, n):
    return l[n:] + l[:n] 

def single_digits_multiply(x,y,c):
    prod = (x * y) + c
    keep = prod % 10
    carry = int(prod/10)
    #print(x,y,prod,keep,carry)
    return (keep, carry)

def column_sum(l,c):
    csum = sum(l) + c
    keep = csum % 10
    carry = int(csum/10)
    return (keep, carry)

# read the arguments
if len(sys.argv) != 3:
    print("Expected 2 positive integer arguments to multiply. Exiting.")
    sys.exit()
n_a = sys.argv[1]
n_b = sys.argv[2]

# remove negative signs, but keep track of product's sign
sign = 1
n_ai = int(n_a)
n_bi = int(n_b)
if n_ai < 0:
    n_ai *= -1
    n_a = str(n_ai)
    sign *= -1
if n_bi < 0:
    n_bi *= -1
    n_b = str(n_bi)
    sign *= -1

# ensure that a number with more digits is named n_a
if len(n_b) > len(n_a):
    temp = n_b
    n_b = n_a
    n_a = temp

# convert integers to string, then reverse
s_a = str(n_a)[::-1]
s_b = str(n_b)[::-1]

# multiple the digits with carries
rows = []
for i in range(len(s_b)):
    carry = 0
    res = []
    for j in range(len(s_a)):
        keep, to_carry = single_digits_multiply(int(s_b[i]), int(s_a[j]), carry)
        res.append(keep)
        carry = to_carry
    if carry > 0:
        res.append(carry)
    rows.append(res[::-1])

rrows = []
# pad the rows with zeros, then rotate right
nb_rows = len(rows)
n = nb_rows - 1
for row in rows:
    row += [0] * (nb_rows - 1)
    row = rotate(row, -n)
    n -= 1
    rrows.append(row)

# add the row columns with carries
res = []
ncols = len(rows[0])
icol = ncols-1
carry = 0
while icol >= 0:
    l = [rrows[irow][icol] for irow in range(nb_rows)]
    keep, to_carry = column_sum(l, carry)
    carry = to_carry
    icol -= 1
    res.append(keep)
if carry > 0:
    res.append(carry)

# reverse the list and create a single int from the digits
res = res[::-1]
res_str = ''
for x in res:
    res_str += str(x)
res = int(res_str) * sign

print(sys.argv[1], " x ", sys.argv[2], " = ", res, sep='')
