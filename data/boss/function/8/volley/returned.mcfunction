kill @e[tag=frostbyte_volley,distance=0..]
kill @e[tag=frostbyte_volley_pos,distance=0..]

#HURT
execute if score boss:fs_return Value matches 0 run setblock -10826 67 370 redstone_block

#RETURN
execute unless score boss:fs_return Value matches 0 run setblock -10826 67 367 redstone_block
