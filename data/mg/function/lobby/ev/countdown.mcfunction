bossbar set mg:ev players @a[tag=mg.evl]
execute store result bossbar mg:ev value run scoreboard players get $evn mg.st
execute if score $evn mg.st matches 1..5 as @a[tag=mg.evl] at @s run playsound minecraft:block.note_block.hat master @s ~ ~ ~ 1 1.4
execute if score $evn mg.st matches 10 run title @a[tag=mg.evl] actionbar {"text":"🎉 L'événement commence dans 10 s !","color":"light_purple"}
