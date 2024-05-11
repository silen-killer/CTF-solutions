from Crypto.Util.number import long_to_bytes
from sympy.ntheory.modular import crt
from sympy import cbrt

ns = [231689896592553079225008346159565141292942746185614335113030628126523977770897610833, 7171431858055720778675521, 66926822362327139196541990168817936306935699,
      437335592290538364420374052921942150635299817629860400585996176158735283605573507708521, 289641633885807692370107575915133663791, 667489211907833441904090408183964916738111, 3567528272153764003837574317682649383619949327607]
cs = [70932244057518414814271820586538428333420562252483260602196856595136636875881109254, 6776581747370220150625940, 48565469191356626147008517582743644359421796,
      8794419984130129081066440741470891653922464557881503503363167507918405790466608773101, 172864555741817549854149625512946760571, 123698332225047871848637413013333477895868, 2621823962661199268500092259451160990545103771980,]
print(long_to_bytes(cbrt(crt(ns, cs)[0])))
# flag{Wh4t_d0_y0u_m34n_1t_h4s_t0_b3_co-pr1m3}
