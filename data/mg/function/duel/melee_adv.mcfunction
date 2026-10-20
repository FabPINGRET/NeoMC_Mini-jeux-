# Récompense de mg:duel_melee (@s = attaquant) : coup de couteau = 1 dégât à l'adversaire de la même arène
advancement revoke @s only mg:duel_melee
execute unless entity @s[tag=mg.dl,tag=!mg.dlp] run return 0
execute unless items entity @s weapon.mainhand *[custom_data~{mg_kn:1b}] run return 0
execute if score @s mg.dlkc matches 1.. run return 0
# recharge posée AVANT le coup (un coup balayé déclenche l'advancement plusieurs fois dans le même tick)
scoreboard players set @s mg.dlkc 20
tag @s add mg.dlsh
scoreboard players operation $dli mg.st = @s mg.dli
execute as @a[tag=mg.dl,tag=!mg.dlsh,tag=!mg.dlp,distance=..5] if score @s mg.dli = $dli mg.st if data entity @s {HurtTime:10s} run tag @s add mg.dlvc
execute as @p[tag=mg.dlvc] run function mg:duel/melee_hit
tag @a remove mg.dlvc
tag @s remove mg.dlsh
