from decimal import Decimal

def plumiu(x, neg_sig = False):
    if x[0] == '-':
        fir_sig = -1
        i = 1
    else:
        fir_sig = 1
        i = 0

    po = 1
    t = False
    tem = 0
    while i < len(x):
        if x[i] == '.':
            po = Decimal('0.1')
            t = False
        elif x[i] == '+':
            po = 1
            t = False
            return Decimal(str(fir_sig * tem)) - plumiu(x[i + 1:], neg_sig) if neg_sig else Decimal(
                str(fir_sig * tem)) + plumiu(x[i + 1:], neg_sig)
        elif x[i] == '-':
            po = 1
            t = False
            return Decimal(str(fir_sig * tem)) + plumiu(x[i+1:], not neg_sig) if neg_sig else Decimal(
                str(fir_sig * tem)) - plumiu(x[i+1:], not neg_sig)
        elif x[i] == '×':
            po = 1
            t = False
            return muldiv(Decimal(str(fir_sig * tem)), x[i+1:], '×', neg_sig)
        elif x[i] == '÷':
            po = 1
            t = False
            return muldiv(Decimal(str(fir_sig * tem)), x[i+1:], '÷', neg_sig)
        elif po == 1:
            if t:
                tem = tem * 10 + int(x[i])
            else:
                tem = int(x[i])
                t = True
        else:
            tem = tem + Decimal(str(po)) * int(x[i])
            po *= Decimal('0.1')

        i += 1

    return Decimal(str(fir_sig * tem))


def muldiv(pre, x, sig, neg_sig):
    if x[0] == '-':
        fir_sig = -1
        i = 1
    else:
        fir_sig = 1
        i = 0

    po = 1
    t = False
    tem = 0
    while i < len(x):
        if x[i] == '.':
            po = Decimal('0.1')
            t = False
        elif x[i] == '+':
            po = 1
            t = False
            return cal(pre, Decimal(fir_sig * tem), sig) - plumiu(x[i + 1:], neg_sig) if neg_sig \
                else cal(pre, Decimal(fir_sig * tem), sig) + plumiu(x[i + 1:], neg_sig)
        elif x[i] == '-':
            po = 1
            t = False
            return cal(pre, Decimal(fir_sig * tem), sig) + plumiu(x[i+1:], not neg_sig) if neg_sig \
                else cal(pre, Decimal(fir_sig * tem), sig) - plumiu(x[i+1:], not neg_sig)
        elif x[i] == '×':
            po = 1
            t = False
            return muldiv(cal(pre, Decimal(fir_sig * tem), sig), x[i+1:], '×', neg_sig)
        elif x[i] == '÷':
            po = 1
            t = False
            return muldiv(cal(pre, Decimal(fir_sig * tem), sig), x[i+1:], '÷', neg_sig)
        elif po == 1:
            if t:
                tem = tem * 10 + int(x[i])
            else:
                tem = int(x[i])
                t = True
        else:
            tem = tem + Decimal(str(po)) * int(x[i])
            po *= Decimal('0.1')

        i += 1

    return cal(Decimal(pre), Decimal(fir_sig * tem), sig)

def cal(pre, tem, sig):
    if sig == '×':
        ans = pre * tem
    else:
        ans = pre/tem
    return ans

def square(x):
    ans = Decimal(str(x)) ** 2
    return float(ans)

def sqrt(x):
    ans = Decimal(str(x)).sqrt()
    return float(ans)

def exp(x):
    ans = Decimal(x).exp()
    return float(ans)

def ln(x):
    ans = Decimal(x).ln()
    return float(ans)
