# Admin (mg.opt 74) : pose ou retire le décor 🎄 Noël
function mg:lobby/theme/sync
execute if score $theme mg.st matches 2 run return run function mg:lobby/theme/off
function mg:lobby/theme/noel/on
