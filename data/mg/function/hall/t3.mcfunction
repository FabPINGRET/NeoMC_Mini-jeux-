# @s : sa place dans le top 3 du jeu $(k) (score dans $(obj)) — macro {k, obj, lbl, col}
$execute store result score #t3s mg.st run scoreboard players get @s $(obj)
execute unless score #t3s mg.st matches 1.. run return 0
data modify storage mg:hall t3w set value {}
data modify storage mg:hall t3w.u set from entity @s UUID
execute store result storage mg:hall t3w.s int 1 run scoreboard players get #t3s mg.st
item modify entity @e[type=minecraft:item_display,tag=mg.hallbuf,limit=1] contents {function:"minecraft:set_name",entity:"this",target:"custom_name",name:{selector:"@s"}}
data modify storage mg:hall t3w.n set from entity @e[type=minecraft:item_display,tag=mg.hallbuf,limit=1] item.components."minecraft:custom_name"
data modify storage mg:hall t3c set value []
$data modify storage mg:hall t3c set from storage mg:hall t3.$(k)
function mg:hall/t3_merge
$execute store success score #t3d mg.st run data modify storage mg:hall t3.$(k) set from storage mg:hall t3c
$execute if score #t3d mg.st matches 1 run function mg:hall/t3_show {k:"$(k)",lbl:"$(lbl)",col:"$(col)"}
