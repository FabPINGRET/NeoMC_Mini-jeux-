# Nouvelle manche : tout le monde en haut du niveau tiré
scoreboard players set $dcph mg.st 1
scoreboard players set $dct mg.st 0
scoreboard players set $dci mg.st 0
execute as @a[tag=mg.play] run function mg:dropadv/c_spawn
execute as @a[tag=mg.play] run function mg:dropadv/show_level
execute as @a[tag=mg.play] at @s run playsound minecraft:block.note_block.pling master @s ~ ~ ~ 1 1.4
