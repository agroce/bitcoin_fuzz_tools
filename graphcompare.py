import scipy
import scipy.stats

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

N1 = [('mutants_seed42/killed_1502', 55.56160593032837), ('mutants_seed42/killed_449', 140.7861111164093), ('mutants_seed42/killed_9', 74.3017635345459), ('mutants_seed42/killed_460', 108.03766751289368), ('mutants_seed42/killed_1129', 57.15281367301941), ('mutants_seed42/killed_348', 4439.250566244125), ('mutants_seed42/killed_1137', 2032.2104532718658), ('mutants_seed42/killed_3', 67.61023306846619), ('mutants_seed42/killed_431', 75.73776483535767), ('mutants_seed42/killed_618', 43203.028584718704), ('mutants_seed42/killed_1066', 79.49195766448975), ('mutants_seed42/killed_242', 5401.356610774994), ('mutants_seed42/killed_1417', 168.74587726593018), ('mutants_seed42/survived_658', 43202.803599357605), ('mutants_seed42/survived_1753', 43202.428923130035), ('mutants_seed42/survived_759', 10491.193236351013), ('mutants_seed42/survived_805', 43202.919251680374), ('mutants_seed42/survived_228', 43203.44841217995), ('mutants_seed42/killed_1502', 61.07845187187195), ('mutants_seed42/killed_449', 298.06552147865295), ('mutants_seed42/killed_9', 106.74383807182312), ('mutants_seed42/killed_460', 54.44321608543396), ('mutants_seed42/killed_1129', 47.075960874557495), ('mutants_seed42/killed_348', 2266.6716828346252), ('mutants_seed42/killed_1137', 1994.4586668014526), ('mutants_seed42/killed_3', 130.82659816741943), ('mutants_seed42/killed_431', 76.98770833015442), ('mutants_seed42/killed_618', 24217.776700019836), ('mutants_seed42/killed_1066', 104.55267572402954), ('mutants_seed42/killed_242', 936.3390669822693), ('mutants_seed42/killed_1417', 61.47227907180786), ('mutants_seed42/survived_658', 43202.689633369446), ('mutants_seed42/survived_1753', 43208.48574972153), ('mutants_seed42/survived_759', 43202.76196074486), ('mutants_seed42/survived_805', 43203.9697394371), ('mutants_seed42/survived_228', 43202.24044895172), ('mutants_seed42/killed_1502', 297.30779242515564), ('mutants_seed42/killed_449', 933.325766324997), ('mutants_seed42/killed_9', 219.36620950698853), ('mutants_seed42/killed_460', 68.98412108421326), ('mutants_seed42/killed_1129', 57.43545150756836), ('mutants_seed42/killed_348', 7006.9418387413025), ('mutants_seed42/killed_1137', 951.5882303714752), ('mutants_seed42/killed_3', 82.99896550178528), ('mutants_seed42/killed_431', 102.15510034561157), ('mutants_seed42/killed_618', 40669.6086101532), ('mutants_seed42/killed_1066', 225.4459264278412), ('mutants_seed42/killed_242', 457.77613639831543), ('mutants_seed42/killed_1417', 159.62359428405762)]
N2 = [('mutants_seed42/killed_1502', 53.79181170463562), ('mutants_seed42/killed_449', 131.26873421669006), ('mutants_seed42/killed_9', 263.7123878002167), ('mutants_seed42/killed_460', 67.45381283760071), ('mutants_seed42/killed_1129', 49.35186004638672), ('mutants_seed42/killed_348', 2342.4895033836365), ('mutants_seed42/killed_1137', 910.8268361091614), ('mutants_seed42/killed_3', 83.99982285499573), ('mutants_seed42/killed_431', 68.78929543495178), ('mutants_seed42/killed_618', 32264.159745693207), ('mutants_seed42/killed_1066', 98.96442246437073), ('mutants_seed42/killed_242', 128.50975370407104), ('mutants_seed42/killed_1417', 150.29492092132568), ('mutants_seed42/survived_658', 43202.65274858475), ('mutants_seed42/survived_1753', 584.4955701828003), ('mutants_seed42/survived_759', 12383.588916063309), ('mutants_seed42/survived_805', 43203.53522443771), ('mutants_seed42/survived_228', 43203.2775285244), ('mutants_seed42/killed_1502', 59.55177688598633), ('mutants_seed42/killed_449', 278.037713766098), ('mutants_seed42/killed_9', 165.37012004852295), ('mutants_seed42/killed_460', 80.2530586719513), ('mutants_seed42/killed_1129', 47.982736587524414), ('mutants_seed42/killed_348', 6574.0064561367035), ('mutants_seed42/killed_1137', 505.18670415878296), ('mutants_seed42/killed_3', 161.12479066848755), ('mutants_seed42/killed_431', 49.116337060928345), ('mutants_seed42/killed_618', 2076.4643971920013), ('mutants_seed42/killed_1066', 96.09596228599548), ('mutants_seed42/killed_242', 317.00660586357117), ('mutants_seed42/killed_1417', 72.27675938606262), ('mutants_seed42/survived_658', 43205.4211769104), ('mutants_seed42/survived_1753', 43202.233770132065), ('mutants_seed42/survived_759', 12025.95254611969), ('mutants_seed42/survived_805', 43202.697476148605), ('mutants_seed42/survived_228', 43203.581453084946), ('mutants_seed42/killed_1502', 60.65534806251526), ('mutants_seed42/killed_449', 85.66209292411804), ('mutants_seed42/killed_9', 64.07904148101807), ('mutants_seed42/killed_460', 91.95375180244446), ('mutants_seed42/killed_1129', 51.524478912353516), ('mutants_seed42/killed_348', 43202.5502102375), ('mutants_seed42/killed_1137', 1894.183367729187), ('mutants_seed42/killed_3', 68.58820056915283), ('mutants_seed42/killed_431', 68.14674830436707), ('mutants_seed42/killed_618', 7763.0147042274475), ('mutants_seed42/killed_1066', 271.3674490451813), ('mutants_seed42/killed_242', 605.4740605354309), ('mutants_seed42/killed_1417', 125.22593307495117), ('mutants_seed42/survived_658', 43202.59993600845)]

V1 = [('mutants_seed42/killed_1502', 76.35064339637756), ('mutants_seed42/killed_449', 59.126580476760864), ('mutants_seed42/killed_9', 87.77212262153625), ('mutants_seed42/killed_460', 72.40932774543762), ('mutants_seed42/killed_1129', 67.9616949558258), ('mutants_seed42/killed_348', 3652.9100041389465), ('mutants_seed42/killed_1137', 3840.9078476428986), ('mutants_seed42/killed_3', 91.45432376861572), ('mutants_seed42/killed_431', 75.68387365341187), ('mutants_seed42/killed_618', 1641.3930513858795), ('mutants_seed42/killed_1066', 141.95360112190247), ('mutants_seed42/killed_242', 1026.0413575172424), ('mutants_seed42/killed_1417', 267.6162648200989), ('mutants_seed42/survived_658', 19162.81358885765), ('mutants_seed42/survived_1753', 3563.0400013923645), ('mutants_seed42/survived_759', 9831.192429542542), ('mutants_seed42/survived_805', 13099.194093942642), ('mutants_seed42/survived_228', 43202.22873330116), ('mutants_seed42/killed_1502', 55.097577810287476), ('mutants_seed42/killed_449', 253.610200881958), ('mutants_seed42/killed_9', 198.92114925384521), ('mutants_seed42/killed_460', 68.45341444015503), ('mutants_seed42/killed_1129', 49.829333782196045), ('mutants_seed42/killed_348', 31748.08025431633), ('mutants_seed42/killed_1137', 75.73792910575867), ('mutants_seed42/killed_3', 138.96391081809998), ('mutants_seed42/killed_431', 59.95818090438843), ('mutants_seed42/killed_618', 10395.665775060654), ('mutants_seed42/killed_1066', 63.973055839538574), ('mutants_seed42/killed_242', 468.2161331176758), ('mutants_seed42/killed_1417', 105.34765481948853), ('mutants_seed42/survived_658', 43202.68243384361), ('mutants_seed42/survived_1753', 7661.848161458969), ('mutants_seed42/survived_759', 31705.852573394775), ('mutants_seed42/survived_805', 43203.39366316795), ('mutants_seed42/survived_228', 43203.33075237274), ('mutants_seed42/killed_1502', 260.33771681785583), ('mutants_seed42/killed_449', 118.82696080207825), ('mutants_seed42/killed_9', 120.23242282867432), ('mutants_seed42/killed_460', 63.80321002006531), ('mutants_seed42/killed_1129', 59.93639659881592), ('mutants_seed42/killed_348', 23888.628585100174), ('mutants_seed42/killed_1137', 1516.7616176605225), ('mutants_seed42/killed_3', 84.60417890548706), ('mutants_seed42/killed_431', 74.77655911445618), ('mutants_seed42/killed_618', 12328.768921613693), ('mutants_seed42/killed_1066', 272.1830098628998), ('mutants_seed42/killed_242', 139.6454095840454), ('mutants_seed42/killed_1417', 106.02397751808167)]
V2 = [('mutants_seed42/killed_1502', 58.84327006340027), ('mutants_seed42/killed_449', 81.3130874633789), ('mutants_seed42/killed_9', 197.7460114955902), ('mutants_seed42/killed_460', 82.25485420227051), ('mutants_seed42/killed_1129', 52.019211292266846), ('mutants_seed42/killed_348', 8843.326258182526), ('mutants_seed42/killed_1137', 2168.158437728882), ('mutants_seed42/killed_3', 160.36366319656372), ('mutants_seed42/killed_431', 59.47570061683655), ('mutants_seed42/killed_618', 12008.861892461777), ('mutants_seed42/killed_1066', 75.23991990089417), ('mutants_seed42/killed_242', 320.5345997810364), ('mutants_seed42/killed_1417', 72.02591490745544), ('mutants_seed42/survived_658', 43202.52312541008), ('mutants_seed42/survived_1753', 4442.391037225723), ('mutants_seed42/survived_759', 5306.9947600364685), ('mutants_seed42/survived_805', 5413.599029541016), ('mutants_seed42/survived_228', 43203.06744360924), ('mutants_seed42/killed_1502', 59.1057186126709), ('mutants_seed42/killed_449', 273.0764844417572), ('mutants_seed42/killed_9', 77.06938982009888), ('mutants_seed42/killed_460', 66.86758780479431), ('mutants_seed42/killed_1129', 51.92722821235657), ('mutants_seed42/killed_348', 22742.20089530945), ('mutants_seed42/killed_1137', 1996.4181728363037), ('mutants_seed42/killed_3', 248.61504411697388), ('mutants_seed42/killed_431', 55.80852699279785), ('mutants_seed42/killed_618', 3641.8671095371246), ('mutants_seed42/killed_1066', 106.03026986122131), ('mutants_seed42/killed_242', 241.81633973121643), ('mutants_seed42/killed_1417', 168.86794471740723), ('mutants_seed42/survived_658', 43204.2867910862), ('mutants_seed42/survived_1753', 42101.477617263794), ('mutants_seed42/survived_759', 23006.485098600388), ('mutants_seed42/survived_805', 875.4315164089203), ('mutants_seed42/survived_228', 43202.61391186714), ('mutants_seed42/killed_1502', 66.51235938072205), ('mutants_seed42/killed_449', 218.7146599292755), ('mutants_seed42/killed_9', 127.10953736305237), ('mutants_seed42/killed_460', 69.0529420375824), ('mutants_seed42/killed_1129', 56.60935664176941), ('mutants_seed42/killed_348', 796.3966822624207), ('mutants_seed42/killed_1137', 5962.709785461426), ('mutants_seed42/killed_3', 57.81143569946289), ('mutants_seed42/killed_431', 59.53876852989197), ('mutants_seed42/killed_618', 112.8123528957367), ('mutants_seed42/killed_1066', 484.75781202316284), ('mutants_seed42/killed_242', 300.72843194007874), ('mutants_seed42/killed_1417', 84.03209638595581), ('mutants_seed42/survived_658', 43204.72905111313)]

N3 = [('mutants_seed100/killed_5', 43205.40952920914), ('mutants_seed100/killed_166', 4689.9068150520325), ('mutants_seed100/killed_422', 302.4042344093323), ('mutants_seed100/killed_457', 3609.285752058029), ('mutants_seed100/killed_478', 47.93768119812012), ('mutants_seed100/killed_184', 61.474650859832764), ('mutants_seed100/killed_596', 172.10302090644836)]

V3 = [('mutants_seed100/killed_5', 13361.41188621521), ('mutants_seed100/killed_166', 697.7914156913757), ('mutants_seed100/killed_422', 233.58395981788635), ('mutants_seed100/killed_457', 795.7774965763092), ('mutants_seed100/killed_478', 48.13772797584534), ('mutants_seed100/killed_184', 197.54292702674866), ('mutants_seed100/killed_596', 58.33727717399597)]

N4 = [('mutants_seed100/killed_5', 43203.300072193146), ('mutants_seed100/killed_166', 3172.2327947616577), ('mutants_seed100/killed_422', 518.366423368454), ('mutants_seed100/killed_457', 4154.5212943553925), ('mutants_seed100/killed_478', 45.80846858024597), ('mutants_seed100/killed_184', 271.77821159362793), ('mutants_seed100/killed_596', 123.69228529930115)]

V4 = [('mutants_seed100/killed_5', 43204.43036818504), ('mutants_seed100/killed_166', 699.1304626464844), ('mutants_seed100/killed_422', 273.8956253528595), ('mutants_seed100/killed_457', 900.8616733551025), ('mutants_seed100/killed_478', 47.03464698791504), ('mutants_seed100/killed_184', 538.53555727005), ('mutants_seed100/killed_596', 109.7285783290863)]

N = N1 + N2 + N3 + N4
V = V1 + V2 + V3 + V4
A = N + V

mall = {}
mhard = {}

for (m, t) in A:
    mall[m] = True
    if t > 43000:
        mhard[m] = True
print()
print()
for m in mhard:
    Nm = list(map(lambda x: x[1], filter(lambda x: x[0] == m, N)))
    Vm = list(map(lambda x: x[1], filter(lambda x: x[0] == m, V)))
    print("="*80)
    print(m, len(Nm))
    print("no value profile:", scipy.mean(Nm), scipy.median(Nm), scipy.std(Nm))
    print("value profile:", scipy.mean(Vm), scipy.median(Vm), scipy.std(Vm))
    print(scipy.stats.wilcoxon(Nm, Vm))
    print()
                      
        
print("TOTAL OF", len(mall), "MUTANTS")
print(len(mhard), "HARD MUTANTS", len(mall)-len(mhard), "EASY MUTANTS")
print()

Neasy = list(map(lambda x: x[1], filter(lambda x: x[0] not in mhard, N)))
Veasy = list(map(lambda x: x[1], filter(lambda x: x[0] not in mhard, V)))
Nhard = list(map(lambda x: x[1], filter(lambda x: x[0] in mhard, N)))
Vhard = list(map(lambda x: x[1], filter(lambda x: x[0] in mhard, V)))

print("EASY MUTANTS: TOTAL DATA POINTS:", len(Neasy), "PER METHOD")
print("no value profile:", scipy.mean(Neasy), scipy.median(Neasy), scipy.std(Neasy))
print("with value profile:", scipy.mean(Veasy), scipy.median(Veasy), scipy.std(Veasy))
print(scipy.stats.wilcoxon(Neasy,Veasy))
print()
print("HARD MUTANTS: TOTAL DATA POINTS:", len(Nhard), "PER METHOD")
print("no value profile:", scipy.mean(Nhard), scipy.median(Nhard), scipy.std(Nhard))
print("with value profile:", scipy.mean(Vhard), scipy.median(Vhard), scipy.std(Vhard))

print(scipy.stats.wilcoxon(Nhard,Vhard))

f1 = plt.figure(figsize=(7,4))
plt.ylabel("Time")
plt.yscale('log')
bb = plt.boxplot([Neasy, Veasy, Nhard, Vhard], labels=["E/no value profile", "E/value profile", "H/no value profile", "H/value profile"])
pp = PdfPages("time.pdf")
pp.savefig(f1)
pp.close()
