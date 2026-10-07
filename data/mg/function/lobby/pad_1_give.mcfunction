title @s actionbar [{"text":"⚡ Railgun récupéré !","color":"green"}]
execute at @s run playsound minecraft:entity.item.pickup master @s ~ ~ ~ 1 1.2
item replace entity @s hotbar.0 with minecraft:warped_fungus_on_a_stick[unbreakable={},custom_name=[{"text":"⚡ Railgun","color":"red","bold":true,"italic":false}],lore=[{"text":"Clic droit : tir de railgun (1 cœur, jamais mortel)","color":"gray","italic":false}],enchantment_glint_override=true]
execute if score $rp mg.st matches 1 run item modify entity @s hotbar.0 {"function":"minecraft:set_components","components":{"minecraft:item_model":"mg:laser_gun"}}
