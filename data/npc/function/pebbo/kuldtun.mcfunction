execute positioned 10071 187 1249 run playsound minecraft:entity.goat.milk neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute positioned 10071 187 1249 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Kuldtun the Strongback","color":"blue"},{"text":"> Most Rubblewalkers are out exploring the world, defending our home, or on Monk duty. I'm stuck at home with a hurt leg, so I might as well train my accuracy while it heals.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
