s=set()
# l=[1,2,3,4]
# s_from_list=set(l)
# print(type(s_from_list))
# print(s_from_list)
s.add(1)
s.add(2)
print(s.union({3,4,5,6}))
print(s.intersection({2,3,3,2,}))
print(s.symmetric_difference({1,2,3,4,5,6}))
print(s.isdisjoint({3,4,5}))
print(s.remove(2))
print(s)