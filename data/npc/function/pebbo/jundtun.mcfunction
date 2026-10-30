execute positioned 10117 174 1321 run playsound minecraft:entity.goat.milk neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute positioned 10117 174 1321 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Jundtun the Grudge","color":"blue"},{"text":"> His majesty enjoys sparring. It's good exercise and we ","color":"white"},{"text":"Rubblewalkers","color":"blue"},{"text":" make good sparring partners.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
