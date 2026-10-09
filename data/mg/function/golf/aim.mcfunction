# @s : visée (balle à l'arrêt) : jauge, barre d'action, ligne de visée, tir au clic droit
scoreboard players remove @s[scores={mg.gfk=1..}] mg.gfk 1
function mg:golf/own
execute unless entity @e[tag=mg.gfmy] run return run tag @e[tag=mg.gfmy] remove mg.gfmy
execute unless entity @e[tag=mg.gfmy,distance=..5] run function mg:golf/place
scoreboard players set $gfclub mg.st 0
execute if items entity @s weapon.mainhand minecraft:warped_fungus_on_a_stick[custom_data~{golf:1}] run scoreboard players set $gfclub mg.st 1
execute if items entity @s weapon.mainhand minecraft:warped_fungus_on_a_stick[custom_data~{golf:2}] run scoreboard players set $gfclub mg.st 2
scoreboard players operation $gfnc mg.st = @s mg.gfc
scoreboard players add $gfnc mg.st 1
scoreboard players operation $gfcol mg.st = @s mg.gfi
scoreboard players operation $gfcol mg.st %= #gf8 mg.st
execute if score $gfclub mg.st matches 0 run title @s actionbar [{"text":"⛳ Prends un club en main : ","color":"gray"},{"text":"Bois/Fer","color":"gold"},{"text":" (vol) ou ","color":"gray"},{"text":"Putter","color":"green"},{"text":" (roule)","color":"gray"}]
execute if score $gfclub mg.st matches 1.. if score @s mg.gfk matches ..0 run function mg:golf/gauge
execute if score $gfclub mg.st matches 1 run scoreboard players operation $gfe mg.st = @s mg.gfp
execute if score $gfclub mg.st matches 1 run scoreboard players operation $gfe mg.st *= #gfest1 mg.st
execute if score $gfclub mg.st matches 2 run scoreboard players operation $gfe mg.st = @s mg.gfp
execute if score $gfclub mg.st matches 2 run scoreboard players operation $gfe mg.st *= #gfest2 mg.st
scoreboard players operation $gfe mg.st /= #gf100 mg.st
execute if score $gfclub mg.st matches 1 run scoreboard players add $gfe mg.st 6
execute if score $gfclub mg.st matches 1 run function mg:golf/bar1
execute if score $gfclub mg.st matches 2 run function mg:golf/bar2
scoreboard players operation $gfq mg.st = $gft mg.st
scoreboard players operation $gfq mg.st %= #gf4 mg.st
tag @s add mg.gfme
execute if score $gfq mg.st matches 0 if score $gfclub mg.st matches 1.. as @e[tag=mg.gfmy,limit=1] at @s rotated as @a[tag=mg.gfme,limit=1] rotated ~ 0 run function mg:golf/aimline
execute if score @s mg.qs matches 1.. if score $gfclub mg.st matches 1.. if score @s mg.gfk matches ..0 run function mg:golf/shoot
tag @s remove mg.gfme
tag @e[tag=mg.gfmy] remove mg.gfmy
