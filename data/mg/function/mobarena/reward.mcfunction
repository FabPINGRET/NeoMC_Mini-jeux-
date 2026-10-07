# Mob Arena — récompense de fin de vague + pause 15 s
scoreboard players set $wt mg.st 300
give @a[tag=mg.play] minecraft:arrow 8

execute unless score $mt mg.st matches 3 as @a[tag=mg.play,scores={mg.cl=6}] run function mg:mobarena/class/pyro_refill

tellraw @a [{"text":"[Mob Arena] ","color":"dark_green","bold":true},{"text":"✔ Vague ","color":"green"},{"score":{"name":"$wv","objective":"mg.st"},"color":"green","bold":true},{"text":" nettoyée ! Soin + repas + 8 flèches. Prochaine vague dans 15 s (change de classe si tu veux)...","color":"green"}]

# Soin instantané + repas (la saturation n'est donnée qu'ici, en récompense)
execute unless score $mt mg.st matches 3 run effect give @a[tag=mg.play] minecraft:instant_health 1 3 true
execute if score $mt mg.st matches 3 run effect give @a[tag=mg.play] minecraft:instant_health 1 1 true
effect give @a[tag=mg.play] minecraft:saturation 5 0 true

title @a[tag=mg.play] title [{"text":"✔ Vague nettoyée !","color":"green"}]
title @a[tag=mg.play] subtitle [{"text":"Soin complet + repas + 8 flèches — vague suivante dans 15 s","color":"gray"}]
execute as @a[tag=!mg.surv] at @s run playsound minecraft:entity.player.levelup master @s ~ ~ ~ 1 1


# Bonus des parties à 20 vagues
execute if score $wmax mg.st matches 20 if score $wv mg.st matches 5 run give @a[tag=mg.play] minecraft:golden_apple 2
execute if score $wmax mg.st matches 20 if score $wv mg.st matches 10 run give @a[tag=mg.play] minecraft:golden_apple 3
execute if score $wmax mg.st matches 20 if score $wv mg.st matches 10 run give @a[tag=mg.play] minecraft:diamond_sword[unbreakable={}]
execute if score $wmax mg.st matches 20 if score $wv mg.st matches 15 run give @a[tag=mg.play] minecraft:golden_apple 3
execute if score $wmax mg.st matches 20 if score $wv mg.st matches 15 run give @a[tag=mg.play] minecraft:arrow 32
execute if score $wmax mg.st matches 20 if score $wv mg.st matches 5 run tellraw @a[tag=mg.play] [{"text":"  + ","color":"gold"},{"text":"pommes d'or de renfort","color":"yellow"}]
execute if score $wmax mg.st matches 20 if score $wv mg.st matches 10 run tellraw @a[tag=mg.play] [{"text":"  + ","color":"gold"},{"text":"épée en diamant et pommes d'or","color":"yellow"}]
execute if score $wmax mg.st matches 20 if score $wv mg.st matches 15 run tellraw @a[tag=mg.play] [{"text":"  + ","color":"gold"},{"text":"flèches et pommes d'or","color":"yellow"}]

# Pause : on renvoie la liste des classes (changement possible avant la vague suivante)
execute unless score $mt mg.st matches 3 as @a[tag=mg.play] run function mg:mobarena/class_menu
