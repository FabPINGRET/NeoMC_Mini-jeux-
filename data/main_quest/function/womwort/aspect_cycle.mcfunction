fill ~-1 ~ ~1 ~-1 ~ ~1 white_wool replace minecraft:purple_wool
fill ~-1 ~ ~1 ~-1 ~ ~1 purple_wool replace minecraft:blue_wool
fill ~-1 ~ ~1 ~-1 ~ ~1 blue_wool replace minecraft:lime_wool
fill ~-1 ~ ~1 ~-1 ~ ~1 lime_wool replace minecraft:yellow_wool
fill ~-1 ~ ~1 ~-1 ~ ~1 yellow_wool replace minecraft:orange_wool
fill ~-1 ~ ~1 ~-1 ~ ~1 orange_wool replace minecraft:red_wool
fill ~-1 ~ ~1 ~-1 ~ ~1 red_wool replace minecraft:white_wool


execute if block ~-1 ~ ~1 red_wool run setblock ~2 ~ ~1 minecraft:pale_oak_wall_sign[facing=east,waterlogged=false]{back_text:{color:"black",has_glowing_text:0b,messages:["","","",""]},components:{},front_text:{color:"cyan",has_glowing_text:1b,messages:["","Twisting &","Rotating",""]},is_waxed:0b}
execute if block ~-1 ~ ~1 orange_wool run setblock ~2 ~ ~1 minecraft:pale_oak_wall_sign[facing=east,waterlogged=false]{back_text:{color:"black",has_glowing_text:0b,messages:["","","",""]},components:{},front_text:{color:"cyan",has_glowing_text:1b,messages:["","Forgetting","",""]},is_waxed:0b}
execute if block ~-1 ~ ~1 yellow_wool run setblock ~2 ~ ~1 minecraft:pale_oak_wall_sign[facing=east,waterlogged=false]{back_text:{color:"black",has_glowing_text:0b,messages:["","","",""]},components:{},front_text:{color:"cyan",has_glowing_text:1b,messages:["","Inventing","Discoveries",""]},is_waxed:0b}
execute if block ~-1 ~ ~1 lime_wool run setblock ~2 ~ ~1 minecraft:pale_oak_wall_sign[facing=east,waterlogged=false]{back_text:{color:"black",has_glowing_text:0b,messages:["","","",""]},components:{},front_text:{color:"cyan",has_glowing_text:1b,messages:["","Firm","Gripping",""]},is_waxed:0b}
execute if block ~-1 ~ ~1 blue_wool run setblock ~2 ~ ~1 minecraft:pale_oak_wall_sign[facing=east,waterlogged=false]{back_text:{color:"black",has_glowing_text:0b,messages:["","","",""]},components:{},front_text:{color:"cyan",has_glowing_text:1b,messages:["","Folding &","Kneading",""]},is_waxed:0b}
execute if block ~-1 ~ ~1 purple_wool run setblock ~2 ~ ~1 minecraft:pale_oak_wall_sign[facing=east,waterlogged=false]{back_text:{color:"black",has_glowing_text:0b,messages:["","","",""]},components:{},front_text:{color:"cyan",has_glowing_text:1b,messages:["","Snacks &","Treats",""]},is_waxed:0b}

execute if blocks 10659 78 -71 10659 79 -55 10657 78 -71 all run function main_quest:womwort/solve
