bossbar set mg:ev color blue
execute in minecraft:overworld run summon minecraft:marker 0 64 0 {Tags:["mg.evx","mg.evt"]}
execute in minecraft:overworld run spreadplayers 0 0 0 45 under 75 false @e[type=minecraft:marker,tag=mg.evt]
execute in minecraft:overworld at @e[type=minecraft:marker,tag=mg.evt] align xz positioned ~0.5 ~ ~0.5 run function mg:lobby/ev/e3_place
title @a[tag=mg.evl] title {"text":"🗝 CHASSE AU TRÉSOR","color":"aqua","bold":true}
title @a[tag=mg.evl] subtitle {"text":"Un coffre est caché sur l'île","color":"gray"}
