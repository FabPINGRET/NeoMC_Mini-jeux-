execute positioned 10121 188 1314 run playsound minecraft:entity.goat.milk neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute positioned 10121 188 1314 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Quistlin the Ledgerbearer","color":"red"},{"text":"> My wife is worried that I bury myself too deeply in my work. So are my two kids. Or, wait, four kids? Three?","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
