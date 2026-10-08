# Départ
scoreboard players set $zr mg.st 0
scoreboard players set $zph mg.st 0
scoreboard players set $zb mg.st 100
scoreboard players set #2 mg.st 2
scoreboard players set @a[tag=mg.play] mg.zpt 500
scoreboard players reset @a mg.zk
scoreboard objectives setdisplay sidebar mg.zpt
scoreboard players set @a mg.deaths 0
execute as @a[tag=mg.play] run function mg:zm/kit
tellraw @a[tag=mg.play] [{"text":"🧟 ZOMBIES : ","color":"dark_green","bold":true},{"text":"survivez à 10 manches ! Clic droit = tirer, accroupi = recharger. Chaque balle qui touche = 10 pts, chaque kill = 60 pts. Clic droit sur les portes, armes au mur, boîte mystère et boissons pour les acheter. Un joueur mort revient à la manche suivante.","color":"gray"}]
