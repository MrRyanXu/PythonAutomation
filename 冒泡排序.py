'''
冒泡排序
'''

def bubble_sort(items):
    for i in range(0,len(items)-1):
        status = False
        for j in range(0,len(items)-i-1):
            if items[j] > items[j+1]:
                items[j],items[j+1] = items[j+1],items[j]
                status = True
        print(items)
        if status == False:
            break
    return items

num = [5,7,8,3,1]
bubble_sort(num)
