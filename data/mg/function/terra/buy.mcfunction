# @s (joueur) achète au présentoir $tvk : prix, conditions, objet
scoreboard players set $tvp mg.st 0
execute if score $tvk mg.st matches 1 run scoreboard players set $tvp mg.st 150
execute if score $tvk mg.st matches 2 run scoreboard players set $tvp mg.st 220
execute if score $tvk mg.st matches 3 run scoreboard players set $tvp mg.st 80
execute if score $tvk mg.st matches 4 run scoreboard players set $tvp mg.st 25
execute if score $tvk mg.st matches 5 run scoreboard players set $tvp mg.st 45
execute if score $tvk mg.st matches 6 run scoreboard players set $tvp mg.st 15
execute if score $tvk mg.st matches 7 run scoreboard players set $tvp mg.st 100
execute if score $tvk mg.st matches 8 run scoreboard players set $tvp mg.st 40
execute if score $tvk mg.st matches 1 if items entity @s container.* *[custom_data~{tv:4}] run return run function mg:terra/buy_has
execute if score $tvk mg.st matches 2 if score @s mg.trwp matches 2.. run return run function mg:terra/buy_has
execute if score $tvk mg.st matches 3 if items entity @s container.* *[custom_data~{tv:5}] run return run function mg:terra/buy_has_net
execute if score $tvk mg.st matches 4 unless items entity @s container.* *[custom_data~{tv:5}] run return run function mg:terra/buy_need_net
execute if score $tvk mg.st matches 7 if score @s mg.trar matches 1.. run return run function mg:terra/buy_has
execute if score @s mg.tvc < $tvp mg.st run return run function mg:terra/buy_poor
scoreboard players operation @s mg.tvc -= $tvp mg.st
execute if score $tvk mg.st matches 1 run give @s minecraft:warped_fungus_on_a_stick[custom_data={tv:4},item_model="minecraft:goat_horn",unbreakable={},use_cooldown={seconds:4f,cooldown_group:"mg:tvsonic"},custom_name={"text":"📢 Canon sonique","color":"aqua","italic":false,"bold":true},lore=[{"text":"Clic droit : onde de choc en cône (8 blocs)","color":"gray","italic":false},{"text":"Repousse et ralentit, recharge 4 s","color":"gray","italic":false}]]
execute if score $tvk mg.st matches 2 run clear @s minecraft:warped_fungus_on_a_stick[minecraft:custom_data~{tv:2}]
execute if score $tvk mg.st matches 2 run give @s minecraft:warped_fungus_on_a_stick[custom_data={tv:3},item_model="minecraft:crossbow",unbreakable={},enchantment_glint_override=true,custom_name={"text":"🔫 Fusil à impulsions Mk2","color":"gold","italic":false,"bold":true},lore=[{"text":"Plus puissant, chauffe moins vite","color":"gray","italic":false},{"text":"Clic droit : tir","color":"gray","italic":false}]]
execute if score $tvk mg.st matches 2 run scoreboard players set @s mg.trwp 2
execute if score $tvk mg.st matches 3 run give @s minecraft:warped_fungus_on_a_stick[custom_data={tv:5},item_model="minecraft:fishing_rod",unbreakable={},custom_name={"text":"🕸 Lance-filets","color":"white","italic":false,"bold":true},lore=[{"text":"Clic droit : immobilise un dinosaure 5 s","color":"gray","italic":false},{"text":"Filets en vente au dépôt","color":"gray","italic":false}]]
execute if score $tvk mg.st matches 3..4 run scoreboard players add @s mg.tvnet 3
execute if score $tvk mg.st matches 5 unless items entity @s container.* *[custom_data~{tv:6}] run give @s minecraft:warped_fungus_on_a_stick[custom_data={tv:6},item_model="minecraft:tripwire_hook",unbreakable={},custom_name={"text":"⚙ Pièges au sol","color":"gray","italic":false,"bold":true},lore=[{"text":"Clic droit : pose un piège à tes pieds","color":"gray","italic":false},{"text":"Le premier prédateur qui marche dessus est bloqué 6 s","color":"gray","italic":false}]]
execute if score $tvk mg.st matches 5 run scoreboard players add @s mg.tvtr 3
execute if score $tvk mg.st matches 6 run give @s minecraft:golden_apple[custom_name={"text":"✚ Trousse de soins","color":"red","italic":false,"bold":true}] 2
execute if score $tvk mg.st matches 7 run item replace entity @s armor.head with minecraft:chainmail_helmet[unbreakable={},custom_data={tvarm:1b},custom_name={"text":"🛡 Armure de patrouille","color":"dark_aqua","italic":false,"bold":true}]
execute if score $tvk mg.st matches 7 run item replace entity @s armor.chest with minecraft:chainmail_chestplate[unbreakable={},custom_data={tvarm:1b},custom_name={"text":"🛡 Armure de patrouille","color":"dark_aqua","italic":false,"bold":true}]
execute if score $tvk mg.st matches 7 run item replace entity @s armor.legs with minecraft:chainmail_leggings[unbreakable={},custom_data={tvarm:1b},custom_name={"text":"🛡 Armure de patrouille","color":"dark_aqua","italic":false,"bold":true}]
execute if score $tvk mg.st matches 7 run scoreboard players set @s mg.trar 1
execute if score $tvk mg.st matches 8 run give @s minecraft:saddle[custom_name={"text":"🐴 Selle de brachiosaure","color":"yellow","italic":false,"bold":true},lore=[{"text":"Clic droit sur un brachiosaure pour la poser,","color":"gray","italic":false},{"text":"puis clic droit pour monter (Z/Q/S/D, espace = élan)","color":"gray","italic":false}]]
scoreboard players set @s mg.tval 50
title @s actionbar [{"text":"✔ Acheté ! ","color":"green","bold":true},{"text":"reste ","color":"gray"},{"score":{"name":"@s","objective":"mg.tvc"},"color":"yellow"},{"text":" ₵","color":"yellow"}]
execute at @s run playsound minecraft:entity.villager.yes player @s ~ ~ ~ 0.8 1.1
