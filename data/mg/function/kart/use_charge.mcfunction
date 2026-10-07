# Une charge en moins ; la dernière vide la main ; une banane ou une carapace en orbite disparaît
scoreboard players remove @s mg.kic 1
scoreboard players operation $kix mg.st = @s mg.kic
scoreboard players operation $me mg.st = @s mg.ri
execute as @e[type=minecraft:item_display,tag=mg.korb] if score @s mg.ri = $me mg.st if score @s mg.kdd = $kix mg.st run kill @s
execute if score @s mg.kic matches ..0 run scoreboard players set @s mg.kit 0
