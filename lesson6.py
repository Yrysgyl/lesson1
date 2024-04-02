# def sq(r):
#     print(3.14*r**2)
#
# sq(1)



# def is_num(x):
#     if x % 3 == 0:
#         print(True)
#     else:
#         print(False)
#
# is_num(8)



# def max_list(mylist):
#     print(max(mylist))
#
# max_list([1, 3, 2])

evens = 0
def even_counter(mylist):

    for x in mylist:
        if x % 2 == 0:
            evens += 1
    print(evens)

even_counter([1, 2, 3, 4])


