def divide_par_1(lst, start, end):
	i = start - 1
	pivot = lst[end]

	for j in range(start, end):
		if(lst[j] <= pivot):
			i += 1
			lst[i],lst[j] = lst[j],lst[i]
	lst[i+1],lst[end] = lst[end],lst[i+1]
	return (i+1)

def Qsort(lst, start, end):
	if(len(lst) == 1):
		return lst
	if(start < end):
		mid = divide_par_1(lst, 0, end)

		Qsort(lst, start, mid - 1)
		Qsort(lst, mid + 1, end)

a = list([10, 80, 30, 90, 40, 50, 70])
Qsort(a, 0, len(a) - 1)
print(a)
