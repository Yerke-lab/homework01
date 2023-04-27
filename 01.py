#1. Реализуйте метод, принимающий в качестве аргументов два целочисленных массива, 
# и возвращающий новый массив, каждый элемент которого равен разности элементов двух входящих массивов в той же ячейке. 
#Если длины массивов не равны, необходимо как-то оповестить пользователя.

def diff_arrays(arr1, arr2):
    if len(arr1) != len(arr2):
        print("Длина массивов не равны")
        return None
    
    diff_arr = []
    for i in range(len(arr1)):
        diff_arr.append(arr1[i] - arr2[i])
    
    return diff_arr

arr1 = [7, 4, 8]
arr2 = [5, 1, 3]

result = diff_arrays(arr1, arr2)
print(result) 

#Реализуйте метод, принимающий в качестве аргументов два целочисленных массива, и возвращающий 
# новый массив, каждый элемент которого равен частному элементов двух входящих массивов в той же ячейке.
# Если длины массивов не равны, необходимо как-то оповестить пользователя. 


def divide_arrays(arr1, arr2):
    if len(arr1) != len(arr2):
        print("Длина массивов не равны")
        return None
    
    result = [0] * len(arr1)
    for i in range(len(arr1)):
        result[i] = arr1[i] / arr2[i]
    
    return result
 
arr1 = [8, 4, 5]
arr2 = [2, 1, 5]
print(divide_arrays(arr1, arr2))

#Реализуйте метод, принимающий в качестве аргументов два целочисленных массива, и возвращающий новый массив,
# каждый элемент которого равен сумме элементов двух входящих массивов в той же ячейке. 
# Если длины массивов не равны, необходимо как-то оповестить пользователя.

def sum_arrays(arr1, arr2):
    if len(arr1) != len(arr2):
        print("Длина массивов не равны")
        return None
    
    sum_arr = []
    for i in range(len(arr1)):
        sum_arr.append(arr1[i] + arr2[i])
    
    return sum_arr

arr1 = [7, 4, 8]
arr2 = [5, 1, 3]

result = sum_arrays(arr1, arr2)
print(result) 

# Реализуйте метод, принимающий в качестве аргументов двумерный массив. 
# Метод должен проверить что длина строк и столбцов с одинаковым индексом одинакова, 
# детализировать какие строки со столбцами не требуется. Как бы вы реализовали подобный метод?

def check_array(array):
    rows = len(array)
    cols = len(array[0]) if rows > 0 else 0

    for i in range(rows):
        if len(array[i]) != cols:
            return False

    return True


arr = [[6, 1, 3], [4, 1, 6], [7, 8, 2]]
print(check_array(arr))  

invalid_array = [[11, 2, 3], [4, 7], [7, 1, 9]]
print(check_array(invalid_array)) 
