# TDM sniper — tick (état 2)
scoreboard players add $tmt mg.st 1
# morts hors tir (commande, vide) : réapparition sans frag ; lunette avant les tirs
execute as @a[tag=mg.play,gamemode=adventure,scores={mg.deaths=1..}] run function mg:tdm/respawn
execute as @a[tag=mg.play,gamemode=adventure] at @s run function mg:tdm/scope
execute as @a[tag=mg.tmp,tag=mg.play] run function mg:tdm/prot_tick
execute as @a[tag=mg.play,gamemode=adventure,tag=!mg.tmp,scores={mg.tmcd=1}] run title @s actionbar [{"text":"🎯 Sniper prêt","color":"aqua"}]
execute as @a[tag=mg.play,gamemode=adventure,scores={mg.tmcd=1}] at @s run playsound minecraft:block.note_block.hat master @s ~ ~ ~ 0.6 2
scoreboard players remove @a[tag=mg.play,gamemode=adventure,scores={mg.tmcd=1..}] mg.tmcd 1
scoreboard players remove @a[tag=mg.play,gamemode=adventure,scores={mg.tmkc=1..}] mg.tmkc 1
execute as @a[tag=mg.play,gamemode=adventure,scores={mg.qs=1..}] run function mg:tdm/shoot
# le kit (sniper et couteau) est rendu si un effacement ou un jet l'a retiré
execute as @a[tag=mg.play,gamemode=adventure] unless items entity @s container.* minecraft:warped_fungus_on_a_stick[custom_data~{mg_tm:1b}] run function mg:tdm/kit
execute as @a[tag=mg.play,gamemode=adventure] unless items entity @s container.* *[custom_data~{mg_tm:1b,mg_kn:1b}] run function mg:tdm/kit
# sniper et couteau jetés ou ramassés par un autre : retirés
execute as @e[type=minecraft:item,x=-22,y=60,z=39928,dx=44,dy=500,dz=945] if items entity @s contents *[custom_data~{mg_tm:1b}] run kill @s
clear @a[tag=!mg.play] *[custom_data~{mg_tm:1b}]
# packs de soin
function mg:tdm/pack_tick
# hors de l'arène (chute...) : réapparition sans frag
execute if score $tma mg.st matches 1 as @a[tag=mg.play,gamemode=adventure] unless entity @s[x=-22,dx=44,y=60,dy=500,z=39928,dz=145] run function mg:tdm/respawn
execute if score $tma mg.st matches 2 as @a[tag=mg.play,gamemode=adventure] unless entity @s[x=-22,dx=44,y=60,dy=500,z=40328,dz=145] run function mg:tdm/respawn
execute if score $tma mg.st matches 3 as @a[tag=mg.play,gamemode=adventure] unless entity @s[x=-22,dx=44,y=60,dy=500,z=40728,dz=145] run function mg:tdm/respawn
execute if score $tmt mg.st matches 8400 run tellraw @a[tag=mg.play] [{"text":"🎯 Plus qu'une minute !","color":"gold"}]
execute if score $state mg.st matches 2 if score $tmt mg.st matches 9600.. run function mg:tdm/timeout
# équipe vide (déconnexions) : l'autre gagne ; plus personne : égalité (seul : entraînement, pas de victoire)
execute store result score $tmn mg.st if entity @a[tag=mg.play,team=mg_red]
execute store result score $tmm mg.st if entity @a[tag=mg.play,team=mg_blue]
execute if score $state mg.st matches 2 if score $n0 mg.st matches 2.. if score $tmn mg.st matches 0 if score $tmm mg.st matches 1.. run return run function mg:core/win_blue
execute if score $state mg.st matches 2 if score $n0 mg.st matches 2.. if score $tmm mg.st matches 0 if score $tmn mg.st matches 1.. run return run function mg:core/win_red
execute if score $state mg.st matches 2 if score $tmn mg.st matches 0 if score $tmm mg.st matches 0 run function mg:core/draw
