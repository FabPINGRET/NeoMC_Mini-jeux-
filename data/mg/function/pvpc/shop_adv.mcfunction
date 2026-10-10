advancement revoke @s only mg:pvpc_shop
item replace entity @s hotbar.7 with minecraft:emerald[custom_data={pvpc_shop:1b},enchantment_glint_override=true,consumable={consume_seconds:0.05f,animation:"none",sound:"minecraft:ui.button.click",has_consume_particles:false},custom_name=[{"text":"💰 Boutique","color":"green","bold":true,"italic":false}],lore=[[{"text":"Clic droit : acheter des bonus avec tes pièces","color":"gray","italic":false}]]]
execute if entity @s[tag=mg.pvpc] run function mg:pvpc/shop
