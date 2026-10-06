# Socle 1 (@s = joueur sur le socle)
execute unless items entity @s hotbar.* minecraft:warped_fungus_on_a_stick run title @s actionbar [{"text":"⚡ Pistolet laser récupéré !","color":"green"}]
execute unless items entity @s hotbar.* minecraft:warped_fungus_on_a_stick at @s run playsound minecraft:entity.item.pickup master @s ~ ~ ~ 1 1.2
execute unless items entity @s hotbar.* minecraft:warped_fungus_on_a_stick run item replace entity @s hotbar.0 with minecraft:warped_fungus_on_a_stick[unbreakable={},custom_name=[{"text":"⚡ Pistolet laser","color":"red","bold":true,"italic":false}],lore=[{"text":"Clic droit : rayon laser inoffensif","color":"gray","italic":false}],enchantment_glint_override=true]
