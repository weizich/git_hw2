input_richter=input("Please input a Richter scale value:")
ritchter=float(input_richter)
#寫出地震能量計算公式
E=10**((1.5*ritchter)+4.8)
#把地震能量除以炸彈能量
E_TNT=E/(4.184*(10**9))
#把地震能量除以午餐能量
E_lunch=E/2930200
#印出
print("Richter scale value:",input_richter)
print("Equivalence in Joules:",E)
print("Equivalence in tons of TNT:",E_TNT)
print("Equivalence in the number of nutritious lunches:",E_lunch)