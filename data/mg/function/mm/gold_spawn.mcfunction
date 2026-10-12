# Une pièce d'or au hasard dans la carte (14 au plus)
execute store result score $mmq mg.st if entity @e[type=minecraft:item,tag=mg.mmg]
execute if score $mmq mg.st matches 14.. run return 0
execute if score $mmm mg.st matches 1 run summon minecraft:marker 0 85 23600 {Tags:["mg.mmp"]}
execute if score $mmm mg.st matches 2 run summon minecraft:marker 0 90 23700 {Tags:["mg.mmp"]}
execute if score $mmm mg.st matches 3 run summon minecraft:marker 0 84 23800 {Tags:["mg.mmp"]}
execute if score $mmm mg.st matches 4 run summon minecraft:marker 0 87 23900 {Tags:["mg.mmp"]}
execute if score $mmm mg.st matches 1 run spreadplayers 0 23600 0 13 under 85 false @e[type=minecraft:marker,tag=mg.mmp]
execute if score $mmm mg.st matches 2 run spreadplayers 0 23700 0 14 under 90 false @e[type=minecraft:marker,tag=mg.mmp]
execute if score $mmm mg.st matches 3 run spreadplayers 0 23800 0 12 under 84 false @e[type=minecraft:marker,tag=mg.mmp]
execute if score $mmm mg.st matches 4 run spreadplayers 0 23900 0 13 under 87 false @e[type=minecraft:marker,tag=mg.mmp]
execute at @e[type=minecraft:marker,tag=mg.mmp] run summon minecraft:item ~ ~0.3 ~ {Tags:["mg.mmg","mg.keep"],Age:-32768s,Item:{id:"minecraft:gold_ingot",count:1,components:{"minecraft:custom_name":{"text":"🪙 Pièce d'or","color":"gold","italic":false}}}}
kill @e[type=minecraft:marker,tag=mg.mmp]
