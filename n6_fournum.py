n=4311
def uby(n):
        a=n/1000
        b=(n-(int(a)*1000))/100
        c=n-((a*1000)+(b*100))/10
        d=n-(a*1000)+(b*100)+(c*10)
        if(a>b>c>d):
                print("raspolojeny po ubyvaniu")
        else:
                print("ne po ubyvaniu")
uby(4311)
