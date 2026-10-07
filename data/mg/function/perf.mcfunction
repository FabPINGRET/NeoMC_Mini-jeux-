# Outil dev : état de performance côté datapack (à lancer via /function mg:perf)
tellraw @s [{"text":"— mg:perf —","color":"gold","bold":true}]
execute store result score $pc1 mg.t if entity @e[type=minecraft:block_display]
execute store result score $pc2 mg.t if entity @e[type=minecraft:text_display]
execute store result score $pc3 mg.t if entity @e[type=minecraft:item_display]
execute store result score $pc4 mg.t if entity @e[type=minecraft:marker]
execute store result score $pc5 mg.t if entity @e[type=minecraft:armor_stand]
execute store result score $pc6 mg.t if entity @e[type=minecraft:item]
execute store result score $pc7 mg.t if entity @e[type=!minecraft:player]
tellraw @s [{"text":"Entités : ","color":"gray"},{"score":{"name":"$pc7","objective":"mg.t"},"color":"white"},{"text":" au total — block_display ","color":"gray"},{"score":{"name":"$pc1","objective":"mg.t"},"color":"white"},{"text":", text_display ","color":"gray"},{"score":{"name":"$pc2","objective":"mg.t"},"color":"white"},{"text":", item_display ","color":"gray"},{"score":{"name":"$pc3","objective":"mg.t"},"color":"white"},{"text":", marker ","color":"gray"},{"score":{"name":"$pc4","objective":"mg.t"},"color":"white"},{"text":", armor_stand ","color":"gray"},{"score":{"name":"$pc5","objective":"mg.t"},"color":"white"},{"text":", items au sol ","color":"gray"},{"score":{"name":"$pc6","objective":"mg.t"},"color":"white"}]
execute store result score $pc8 mg.t run forceload query
tellraw @s [{"text":"Chunks forceload : ","color":"gray"},{"score":{"name":"$pc8","objective":"mg.t"},"color":"white"}]
tellraw @s [{"text":"Temps de tick : ","color":"gray"},{"text":"/tick query","color":"yellow","click_event":{"action":"suggest_command","command":"/tick query"}},{"text":" (vanilla) · ","color":"gray"},{"text":"/mspt","color":"yellow","click_event":{"action":"suggest_command","command":"/mspt"}},{"text":" (Paper). À comparer avant/après une modification.","color":"gray"}]
