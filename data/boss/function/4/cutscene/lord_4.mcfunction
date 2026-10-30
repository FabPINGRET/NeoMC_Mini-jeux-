playsound minecraft:entity.ravager.stunned neutral @a[tag=mg.flw] -10058 117 -355 3 1.4
tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Lord of Flame","color":"red"},{"text":"> I must return to ","color":"white"},{"text":"Valor Tower ","color":"red"},{"text":"quickly. If you can free the other ","color":"white"},{"text":"Lords","color":"gold"},{"text":", we might have a chance to reclaim these lands.","color":"white"},{"text":" ⇒","color":"light_purple"}]

# Every 5 full repeaters is 2 seconds. Every 1 repeater tick is 0.1 seconds
schedule function floaty:sched/boss/4/cutscene/lord_5 8s
