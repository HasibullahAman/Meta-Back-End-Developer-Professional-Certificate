def d():
    animal = 'elephent'
    def e():
        nonlocal animal
        animal = 'griaffe'
        print("Inside Nested function " + animal)
    print("beffor calling function " + animal)
    e()
    print("afther calling function " + animal)
    
    
animal = 'camel'
d()
print("Global animal " + animal)

