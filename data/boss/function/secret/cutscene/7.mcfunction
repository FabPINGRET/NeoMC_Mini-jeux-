# Every 5 full repeaters is 2 seconds. Every 1 repeater tick is 0.1 seconds
schedule function floaty:sched/boss/secret/cutscene/8 2s

scoreboard players set sc_boss_color bool 1
function boss:secret/toggle
function boss:secret/display/pose/release

bossbar set boss:secret players @a[tag=mg.flw]
function music:boss_fanfare
schedule function floaty:sched/music/dark_boss 45t replace

#","color":"white"},{"text":"
