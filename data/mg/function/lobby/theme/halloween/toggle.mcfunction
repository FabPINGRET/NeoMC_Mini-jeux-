# Admin (mg.opt 73) : pose ou retire le décor 🎃 Halloween
function mg:lobby/theme/sync
execute if score $theme mg.st matches 1 run return run function mg:lobby/theme/off
function mg:lobby/theme/halloween/on
