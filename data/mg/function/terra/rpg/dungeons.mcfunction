# Chaque seconde : donjons (salles à vagues, déclenchement de l'alpha à l'approche, suivi, victoire, reset si plus personne)
scoreboard players remove $trdc0 mg.st 1
execute unless score $trds0 mg.st matches 0 positioned 55.5 102 -177.5 unless entity @a[tag=mg.tvw,gamemode=adventure,distance=..45] run scoreboard players add $trdr0 mg.st 1
execute unless score $trds0 mg.st matches 0 positioned 55.5 102 -177.5 if entity @a[tag=mg.tvw,gamemode=adventure,distance=..45] run scoreboard players set $trdr0 mg.st 0
execute unless score $trds0 mg.st matches 0 if score $trdr0 mg.st matches 20.. run function mg:terra/rpg/dg/arbre_reset
execute if score $trda0 mg.st matches 1 unless entity @e[tag=mg.trdg_arbre] run function mg:terra/rpg/dg/arbre_win
execute if score $trds0 mg.st matches 0 if score $trdc0 mg.st matches ..0 positioned 55 66 -178 if entity @a[tag=mg.tvw,gamemode=adventure,distance=..7] run function mg:terra/rpg/dg/arbre_w0
execute if score $trds0 mg.st matches 1 positioned 55 66 -178 if loaded ~ ~ ~ unless entity @e[tag=mg.trdw0] run function mg:terra/rpg/dg/arbre_c0
execute if score $trds0 mg.st matches 1 as @e[tag=mg.trdw0] positioned 55.5 102 -177.5 unless entity @s[distance=..45] run tp @s 53.5 64 -179.5
execute if score $trds0 mg.st matches 2 if score $trdc0 mg.st matches ..0 positioned 54 77 -178 if entity @a[tag=mg.tvw,gamemode=adventure,distance=..7] run function mg:terra/rpg/dg/arbre_w1
execute if score $trds0 mg.st matches 3 positioned 54 77 -178 if loaded ~ ~ ~ unless entity @e[tag=mg.trdw0] run function mg:terra/rpg/dg/arbre_c1
execute if score $trds0 mg.st matches 3 as @e[tag=mg.trdw0] positioned 55.5 102 -177.5 unless entity @s[distance=..45] run tp @s 53.5 76 -177.5
execute if score $trds0 mg.st matches 4 if score $trdc0 mg.st matches ..0 positioned 54 89 -178 if entity @a[tag=mg.tvw,gamemode=adventure,distance=..7] run function mg:terra/rpg/dg/arbre_w2
execute if score $trds0 mg.st matches 5 positioned 54 89 -178 if loaded ~ ~ ~ unless entity @e[tag=mg.trdw0] run function mg:terra/rpg/dg/arbre_c2
execute if score $trds0 mg.st matches 5 as @e[tag=mg.trdw0] positioned 55.5 102 -177.5 unless entity @s[distance=..45] run tp @s 53.5 88 -179.5
execute unless score $trda0 mg.st matches 1 if score $trdc0 mg.st matches ..0 if score $trds0 mg.st matches 6 positioned 55.5 102 -177.5 if entity @a[tag=mg.tvw,gamemode=adventure,distance=..12] run function mg:terra/rpg/dg/arbre_start
execute unless score $trds0 mg.st matches 6 if score $trdc0 mg.st matches ..0 unless entity @e[tag=mg.trdw0] positioned 55.5 102 -177.5 if entity @a[tag=mg.tvw,gamemode=adventure,distance=..12] run function mg:terra/rpg/dg/arbre_lock
execute if score $trda0 mg.st matches 1 run function mg:terra/rpg/dg/arbre
scoreboard players remove $trdc1 mg.st 1
execute unless score $trds1 mg.st matches 0 positioned 228.5 114 24.5 unless entity @a[tag=mg.tvw,gamemode=adventure,distance=..53] run scoreboard players add $trdr1 mg.st 1
execute unless score $trds1 mg.st matches 0 positioned 228.5 114 24.5 if entity @a[tag=mg.tvw,gamemode=adventure,distance=..53] run scoreboard players set $trdr1 mg.st 0
execute unless score $trds1 mg.st matches 0 if score $trdr1 mg.st matches 20.. run function mg:terra/rpg/dg/pic_reset
execute if score $trda1 mg.st matches 1 unless entity @e[tag=mg.trdg_pic] run function mg:terra/rpg/dg/pic_win
execute if score $trds1 mg.st matches 0 if score $trdc1 mg.st matches ..0 positioned 228 70 24 if entity @a[tag=mg.tvw,gamemode=adventure,distance=..9] run function mg:terra/rpg/dg/pic_w0
execute if score $trds1 mg.st matches 1 positioned 228 70 24 if loaded ~ ~ ~ unless entity @e[tag=mg.trdw1] run function mg:terra/rpg/dg/pic_c0
execute if score $trds1 mg.st matches 1 as @e[tag=mg.trdw1] positioned 228.5 114 24.5 unless entity @s[distance=..53] run tp @s 225.5 68 21.5
execute if score $trds1 mg.st matches 2 if score $trdc1 mg.st matches ..0 positioned 228 91 24 if entity @a[tag=mg.tvw,gamemode=adventure,distance=..8] run function mg:terra/rpg/dg/pic_w1
execute if score $trds1 mg.st matches 3 positioned 228 91 24 if loaded ~ ~ ~ unless entity @e[tag=mg.trdw1] run function mg:terra/rpg/dg/pic_c1
execute if score $trds1 mg.st matches 3 as @e[tag=mg.trdw1] positioned 228.5 114 24.5 unless entity @s[distance=..53] run tp @s 226.5 91 21.5
execute if score $trds1 mg.st matches 4 if score $trdc1 mg.st matches ..0 positioned 228 113 24 if entity @a[tag=mg.tvw,gamemode=adventure,distance=..9] run function mg:terra/rpg/dg/pic_w2
execute if score $trds1 mg.st matches 5 positioned 228 113 24 if loaded ~ ~ ~ unless entity @e[tag=mg.trdw1] run function mg:terra/rpg/dg/pic_c2
execute if score $trds1 mg.st matches 5 as @e[tag=mg.trdw1] positioned 228.5 114 24.5 unless entity @s[distance=..53] run tp @s 224.5 114 24.5
execute unless score $trda1 mg.st matches 1 if score $trdc1 mg.st matches ..0 if score $trds1 mg.st matches 6 positioned 228.5 114 24.5 if entity @a[tag=mg.tvw,gamemode=adventure,distance=..12] run function mg:terra/rpg/dg/pic_start
execute unless score $trds1 mg.st matches 6 if score $trdc1 mg.st matches ..0 unless entity @e[tag=mg.trdw1] positioned 228.5 114 24.5 if entity @a[tag=mg.tvw,gamemode=adventure,distance=..12] run function mg:terra/rpg/dg/pic_lock
execute if score $trda1 mg.st matches 1 run function mg:terra/rpg/dg/pic
scoreboard players remove $trdc2 mg.st 1
execute unless score $trds2 mg.st matches 0 positioned -224.5 65 -54.5 unless entity @a[tag=mg.tvw,gamemode=adventure,distance=..44] run scoreboard players add $trdr2 mg.st 1
execute unless score $trds2 mg.st matches 0 positioned -224.5 65 -54.5 if entity @a[tag=mg.tvw,gamemode=adventure,distance=..44] run scoreboard players set $trdr2 mg.st 0
execute unless score $trds2 mg.st matches 0 if score $trdr2 mg.st matches 20.. run function mg:terra/rpg/dg/mine_reset
execute if score $trda2 mg.st matches 1 unless entity @e[tag=mg.trdg_mine] run function mg:terra/rpg/dg/mine_win
execute if score $trds2 mg.st matches 0 if score $trdc2 mg.st matches ..0 positioned -207 66 -55 if entity @a[tag=mg.tvw,gamemode=adventure,distance=..8] run function mg:terra/rpg/dg/mine_w0
execute if score $trds2 mg.st matches 1 positioned -207 66 -55 if loaded ~ ~ ~ unless entity @e[tag=mg.trdw2] run function mg:terra/rpg/dg/mine_c0
execute if score $trds2 mg.st matches 1 as @e[tag=mg.trdw2] positioned -224.5 65 -54.5 unless entity @s[distance=..44] run tp @s -210.5 65 -55.5
execute if score $trds2 mg.st matches 2 if score $trdc2 mg.st matches ..0 positioned -207 66 -70 if entity @a[tag=mg.tvw,gamemode=adventure,distance=..7] run function mg:terra/rpg/dg/mine_w1
execute if score $trds2 mg.st matches 3 positioned -207 66 -70 if loaded ~ ~ ~ unless entity @e[tag=mg.trdw2] run function mg:terra/rpg/dg/mine_c1
execute if score $trds2 mg.st matches 3 as @e[tag=mg.trdw2] positioned -224.5 65 -54.5 unless entity @s[distance=..44] run tp @s -209.5 65 -67.5
execute if score $trds2 mg.st matches 4 if score $trdc2 mg.st matches ..0 positioned -207 66 -40 if entity @a[tag=mg.tvw,gamemode=adventure,distance=..7] run function mg:terra/rpg/dg/mine_w2
execute if score $trds2 mg.st matches 5 positioned -207 66 -40 if loaded ~ ~ ~ unless entity @e[tag=mg.trdw2] run function mg:terra/rpg/dg/mine_c2
execute if score $trds2 mg.st matches 5 as @e[tag=mg.trdw2] positioned -224.5 65 -54.5 unless entity @s[distance=..44] run tp @s -209.5 65 -40.5
execute unless score $trda2 mg.st matches 1 if score $trdc2 mg.st matches ..0 if score $trds2 mg.st matches 6 positioned -224.5 65 -54.5 if entity @a[tag=mg.tvw,gamemode=adventure,distance=..12] run function mg:terra/rpg/dg/mine_start
execute unless score $trds2 mg.st matches 6 if score $trdc2 mg.st matches ..0 unless entity @e[tag=mg.trdw2] positioned -224.5 65 -54.5 if entity @a[tag=mg.tvw,gamemode=adventure,distance=..12] run function mg:terra/rpg/dg/mine_lock
execute if score $trda2 mg.st matches 1 run function mg:terra/rpg/dg/mine
scoreboard players remove $trdc3 mg.st 1
execute unless score $trds3 mg.st matches 0 positioned -23.5 90 186.5 unless entity @a[tag=mg.tvw,gamemode=adventure,distance=..44] run scoreboard players add $trdr3 mg.st 1
execute unless score $trds3 mg.st matches 0 positioned -23.5 90 186.5 if entity @a[tag=mg.tvw,gamemode=adventure,distance=..44] run scoreboard players set $trdr3 mg.st 0
execute unless score $trds3 mg.st matches 0 if score $trdr3 mg.st matches 20.. run function mg:terra/rpg/dg/tube_reset
execute if score $trda3 mg.st matches 1 unless entity @e[tag=mg.trdg_tube] run function mg:terra/rpg/dg/tube_win
execute if score $trds3 mg.st matches 0 if score $trdc3 mg.st matches ..0 positioned -50 90 182 if entity @a[tag=mg.tvw,gamemode=adventure,distance=..5] run function mg:terra/rpg/dg/tube_w0
execute if score $trds3 mg.st matches 1 positioned -50 90 182 if loaded ~ ~ ~ unless entity @e[tag=mg.trdw3] run function mg:terra/rpg/dg/tube_c0
execute if score $trds3 mg.st matches 1 as @e[tag=mg.trdw3] positioned -23.5 90 186.5 unless entity @s[distance=..44] run tp @s -49.5 90 181.5
execute if score $trds3 mg.st matches 2 if score $trdc3 mg.st matches ..0 positioned -42 90 183 if entity @a[tag=mg.tvw,gamemode=adventure,distance=..5] run function mg:terra/rpg/dg/tube_w1
execute if score $trds3 mg.st matches 3 positioned -42 90 183 if loaded ~ ~ ~ unless entity @e[tag=mg.trdw3] run function mg:terra/rpg/dg/tube_c1
execute if score $trds3 mg.st matches 3 as @e[tag=mg.trdw3] positioned -23.5 90 186.5 unless entity @s[distance=..44] run tp @s -43.5 89 182.5
execute if score $trds3 mg.st matches 4 if score $trdc3 mg.st matches ..0 positioned -36 90 186 if entity @a[tag=mg.tvw,gamemode=adventure,distance=..6] run function mg:terra/rpg/dg/tube_w2
execute if score $trds3 mg.st matches 5 positioned -36 90 186 if loaded ~ ~ ~ unless entity @e[tag=mg.trdw3] run function mg:terra/rpg/dg/tube_c2
execute if score $trds3 mg.st matches 5 as @e[tag=mg.trdw3] positioned -23.5 90 186.5 unless entity @s[distance=..44] run tp @s -33.5 90 184.5
execute unless score $trda3 mg.st matches 1 if score $trdc3 mg.st matches ..0 if score $trds3 mg.st matches 6 positioned -23.5 90 186.5 if entity @a[tag=mg.tvw,gamemode=adventure,distance=..12] run function mg:terra/rpg/dg/tube_start
execute unless score $trds3 mg.st matches 6 if score $trdc3 mg.st matches ..0 unless entity @e[tag=mg.trdw3] positioned -23.5 90 186.5 if entity @a[tag=mg.tvw,gamemode=adventure,distance=..12] run function mg:terra/rpg/dg/tube_lock
execute if score $trda3 mg.st matches 1 run function mg:terra/rpg/dg/tube
