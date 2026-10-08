# One in the Chamber, variante : kills pour gagner ($og) et flèches enchantées ($osi). Généré.
execute if score $dif mg.st matches 1 run scoreboard players set $og mg.st 7
execute if score $dif mg.st matches 4 run scoreboard players set $og mg.st 12
execute if score $dif mg.st matches 1 run scoreboard players set $osi mg.st 300
execute if score $dif mg.st matches 3 run scoreboard players set $osi mg.st 900
execute if score $dif mg.st matches 4 run scoreboard players set $osi mg.st 2000000000
tellraw @a[tag=mg.play] [{"text":"➶ Objectif de la variante : ","color":"gold"},{"score":{"name":"$og","objective":"mg.st"},"color":"yellow","bold":true},{"text":" kills.","color":"gold"}]
