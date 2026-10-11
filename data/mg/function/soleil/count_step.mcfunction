scoreboard players operation $sqk mg.st = $k mg.st
execute if score $k mg.st matches 0 run title @a[tag=mg.play] title {"text":"1…","color":"green","bold":true}
execute if score $k mg.st matches 1 run title @a[tag=mg.play] title {"text":"2…","color":"yellow","bold":true}
execute if score $k mg.st matches 2 run title @a[tag=mg.play] title {"text":"3…","color":"gold","bold":true}
execute if score $k mg.st matches 0 as @a[tag=mg.play] at @s run playsound minecraft:block.note_block.bell master @s ~ ~ ~ 1 0.9
execute if score $k mg.st matches 1 as @a[tag=mg.play] at @s run playsound minecraft:block.note_block.bell master @s ~ ~ ~ 1 1.1
execute if score $k mg.st matches 2 as @a[tag=mg.play] at @s run playsound minecraft:block.note_block.bell master @s ~ ~ ~ 1 1.35
