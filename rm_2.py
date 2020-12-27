# cmd /k D:\devlop\Python\Anaconda3\python.exe "$(FULL_CURRENT_PATH)" & PAUSE & EXIT
''' 拼接两个数组,并升序输出'''
class Sarray:
    def slist(self,A,B):
        i,j = 0,0
        C = []
        while i < len(A) and j < len(B):
            if A[i] < B[j]:
                C.append(A[i])
                i +=1
            else:
                C.append(B[j])
                j +=1
          
        while i < len(A):
            C.append(A[i])
            i +=1
        while j < len(B):
            C.append(B[j])
            j += 1
        return C
 
if __name__ == '__main__':
    x = [1,3,5,8,13]
    y = [23,5,16,67,1]
    z = [9,5,6,1,2,4]
    g = 0
    
    s = Sarray()
    print('x+y:',s.slist(x,y))
   
#本案例失败,需重构   