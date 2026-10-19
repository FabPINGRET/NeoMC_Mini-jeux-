# Chaque seconde : boss (déclenchement, suivi, victoire) et donjons
scoreboard players remove $obc0 mg.st 1
# arène plus chargée (plus personne autour) : le combat s'arrête sans victoire ; boss resté d'un ancien combat : retiré
execute if score $ob0 mg.st matches 1 positioned -204.5 71 -41.5 unless loaded ~ ~ ~ run scoreboard players set $ob0 mg.st 0
execute unless score $ob0 mg.st matches 1 as @e[tag=mg.olb_brennic] run kill @s
execute if score $ob0 mg.st matches 1 unless entity @e[tag=mg.olb_brennic] run function mg:ombre/boss/brennic_win
execute unless score $ob0 mg.st matches 1 if score $obc0 mg.st matches ..0 positioned -204.5 71 -41.5 if entity @a[tag=mg.olw,gamemode=adventure,distance=..18,scores={mg.olch=8..}] run function mg:ombre/boss/brennic_start
execute if score $ob0 mg.st matches 1 run function mg:ombre/boss/brennic
scoreboard players remove $obc1 mg.st 1
# arène plus chargée (plus personne autour) : le combat s'arrête sans victoire ; boss resté d'un ancien combat : retiré
execute if score $ob1 mg.st matches 1 positioned -204.5 72 -204.5 unless loaded ~ ~ ~ run scoreboard players set $ob1 mg.st 0
execute unless score $ob1 mg.st matches 1 as @e[tag=mg.olb_ystar] run kill @s
execute if score $ob1 mg.st matches 1 unless entity @e[tag=mg.olb_ystar] run function mg:ombre/boss/ystar_win
execute unless score $ob1 mg.st matches 1 if score $obc1 mg.st matches ..0 positioned -204.5 72 -204.5 if entity @a[tag=mg.olw,gamemode=adventure,distance=..13,scores={mg.olch=14..}] run function mg:ombre/boss/ystar_start
execute if score $ob1 mg.st matches 1 run function mg:ombre/boss/ystar
scoreboard players remove $obc2 mg.st 1
# arène plus chargée (plus personne autour) : le combat s'arrête sans victoire ; boss resté d'un ancien combat : retiré
execute if score $ob2 mg.st matches 1 positioned 30.5 105 -204.5 unless loaded ~ ~ ~ run scoreboard players set $ob2 mg.st 0
execute unless score $ob2 mg.st matches 1 as @e[tag=mg.olb_hrimgar] run kill @s
execute if score $ob2 mg.st matches 1 unless entity @e[tag=mg.olb_hrimgar] run function mg:ombre/boss/hrimgar_win
execute unless score $ob2 mg.st matches 1 if score $obc2 mg.st matches ..0 positioned 30.5 105 -204.5 if entity @a[tag=mg.olw,gamemode=adventure,distance=..15,scores={mg.olch=21..}] run function mg:ombre/boss/hrimgar_start
execute if score $ob2 mg.st matches 1 run function mg:ombre/boss/hrimgar
scoreboard players remove $obc3 mg.st 1
# arène plus chargée (plus personne autour) : le combat s'arrête sans victoire ; boss resté d'un ancien combat : retiré
execute if score $ob3 mg.st matches 1 positioned 205.5 65 -187.5 unless loaded ~ ~ ~ run scoreboard players set $ob3 mg.st 0
execute unless score $ob3 mg.st matches 1 as @e[tag=mg.olb_morvaine] run kill @s
execute if score $ob3 mg.st matches 1 unless entity @e[tag=mg.olb_morvaine] run function mg:ombre/boss/morvaine_win
execute unless score $ob3 mg.st matches 1 if score $obc3 mg.st matches ..0 positioned 205.5 65 -187.5 if entity @a[tag=mg.olw,gamemode=adventure,distance=..12,scores={mg.olch=27..}] run function mg:ombre/boss/morvaine_start
execute if score $ob3 mg.st matches 1 run function mg:ombre/boss/morvaine
scoreboard players remove $obc4 mg.st 1
# arène plus chargée (plus personne autour) : le combat s'arrête sans victoire ; boss resté d'un ancien combat : retiré
execute if score $ob4 mg.st matches 1 positioned 198.5 65 -27.5 unless loaded ~ ~ ~ run scoreboard players set $ob4 mg.st 0
execute unless score $ob4 mg.st matches 1 as @e[tag=mg.olb_sethkar] run kill @s
execute if score $ob4 mg.st matches 1 unless entity @e[tag=mg.olb_sethkar] run function mg:ombre/boss/sethkar_win
execute unless score $ob4 mg.st matches 1 if score $obc4 mg.st matches ..0 positioned 198.5 65 -27.5 if entity @a[tag=mg.olw,gamemode=adventure,distance=..10,scores={mg.olch=33..}] run function mg:ombre/boss/sethkar_start
execute if score $ob4 mg.st matches 1 run function mg:ombre/boss/sethkar
scoreboard players remove $obc5 mg.st 1
# arène plus chargée (plus personne autour) : le combat s'arrête sans victoire ; boss resté d'un ancien combat : retiré
execute if score $ob5 mg.st matches 1 positioned 180.5 117 180.5 unless loaded ~ ~ ~ run scoreboard players set $ob5 mg.st 0
execute unless score $ob5 mg.st matches 1 as @e[tag=mg.olb_ignarok] run kill @s
execute if score $ob5 mg.st matches 1 unless entity @e[tag=mg.olb_ignarok] run function mg:ombre/boss/ignarok_win
execute unless score $ob5 mg.st matches 1 if score $obc5 mg.st matches ..0 positioned 180.5 117 180.5 if entity @a[tag=mg.olw,gamemode=adventure,distance=..14,scores={mg.olch=38..}] run function mg:ombre/boss/ignarok_start
execute if score $ob5 mg.st matches 1 run function mg:ombre/boss/ignarok
scoreboard players remove $obc6 mg.st 1
# arène plus chargée (plus personne autour) : le combat s'arrête sans victoire ; boss resté d'un ancien combat : retiré
execute if score $ob6 mg.st matches 1 positioned 0.5 67 188.5 unless loaded ~ ~ ~ run scoreboard players set $ob6 mg.st 0
execute unless score $ob6 mg.st matches 1 as @e[tag=mg.olb_colosse] run kill @s
execute if score $ob6 mg.st matches 1 unless entity @e[tag=mg.olb_colosse] run function mg:ombre/boss/colosse_win
execute unless score $ob6 mg.st matches 1 if score $obc6 mg.st matches ..0 positioned 0.5 67 188.5 if entity @a[tag=mg.olw,gamemode=adventure,distance=..16,scores={mg.olch=43..}] run function mg:ombre/boss/colosse_start
execute if score $ob6 mg.st matches 1 run function mg:ombre/boss/colosse
scoreboard players remove $obc7 mg.st 1
# arène plus chargée (plus personne autour) : le combat s'arrête sans victoire ; boss resté d'un ancien combat : retiré
execute if score $ob7 mg.st matches 1 positioned -171.5 67 178.5 unless loaded ~ ~ ~ run scoreboard players set $ob7 mg.st 0
execute unless score $ob7 mg.st matches 1 as @e[tag=mg.olb_malveth] run kill @s
execute if score $ob7 mg.st matches 1 unless entity @e[tag=mg.olb_malveth] run function mg:ombre/boss/malveth_win
execute unless score $ob7 mg.st matches 1 if score $obc7 mg.st matches ..0 positioned -171.5 67 178.5 if entity @a[tag=mg.olw,gamemode=adventure,distance=..13,scores={mg.olch=48..}] run function mg:ombre/boss/malveth_start
execute if score $ob7 mg.st matches 1 run function mg:ombre/boss/malveth
scoreboard players remove $obc8 mg.st 1
# arène plus chargée (plus personne autour) : le combat s'arrête sans victoire ; boss resté d'un ancien combat : retiré
execute if score $ob8 mg.st matches 1 positioned -171.5 102 178.5 unless loaded ~ ~ ~ run scoreboard players set $ob8 mg.st 0
execute unless score $ob8 mg.st matches 1 as @e[tag=mg.olb_nyxar] run kill @s
execute if score $ob8 mg.st matches 1 unless entity @e[tag=mg.olb_nyxar] run function mg:ombre/boss/nyxar_win
execute unless score $ob8 mg.st matches 1 if score $obc8 mg.st matches ..0 positioned -171.5 102 178.5 if entity @a[tag=mg.olw,gamemode=adventure,distance=..13,scores={mg.olch=50..}] run function mg:ombre/boss/nyxar_start
execute if score $ob8 mg.st matches 1 run function mg:ombre/boss/nyxar
function mg:ombre/dg/crypt/tick
function mg:ombre/dg/nest/tick
function mg:ombre/dg/ice/tick
function mg:ombre/dg/sunken/tick
function mg:ombre/dg/tomb/tick
function mg:ombre/dg/forge/tick
function mg:ombre/dg/mine/tick
function mg:ombre/dg/souls/tick
function mg:ombre/boss/fx_sec
