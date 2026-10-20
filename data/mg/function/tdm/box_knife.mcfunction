# Coup de couteau sur la boîte de clic d'un adversaire (gun/cl_foreign : @s = attaquant, victime = @a[tag=mg.gcme]) :
# la boîte de 2,6 blocs autour de ses yeux intercepte le coup, mg:tdm_melee ne se déclenche donc pas ; mêmes règles que melee_adv
execute unless score $game mg.st matches 246 run return 0
execute unless score $state mg.st matches 2 run return 0
execute unless entity @s[tag=mg.play,tag=!mg.tmp] run return 0
execute unless items entity @s weapon.mainhand *[custom_data~{mg_kn:1b}] run return 0
execute if score @s mg.tmkc matches 1.. run return 0
execute if entity @s[team=mg_red] run tag @a[tag=mg.play,gamemode=adventure,team=mg_blue] add mg.tmen
execute if entity @s[team=mg_blue] run tag @a[tag=mg.play,gamemode=adventure,team=mg_red] add mg.tmen
# victime = adversaire non protégé propriétaire de la boîte frappée, à portée du couteau (pas de coup ami)
execute at @s as @a[tag=mg.gcme,tag=mg.tmen,tag=!mg.tmp,distance=..4.5] run tag @s add mg.tmvc
execute unless entity @a[tag=mg.tmvc] run return run tag @a remove mg.tmen
# recharge posée AVANT le coup (comme melee_adv), puis le coup existant (melee_hit)
scoreboard players set @s mg.tmkc 20
tag @s add mg.tmsh
execute as @a[tag=mg.tmvc,limit=1] run function mg:tdm/melee_hit
tag @a remove mg.tmvc
tag @a remove mg.tmen
tag @s remove mg.tmsh
