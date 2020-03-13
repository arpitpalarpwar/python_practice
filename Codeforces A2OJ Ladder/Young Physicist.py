n = int(input())
sum = [0, 0, 0]
strvectors = []
for each in range(n):
	temp = input()
	temp_list = temp.split(" ")
	strvectors.append(temp_list)
for each in range(3):
	for every in strvectors:
		sum[each] += int(every[each])
print(sum)
if sum[0]==0 and sum[1]==0 and sum[2]==0:
	print("YES")
else:
	print("NO")
