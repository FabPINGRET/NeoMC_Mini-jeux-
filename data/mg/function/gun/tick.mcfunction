# Armes : à appeler chaque tick par le jeu
execute as @a[tag=mg.play,scores={mg.qs=1..}] at @s run function mg:gun/use
scoreboard players reset @a[scores={mg.qs=1..}] mg.qs
scoreboard players remove @a[scores={mg.gcd=1..}] mg.gcd 1
execute as @a[scores={mg.grl=1..}] at @s run function mg:gun/reload_tick
execute as @a[tag=mg.play,scores={mg.gsn=1..}] at @s run function mg:gun/sneak
scoreboard players reset @a[scores={mg.gsn=1..}] mg.gsn
execute as @a[tag=mg.play] if items entity @s weapon.mainhand *[custom_data~{mg_gun:1b}] run function mg:gun/hud
