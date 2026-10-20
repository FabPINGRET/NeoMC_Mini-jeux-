# Récompense de mg:tdm_melee (@s = attaquant) : coup de couteau = 1 dégât à l'équipe adverse (partie TDM en cours seulement)
advancement revoke @s only mg:tdm_melee
execute unless score $game mg.st matches 246 run return 0
execute unless score $state mg.st matches 2 run return 0
execute unless entity @s[tag=mg.play,tag=!mg.tmp] run return 0
execute unless items entity @s weapon.mainhand *[custom_data~{mg_kn:1b}] run return 0
execute if score @s mg.tmkc matches 1.. run return 0
# recharge posée AVANT le coup (un coup balayé déclenche l'advancement plusieurs fois dans le même tick)
scoreboard players set @s mg.tmkc 20
tag @s add mg.tmsh
execute if entity @s[team=mg_red] run tag @a[tag=mg.play,gamemode=adventure,team=mg_blue] add mg.tmen
execute if entity @s[team=mg_blue] run tag @a[tag=mg.play,gamemode=adventure,team=mg_red] add mg.tmen
# victime = adversaire non protégé touché ce tick ET dont le dernier attaquant est @s (pas un autre adversaire à portée)
execute as @a[tag=mg.tmen,tag=!mg.tmp,distance=..5] if data entity @s {HurtTime:10s} if function mg:tdm/melee_att run tag @s add mg.tmvc
execute as @p[tag=mg.tmvc] run function mg:tdm/melee_hit
tag @a remove mg.tmvc
tag @a remove mg.tmen
tag @s remove mg.tmsh
