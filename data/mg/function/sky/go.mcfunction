# Élytra — départ
execute if score $skpd mg.st matches 0 run function mg:sky/pad_place
scoreboard players set $skt mg.st 0
effect give @a[tag=mg.play] minecraft:resistance infinite 4 true
effect give @a[tag=mg.play] minecraft:saturation infinite 0 true
scoreboard players set @a[tag=mg.play] mg.skg -40
execute if score $elm mg.st matches 1..2 run function mg:sky/go_race
execute if score $elm mg.st matches 3 run function mg:sky/go_surv
execute as @a[tag=!mg.surv] at @s run playsound minecraft:entity.ender_dragon.flap master @s ~ ~ ~ 1 1.2
