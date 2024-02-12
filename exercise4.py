print('grades calculator')

math = int( input('math; '))
eng = int(input('eng: '))
phy = int(input('phy; '))
kisw = int(input('kisw: '))
hist = int( input('hist; '))

tt = math +eng +phy + kisw + hist
avg = tt/5
print(avg)

if avg < 0 or avg > 100:
    print('invalid')
elif avg >= 0 and avg<=39:
    print('E')
elif avg >= 40 and avg<=50:
    print('D')
elif avg >= 51 and avg <= 60:
    print('C')
elif avg >=61 and avg<=70:
    print('B')
elif avg >=71 and avg<=100:
    print('A')
else:
    print('invalid')

















