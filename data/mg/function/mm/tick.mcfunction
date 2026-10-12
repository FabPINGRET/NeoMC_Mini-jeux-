# 🔪 Murder Mystery — tick
scoreboard players add $mmt mg.st 1
execute if score $n0 mg.st matches 2.. if score $mmt mg.st matches 200 run function mg:mm/knife
# couteau : au tueur seulement ; arc : jamais au tueur
clear @a[tag=mg.play,tag=!mg.mmm] minecraft:iron_sword
execute as @e[type=minecraft:item] if items entity @s contents minecraft:iron_sword run kill @s
execute if score $mmt mg.st matches 201.. as @a[tag=mg.play,tag=mg.mmm] unless items entity @s container.* minecraft:iron_sword run function mg:mm/knife_give
execute as @a[tag=mg.play,tag=mg.mmm] if items entity @s container.* minecraft:bow run function mg:mm/bow_spit
clear @a[tag=mg.play,tag=mg.mmm] minecraft:arrow
clear @a[tag=mg.play,tag=mg.mmm] minecraft:gold_ingot
# flèches : un tir chargé tue, pas de ramassage
execute as @e[type=minecraft:arrow,tag=!mg.mmar] run data merge entity @s {damage:20.0d,pickup:0b,Tags:["mg.mmar"]}
execute as @a[tag=mg.play,tag=!mg.mmm] if items entity @s container.* minecraft:bow unless items entity @s container.* minecraft:arrow run scoreboard players add @s mg.mma 1
execute as @a[tag=mg.play,scores={mg.mma=100..}] run function mg:mm/arrow
# or
scoreboard players operation $mmq mg.st = $mmt mg.st
scoreboard players set #60 mg.st 60
scoreboard players operation $mmq mg.st %= #60 mg.st
execute if score $mmq mg.st matches 0 run function mg:mm/gold_spawn
execute as @a[tag=mg.play,tag=!mg.mmm] run function mg:mm/gold
# morts : le tueur abattu → héros ; un innocent qui tue un innocent → éliminé
execute as @a[tag=mg.mmm] run scoreboard players operation $mmc mg.st += @s mg.mmk
execute if entity @a[tag=mg.play,tag=mg.mmm,scores={mg.deaths=1..}] as @a[tag=mg.play,tag=!mg.mmm,scores={mg.mmk=1..}] run function mg:mm/hero
execute if score $n0 mg.st matches 2.. as @a[tag=mg.play,tag=!mg.mmm,scores={mg.mmk=1..,mg.deaths=0}] run function mg:mm/bad_kill
execute as @a[tag=mg.play,scores={mg.deaths=1..}] run function mg:mm/die
scoreboard players set @a[tag=mg.mmx] mg.mmk 0
execute if score $n0 mg.st matches 2.. if score $mmt mg.st matches 4500 run function mg:mm/glow
scoreboard players operation $mmq mg.st = $mmt mg.st
scoreboard players set #20 mg.st 20
scoreboard players operation $mmq mg.st %= #20 mg.st
execute store result score $mmn mg.st if entity @a[tag=mg.play,tag=!mg.mmm]
execute store result score $mmk mg.st if entity @a[tag=mg.play,tag=mg.mmm]
execute if score $mmq mg.st matches 0 run function mg:mm/second
execute if score $state mg.st matches 2 if score $n0 mg.st matches 2.. if score $mmk mg.st matches 0 run return run function mg:mm/innocents_win
execute if score $state mg.st matches 2 if score $n0 mg.st matches 2.. if score $mmn mg.st matches 0 run return run function mg:mm/murderer_win
execute if score $state mg.st matches 2 if score $mmt mg.st matches 5400.. run function mg:mm/timeout
