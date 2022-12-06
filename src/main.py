
# Online IDE - Code Editor, Compiler, Interpreter
with open('data.txt') as f:
    read = f.readlines()
    modified = []
    
    for line in read:
        items = line.strip()
        modified.append(items.split(","))
 
    
    #totalsales
    
    totalSales = 0
    
    for i in range(1,len(modified)):
            p = int(modified[i][-1])
            totalSales += p
        
    #print(totalSales)
    
    #monthwiseSales
    
    monthwiseSales = 0
    count = 1
    
    for i in range(1,len(modified)):
        q = modified[i][0][5:7]
        if q=="01":
            q=int(q[-1])
        else:
            q=int(q)
        if count == q:
            monthwiseSales += int(modified[i][-1])
        else:
            #print(count ,monthwiseSales)
            count = q
            monthwiseSales = int(modified[i][-1])
    #print(q,monthwiseSales)

        
    #mostpopularItem
    dictofitems = {}
    monthwiseSales = 0
    count = 1
    
    for i in range(1,len(modified)):
        q = modified[i][0][5:7]
        if q=="01":
            q=int(q[-1])
        else:
            q=int(q)
        if count == q:
            monthwiseSales += int(modified[i][-1])
            e = modified[i][1]
            if e not in dictofitems:
                dictofitems[e] = int(modified[i][-2])
            if e in dictofitems:
                dictofitems[e] = dictofitems[e] + int(modified[i][-2])
        else:
            maximum = max(dictofitems, key=dictofitems.get)
            #print(maximum, dictofitems[maximum])
            count = q
            monthwiseSales = int(modified[i][-1])
            dictofitems = {}
    maximum = max(dictofitems, key=dictofitems.get)
    #print(maximum, dictofitems[maximum])
    
    
   #mostrevenueItem
    dictofitems2 = {}
    monthwiseSales = 0
    count = 1
    
    for i in range(1,len(modified)):
        q = modified[i][0][5:7]
        if q=="01":
            q=int(q[-1])
        else:
            q=int(q)
        if count == q:
            monthwiseSales += int(modified[i][-1])
            e = modified[i][1]
            if e not in dictofitems2:
                dictofitems2[e] = int(modified[i][-1])
            if e in dictofitems2:
                dictofitems2[e] = dictofitems2[e] + int(modified[i][-1])
        else:
            maximum = max(dictofitems2, key=dictofitems2.get)
            #print(maximum, dictofitems2[maximum])
            count = q
            monthwiseSales = int(modified[i][-1])
            dictofitems2 = {}
    maximum = max(dictofitems2, key=dictofitems2.get)
    #print(maximum, dictofitems2[maximum])
    
    #minmaxavgofitem
    import statistics
    
    dictofitems3 = {}
    monthwiseSales = 0
    count = 1
    daycount = 1
    ordercount = 0
    eachdayorders = []
    mostpopularItem2 = maximum
    
    for i in range(1,len(modified)):
        r = modified[i][0][-2:]
        q = modified[i][0][5:7]
        if q=="01" or r=="01":
            q=int(q[-1])
            r = int(r[-1])
        else:
            q=int(q)
            r = int(r)
        if count == q:
            monthwiseSales += int(modified[i][-1])
            e = modified[i][1]
            if e not in dictofitems3:
                dictofitems3[e] = int(modified[i][-2])
                if e==mostpopularItem2 and daycount==r:
                    ordercount += 1
                elif e==mostpopularItem2 and daycount!=r:
                    eachdayorders.append(ordercount)
                    ordercount = 1
                    daycount = r
            if e in dictofitems3:
                dictofitems3[e] = dictofitems3[e] + int(modified[i][-2])
                if e==mostpopularItem2 and daycount==r:
                    ordercount += 1
                elif e==mostpopularItem2 and daycount!=r:
                    eachdayorders.append(ordercount)
                    ordercount = 1
                    daycount = r
        else:
            min1 = min(eachdayorders)
            print('month',count,'min',min1)
            max1 = max(eachdayorders)
            print('month',count,'max',max1)
            avg1 = statistics.mean(eachdayorders)
            print('month',count,'avg',round(avg1,3))
            count = q
            monthwiseSales = int(modified[i][-1])
            dictofitems3 = {}
            ordercount = 0
            daycount = 1
            eachdayorders = []
    min1 = min(eachdayorders)
    print('month',count,'min',min1)
    max1 = max(eachdayorders)
    print('month',count,'max',max1)
    avg1 = statistics.mean(eachdayorders)
    print('month',count,'avg',round(avg1,3))