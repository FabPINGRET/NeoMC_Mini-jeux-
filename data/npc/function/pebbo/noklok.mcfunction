execute positioned 10061 187 1216 run playsound minecraft:entity.goat.milk neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute positioned 10061 187 1216 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Noklok the Bluntedge","color":"blue"},{"text":"> Monk duty is exhausting. We all have to climb on top of one another in a huge stack, and the Pebbos at the top have to see as much as they can before someone slips and the tower of Pebbos inevitably collapses.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
