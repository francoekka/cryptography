from audioop import reverse

def multiplicative_inverse(n, mod):
    t1 = 0
    t2 = 1
    r1=mod
    r2=n
    while r2>0:
        q=r1//r2
        r=r1-(q*r2)
        t=t1-(q*t2)
        r1=r2
        r2=r
        t1=t2
        t2=t
    if r1==1:
        if t1<0:
            return t1+mod
        else:
            return t1
    else:
        return -1


def encryption(plain_text,public_key):
    count=len(public_key)
    encrypted=[]
    res=0
    index=0
    plain_text.append(0) #for one extra count
    #print(public_key[0])
    for i in plain_text:
        if(count==0):
            encrypted.append(res)
            res=0
            index=0
            count=len(public_key)
        
        if(i==1):
            res = res + public_key[index]
        count=count-1
        index=index+1
    
    # for i in range(0,len(decrypted)):
    #     print(decrypted[i])
    return encrypted
        


def decryption(encrypted_res,private_key,n,m):
    mul_inv = multiplicative_inverse(n,m)
    res_list=[]
    plain_text=[]
    for i in encrypted_res:
        res=mul_inv*int(i)
        res_list.append(res%m)
    
    print("\ndecrypted list: ")
    for i in range(0,len(res_list)):
        print(res_list[i],end=" ")
    

    private_key.reverse()
    decrypted_text=[]
    for i in res_list:
        value = i
        j = 0
        while(value>0):
            if(private_key[j]>value):
                plain_text.append(0)
                j=j+1
            elif(private_key[j]<=value):
                plain_text.append(1)
                value=value-private_key[j]
                j=j+1
        plain_text.reverse()
        decrypted_text.extend(plain_text)
        plain_text=[]

    # print("\ndecrytion: ")
    # for i in range(0,len(decrypted_text)):
    #     print(decrypted_text[i],end=" ")
    return decrypted_text




private_key = [1,2,4,10,20,40]
m = 110 #m>sum of all elements in private key
n=31 #n is the multiplier, no factor should be common with modulus
public_key=[]
for i in range(0,len(private_key)):
    res = n*int(private_key[i])
    public_key.append(res%m)
# for i in range(0,len(private_key)):
#     print(public_key[i])



plain_text = [1,0,0,1,0,0,1,1,1,1,0,0,1,0,1,1,1,0] #user-defined
print("\nplain text: ")
for i in plain_text:
    print(i,end=" ")

encrypted_res = encryption(plain_text,public_key)
print("\nencryption: ")
for i in range (0,len(encrypted_res)):
    print(encrypted_res[i],end=" ")

decrypted_res = decryption(encrypted_res,private_key,n,m)
print("\ndecryption: ")
for i in range (0,len(decrypted_res)):
    print(decrypted_res[i],end=" ")

