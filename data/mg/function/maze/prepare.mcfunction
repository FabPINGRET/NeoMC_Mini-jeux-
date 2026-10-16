# 🌀 Labyrinthe géant — préparation (le labyrinthe est construit 1 s plus tard, chunks chargés)
forceload add -51 41049 57 41150
scoreboard players set $jok mg.st 0
execute store result score $jv mg.st run random value 1..3
function mg:maze/sas
schedule function mg:maze/build 20t
scoreboard players set $px mg.st 0
scoreboard players set $py mg.st 95
scoreboard players set $pz mg.st 41100
clear @a[tag=mg.play]
effect clear @a[tag=mg.play]
gamemode adventure @a[tag=mg.play]
team join mg_sq @a[tag=mg.play]
scoreboard players set @a[tag=mg.play] mg.jc 0
scoreboard players set @a[tag=mg.play] mg.je 0
scoreboard players set @a[tag=mg.play] mg.jk 0
scoreboard players set $jid mg.st 0
execute as @a[tag=mg.play] store result score @s mg.jid run scoreboard players add $jid mg.st 1
spreadplayers -53.5 41100 0.5 2 under 67 false @a[tag=mg.play]
execute as @a[tag=mg.play] at @s run spawnpoint @s ~ ~ ~
tellraw @a[tag=mg.play] [{"text":"🌀 LABYRINTHE GÉANT : ","color":"light_purple","bold":true},{"text":"traverse le labyrinthe d'ouest en est, le premier sur l'or gagne ! Bonus : ⚡ vitesse, 🧭 boussole vers la sortie, 🦅 vue d'aigle. Méfie-toi des toiles, des grilles qui se ferment, des téléporteurs (obsidienne) et des cases piégées.","color":"gray"}]
