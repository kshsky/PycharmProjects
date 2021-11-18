from decimal import *

class NumberUtil(object):
    @staticmethod
    def _round_by_decimal(number,quantize_exp):
        str_num = str(number)
        quantize=Decimal(str(quantize_exp))
        dec_num = Decimal(str_num).quantize(quantize,rounding=ROUND_HALF_UP)
        return float(dec_num)

a = NumberUtil()
print(a._round_by_decimal(4.555,'0.00'))
print(a._round_by_decimal(4.555,'0.0'))
print(a._round_by_decimal(4.555,'0'))
print(a._round_by_decimal(1.5,'0'))
print(a._round_by_decimal(2.5,'0'))

print(a._round_by_decimal(1.234,'.00'))
print(a._round_by_decimal(1.235,'.00'))
print(a._round_by_decimal(1.236,'.00'))
print(a._round_by_decimal(-1.234,'.00'))
print(a._round_by_decimal(-1.235,'.00'))
print(a._round_by_decimal(-1.236,'.00'))