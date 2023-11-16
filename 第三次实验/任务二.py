class MyArray:
    def __IsNumber(self,n):
        return isinstance(n, (int, float, complex))
    def __init__(self,*args):
        if not args:
            self.__value =[]
        else:
            for arg in args:
                if not self.__IsNumber(arg):
                    print('All elements must be numbers')
                    return
            self.__value = list(args)
    def __add__(self,n):
        if self.__IsNumber(n):
            b = MyArray()
            b.__value = [item + n for item in self.__value]
            return b
        elif isinstance(n, MyArray):
            if len(n.__value)==len(self.__value):
                c = MyArray()
                c.__value = [i+j for i, j in zip(self.__value, n.__value)]
                return c
            else:
                print('Length not equal')
        else:
            print('Not supported')
    def __sub__(self,n):
        if not self.__IsNumber(n):
            print('- operation with ',type(n),'and number type is not supported')
            return
        b = MyArray()
        b.__value = [item-n for item in self.__value]
        return b
    def __mul__(self,n):
        if type(n)==int:
            b=MyArray()
            b.__value=[item*n for item in self.__value]
            return b
        elif type(n.__value)==list:
            if len(self.__value)==len(n.__value):
                result=0
                for i in range(0,len(self.__value)):
                    result=result+n.__value[i]*self.__value[i]
                return result
            else:
                print('两向量的长度不相同')
                return self
        else:
            print('* operation with ', type(n), 'and number type is not supported')
            return
    def __truediv__(self,n):
        if not self.__IsNumber(n):
            print(r'/ operation with ',type(n),'and number type is not supported')
            return
        b = MyArray()
        b.__value = [item/n for item in self.__value]
        return b
    def __floordiv__(self,n):
        if not self.__IsNumber(n):
            print(n,' is not a integer')
            return
        b = MyArray()
        b.__value = [item//n for item in self.__value]
        return b
    def __mod__(self,n):
        if not self.__IsNumber(n):
            print(r'% operation with ',type(n),'and number type is not supported')
            return
        b = MyArray()
        b.__value = [item%n for item in self.__value]
        return b
    def __pow__(self,n):
        if not self.__IsNumber(n):
            print('** operation with ',type(n),'and number type is not supported')
            return
        b = MyArray()
        b.__value = [item**n for item in self.__value]
        return b
    def __len__(self):
        return len(self.__value)
    def __repr__(self):
        return repr(self.__value)
    def __str__(self):
        return str(self.__value)
    #追加元素
    def append(self,v):
        assert self.__IsNumber(v),'Only number can be appended.'
        self.__value.append(v)
    def __getitem__(self,index):
        length = len(self.__value)
        if isinstance(index, int) and 0<=index<length:
            return self.__value[index]
        elif isinstance(index,(list,tuple)):
            for i in index:
                if not (isinstance(i, int) and 0<=i<length):
                    return 'index error'
            result = []
            for item in index:
                result.append(self.__value[item])
            return result
        else:
            return 'index error'
    def __setitem__(self, index, value):
        length = len(self.__value)
        if isinstance(index, int) and 0<=index<length:
            self.__value[index] = value
        elif isinstance(index,(list,tuple)):
            for i in index:
                if not (isinstance(i, int) and 0<=i<length):
                    raise Exception('index error')
            if isinstance(value,(list,tuple)):
                if len(index) == len(value):
                    for i,v in enumerate(index):
                        self.__value[v] = value[i]
                else:
                    raise Exception('values and index must be of the same length')
            elif isinstance(value, (int,float,complex)):
                for i in index:
                    self.__value[i] = value
            else:
                raise Exception('value error')
        else:
            raise Exception('index error')
    def __contains__(self, v):
        return v in self.__value
    def __eq__(self, v):
        assert isinstance(v, MyArray), 'wrong type'
        return self.__value == v.__value
    def __lt__(self, v):
        assert isinstance(v, MyArray), 'wrong type'
        return self.__value < v.__value


if __name__=='__main__':
    ma=MyArray(1,2,3,4,5,6)
    ma=ma*2
    print(ma)
    print('------------')
    mb=MyArray(1,2,3,4)
    ma=ma*mb
    print('------------')
    mc=MyArray(1,2,3,4,5,6)
    result=ma*mc
    print(result)
