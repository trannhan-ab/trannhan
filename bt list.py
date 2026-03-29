'''Bài 3: Cho đầu vào là _list= [1, 2, 3, 4, 5, 6, 7, 8, 9]. Viết chương trình python tạo 2 list mới từ list đó cho. Trong đó 1 list chỉ bao gồm số chẵn (even), 1 list chỉ bao gồm số lẻ (odd).
 '''
_list= [1,2,3,4,5,6,7,8,9]
lc=[]
ll=[]
for i in _list:
    if i%2==0:
        lc.append(i)
    else:
        ll.append(i)
print('list chan ka: ', lc)
print('list le la: ', ll)
'''Bài 4: Cho danh sách ban đầu _list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']. Tạo danh sách mới chứa 2 phần tử ở vị trí thứ 2 và thứ 3 _new = ['White', 'Black']
 '''
_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
_new=[]
_new.insert(0, _list[2:4])
print(_new)
''' Bài 5: Cho danh sách đầu vào _list = [‘zero’, ‘three’]. Tạo ra danh sách mới _new = [‘zero’, ‘one’, ‘two’, ‘three’] bằng cách thêm các phần tử vào danh sách ban đầu.'''
_list = ['zero', 'three']
_new=_list
_new.insert(1, 'one')
_new.insert(2, 'two')
print(_new)

'''
         