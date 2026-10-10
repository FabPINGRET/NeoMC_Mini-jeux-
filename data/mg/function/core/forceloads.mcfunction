# Zones toujours chargées (lobby + arènes) — idempotent, relancé à chaque /reload
forceload add -16 -16 16 16
forceload add 16 -24 144 24
forceload add -24 11076 24 11124
forceload add -24 11276 24 11324
forceload add -32 11468 32 11532
forceload add -24 11676 24 11724
forceload add -48 11952 48 12048
forceload add -24 12256 24 12324
forceload add -56 12636 56 12764
forceload add -80 13140 80 13260
# Build Battle : parcelles très éloignées (640 blocs) pour qu'on ne voie pas les autres construire
forceload remove -136 13632 136 13768
forceload add -664 13624 -616 13676
forceload add -24 13664 24 13724
forceload add 616 13664 664 13724
forceload add 1256 13664 1304 13724
forceload add 1896 13664 1944 13724
forceload add 2536 13664 2584 13724
forceload add 3176 13664 3224 13724
forceload add -24 14304 24 14364
forceload add 616 14304 664 14364
forceload add 1256 14304 1304 14364
forceload add 1896 14304 1944 14364
forceload add 2536 14304 2584 14364
forceload add 3176 14304 3224 14364
forceload add -16 284 16 316
forceload add -24 4160 24 4240
forceload add -48 4552 48 4648
forceload add -24 4876 24 4924
forceload add -24 5776 24 5824
forceload add -24 6076 24 6124
forceload add -24 6376 24 6424
forceload add -24 6676 24 6724
forceload add 90 6970 140 7030
forceload add -24 5476 24 5524
forceload add -16 5180 112 5220
forceload add 113 5180 144 5220
forceload add -16 584 16 616
forceload add -16 884 16 916
forceload add -40 1160 40 1240
forceload add -48 1470 48 1530
forceload add -17 1783 17 1817
forceload add -48 2065 48 2135
forceload add -48 2365 48 2435
forceload add -48 2660 48 2740
forceload add -48 2960 48 3040
forceload add -48 3260 48 3340
forceload add -64 3560 64 3640
forceload add -48 3860 48 3940
forceload add -48 7260 48 7340
forceload add -64 7540 64 7660
forceload add -64 7840 64 7960
forceload add -48 8160 48 8240
forceload add -32 8470 32 8530
forceload add -48 8760 48 8840
forceload add -24 9070 24 9130
forceload add -24 9470 24 9530
forceload add -32 9868 32 9932
forceload add -40 10260 40 10340
forceload add -32 10668 32 10732
forceload add -96 14904 96 15096
forceload add 30000 -30000 30255 -30000
# TNT Tag : cartes à relief (z 26500 / 26800 / 27400)
# Quake sniper (Ravin z 15450, Tours z 15800)
forceload add -24 15386 24 15514
forceload add -54 15746 54 15854
# Téléphone : salle d'attente (les parcelles sont chargées pendant la partie)
forceload add -8 19412 8 19428
# King of the Hill (z 20400)
forceload add -27 20373 27 20427
# The Towers (z 20800)
forceload add -48 20784 48 20816
# Convoi (z 21200)
forceload add -72 21186 72 21214
# Capture the Flag (z 21600)
forceload add -44 21576 44 21624
# Mini UHC Run (z 22400) et Mini Hunger Games (z 22800)
forceload add -42 22358 42 22442
forceload add -52 22748 52 22852
# Bunker Zombies / Infection (z 23200)
forceload add -17 23161 39 23217
# Prop Hunt (z 23600)
forceload add -23 23582 23 23618
# Tron (z 20000)
forceload add -52 19948 52 20052
# Bombardier (z 32400)
forceload add -88 32312 88 32488
# Meccha Chameleon (z 26600)
forceload add -31 26577 31 26623
# Tennis (z 35400)
forceload add -80 35375 79 35425
# 🎳 Bowling (z 35170)
forceload add -35 35129 34 35185
# 1, 2, 3 Soleil (z 37000)
forceload add -23 36996 23 37099
# Autos tamponneuses (z 37400)
forceload add -24 37376 24 37424
# Slime Jump (z 37800)
forceload add -14 37794 14 37959
# Labyrinthe aveugle (z 38200)
forceload add -3 38197 334 38240
function mg:tnttag/map/fl
# [variantes] sols des variantes (z 24300)
function mg:var/fl
