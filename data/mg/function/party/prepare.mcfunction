# Mini Party (jeu 59) : préparation pendant le compte à rebours (@s = admin qui lance)
scoreboard players set $mp mg.st 1
scoreboard players set $mpround mg.st 1
scoreboard players set #2 mg.st 2
scoreboard players set #4 mg.st 4
scoreboard players set #1000 mg.st 1000
tag @a remove mg.mpp
tag @a remove mg.mpa
tag @a remove mg.mpcur
tag @s add mg.mpa
tag @a[tag=mg.play] add mg.mpp

scoreboard players set @a[tag=mg.mpp] mg.mpm 10
scoreboard players set @a[tag=mg.mpp] mg.mpk 0
scoreboard players set @a[tag=mg.mpp] mg.mpi 0
scoreboard players reset * mg.mpo
scoreboard players set $mpn mg.st 0
tellraw @a[tag=mg.mpp] [{"text":"Ordre de passage :","color":"gold"}]
execute as @a[tag=mg.mpp,sort=random] run function mg:party/order_one

# Perchoir des spectateurs (reconnexion, abandon)
scoreboard players set $px mg.st 0
scoreboard players set $py mg.st 78
scoreboard players set $pz mg.st 14300

# Étoile et grand dé
execute store result score $mps mg.st run random value 1..31
function mg:party/star_place
kill @e[type=minecraft:text_display,tag=mg.mpdice]
summon minecraft:text_display 0.5 67 14300.5 {Tags:["mg.mpdice"],billboard:"center",text:[{"text":"?","color":"white","bold":true}],background:-1442840576,transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[4f,4f,4f]}}

execute as @a[tag=mg.mpp] run function mg:party/rejoin
function mg:party/hud
tellraw @a[tag=mg.mpp] [{"text":"Règles : ","color":"gold"},{"text":"chacun lance le dé à son tour et avance. Case bleue +3 pièces, rouge -3, verte ? = surprise, noire ☠ = piège. Passe sur l'étoile ★ avec 20 pièces pour l'acheter. Après chaque tour : un mini-jeu (vainqueur +10, les autres +3). Le plus d'étoiles gagne, puis le plus de pièces.","color":"gray"}]
