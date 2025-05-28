from multipledispatch import dispatch

@dispatch(int,int)
def sub(a,b):
    result=a - b
    print(result)
    
@dispatch(int,int,int)
def sub(a,b,c):
    result=a-b-c
    print(result) 
    
    
sub(1,2)
sub(1,2,3)
    
       