# Dernière minute : une bombe atomique par joueur
execute as @a[tag=mg.play] run item replace entity @s hotbar.3 with minecraft:warped_fungus_on_a_stick[custom_data={bomb:4},item_model="minecraft:nether_star",unbreakable={},custom_name={"text":"☢ Bombe atomique","color":"green","bold":true,"italic":false},lore=[{"text":"Rayon 11, une seule !","color":"gray","italic":false},{"text":"Clic droit : larguer (dans la direction du regard)","color":"dark_gray","italic":false}]]
title @a[tag=mg.play] title {"text":"☢","color":"green","bold":true}
title @a[tag=mg.play] subtitle {"text":"Bombe atomique disponible (case 4) !","color":"green"}
execute as @a[tag=mg.play] at @s run playsound minecraft:block.beacon.activate master @s ~ ~ ~ 1 0.6
