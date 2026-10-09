# @s reçoit le contenu du point ($gpt)
execute if score $gpt mg.st matches 2 run scoreboard players set @s mg.gal 40
execute if score $gpt mg.st matches 2 run function mg:gun/put_2 {slot:"hotbar.2"}
execute if score $gpt mg.st matches 2 run title @s actionbar {"text":"🔫 Mitraillette","color":"aqua","bold":true}
execute if score $gpt mg.st matches 3 run scoreboard players set @s mg.gal 40
execute if score $gpt mg.st matches 3 run function mg:gun/put_3 {slot:"hotbar.2"}
execute if score $gpt mg.st matches 3 run title @s actionbar {"text":"🔫 Fusil à pompe","color":"gold","bold":true}
execute if score $gpt mg.st matches 4 run scoreboard players set @s mg.gal 40
execute if score $gpt mg.st matches 4 run function mg:gun/put_4 {slot:"hotbar.2"}
execute if score $gpt mg.st matches 4 run title @s actionbar {"text":"🔫 Fusil M14","color":"yellow","bold":true}
execute if score $gpt mg.st matches 5 run scoreboard players set @s mg.gal 40
execute if score $gpt mg.st matches 5 run function mg:gun/put_5 {slot:"hotbar.3"}
execute if score $gpt mg.st matches 5 run title @s actionbar {"text":"🎯 Sniper","color":"light_purple","bold":true}
execute if score $gpt mg.st matches 6 run scoreboard players set @s mg.gal 40
execute if score $gpt mg.st matches 6 run function mg:gun/put_6 {slot:"hotbar.3"}
execute if score $gpt mg.st matches 6 run title @s actionbar {"text":"✦ Ray Gun","color":"green","bold":true}
execute if score $gpt mg.st matches 7 run scoreboard players set @s mg.gal 40
execute if score $gpt mg.st matches 7 run function mg:gta/rpg_give
execute if score $gpt mg.st matches 7 run title @s actionbar {"text":"🚀 Lance-roquettes","color":"red","bold":true}
execute if score $gpt mg.st matches 8 run scoreboard players set @s mg.gal 40
execute if score $gpt mg.st matches 8 run effect give @s minecraft:instant_health 1 2 true
execute if score $gpt mg.st matches 8 run effect give @s minecraft:regeneration 8 1 true
execute if score $gpt mg.st matches 8 run title @s actionbar {"text":"✚ Trousse de soins","color":"red","bold":true}
execute if score $gpt mg.st matches 9 run scoreboard players set @s mg.gal 40
execute if score $gpt mg.st matches 9 run item replace entity @s armor.chest with minecraft:iron_chestplate[unbreakable={},custom_name={"text":"🛡 Gilet pare-balles","color":"gray","italic":false}]
execute if score $gpt mg.st matches 9 run effect give @s minecraft:absorption 60 1 true
execute if score $gpt mg.st matches 9 run title @s actionbar {"text":"🛡 Gilet pare-balles","color":"gray","bold":true}
execute if score $gpt mg.st matches 52 run scoreboard players set @s mg.gal 40
execute if score $gpt mg.st matches 53 run scoreboard players set @s mg.gal 40
execute if score $gpt mg.st matches 54 run scoreboard players set @s mg.gal 40
execute if score $gpt mg.st matches 55 run scoreboard players set @s mg.gal 40
execute if score $gpt mg.st matches 11 run scoreboard players set @s mg.gal 40
execute if score $gpt mg.st matches 21 run scoreboard players set @s mg.gal 40
execute if score $gpt mg.st matches 22 run scoreboard players set @s mg.gal 40
execute if score $gpt mg.st matches 23 run scoreboard players set @s mg.gal 40
execute if score $gpt mg.st matches 24 run scoreboard players set @s mg.gal 40
execute if score $gpt mg.st matches 25 run scoreboard players set @s mg.gal 40
execute if score $gpt mg.st matches 70 run scoreboard players set @s mg.gal 40
execute if score $gpt mg.st matches 71 run scoreboard players set @s mg.gal 40
execute if score $gpt mg.st matches 60 run scoreboard players set @s mg.gal 40
execute if score $gpt mg.st matches 31 run scoreboard players set @s mg.gal 40
execute if score $gpt mg.st matches 32 run scoreboard players set @s mg.gal 40
execute if score $gpt mg.st matches 33 run scoreboard players set @s mg.gal 40
execute if score $gpt mg.st matches 34 run scoreboard players set @s mg.gal 40
execute if score $gpt mg.st matches 35 run scoreboard players set @s mg.gal 40
execute if score $gpt mg.st matches 42 run scoreboard players set @s mg.gal 40
execute if score $gpt mg.st matches 43 run scoreboard players set @s mg.gal 40
execute if score $gpt mg.st matches 44 run scoreboard players set @s mg.gal 40
execute if score $gpt mg.st matches 45 run scoreboard players set @s mg.gal 40
execute if score $gpt mg.st matches 46 run scoreboard players set @s mg.gal 40
execute if score $gpt mg.st matches 47 run scoreboard players set @s mg.gal 40
execute if score $gpt mg.st matches 49 run scoreboard players set @s mg.gal 40
execute if score $gpt mg.st matches 70 run function mg:gta/casino_slot
execute if score $gpt mg.st matches 71 run function mg:gta/casino_roulette
execute if score $gpt mg.st matches 60 run function mg:gta/paint
execute if score $gpt mg.st matches 11 run effect give @s minecraft:instant_health 1 1 true
execute if score $gpt mg.st matches 11 run title @s actionbar {"text":"✚ Soigné","color":"red","bold":true}
execute if score $gpt mg.st matches 21 run function mg:gta/veh_buy {t:"moto"}
execute if score $gpt mg.st matches 22 run function mg:gta/veh_buy {t:"muscle"}
execute if score $gpt mg.st matches 23 run function mg:gta/veh_buy {t:"supercar"}
execute if score $gpt mg.st matches 24 run function mg:gta/veh_buy {t:"heli"}
execute if score $gpt mg.st matches 25 run function mg:gta/veh_buy {t:"plane"}
