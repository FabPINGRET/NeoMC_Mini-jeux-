# Match gagné (3 manches) : le gagnant porte mg.dlwn, $dli = arène
tellraw @a [{"text":"⚔ ","color":"gold"},{"selector":"@a[tag=mg.dlwn,limit=1]","color":"yellow","bold":true},{"text":" bat ","color":"gray"},{"selector":"@a[tag=mg.dlsp,tag=!mg.dlwn,limit=1]","color":"red"},{"text":" en duel sniper : ","color":"gray"},{"score":{"name":"@a[tag=mg.dlwn,limit=1]","objective":"mg.dlr"},"color":"gold"},{"text":" - ","color":"gray"},{"score":{"name":"@a[tag=mg.dlsp,tag=!mg.dlwn,limit=1]","objective":"mg.dlr"},"color":"red"}]
function mg:duel/end
