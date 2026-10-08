# One in the Chamber — début de partie (premier à 10 kills)
gamemode adventure @a[tag=mg.play]
scoreboard players set @a[tag=mg.play] mg.lv 3
scoreboard players set @a[tag=mg.play] mg.ok 0
scoreboard players set $og mg.st 10
scoreboard players set $osi mg.st 600
execute if score $ar mg.st matches 1.. run function mg:var/mode/oitc_go
scoreboard players set $os mg.st 0
scoreboard players reset @a mg.pk
execute as @a[tag=mg.play] run function mg:oitc/kit
scoreboard objectives setdisplay below_name
scoreboard objectives setdisplay sidebar mg.ok
tellraw @a[tag=mg.play] [{"text":"➶ ONE IN THE CHAMBER : ","color":"gold","bold":true},{"text":"une épée et UNE flèche. Une flèche = un kill instantané. Chaque kill te donne une flèche de plus. Respawn illimité : le premier à 10 kills gagne !","color":"gray"}]
tellraw @a[tag=mg.play] [{"text":"✦ Flèches enchantées : ","color":"light_purple","bold":true},{"text":"de temps en temps (kill chanceux ou toutes les 30 s) : explosive, perforante ou révélatrice.","color":"gray"}]
