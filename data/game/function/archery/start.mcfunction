scoreboard players set archery_going bool 1
scoreboard players set archery_frame Value 0
scoreboard players set archery_points Value 0

scoreboard players set archery_timer_tick Value 1219
scoreboard players set archery_timer_second Value 60

function game:archery/next_frame
setblock 113 40 166 air
setblock 114 34 165 redstone_block

summon text_display 113 41 167 {NoGravity:1b,Silent:1b,billboard:"center",Tags:["archery_scoreboard"],brightness:{sky:15,block:15},text:{"score":{"name":"archery_timer_second","objective":"Value"}}}
