N = int(input("Введіть кількість студентів, N= "))
K = int(input("Введіть кількість яблук, K= "))
if K >= N:
    B = K//N
    C = K%N
    print("Кількість яблук у студентів, В=  ", B)
    print("Кількість яблук в корзині, С= ", C)
else:
    print("Яблук менше, ніж студентів")
    
input()
