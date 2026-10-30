execute as @n[tag=cob_boss_cutscene,distance=0..] at @s run playsound minecraft:entity.skeleton.hurt neutral @a[tag=mg.flw] ~ ~ ~ 3 0.7
tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Bone Nexus","color":"gray"},{"text":"> Even still, she's gonna burn you to the bone, hero.","color":"white"},{"text":" ⇒","color":"light_purple"}]
function music:boss_intro

# Every 5 full repeaters is 2 seconds. Every 1 repeater tick is 0.1 seconds
schedule function floaty:sched/boss/2/cutscene/9 5s
