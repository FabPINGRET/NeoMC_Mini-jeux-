execute positioned -10060 115 332 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.spider.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 0.5
execute positioned -10060 115 332 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"The Eye in the Grove","color":"gold"},{"text":"> Now you will gi","color":"white","italic":false},{"text":"vvvvvvv","color":"gray","italic":true},{"text":"e your eyes to m","color":"white","italic":false},{"text":"eeeeeeee","color":"gray","italic":true},{"text":". I will t","color":"white","italic":false},{"text":"aaaaaaa","color":"gray","italic":true},{"text":"ke them!","color":"white","italic":false}]

schedule function floaty:sched/npc/overworld_cutscene/eye_in_the_grove/3 6s

spawnpoint @a[tag=mg.flw] -10060 116 322 0 0
scoreboard players set $flsp mg.st 28
setblock -10044 105 323 minecraft:redstone_block

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
