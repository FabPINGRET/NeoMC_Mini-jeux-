execute positioned 10120 187 1214 run playsound minecraft:entity.goat.milk neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute positioned 10120 187 1214 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Foobleez Anneal","color":"dark_purple"},{"text":"> Picture a window... now, stain the glass... Impressed? I just invented the idea! I create panes of colored glass, and... what? Big Ones already have these?","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
