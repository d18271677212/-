# cmd /k D:\devlop\Python\Anaconda3\python.exe "$(FULL_CURRENT_PATH)" & PAUSE & EXIT
class Solution:
    def reverseinteger(self,number):
        x =  int (number/100)
        y =  int (number%100/10)
        z =  int (number%100%10)
        return z*100+y*10+x

#主函数
if __name__ == '__main__':
    s = Solution()
    num = 345
    ans = s.reverseinteger(num)
    print(ans)