scoreboard players add $bpc mg.st 1
# Têtes de Wither à haute fréquence : une salve sur un joueur au hasard toutes les 12 ticks
scoreboard players operation $m1 mg.st = $bpc mg.st
scoreboard players operation $m1 mg.st %= $k12 mg.st
execute if score $m1 mg.st matches 0 as @e[tag=mg.boss,limit=1] at @s positioned ~ ~2.2 ~ facing entity @r[tag=mg.play] eyes run function mg:mobarena/ship/skull
# Endermen agressifs toutes les 10 s
scoreboard players operation $m2 mg.st = $bpc mg.st
scoreboard players operation $m2 mg.st %= $k200 mg.st
execute if score $m2 mg.st matches 0 run function mg:mobarena/ship/endermen
# Poursuite des endermen
execute as @e[type=minecraft:enderman,tag=mg.mob] at @s facing entity @p[tag=mg.play] feet run tp @s ^ ^ ^0.25
scoreboard players operation $m3 mg.st = $bpc mg.st
scoreboard players operation $m3 mg.st %= $k20 mg.st
execute if score $m3 mg.st matches 0 as @e[type=minecraft:enderman,tag=mg.mob] at @s as @p[tag=mg.play,distance=..2.6] run damage @s 4 minecraft:mob_attack
