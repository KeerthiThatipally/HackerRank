class Solution(object):
    def reduce(self,str):
        res_str=" "

        # while(True):
        #     count=0
        #     for i in range(0,len(str)-1):
        #         print("i:",i)
        #         print("str is :"+str[i])
        #         if(str[i]==str[i+1]):
        #             res_str=str[:i]+str[i+2:]
        #             print(res_str)
        #             count=count+1
        #         i=i+1
        #     if(count>0):
        #         self.reduce(res_str)
        #     else:
        #         break


        for(i=1;i<len(str);i=i+1):
                print("i:", i)
                print("str is :" + str[i])
                if (str[i] == str[i + 1]):
                    str = str[:i] + str[i + 2:]

                    print(res_str)

                i=0



        return res_str



if __name__=="__main__":
    sol=Solution()
    str=input("enter the String to be reduced")
    res=sol.reduce(str)
    print("res is"+res)

