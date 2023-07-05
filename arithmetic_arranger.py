def arithmetic_arranger(arr,opt=None):
        if len(arr)>5:
                return "Error: Too many problems"
        for i in arr:
                if "+" not in i and "-" not in i:
                        return "Error: Operator must be '+' or '-'"
        n=len(arr)
        a=[]
        b=[]
        c=[]
        s=" "
        d="-"
        for i in range(n):
                p="+"
                q="-"
                arr[i]=arr[i].replace(" ","")
                if p in arr[i]:
                        a.append(arr[i][:arr[i].index(p)])
                        b.append(arr[i][arr[i].index(p)+1:])
                        c.append("+")
                elif q in arr[i]:
                        a.append(arr[i][:arr[i].index(q)])
                        b.append(arr[i][arr[i].index(q)+1:])
                        c.append("-")
        for i in range(n):
                if a[i].isdigit()==False or b[i].isdigit()==False:
                        return "Error: Numbers must only contain digits"
                if len(a[i])>4 or len(b[i])>4:
                        return "Error: Numbers cannot be more than four digits"
        for i in range(n):
                if len(a[i])>=len(b[i]):
                        print("  "+a[i]+"\t",end="")
                else:
                        print("  "+s*(len(b[i])-len(a[i]))+a[i]+"\t",end="")
        print()
        for i in range(n):
                if len(a[i])>=len(b[i]):
                        print(c[i]+" "+s*(len(a[i])-len(b[i]))+b[i]+"\t",end="")
                else:
                        print(c[i]+" "+b[i]+"\t",end="")
        print()
        for i in range(n):
                m=max(len(a[i]),len(b[i]))
                print(d*(m+2)+"\t"+s,end="")
        print()
        if opt==True:
                for i in range(n):
                        if "+" in arr[i]:
                                print(" "+str(int(a[i])+int(b[i]))+"\t",end="")
                        elif "-" in arr[i]:
                                print(" "+str(int(a[i])-int(b[i]))+"\t",end="")
                        
        return ""
        
import main
