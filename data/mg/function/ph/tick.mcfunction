# 🎭 Prop Hunt — tick
scoreboard players add $pht mg.st 1
execute if score $pht mg.st matches ..599 run tp @a[tag=mg.phs] 0.5 89 23600.5
execute if score $pht mg.st matches 600 run function mg:ph/release
execute as @a[tag=mg.phh,scores={mg.gsn=1..},tag=!mg.phsn] run function mg:ph/copy
tag @a[tag=mg.phh,scores={mg.gsn=1..}] add mg.phsn
tag @a[tag=mg.phsn,scores={mg.gsn=0}] remove mg.phsn
execute as @a[tag=mg.phsn] unless score @s mg.gsn matches 1.. run tag @s remove mg.phsn
scoreboard players set @a[tag=mg.phx] mg.gsn 0
execute as @a[tag=mg.phh] at @s run function mg:ph/follow
execute as @a[tag=mg.phh,scores={mg.phn=1..}] at @s run function mg:ph/taunt_one
scoreboard players reset @a[scores={mg.phn=1..}] mg.phn
execute as @e[type=minecraft:interaction,tag=mg.phi] if data entity @s attack run function mg:ph/hit_prop
execute if score $n0 mg.st matches 2.. as @a[tag=mg.phh,scores={mg.deaths=1..}] run function mg:ph/found
execute unless score $n0 mg.st matches 2.. as @e[type=minecraft:player,tag=mg.phh,scores={mg.deaths=1..}] run function mg:ph/srevive
execute as @a[tag=mg.phs,scores={mg.deaths=1..}] run scoreboard players set @s mg.deaths 0
scoreboard players operation $phq mg.st = $pht mg.st
scoreboard players set #400 mg.st 400
scoreboard players operation $phq mg.st %= #400 mg.st
execute if score $pht mg.st matches 601.. if score $phq mg.st matches 0 run function mg:ph/taunt
scoreboard players operation $phq mg.st = $pht mg.st
scoreboard players set #20 mg.st 20
scoreboard players operation $phq mg.st %= #20 mg.st
execute if score $phq mg.st matches 0 run function mg:ph/second
execute store result score $phh mg.st if entity @a[tag=mg.play,tag=mg.phh]
execute store result score $phk mg.st if entity @a[tag=mg.play,tag=mg.phs]
execute if score $state mg.st matches 2 if score $n0 mg.st matches 2.. if score $phh mg.st matches 0 run return run function mg:ph/seekers_win
execute if score $state mg.st matches 2 if score $n0 mg.st matches 2.. if score $phk mg.st matches 0 run return run function mg:ph/hiders_win
execute if score $state mg.st matches 2 if score $pht mg.st matches 4800.. run function mg:ph/hiders_win
