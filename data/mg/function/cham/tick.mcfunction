# 🦎 Meccha Chameleon : tick
scoreboard players add $cmt mg.st 1
execute if score $cmt mg.st matches ..899 run tp @a[tag=mg.cms] 0.5 89 26600.5
execute if score $cmt mg.st matches 900 run function mg:cham/release
execute as @a[tag=mg.cmx,scores={mg.cmq=1..}] at @s run function mg:cham/use
execute as @a[tag=mg.cmh,tag=!mg.cmout,scores={mg.cmp=1..}] run function mg:cham/palette_cmd
execute as @a[tag=mg.cmh,tag=!mg.cmout,scores={mg.cmo=1..}] run function mg:cham/pose_cmd
execute as @a[tag=mg.cmh,tag=!mg.cmout] at @s run function mg:cham/follow
scoreboard players remove @a[tag=mg.cmx,scores={mg.cmtc=1..}] mg.cmtc 1
scoreboard players remove @a[tag=mg.cmx,scores={mg.cmgc=1..}] mg.cmgc 1
execute as @e[type=minecraft:interaction,tag=mg.cmi] if data entity @s attack run function mg:cham/hit_int
execute as @e[type=minecraft:interaction,tag=mg.cmdi] if data entity @s attack run function mg:cham/hit_dec
execute as @e[type=minecraft:interaction,tag=mg.cmi] if data entity @s interaction run data remove entity @s interaction
execute as @e[type=minecraft:interaction,tag=mg.cmdi] if data entity @s interaction run data remove entity @s interaction
scoreboard players operation $cmq mg.st = $cmt mg.st
scoreboard players set #20 mg.st 20
scoreboard players operation $cmq mg.st %= #20 mg.st
execute if score $cmq mg.st matches 0 run function mg:cham/second
execute store result score $cmh mg.st if entity @a[tag=mg.play,tag=mg.cmh,tag=!mg.cmout]
execute store result score $cmk mg.st if entity @a[tag=mg.play,tag=mg.cms]
execute if score $state mg.st matches 2 if score $cmh mg.st matches 0 run return run function mg:cham/seekers_win
execute if score $state mg.st matches 2 if score $cmk mg.st matches 0 run return run function mg:cham/hiders_win
execute if score $state mg.st matches 2 if score $cmt mg.st matches 4500.. run function mg:cham/hiders_win
