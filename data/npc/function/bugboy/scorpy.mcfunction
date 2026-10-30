execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.bee.hurt neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Scorpy","color":"green"},{"text":"> I come to this shrine often to pray to our three goddesses: Advent, Burgeoning, and Decay. Each serves a vital, beautiful role in keeping this forest flourishing. Decay is not stronger than Advent, nor is Burgeoning stronger than Decay. Each holds the others in balance. If balance is to be restored to our forest, it will be according to their design.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
