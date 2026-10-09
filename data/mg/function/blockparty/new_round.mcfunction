# Nouvelle manche : nouveau sol (carrés, bandes ou les deux selon $bpm), nouvelle couleur, minuteur 5 s → 2 s
scoreboard players add $rd mg.st 1
execute if score $bpm mg.st matches 0 store result score $k mg.st run random value 1..10
execute if score $bpm mg.st matches 1 store result score $k mg.st run random value 11..20
execute if score $bpm mg.st matches 2 store result score $k mg.st run random value 1..20
execute if score $k mg.st matches 1 run function mg:blockparty/pattern_1
execute if score $k mg.st matches 2 run function mg:blockparty/pattern_2
execute if score $k mg.st matches 3 run function mg:blockparty/pattern_3
execute if score $k mg.st matches 4 run function mg:blockparty/pattern_4
execute if score $k mg.st matches 5 run function mg:blockparty/pattern_5
execute if score $k mg.st matches 6 run function mg:blockparty/pattern_6
execute if score $k mg.st matches 7 run function mg:blockparty/pattern_7
execute if score $k mg.st matches 8 run function mg:blockparty/pattern_8
execute if score $k mg.st matches 9 run function mg:blockparty/pattern_9
execute if score $k mg.st matches 10 run function mg:blockparty/pattern_10
execute if score $k mg.st matches 11 run function mg:blockparty/pattern_11
execute if score $k mg.st matches 12 run function mg:blockparty/pattern_12
execute if score $k mg.st matches 13 run function mg:blockparty/pattern_13
execute if score $k mg.st matches 14 run function mg:blockparty/pattern_14
execute if score $k mg.st matches 15 run function mg:blockparty/pattern_15
execute if score $k mg.st matches 16 run function mg:blockparty/pattern_16
execute if score $k mg.st matches 17 run function mg:blockparty/pattern_17
execute if score $k mg.st matches 18 run function mg:blockparty/pattern_18
execute if score $k mg.st matches 19 run function mg:blockparty/pattern_19
execute if score $k mg.st matches 20 run function mg:blockparty/pattern_20

# Couleur cible
execute store result score $k mg.st run random value 0..15
execute if score $k mg.st matches 0 run function mg:blockparty/show_0
execute if score $k mg.st matches 1 run function mg:blockparty/show_1
execute if score $k mg.st matches 2 run function mg:blockparty/show_2
execute if score $k mg.st matches 3 run function mg:blockparty/show_3
execute if score $k mg.st matches 4 run function mg:blockparty/show_4
execute if score $k mg.st matches 5 run function mg:blockparty/show_5
execute if score $k mg.st matches 6 run function mg:blockparty/show_6
execute if score $k mg.st matches 7 run function mg:blockparty/show_7
execute if score $k mg.st matches 8 run function mg:blockparty/show_8
execute if score $k mg.st matches 9 run function mg:blockparty/show_9
execute if score $k mg.st matches 10 run function mg:blockparty/show_10
execute if score $k mg.st matches 11 run function mg:blockparty/show_11
execute if score $k mg.st matches 12 run function mg:blockparty/show_12
execute if score $k mg.st matches 13 run function mg:blockparty/show_13
execute if score $k mg.st matches 14 run function mg:blockparty/show_14
execute if score $k mg.st matches 15 run function mg:blockparty/show_15
# Minuteur : 105 - 5 ticks par manche, minimum 40 (2 s)
scoreboard players set $bt mg.st 105
scoreboard players operation $tmp mg.st = $rd mg.st
scoreboard players operation $tmp mg.st *= $c5 mg.st
scoreboard players operation $bt mg.st -= $tmp mg.st
scoreboard players operation $bt mg.st > $bmin mg.st
scoreboard players set $bp mg.st 1
execute as @a[tag=!mg.surv] at @s run playsound minecraft:block.note_block.bell master @s ~ ~ ~ 1 1.5
function mg:blockparty/music_start
