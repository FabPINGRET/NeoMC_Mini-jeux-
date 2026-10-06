# Bedwars — tick de jeu

# --- Générateurs ---
scoreboard players remove $gi mg.st 1
execute if score $gi mg.st matches ..0 run function mg:bedwars/gen_iron
scoreboard players remove $gg mg.st 1
execute if score $gg mg.st matches ..0 run function mg:bedwars/gen_gold
scoreboard players remove $gd mg.st 1
execute if score $gd mg.st matches ..0 run function mg:bedwars/gen_diamond

# --- Lits détruits ? ---
execute if score $bed_red mg.st matches 1 unless block -35 64 1200 #minecraft:beds run function mg:bedwars/bed_red
execute if score $bed_blue mg.st matches 1 unless block 35 64 1200 #minecraft:beds run function mg:bedwars/bed_blue
execute if score $bed_green mg.st matches 1 unless block 0 64 1164 #minecraft:beds run function mg:bedwars/bed_green
execute if score $bed_yellow mg.st matches 1 unless block 0 64 1236 #minecraft:beds run function mg:bedwars/bed_yellow

# --- Chute dans le vide = mort ---
execute as @a[tag=mg.play] store result score @s mg.t run data get entity @s Pos[1]
execute as @a[tag=mg.play,scores={mg.t=..35}] run tp @s 0.5 85 1200.5
execute as @a[tag=mg.play,scores={mg.t=..35}] run scoreboard players add @s mg.deaths 1

# --- Morts / réapparitions ---
execute as @a[team=mg_red,tag=mg.play,scores={mg.deaths=1..}] run function mg:bedwars/death_red
execute as @a[team=mg_blue,tag=mg.play,scores={mg.deaths=1..}] run function mg:bedwars/death_blue
execute as @a[team=mg_green,tag=mg.play,scores={mg.deaths=1..}] run function mg:bedwars/death_green
execute as @a[team=mg_yellow,tag=mg.play,scores={mg.deaths=1..}] run function mg:bedwars/death_yellow

# --- Placement après réapparition (île d'équipe garantie, jamais le centre) ---
execute as @e[type=minecraft:player,tag=mg.rsp] run function mg:bedwars/respawn

# --- Victoire ---
scoreboard players set $ta mg.st 0
execute if entity @a[team=mg_red,tag=mg.play] run scoreboard players add $ta mg.st 1
execute if entity @a[team=mg_blue,tag=mg.play] run scoreboard players add $ta mg.st 1
execute if entity @a[team=mg_green,tag=mg.play] run scoreboard players add $ta mg.st 1
execute if entity @a[team=mg_yellow,tag=mg.play] run scoreboard players add $ta mg.st 1
execute if score $state mg.st matches 2 if score $n0 mg.st matches 2.. if score $ta mg.st matches 1 run function mg:bedwars/win_check
execute if score $state mg.st matches 2 if score $ta mg.st matches 0 run function mg:core/draw
