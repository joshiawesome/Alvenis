#[('12.056062', '80.046547'), ('13.056062', '81.046547')]
#[{lat:10.999398, lng: 77.024713},{lat: 11.000043, lng: 77.026587},{lat: 11.022264, lng: 77.022038},{lat: 11.026350, lng: 77.020853}]"

dat=[('12.056062', '80.046547'), ('13.056062', '81.046547')]

x=2

z=""
for i in range(0,x):
    
    la=dat[i][0]
    ln=dat[i][1]
    z=z+"{lat: %s,lng: %s}"%(la,ln)
    if i!=(x-1):
        z=z+","
    
z="["+z+"]"
print(z)



    
    
    
    
