# @s : joueur qui fait un clic droit (warped_fungus_on_a_stick) — service ou renvoi
scoreboard players reset @s mg.qs
execute unless items entity @s weapon.* *[minecraft:custom_data~{mg_racket:1b}] run return 0
execute if score @s mg.tnt matches 1.. run return 0
scoreboard players set @s mg.tnt 8
playsound minecraft:entity.player.attack.sweep master @a[tag=!mg.surv,distance=..40] ~ ~ ~ 0.5 1.5
scoreboard players operation $tnk mg.st = @s mg.tnc
function mg:tennis/tagk
scoreboard players operation $tnside mg.st = @s mg.tns
scoreboard players set $tnq mg.st 0
execute as @e[type=minecraft:marker,tag=mg.tncm,tag=mg.tnk,limit=1] if score @s mg.tnph matches 0 if score @s mg.tnl = $tnside mg.st run scoreboard players set $tnq mg.st 1
execute if score $tnq mg.st matches 1 run return run function mg:tennis/toss
tag @e[tag=mg.tnhit] remove mg.tnhit
execute positioned ~ ~1 ~ as @e[type=minecraft:item_display,tag=mg.tnball,tag=mg.tnk,tag=mg.tnlive,distance=..2.5,limit=1,sort=nearest] unless score @s mg.tnl = $tnside mg.st run tag @s add mg.tnhit
execute unless entity @e[tag=mg.tnhit] run return 0
scoreboard players set $tnT mg.st 32
scoreboard players set $tndepth mg.st 8500
scoreboard players set $tnshot mg.st 1
execute positioned ~ ~1 ~ if entity @e[tag=mg.tnhit,distance=1.8..] run scoreboard players set $tnshot mg.st 2
execute positioned ~ ~1 ~ if entity @e[tag=mg.tnhit,distance=..1.0] run scoreboard players set $tnshot mg.st 0
execute if predicate {condition:"minecraft:entity_properties",entity:"this",predicate:{flags:{is_sneaking:true}}} run scoreboard players set $tnshot mg.st 3
execute if score $tnshot mg.st matches 2 run scoreboard players set $tnT mg.st 26
execute if score $tnshot mg.st matches 2 run scoreboard players set $tndepth mg.st 10500
execute if score $tnshot mg.st matches 0 run scoreboard players set $tnT mg.st 38
execute if score $tnshot mg.st matches 0 run scoreboard players set $tndepth mg.st 6000
execute if score $tnshot mg.st matches 3 run scoreboard players set $tnT mg.st 50
execute if score $tnshot mg.st matches 3 run scoreboard players set $tndepth mg.st 10500
execute as @e[tag=mg.tnhit] run scoreboard players operation $tnbx mg.st = @s mg.tnx
execute as @e[tag=mg.tnhit] run scoreboard players operation $tnbz mg.st = @s mg.tnz
function mg:tennis/aim_target
execute as @e[tag=mg.tnhit] run function mg:tennis/shoot
tag @e[tag=mg.tnhit] remove mg.tnhit
execute if score $tnshot mg.st matches 2 run title @s actionbar {"text":"💥 Coup puissant !","color":"gold"}
execute if score $tnshot mg.st matches 1 run title @s actionbar {"text":"✔ Bien joué","color":"green"}
execute if score $tnshot mg.st matches 0 run title @s actionbar {"text":"Frappe tardive…","color":"gray"}
execute if score $tnshot mg.st matches 3 run title @s actionbar {"text":"⤴ Lob !","color":"aqua"}
