# Bedwars — préparation : carte $bwm (0 classique, 1 Caldeira, 2 Hanami, 3 Banquise), toujours au même endroit (centre 0 ~ 1200)
execute unless score $bwm mg.st matches 0..3 run scoreboard players set $bwm mg.st 0
# Zone entièrement remise à neuf (efface aussi la carte précédente et tout ce que les joueurs ont posé)
execute if score $bwm mg.st matches 0 run function mg:bedwars/map/wipe
execute if score $bwm mg.st matches 0 run function mg:bedwars/build
execute if score $bwm mg.st matches 1 run function mg:bedwars/map/build_1
execute if score $bwm mg.st matches 2 run function mg:bedwars/map/build_2
execute if score $bwm mg.st matches 3 run function mg:bedwars/map/build_3
kill @e[type=minecraft:item,x=-45,y=40,z=1155,dx=90,dy=70,dz=90]
kill @e[tag=mg.npc]

# Perchoir spectateur
scoreboard players set $px mg.st 0
scoreboard players set $py mg.st 85
scoreboard players set $pz mg.st 1200

# Équipes : 2, 3 ou 4 selon le nombre de joueurs
scoreboard players set $nt mg.st 2
execute if score $n0 mg.st matches 3 run scoreboard players set $nt mg.st 3
execute if score $n0 mg.st matches 4.. run scoreboard players set $nt mg.st 4
function mg:core/assign_teams

# Boutiques : 2 villageois par île occupée, un de plus par joueur au-delà de 2 (4 max) — plusieurs joueurs peuvent acheter en même temps
execute store result score $bwc mg.st if entity @a[team=mg_red,tag=mg.play]
execute if score $bwc mg.st matches 1.. run function mg:bedwars/npc {x:"-33.5",z:"1196.5",ry:"0"}
execute if score $bwc mg.st matches 1.. run function mg:bedwars/npc {x:"-31.5",z:"1196.5",ry:"0"}
execute if score $bwc mg.st matches 3.. run function mg:bedwars/npc {x:"-33.5",z:"1204.5",ry:"180"}
execute if score $bwc mg.st matches 4.. run function mg:bedwars/npc {x:"-31.5",z:"1204.5",ry:"180"}
execute store result score $bwc mg.st if entity @a[team=mg_blue,tag=mg.play]
execute if score $bwc mg.st matches 1.. run function mg:bedwars/npc {x:"33.5",z:"1196.5",ry:"0"}
execute if score $bwc mg.st matches 1.. run function mg:bedwars/npc {x:"31.5",z:"1196.5",ry:"0"}
execute if score $bwc mg.st matches 3.. run function mg:bedwars/npc {x:"33.5",z:"1204.5",ry:"180"}
execute if score $bwc mg.st matches 4.. run function mg:bedwars/npc {x:"31.5",z:"1204.5",ry:"180"}
execute store result score $bwc mg.st if entity @a[team=mg_green,tag=mg.play]
execute if score $bwc mg.st matches 1.. run function mg:bedwars/npc {x:"-3.5",z:"1166.5",ry:"-90"}
execute if score $bwc mg.st matches 1.. run function mg:bedwars/npc {x:"-3.5",z:"1168.5",ry:"-90"}
execute if score $bwc mg.st matches 3.. run function mg:bedwars/npc {x:"4.5",z:"1166.5",ry:"90"}
execute if score $bwc mg.st matches 4.. run function mg:bedwars/npc {x:"4.5",z:"1168.5",ry:"90"}
execute store result score $bwc mg.st if entity @a[team=mg_yellow,tag=mg.play]
execute if score $bwc mg.st matches 1.. run function mg:bedwars/npc {x:"-3.5",z:"1233.5",ry:"-90"}
execute if score $bwc mg.st matches 1.. run function mg:bedwars/npc {x:"-3.5",z:"1231.5",ry:"-90"}
execute if score $bwc mg.st matches 3.. run function mg:bedwars/npc {x:"4.5",z:"1233.5",ry:"90"}
execute if score $bwc mg.st matches 4.. run function mg:bedwars/npc {x:"4.5",z:"1231.5",ry:"90"}

# Lits « vivants » uniquement pour les équipes occupées
scoreboard players set $gr_red mg.st 0
scoreboard players set $gr_blue mg.st 0
scoreboard players set $gr_green mg.st 0
scoreboard players set $gr_yellow mg.st 0
execute store result score $bed_red mg.st if entity @a[team=mg_red,tag=mg.play]
execute store result score $bed_blue mg.st if entity @a[team=mg_blue,tag=mg.play]
execute store result score $bed_green mg.st if entity @a[team=mg_green,tag=mg.play]
execute store result score $bed_yellow mg.st if entity @a[team=mg_yellow,tag=mg.play]
# CORRECTIF : le compte de joueurs sert d'indicateur « lit vivant » (0/1). Avec 2 joueurs ou plus dans une équipe,
# la valeur valait 2+ : la destruction du lit n'était jamais détectée et l'équipe réapparaissait toujours.
execute if score $bed_red mg.st matches 2.. run scoreboard players set $bed_red mg.st 1
execute if score $bed_blue mg.st matches 2.. run scoreboard players set $bed_blue mg.st 1
execute if score $bed_green mg.st matches 2.. run scoreboard players set $bed_green mg.st 1
execute if score $bed_yellow mg.st matches 2.. run scoreboard players set $bed_yellow mg.st 1

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
