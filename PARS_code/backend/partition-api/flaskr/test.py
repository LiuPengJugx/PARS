pars=[
    'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a0','',
    'a7', 'a8', 'a9', 'a10', 'a11','',
    'a12', 'a13', 'a14', 'a15', 'a16','',
    'a17', 'a18', 'a19', 'a20', 'a21','',
    'a22', 'a23', 'a24','',
    'a25', 'a26', 'a27', 'a28', 'a29', 'a30', 'a31', 'a32', 'a33', 'a34', 'a35', 'a36', 'a37', 'a38', 'a39', 'a40', 'a41', 'a42', 'a43', 'a44', 'a45', 'a46', 'a47', 'a48','a49'
]
import random
data=[]

for x in range(0,7):
    for y in range(len(pars)):
        if pars[y]!='':
            data.append([x,y,random.randint(0,15)])
        else:
            data.append([x, y, 0])
print(data)
