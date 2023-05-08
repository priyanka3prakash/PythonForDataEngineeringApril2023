# from pprint import pp

# # print(f"{globals() = }")

# num1 = 100

# # print("globals\n")
# # pp(globals())
# # print()


# # print("locals\n")
# # pp(locals())



# def myfunc():
#     num1 = 200
#     num2 = 300
#     print("WITHIN FUNCTION")
#     print("globals\n")
#     pp(globals())
#     print()

#     print("locals\n")
#     pp(locals())


# myfunc()


# print("locals\n")
# pp(locals())




assert globals() == locals()



def myfunc():
    assert globals() != locals()


