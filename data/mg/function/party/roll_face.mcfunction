# Nouvelle face du dé qui roule ($mdn dés de 1 à 10, total dans $dv)
execute store result score $d1 mg.st run random value 1..10
scoreboard players set $d2 mg.st 0
scoreboard players set $d3 mg.st 0
execute if score $mdn mg.st matches 2.. store result score $d2 mg.st run random value 1..10
execute if score $mdn mg.st matches 3.. store result score $d3 mg.st run random value 1..10
scoreboard players operation $dv mg.st = $d1 mg.st
scoreboard players operation $dv mg.st += $d2 mg.st
scoreboard players operation $dv mg.st += $d3 mg.st
function mg:party/dice_show
execute as @a[tag=mg.mpp] at @s run playsound minecraft:block.note_block.hat master @s ~ ~ ~ 0.4 2
