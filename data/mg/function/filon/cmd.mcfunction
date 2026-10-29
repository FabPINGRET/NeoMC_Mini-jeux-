# Trigger mg.fnt (@s) : 1-10 achats, 20 vendre, 21 cours du marché, 30 retour au lobby
execute unless entity @s[tag=mg.fnw] run return run scoreboard players reset @s mg.fnt
execute if score @s mg.fnt matches 30 run return run function mg:filon/leave
execute unless entity @s[x=-4,y=97,z=45976,dx=24,dy=10,dz=20] run tellraw @s {"text":"⚠ Approche-toi du comptoir et du magasin (place de l'île).","color":"red"}
execute unless entity @s[x=-4,y=97,z=45976,dx=24,dy=10,dz=20] run return run scoreboard players reset @s mg.fnt
execute if score @s mg.fnt matches 20 run function mg:filon/sell
execute if score @s mg.fnt matches 21 run function mg:filon/market_show
scoreboard players set #c mg.st -1
execute if score @s mg.fnt matches 1 if score @s mg.fnpk matches 1 run scoreboard players set #c mg.st 400
execute if score @s mg.fnt matches 1 if score @s mg.fnpk matches 2 run scoreboard players set #c mg.st 1500
execute if score @s mg.fnt matches 1 if score #c mg.st matches -1 run tellraw @s {"text":"C'est déjà le niveau maximum.","color":"gray"}
execute if score @s mg.fnt matches 2 if score @s mg.fnef matches 2 run scoreboard players set #c mg.st 150
execute if score @s mg.fnt matches 2 if score @s mg.fnef matches 3 run scoreboard players set #c mg.st 350
execute if score @s mg.fnt matches 2 if score @s mg.fnef matches 4 run scoreboard players set #c mg.st 800
execute if score @s mg.fnt matches 2 if score #c mg.st matches -1 run tellraw @s {"text":"C'est déjà le niveau maximum.","color":"gray"}
execute if score @s mg.fnt matches 3 if score @s mg.fnfo matches 0 run scoreboard players set #c mg.st 300
execute if score @s mg.fnt matches 3 if score @s mg.fnfo matches 1 run scoreboard players set #c mg.st 900
execute if score @s mg.fnt matches 3 if score @s mg.fnfo matches 2 run scoreboard players set #c mg.st 2500
execute if score @s mg.fnt matches 3 if score #c mg.st matches -1 run tellraw @s {"text":"C'est déjà le niveau maximum.","color":"gray"}
execute if score @s mg.fnt matches 4 if score @s mg.fnha matches 0 run scoreboard players set #c mg.st 500
execute if score @s mg.fnt matches 4 if score @s mg.fnha matches 1 run scoreboard players set #c mg.st 1500
execute if score @s mg.fnt matches 4 if score #c mg.st matches -1 run tellraw @s {"text":"C'est déjà le niveau maximum.","color":"gray"}
execute if score @s mg.fnt matches 5 if score @s mg.fnsw matches 0 run scoreboard players set #c mg.st 60
execute if score @s mg.fnt matches 5 if score @s mg.fnsw matches 1 run scoreboard players set #c mg.st 200
execute if score @s mg.fnt matches 5 if score @s mg.fnsw matches 2 run scoreboard players set #c mg.st 600
execute if score @s mg.fnt matches 5 if score @s mg.fnsw matches 3 run scoreboard players set #c mg.st 1500
execute if score @s mg.fnt matches 5 if score #c mg.st matches -1 run tellraw @s {"text":"C'est déjà le niveau maximum.","color":"gray"}
execute if score @s mg.fnt matches 6 if score @s mg.fnar matches 0 run scoreboard players set #c mg.st 80
execute if score @s mg.fnt matches 6 if score @s mg.fnar matches 1 run scoreboard players set #c mg.st 250
execute if score @s mg.fnt matches 6 if score @s mg.fnar matches 2 run scoreboard players set #c mg.st 600
execute if score @s mg.fnt matches 6 if score @s mg.fnar matches 3 run scoreboard players set #c mg.st 1500
execute if score @s mg.fnt matches 6 if score #c mg.st matches -1 run tellraw @s {"text":"C'est déjà le niveau maximum.","color":"gray"}
execute if score @s mg.fnt matches 7 run scoreboard players set #c mg.st 20
execute if score @s mg.fnt matches 8 run scoreboard players set #c mg.st 120
execute if score @s mg.fnt matches 9 run scoreboard players set #c mg.st 150
execute if score @s mg.fnt matches 10 run scoreboard players set #c mg.st 650
execute if score #c mg.st matches 0.. if score @s mg.fnp < #c mg.st run tellraw @s [{"text":"Pas assez de points (","color":"red"},{"score":{"name":"#c","objective":"mg.st"},"color":"yellow"},{"text":" requis).","color":"red"}]
execute if score #c mg.st matches 0.. if score @s mg.fnp < #c mg.st at @s run playsound minecraft:block.note_block.bass master @s ~ ~ ~ 1 0.6
execute if score #c mg.st matches 0.. if score @s mg.fnp < #c mg.st run scoreboard players set #c mg.st -1
execute if score #c mg.st matches 0.. run function mg:filon/buy_ok
scoreboard players reset @s mg.fnt
