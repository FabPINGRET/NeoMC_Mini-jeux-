# Socle 2 (@s = joueur sur le socle)
execute unless items entity @s hotbar.* minecraft:blaze_rod run title @s actionbar [{"text":"✦ Baguette feu d'artifice récupérée !","color":"green"}]
execute unless items entity @s hotbar.* minecraft:blaze_rod at @s run playsound minecraft:entity.item.pickup master @s ~ ~ ~ 1 1.2
execute unless items entity @s hotbar.* minecraft:blaze_rod run item replace entity @s hotbar.1 with minecraft:blaze_rod[custom_name=[{"text":"✦ Baguette feu d'artifice","color":"gold","bold":true,"italic":false}],lore=[{"text":"Clic droit : feu d'artifice dans le ciel","color":"gray","italic":false}],enchantment_glint_override=true,consumable={consume_seconds:0.05,animation:"none",sound:"minecraft:entity.firework_rocket.launch",has_consume_particles:false}]
