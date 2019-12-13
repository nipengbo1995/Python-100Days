"""
英寸和厘米互换
"""

value = float(input('请输入长度: '))
unit = input('请输入单位: ')
if unit == 'in' or unit == '英寸':
    print('{:f}英寸 = {:f}厘米'.format(value, value * 2.54))
elif unit == 'cm' or unit == '厘米':
    print('{:f}厘米 = {:f}英寸'.format(value, value / 2.54))
else:
    print('请输入有效的单位')
