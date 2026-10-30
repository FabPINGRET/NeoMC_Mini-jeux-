execute positioned 10131 187 1212 run playsound minecraft:entity.goat.milk neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute positioned 10131 187 1212 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Loofkins Blotbuck","color":"dark_purple"},{"text":"> Sorry about the fumes, but I'm making paint in here. Paint by the thimble! It's a lot but you'd be surprised how fast it gets used up.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
