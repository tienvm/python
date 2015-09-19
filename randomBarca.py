
import random


ThuMon = ['ER STEGEN', 'C.BRAVO', 'J.MASIP', 'OSE SUAREZ']
HauVeTru = ['PIQUE', 'ADRIANO', 'MONTOYA', 'D.ALVES']
HauVeBien = ['BARTRA', 'DOUGLAS', 'J.ALBA', 'MATHIEU']
TienVe = ['RAKITIC', 'BUSQUETS', 'INIESTA', 'RAFINHA', 'RAMÍREZ', 'S.ROBERTO', 'DEULOFEU', 'A.TURAN']
TienDao = ['SUÁREZ', 'L.MESSI', 'NEYMAR', 'HADDADI', 'S.RAMIREZ']

BDoiHinhRaSan = ThuMon + HauVeTru + HauVeBien + TienDao + TienVe
BThuMon = random.sample(ThuMon, 1)
print('THU MON: %30s ' % list(BThuMon))
BHauVeTru = random.sample(HauVeTru, 2)
print('HAU VE TRU: %30s ' % list(BHauVeTru))
BHauVeBien = random.sample(HauVeBien, 2)
print('HAU VE BIEN: %30s' % list(BHauVeBien))
BTienVe = random.sample(TienVe, 4)
print('TIEN VE: %20s' % list(BTienVe))
BTienDao = random.sample(TienDao, 2)
print('TIEN DAO: %30s' % list(BTienDao))
