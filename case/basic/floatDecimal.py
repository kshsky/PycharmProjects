from decimal import *
print('\n================round=====================')


x = Decimal('-3.1415926535') + Decimal('-2.7182818285')
print(x)
print(type(x))
print( x.quantize(Decimal('1.0000'), ROUND_HALF_EVEN))
print( x.quantize(Decimal('1.0000'), ROUND_HALF_DOWN))
print( x.quantize(Decimal('1.0000'), ROUND_CEILING))
print( x.quantize(Decimal('1.0000'), ROUND_FLOOR))
print( x.quantize(Decimal('1.0000'), ROUND_UP))
print( x.quantize(Decimal('1.0000'), ROUND_DOWN))
#
#
print(Decimal('-1.234').quantize(Decimal('1.00'), ROUND_HALF_UP))
print(Decimal('-1.235').quantize(Decimal('1.00'), ROUND_HALF_UP))
print(Decimal('-1.236').quantize(Decimal('1.00'), ROUND_HALF_UP))
print(Decimal('1.234').quantize(Decimal('1.00'), ROUND_HALF_UP))
print(Decimal('1.235').quantize(Decimal('1.00'), ROUND_HALF_UP))
print(Decimal('1.236').quantize(Decimal('1.00'), ROUND_HALF_UP))

strList = ['-1.234','-1.235','-1.236','1.234','1.235','1.236']
for i in strList:
    print(i,'四舍五入后为 ：',Decimal(i).quantize(Decimal('1.00'), ROUND_HALF_UP))