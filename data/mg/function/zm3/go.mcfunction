# Départ
scoreboard players set $zpts mg.st 1
scoreboard players set $zr mg.st 0
scoreboard players set $zph mg.st 0
scoreboard players set $zb mg.st 100
scoreboard players set #2 mg.st 2
scoreboard players set @a[tag=mg.play] mg.zpt 500
scoreboard players reset @a mg.zkl
scoreboard objectives setdisplay sidebar mg.zpt
scoreboard players set @a mg.deaths 0
function mg:zx/reset
scoreboard players set $zid mg.st 0
execute as @a[tag=mg.play] store result score @s mg.zid run scoreboard players add $zid mg.st 1
execute as @a[tag=mg.play] run function mg:zm3/kit
tellraw @a[tag=mg.play] [{"text":"🧟 ZOMBIES : ","color":"dark_green","bold":true},{"text":"survivez à 10 manches ! Clic droit = tirer, accroupi = recharger, munitions illimitées. Chaque balle qui touche = 10 pts, chaque kill = 60 pts. Clic droit sur les portes, armes au mur, boîte mystère, boissons et Pack-a-Punch pour les acheter. Un joueur mort revient à la manche suivante.","color":"gray"}]
tellraw @a[tag=mg.play] [{"text":" 🪵 Fenêtres : ","color":"gold"},{"text":"les zombies cassent les planches, accroupis-toi devant pour les reclouer (+10 pts). ","color":"gray"},{"text":"🎁 Bonus : ","color":"gold"},{"text":"les zombies lâchent parfois mort instantanée, Kaboom, points doubles, charpentier ou vente de feu, marche dessus. ","color":"gray"},{"text":"🔫 Q : ","color":"gold"},{"text":"jeter ton arme à un coéquipier.","color":"gray"}]
