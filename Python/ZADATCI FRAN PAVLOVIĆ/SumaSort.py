#Problem: Za danu listu n-torki, sortiraj listu po zbroju elemenata iz svake n-torke.
#Npr, za [(5, 9, 1), (25,), (8, 6), (9, 0, 1, 0),(7, 4), (3,)] se dobije [(3,), (9, 0, 1, 0), (7, 4), (8, 6), (5, 9, 1), (25,)]

def suma_sort(n):
    
    return sum(n)



a = [(59, 7, 1), (28, 8, 4), (3, 2), (33, 11, 22), (7,)]


sorted_a = sorted(a, key=suma_sort)

print(sorted_a)
