

# def funcme():
#     with open('./sampletext.txt','r') as file:
#         file = file.read()
#         print(file)
#         return file


def listreturn():
    # mylist=['hello']
    with open('sampletext.txt','r') as file:
        lines = [line.strip() for line in file]
        return lines



print(listreturn())
