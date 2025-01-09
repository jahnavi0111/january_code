re=[]

if len(arr)==1:

    print([])  

else:   

    for i in range(len(arr)):

        for j in range(i+1,len(arr)):

            if arr[i]==arr[j] and arr[i] not in re:

               re.append(arr[j])

    print(re)
