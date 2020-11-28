from numpy import linalg as LA, array


def get_str_number(number, digits=2):
    return f"%.{digits}f" % number


kn = array([[3.147487662,-0.987542948,-0.963792489,-0.576720128,-0.969316377,1.196751577,-0.032752228,1.25464684,0.184524802,-1.098597671],
           [-0.987542948,1.916481565,1.772679294,0.175901843,1.89064521,-0.075331856,0.27339884,-0.179298384,0.43239451,0.253059138],
           [-0.963792489,1.772679294,1.823039876,0.419534682,1.748847223,-0.045652264,0.089212644,-0.188648574,0.392341655,0.032160497],
           [-0.576720128,0.175901843,0.419534682,1.635262499,0.150094112,0.370210629,0.106312697,0.223612777,0.265292909,-0.592825203],
           [-0.969316377,1.89064521,1.748847223,0.150094112,1.872966578,-0.097893705,0.251506113,-0.195833278,0.409156145,0.249186138],
           [1.196751577,-0.075331856,-0.045652264,0.370210629,-0.097893705,2.153607353,-0.014231252,2.057358823,0.88672061,-0.553371802],
           [-0.032752228,0.27339884,0.089212644,0.106312697,0.251506113,-0.014231252,1.976511219,-0.00751519,0.152506639,0.091340142],
           [1.25464684,-0.179298384,-0.188648574,0.223612777,-0.195833278,2.057358823,-0.00751519,2.03788979,0.862647219,-0.5428895],
           [0.184524802,0.43239451,0.392341655,0.265292909,0.409156145,0.88672061,0.152506639,0.862647219,0.86672389,-0.099185481],
           [-1.098597671,0.253059138,0.032160497,-0.592825203,0.249186138,-0.553371802,0.091340142,-0.5428895,-0.099185481,1.918045736]])

kw, kv = LA.eig(kn)
print("kw: ")
print(kw)
for ww in kw:
    print(get_str_number(ww,26))
print("kv: ")
print(kv)
print("\n\n\n\n")


k = array([[452.0991333,-1628.177587,-3390.285903,-38217.02879,-179.7742845,3542.488009,-0.375022372,72.30134807,172.5955291,-1224.16785],
           [-1628.177587,36268.24723,71574.62807,133794.5247,4024.836093,-2559.523905,35.93264146,-118.5980132,4642.277605,3236.685197],
           [-3390.285903,71574.62807,157047.8889,680836.4943,7943.228179,-3309.404434,25.01646235,-266.2328079,8987.157707,877.6233973],
           [-38217.02879,133794.5247,680836.4943,49992109.1,12842.44888,505563.1795,561.5955268,5944.888111,114478.1517,-304755.2012],
           [-179.7742845,4024.836093,7943.228179,12842.44888,448.5226986,-374.1549768,3.71840987,-14.57148357,494.1471021,358.5242663],
           [3542.488009,-2559.523905,-3309.404434,505563.1795,-374.1549768,131372.8581,-3.358104274,2443.259992,17092.13599,-12707.32282],
           [-0.375022372,35.93264146,25.01646235,561.5955268,3.71840987,-3.358104274,1.804107091,-0.034523239,11.37130326,8.113545484],
           [72.30134807,-118.5980132,-266.2328079,5944.888111,-14.57148357,2443.259992,-0.034523239,47.11517959,323.7153405,-242.6995646],
           [172.5955291,4642.277605,8987.157707,114478.1517,494.1471021,17092.13599,11.37130326,323.7153405,5279.110086,-719.7067143],
           [-1224.16785,3236.685197,877.6233973,-304755.2012,358.5242663,-12707.32282,8.113545484,-242.6995646,-719.7067143,16580.35829]])

w,v = LA.eig(k)
print("w: ")
print(w)
print("v: ")
print(v)