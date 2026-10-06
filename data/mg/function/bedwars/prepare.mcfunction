# Bedwars — préparation
function mg:bedwars/reset_field
function mg:bedwars/build
kill @e[type=minecraft:item,x=-45,y=50,z=1155,dx=90,dy=40,dz=90]

# Villageois marchands (un par île)
kill @e[tag=mg.npc]
function mg:bedwars/npc {x:"-33.5",z:"1196.5",ry:"0"}
function mg:bedwars/npc {x:"33.5",z:"1196.5",ry:"0"}
function mg:bedwars/npc {x:"-3.5",z:"1166.5",ry:"-90"}
function mg:bedwars/npc {x:"-3.5",z:"1233.5",ry:"-90"}

# Perchoir spectateur
scoreboard players set $px mg.st 0
scoreboard players set $py mg.st 85
scoreboard players set $pz mg.st 1200

# Équipes : 2, 3 ou 4 selon le nombre de joueurs
scoreboard players set $nt mg.st 2
execute if score $n0 mg.st matches 3 run scoreboard players set $nt mg.st 3
execute if score $n0 mg.st matches 4.. run scoreboard players set $nt mg.st 4
function mg:core/assign_teams

# Lits « vivants » uniquement pour les équipes occupées
execute store result score $bed_red mg.st if entity @a[team=mg_red,tag=mg.play]
execute store result score $bed_blue mg.st if entity @a[team=mg_blue,tag=mg.play]
execute store result score $bed_green mg.st if entity @a[team=mg_green,tag=mg.play]
execute store result score $bed_yellow mg.st if entity @a[team=mg_yellow,tag=mg.play]

# Générateurs
scoreboard players set $gi mg.st 40
scoreboard players set $gg mg.st 160
scoreboard players set $gd mg.st 400

gamemode adventure @a[tag=mg.play]
execute as @a[team=mg_red,tag=mg.play] run spawnpoint @s -31 64 1200
execute as @a[team=mg_blue,tag=mg.play] run spawnpoint @s 31 64 1200
execute as @a[team=mg_green,tag=mg.play] run spawnpoint @s 0 64 1168
execute as @a[team=mg_yellow,tag=mg.play] run spawnpoint @s 0 64 1232
execute as @a[team=mg_red,tag=mg.play] run tp @s -31.5 64 1200.5 facing 0 64 1200
execute as @a[team=mg_blue,tag=mg.play] run tp @s 31.5 64 1200.5 facing 0 64 1200
execute as @a[team=mg_green,tag=mg.play] run tp @s 0.5 64 1168.5 facing 0 64 1200
execute as @a[team=mg_yellow,tag=mg.play] run tp @s 0.5 64 1232.5 facing 0 64 1200
