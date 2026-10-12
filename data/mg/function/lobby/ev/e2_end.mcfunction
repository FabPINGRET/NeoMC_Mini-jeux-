execute as @a[tag=mg.evl] run function mg:lobby/ev/e2_count
scoreboard players set $evbest mg.st 0
execute as @a[tag=mg.evl] run scoreboard players operation $evbest mg.st > @s mg.evc
execute if score $evbest mg.st matches 1.. as @a[tag=mg.evl] if score @s mg.evc = $evbest mg.st run tag @s add mg.evwin
execute unless score $theme mg.st matches 1..2 as @a[tag=mg.evwin,limit=1,sort=random] run tellraw @a [{"text":"💰 Le plus riche : ","color":"gold"},{"selector":"@s","color":"yellow"},{"text":" (","color":"gray"},{"score":{"name":"$evbest","objective":"mg.st"},"color":"yellow"},{"text":" pièces)","color":"gray"}]
execute if score $theme mg.st matches 1 as @a[tag=mg.evwin,limit=1,sort=random] run tellraw @a [{"text":"🍬 Le plus gourmand : ","color":"gold"},{"selector":"@s","color":"yellow"},{"text":" (","color":"gray"},{"score":{"name":"$evbest","objective":"mg.st"},"color":"yellow"},{"text":" bonbons)","color":"gray"}]
execute if score $theme mg.st matches 2 as @a[tag=mg.evwin,limit=1,sort=random] run tellraw @a [{"text":"🎁 Le plus chargé : ","color":"gold"},{"selector":"@s","color":"yellow"},{"text":" (","color":"gray"},{"score":{"name":"$evbest","objective":"mg.st"},"color":"yellow"},{"text":" cadeaux)","color":"gray"}]
execute as @a[tag=mg.evwin,limit=1,sort=random] run function mg:lobby/ev/win
tag @a remove mg.evwin
