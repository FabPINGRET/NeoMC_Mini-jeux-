# Fin de la cachette : les chasseurs entrent
effect clear @a[tag=mg.cms] minecraft:blindness
spreadplayers 0 26600 1 6 under 85 false @a[tag=mg.cms]
execute as @a[tag=mg.cms] at @s run spawnpoint @s ~ ~ ~
bossbar set mg:cham color red
bossbar set mg:cham max 3600
title @a[tag=mg.cmx] title {"text":"🔍 La chasse commence !","color":"red","bold":true}
title @a[tag=mg.cmx] subtitle {"text":"3 minutes","color":"gray"}
execute as @a[tag=mg.cmx] at @s run playsound minecraft:event.raid.horn master @s ~ ~ ~ 0.6 1.2
