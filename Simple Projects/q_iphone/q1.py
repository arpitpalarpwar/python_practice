'''
Question - free iphones
            every person gets 1 iphone at a time
            can take as many as he wants but has to get in queue again to get the phone
            1 sec for 1 iphone
            how much total time for a particular person to get all the iphones he wants

'''

def free_iphone(ar, what_pos):
    curr_len, prev_len, count = 0, 0, 0
    count = 0
    pos = what_pos+1
    print(f'array|||| count|||||| position of person{what_pos+1}')
    print(f'{ar}, 0 , {pos}=====>> Current Data')
    while not ar == []:
        prev_len = len(ar)
        first = ar[0]
        ar.pop(0)
        pos -= 1
        if first > 1:
            ar.extend([first-1])
        curr_len = len(ar)
        if pos <= 0:
            pos += curr_len
        count += 1
        if pos == 1 and ar[pos-1] == 1:
            print(f'{ar}, {count}, pos of person{what_pos+1} in the queue:{pos}')
            break
        print(f'{ar}, {count}, pos of person {what_pos+1}:{pos}')
    print(f"Total Time taken by person {what_pos+1} is {count+1}minutes")


arr, what_pos = [1, 1, 1, 1, 1], 1
free_iphone(arr, what_pos)

