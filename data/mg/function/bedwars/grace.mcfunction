# Bedwars — fenêtre de retour (2 min) : une équipe dont le dernier joueur s'est
# déconnecté n'est pas éliminée tant que son lit est intact et que la fenêtre court.
# $gr_<team> : ticks restants ; rechargé à 2400 tant qu'un joueur de l'équipe est en ligne.
execute if entity @a[team=mg_red,tag=mg.play] run scoreboard players set $gr_red mg.st 2400
execute if score $bed_red mg.st matches 0 run scoreboard players set $gr_red mg.st 0
execute unless entity @a[team=mg_red,tag=mg.play] if score $gr_red mg.st matches 2400 run tellraw @a [{"text":"⌛ L'équipe ","color":"gray"},{"text":"ROUGE","color":"red","bold":true},{"text":" s'est déconnectée — 2 minutes pour revenir (lit intact).","color":"gray"}]
execute unless entity @a[team=mg_red,tag=mg.play] if score $gr_red mg.st matches 1 run tellraw @a [{"text":"☠ L'équipe ","color":"gray"},{"text":"ROUGE","color":"red","bold":true},{"text":" n'est pas revenue à temps : éliminée !","color":"gray"}]
execute unless entity @a[team=mg_red,tag=mg.play] if score $gr_red mg.st matches 1.. run scoreboard players remove $gr_red mg.st 1

execute if entity @a[team=mg_blue,tag=mg.play] run scoreboard players set $gr_blue mg.st 2400
execute if score $bed_blue mg.st matches 0 run scoreboard players set $gr_blue mg.st 0
execute unless entity @a[team=mg_blue,tag=mg.play] if score $gr_blue mg.st matches 2400 run tellraw @a [{"text":"⌛ L'équipe ","color":"gray"},{"text":"BLEUE","color":"blue","bold":true},{"text":" s'est déconnectée — 2 minutes pour revenir (lit intact).","color":"gray"}]
execute unless entity @a[team=mg_blue,tag=mg.play] if score $gr_blue mg.st matches 1 run tellraw @a [{"text":"☠ L'équipe ","color":"gray"},{"text":"BLEUE","color":"blue","bold":true},{"text":" n'est pas revenue à temps : éliminée !","color":"gray"}]
execute unless entity @a[team=mg_blue,tag=mg.play] if score $gr_blue mg.st matches 1.. run scoreboard players remove $gr_blue mg.st 1

execute if entity @a[team=mg_green,tag=mg.play] run scoreboard players set $gr_green mg.st 2400
execute if score $bed_green mg.st matches 0 run scoreboard players set $gr_green mg.st 0
execute unless entity @a[team=mg_green,tag=mg.play] if score $gr_green mg.st matches 2400 run tellraw @a [{"text":"⌛ L'équipe ","color":"gray"},{"text":"VERTE","color":"green","bold":true},{"text":" s'est déconnectée — 2 minutes pour revenir (lit intact).","color":"gray"}]
execute unless entity @a[team=mg_green,tag=mg.play] if score $gr_green mg.st matches 1 run tellraw @a [{"text":"☠ L'équipe ","color":"gray"},{"text":"VERTE","color":"green","bold":true},{"text":" n'est pas revenue à temps : éliminée !","color":"gray"}]
execute unless entity @a[team=mg_green,tag=mg.play] if score $gr_green mg.st matches 1.. run scoreboard players remove $gr_green mg.st 1

execute if entity @a[team=mg_yellow,tag=mg.play] run scoreboard players set $gr_yellow mg.st 2400
execute if score $bed_yellow mg.st matches 0 run scoreboard players set $gr_yellow mg.st 0
execute unless entity @a[team=mg_yellow,tag=mg.play] if score $gr_yellow mg.st matches 2400 run tellraw @a [{"text":"⌛ L'équipe ","color":"gray"},{"text":"JAUNE","color":"yellow","bold":true},{"text":" s'est déconnectée — 2 minutes pour revenir (lit intact).","color":"gray"}]
execute unless entity @a[team=mg_yellow,tag=mg.play] if score $gr_yellow mg.st matches 1 run tellraw @a [{"text":"☠ L'équipe ","color":"gray"},{"text":"JAUNE","color":"yellow","bold":true},{"text":" n'est pas revenue à temps : éliminée !","color":"gray"}]
execute unless entity @a[team=mg_yellow,tag=mg.play] if score $gr_yellow mg.st matches 1.. run scoreboard players remove $gr_yellow mg.st 1
