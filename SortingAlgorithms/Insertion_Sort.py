def Insertion_Sort(a):
    for number in range(1, len(a)):
        current_number = a[number]
        i = number - 1
        while i >= 0 and current_number < a[i]:
            a[i + 1] = a[i] 			
            i -= 1  		
            a[i + 1] = current_number
