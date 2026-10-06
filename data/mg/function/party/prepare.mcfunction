# Mini Party (jeu 59) : préparation pendant le compte à rebours (@s = admin qui lance)
scoreboard players set $mp mg.st 1
scoreboard players set $mpround mg.st 1
scoreboard players set #2 mg.st 2
scoreboard players set #4 mg.st 4
scoreboard players set #8 mg.st 8
scoreboard players set #1000 mg.st 1000
tag @a remove mg.mpp
tag @a remove mg.mpa
tag @a remove mg.mpcur
tag @a remove mg.mpview
tag @s add mg.mpa
tag @a[tag=mg.play] add mg.mpp

scoreboard players set @a[tag=mg.mpp] mg.mpm 10
scoreboard players set @a[tag=mg.mpp] mg.mpk 0
scoreboard players set @a[tag=mg.mpp] mg.mpi 0
scoreboard players set @a[tag=mg.mpp] mg.mid 0
scoreboard players set @a[tag=mg.mpp] mg.mit 0
scoreboard players set @a[tag=mg.mpp] mg.mip 0
scoreboard players reset * mg.mpo
scoreboard players set $mpn mg.st 0
tellraw @a[tag=mg.mpp] [{"text":"★ ","color":"gold"},{"text":"Ordre de passage :","color":"gray"}]
execute as @a[tag=mg.mpp,sort=random] run function mg:party/order_one
kill @e[type=minecraft:armor_stand,tag=mg.mppawn]
tag @a remove mg.mpfree
execute as @a[tag=mg.mpp] run function mg:party/pawn_spawn

# Perchoir des spectateurs (reconnexion, abandon) : au-dessus du château
scoreboard players set $px mg.st 0
scoreboard players set $py mg.st 120
scoreboard players set $pz mg.st 15000

# Étoile et grand dé
scoreboard players set $mps mg.st -1
function mg:party/star_move
kill @e[type=minecraft:text_display,tag=mg.mpdice]
summon minecraft:text_display 0.5 70 14948.5 {Tags:["mg.mpdice"],billboard:"center",text:[{"text":"?","color":"white","bold":true}],background:-1442840576,transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[3f,3f,3f]}}

# Survol de la carte pendant le compte à rebours
execute as @a[tag=mg.mpp] run function mg:party/rejoin
execute as @a[tag=mg.mpp] run function mg:party/view_start
function mg:party/hud
tellraw @a[tag=mg.mpp] [{"text":"★ ","color":"gold"},{"text":"Règles, carte et caméra : menu ","color":"gray"},{"text":"★ Mini Party","color":"gold"},{"text":" (touche Actions rapides, ou Échap).","color":"gray"}]
