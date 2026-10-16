# Duel sniper : (re)construit les 3 arènes (une fois au chargement, ou à la main : /function mg:duel/build_all)
execute if entity @a[tag=mg.dl] run return run tellraw @a[tag=mg.admin] [{"text":"⚔ Duel sniper : reconstruction ignorée, un duel est en cours (réessaie après).","color":"red"}]
data remove storage mg:duel built
forceload add -22 39928 22 40072
forceload add -22 40328 22 40472
forceload add -22 40728 22 40872
schedule function mg:duel/build_canyon_1 60t
schedule function mg:duel/build_canyon_2 64t
schedule function mg:duel/build_canyon_3 68t
schedule function mg:duel/build_canyon_4 72t
schedule function mg:duel/build_canyon_5 76t
schedule function mg:duel/build_canyon_6 80t
schedule function mg:duel/build_canyon_7 84t
schedule function mg:duel/build_canyon_8 88t
schedule function mg:duel/build_canyon_9 92t
schedule function mg:duel/build_ville_1 96t
schedule function mg:duel/build_ville_2 100t
schedule function mg:duel/build_ville_3 104t
schedule function mg:duel/build_ville_4 108t
schedule function mg:duel/build_ville_5 112t
schedule function mg:duel/build_ville_6 116t
schedule function mg:duel/build_ville_7 120t
schedule function mg:duel/build_ville_8 124t
schedule function mg:duel/build_ville_9 128t
schedule function mg:duel/build_ville_10 132t
schedule function mg:duel/build_ville_11 136t
schedule function mg:duel/build_ville_12 140t
schedule function mg:duel/build_ville_13 144t
schedule function mg:duel/build_ville_14 148t
schedule function mg:duel/build_ville_15 152t
schedule function mg:duel/build_ville_16 156t
schedule function mg:duel/build_ville_17 160t
schedule function mg:duel/build_glacier_1 164t
schedule function mg:duel/build_glacier_2 168t
schedule function mg:duel/build_glacier_3 172t
schedule function mg:duel/build_glacier_4 176t
schedule function mg:duel/build_glacier_5 180t
schedule function mg:duel/build_glacier_6 184t
schedule function mg:duel/build_glacier_7 188t
schedule function mg:duel/build_glacier_8 192t
schedule function mg:duel/build_glacier_9 196t
schedule function mg:duel/build_glacier_10 200t
schedule function mg:duel/build_glacier_11 204t
