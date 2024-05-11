from secret import flag
from Crypto.Util.number import *


def genKey(nbits, dbits):
    bbits = (nbits // 2 - dbits) // 2

    while True:
        a = getRandomNBitInteger(dbits)
        b = getRandomNBitInteger(bbits)
        c = getRandomNBitInteger(bbits)
        p1 = a * b * c + 1
        if isPrime(p1):
            # print("p1 =", p1)
            break

    while True:
        d = getRandomNBitInteger(dbits)
        p2 = b * c * d + 1
        if isPrime(p2):
            # print("p2 =", p2)
            break

    while True:
        e = getRandomNBitInteger(bbits)
        f = getRandomNBitInteger(bbits)
        q1 = e * d * f + 1
        p3 = a * e * f + 1
        if isPrime(q1) and isPrime(p3):
            # print("p3 =", p3)
            # print("q1 =", q1)
            break

    while True:
        d_ = getRandomNBitInteger(dbits)
        if GCD(a * b * c * d * e * f, d_) != 1:
            continue
        e_ = inverse(d_, a * b * c * d * e * f)
        k1 = (e_ * d_ - 1) // (a * b * c * d * e * f)
        assert e_ * d_ == (a * b * c * d * e * f) * k1 + 1
        q2 = k1 * e * f + 1
        q3 = k1 * b * c + 1
        if isPrime(q2) and isPrime(q3):
            # print("q2 =", q2)
            # print("q3 =", q3)
            # print("e =", e_)
            # print("d =", d_)
            break

    n1 = p1 * q1
    n2 = p2 * q2
    n3 = p3 * q3
    
    assert pow(pow(0xdeadbeef, e_, n1), d_, n1) == 0xdeadbeef
    assert pow(pow(0xdeadbeef, e_, n2), d_, n2) == 0xdeadbeef
    assert pow(pow(0xdeadbeef, e_, n3), d_, n3) == 0xdeadbeef

    return(e_, n1, n2, n3)


nbits = 0x600
dbits = 0x210

m = bytes_to_long(flag)
e, n1, n2, n3 = genKey(nbits, dbits)
c = pow(m, e, n1)

print("c =", c)
print("e =", e)
print("n1 =", n1)
print("n2 =", n2)
print("n3 =", n3)

# c = 63442255298812942222810837512019302954917822996915527697525497640413662503768308023517128481053593562877494934841788054865410798751447333551319775025362132176942795107214528962480350398519459474033659025815248579631003928932688495682277210240277909527931445899728273182691941548330126199931886748296031014210795428593631253184315074234352536885430181103986084755140024577780815130067722355861473639612699372152970688687877075365330095265612016350599320999156644
# e = 272785315258275494478303901715994595013215169713087273945370833673873860340153367010424559026764907254821416435761617347240970711252213646287464416524071944646705551816941437389777294159359383356817408302841561284559712640940354294840597133394851851877857751302209309529938795265777557840238332937938235024502686737802184255165075195042860413556866222562167425361146312096189555572705076252573222261842045286782816083933952875990572937346408235562417656218440227
# n1 = 473173031410877037287927970398347001343136400938581274026578368211539730987889738033351265663756061524526288423355193643110804217683860550767181983527932872361546531994961481442866335447011683462904976896894011884907968495626837219900141842587071512040734664898328709989285205714628355052565784162841441867556282849760230635164284802614010844226671736675222842060257156860013384955769045790763119616939897544697150710631300004180868397245728064351907334273953201
# n2 = 327163771871802208683424470007561712270872666244394076667663345333853591836596054597471607916850284565474732679392694515656845653581599800514388800663813830528483334021178531162556250468743461443904645773493383915711571062775922446922917130005772040139744330987272549252540089872170217864935146429898458644025927741607569303966038195226388964722300472005107075179204987774627759625183739199425329481632596633992804636690274844290983438078815836605603147141262181
# n3 = 442893163857502334109676162774199722362644200933618691728267162172376730137502879609506615568680508257973678725536472848428042122350184530077765734033425406055810373669798840851851090476687785235612051747082232947418290952863499263547598032467577778461061567081620676910480684540883879257518083587862219344609851852177109722186714811329766477552794034774928983660538381764930765795290189612024799300768559485810526074992569676241537503405494203262336327709010421