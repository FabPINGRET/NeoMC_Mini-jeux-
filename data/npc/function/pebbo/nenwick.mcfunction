execute positioned 10117 187 1198 run playsound minecraft:entity.goat.milk neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute positioned 10117 187 1198 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Nenwick Hangyflap","color":"dark_purple"},{"text":"> Solid-color tapestries are the decor of the future. All the fashionable lords and ladies will be foaming at the mouth for a solid rectangle of blue or gray or pink to hang on their wall.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
