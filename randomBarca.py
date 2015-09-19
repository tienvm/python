
import random


ThuMon = ['ER STEGEN', 'C.BRAVO', 'J.MASIP', 'OSE SUAREZ']
HauVeTru = ['PIQUE', 'ADRIANO', 'MONTOYA', 'D.ALVES']
HauVeBien = ['BARTRA', 'DOUGLAS', 'J.ALBA', 'MATHIEU']
TienVe = ['RAKITIC', 'BUSQUETS', 'INIESTA', 'RAFINHA', 'RAMÍREZ', 'S.ROBERTO', 'DEULOFEU', 'A.TURAN']
TienDao = ['SUÁREZ', 'L.MESSI', 'NEYMAR', 'HADDADI', 'S.RAMIREZ']

BThuMon = random.sample(ThuMon, 1)
BHauVeTru = random.sample(HauVeTru, 2)
BHauVeBien = random.sample(HauVeBien, 2)
BTienVe = random.sample(TienVe, 4)
BTienDao = random.sample(TienDao, 2)

BDoiHinhRaSan = BThuMon + BHauVeTru + BHauVeBien + BTienVe + BTienDao

print('THU MON: %30s ' % list(BThuMon))
print('HAU VE TRU: %30s ' % list(BHauVeTru))
print('HAU VE BIEN: %30s' % list(BHauVeBien))
print('TIEN VE: %20s' % list(BTienVe))
