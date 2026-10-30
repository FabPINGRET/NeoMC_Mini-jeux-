fill ~ ~1 ~ ~ ~2 ~ diorite_wall
setblock ~ ~3 ~ deepslate_lapis_ore
setblock ~ ~-1 ~ minecraft:repeating_command_block[conditional=false,facing=down]{Command:"execute positioned ~ ~2.5 ~ if entity @e[type=minecraft:lightning_bolt,distance=..1.5] run setblock ~ ~-4.5 ~ minecraft:redstone_block",CustomName:'"@"',LastExecution:69767747L,SuccessCount:0,TrackOutput:1b,UpdateLastExecution:1b,auto:0b,conditionMet:1b,powered:1b}
setblock ~ ~-2 ~ redstone_block
setblock ~ ~-3 ~ air
setblock ~ ~-4 ~ minecraft:command_block[conditional=false,facing=down]{Command:"setblock ~ ~2 ~ air",CustomName:'"@"',TrackOutput:1b,UpdateLastExecution:1b,auto:0b,conditionMet:1b,powered:0b}
setblock ~ ~-5 ~ minecraft:chain_command_block[conditional=false,facing=down]{Command:"setblock ~ ~8 ~ minecraft:lapis_ore",CustomName:'"@"',TrackOutput:1b,UpdateLastExecution:1b,auto:1b,conditionMet:1b,powered:0b}
setblock ~ ~-6 ~ minecraft:chain_command_block[conditional=false,facing=down]{Command:"particle minecraft:end_rod ~ ~9 ~ 0.2 0.2 0.2 0.1 50 force",CustomName:'"@"',TrackOutput:1b,UpdateLastExecution:1b,auto:1b,conditionMet:1b,powered:0b}
setblock ~ ~-7 ~ minecraft:chain_command_block[conditional=false,facing=down]{Command:"playsound minecraft:block.respawn_anchor.charge block @a[tag=mg.flw] ~ ~11 ~ 2 2",CustomName:'"@"',TrackOutput:1b,UpdateLastExecution:1b,auto:1b,conditionMet:1b,powered:0b}
setblock ~ ~-8 ~ minecraft:chain_command_block[conditional=false,facing=down]{Command:"setblock ~ ~12 ~ light[level=15]",CustomName:'"@"',TrackOutput:1b,UpdateLastExecution:1b,auto:1b,conditionMet:1b,powered:0b}
setblock ~ ~ ~ diamond_block
