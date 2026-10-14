# Toutes les 20 s : 3 brachiosaures et 4 pachycéphalosaures dans la jungle
execute store result score $tvn mg.st if entity @e[tag=mg.tvbrach]
execute if score $tvn mg.st matches ..2 as @e[type=minecraft:marker,tag=mg.tvhp,sort=random,limit=1] at @s unless entity @a[tag=mg.tvw,distance=..30] run function mg:terra/dino/brachio
execute store result score $tvn mg.st if entity @e[tag=mg.tvpachy]
execute if score $tvn mg.st matches ..3 as @e[type=minecraft:marker,tag=mg.tvhp,sort=random,limit=1] at @s unless entity @a[tag=mg.tvw,distance=..30] run function mg:terra/dino/pachy
