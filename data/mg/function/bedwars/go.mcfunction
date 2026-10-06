# Bedwars — début
gamemode survival @a[tag=mg.play]
execute as @a[team=mg_red,tag=mg.play] run function mg:bedwars/kit_red
execute as @a[team=mg_blue,tag=mg.play] run function mg:bedwars/kit_blue
execute as @a[team=mg_green,tag=mg.play] run function mg:bedwars/kit_green
execute as @a[team=mg_yellow,tag=mg.play] run function mg:bedwars/kit_yellow

tellraw @a[tag=mg.play] [{"text":"⚑ BEDWARS : ","color":"light_purple","bold":true},{"text":"ramasse le fer/or de ton île, achète auprès du ","color":"gray"},{"text":"VILLAGEOIS BOUTIQUE","color":"gold"},{"text":", construis des ponts en laine, détruis les lits ennemis puis élimine tout le monde !","color":"gray"}]
tellraw @a[tag=mg.play] [{"text":"Tant que ton lit existe, tu réapparais. Diamants sur l'île centrale.","color":"dark_gray","italic":true}]
