execute if score BetterGuild bool matches 1 if block -12 93 74 yellow_wool run setblock -12 93 74 white_wool
execute if score BetterGuild bool matches 0 if block -12 93 74 red_wool run setblock -12 93 74 white_wool

execute if score BetterGuild bool matches 1 if block -12 93 74 black_wool run data merge block -13 93 75 {front_text:{messages:[{"text":"The Gill Guild","color":"white"},{"text":"is gathering","color":"white"},{"text":"intel on:","color":"white"},{"text":"LIBRARY BOOKS","color":"yellow","bold":true}]}}
execute if score BetterGuild bool matches 1 if block -12 93 74 black_wool run setblock -12 93 74 yellow_wool

execute if score BetterGuild bool matches 1 if block -12 93 74 light_blue_wool run data merge block -13 93 75 {front_text:{messages:[{"text":"The Gill Guild","color":"white"},{"text":"is gathering","color":"white"},{"text":"intel on:","color":"white"},{"text":"ABNORMAZOIDS","color":"black","bold":true}]}}
execute if score BetterGuild bool matches 1 if block -12 93 74 light_blue_wool run setblock -12 93 74 black_wool

execute if score BetterGuild bool matches 1 if block -12 93 74 brown_wool run data merge block -13 93 75 {front_text:{messages:[{"text":"The Gill Guild","color":"white"},{"text":"is gathering","color":"white"},{"text":"intel on:","color":"white"},{"text":"THE BARD","color":"aqua","bold":true}]}}
execute if score BetterGuild bool matches 1 if block -12 93 74 brown_wool run setblock -12 93 74 light_blue_wool

execute if score BetterGuild bool matches 1 if block -12 93 74 red_wool run data merge block -13 93 75 {front_text:{messages:[{"text":"The Gill Guild","color":"white"},{"text":"is gathering","color":"white"},{"text":"intel on:","color":"white"},{"text":"PATTERNS","color":"gold","bold":true}]}}
execute if score BetterGuild bool matches 1 if block -12 93 74 red_wool run setblock -12 93 74 brown_wool

execute if block -12 93 74 purple_wool run data merge block -13 93 75 {front_text:{messages:[{"text":"The Gill Guild","color":"white"},{"text":"is gathering","color":"white"},{"text":"intel on:","color":"white"},{"text":"LOVE QUESTS","color":"red","bold":true}]}}
execute if block -12 93 74 purple_wool run setblock -12 93 74 red_wool

execute if block -12 93 74 white_wool run data merge block -13 93 75 {front_text:{messages:[{"text":"The Gill Guild","color":"white"},{"text":"is gathering","color":"white"},{"text":"intel on:","color":"white"},{"text":"SECRET KEYS","color":"dark_purple","bold":true}]}}
execute if block -12 93 74 white_wool run setblock -12 93 74 purple_wool
