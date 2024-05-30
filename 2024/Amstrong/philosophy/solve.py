# x = (p + 1) * (q + 1) = n + p + q + 1
# phi = (p - 1) * (q - 1) = n - x + 1 
n = 86088719452932625928188797700212036385645851492281481088289877829109110203124545852827976798704364393182426900932380436551569867036871171400190786913084554536903236375579771401257801115918586590639686117179685431627540567894983403579070366895343181435791515535593260495162656111028487919107927692512155290673
e = 65537
c = 64457111821105649174362298452450091137161142479679349324820456191542295609033025036769398863050668733308827861582321665479620448998471034645792165920115009947792955402994892700435507896792829140545387740663865218579313148804819896796193817727423074201660305082597780007494535370991899386707740199516316196758
x = 86088719452932625928188797700212036385645851492281481088289877829109110203124545852827976798704364393182426900932380436551569867036871171400190786913084573410416063246853198167436938724585247461433706053188624379514833802770205501907568228388536548010385588837258085711058519777393945044905741975952241886308

from Crypto.Util.number import inverse

phi = n - (x%n) + 1
d = inverse(e, phi)
m = pow(c, d, n)
print(bytes.fromhex(hex(m)[2:]).decode())
