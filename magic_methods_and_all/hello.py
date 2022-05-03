def SayHello(name):
    """we can change module __name__ attribute"""
    print ("Hi {}! How are you?".format(name))
    
__name__="SayHello"