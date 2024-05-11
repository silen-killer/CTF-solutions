from Crypto.Util.number import getRandomNBitInteger, bytes_to_long, long_to_bytes
from sage.all import *

# non-residue
D = 136449572493235894105040063345648963382768741227829225155873529439788000141924302071247144068377223170502438469323595278711906213653227972959011573520003821372215616761555719247287249928879121278574549473346526897917771460153933981713383608662604675157541813068900456012262173614716378648849079776150946352466

# redacted
p = "REDACTED" 
q = "REDACTED"

# n = p*q
n = 22409692526386997228129877156813506752754387447752717527887987964559571432427892983480051412477389130668335262274931995291504411262883294295070539542625671556700675266826067588284189832712291138415510613208544808040871773692292843299067831286462494693987261585149330989738677007709580904907799587705949221601393

flag = b"flag{REDACTED}"

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        x = (self.x*other.x + D*self.y*other.y)%n
        y = (self.y*other.x + self.x*other.y)%n
        return Point(x, y)
    def __mul__(self, d):
        Q = Point(1, 0)
        P = Point(self.x, self.y)
        while d != 0:
            if d&1 == 1:
                Q += P
            P += P
            d >>= 1
        return Q
    def __str__(self) -> str:
        return f"{self.x}, {self.y}"

def check_residue(y):
    if pow(y, (p - 1)//2, p) == 1 and pow(y, (q - 1)//2, q) == 1:
        return True
    return False

def gen_point():
    while True:
        x = getRandomNBitInteger(1023 - 240)
        x = bytes_to_long(flag + long_to_bytes(x))
        x %= n
        y2 = ((x*x - 1)*pow(D, -1, n))%n
        if(check_residue(y2)):
            yp = pow(y2, (p + 1) // 4, p)
            yq = pow(y2, (q + 1) // 4, q)
            y = crt([yp, yq], [p, q])
            return Point(x, y)

M = gen_point()
e = 65537
C = M*e
print(C)
# Cx = 10800064805285540717966506671755608695842888167470823375167618999987859282439818341340065691157186820773262778917703163576074192246707402694994764789796637450974439232033955461105503709247073521710698748730331929281150539060841390912041191898310821665024428887410019391364779755961320507576829130434805472435025, Cy = 2768587745458504508888671295007858261576650648888677215556202595582810243646501012099700700934297424175692110043143649129142339125437893189997882008360626232164112542648695106763870768328088062485508904856696799117514392142656010321241751972060171400632856162388575536779942744760787860721273632723718380811912