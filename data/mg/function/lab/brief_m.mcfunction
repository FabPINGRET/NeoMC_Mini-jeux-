$title @a[tag=mg.lbw,scores={mg.lbp=$(p)}] title {"text":"🙈 Tu es AVEUGLE","color":"light_purple","bold":true}
$title @a[tag=mg.lbw,scores={mg.lbp=$(p)}] subtitle {"text":"écoute ton guide, trouve l'or","color":"gray"}
$title @a[tag=mg.lbg,scores={mg.lbp=$(p)}] title {"text":"👁 Tu es le GUIDE","color":"aqua","bold":true}
$title @a[tag=mg.lbg,scores={mg.lbp=$(p)}] subtitle {"text":"mène ton marcheur jusqu'à l'or (au vocal !)","color":"gray"}
$tellraw @a[scores={mg.lbp=$(p)},tag=mg.play] [{"text":"🙈 Paire $(p) : ","color":"light_purple","bold":true},{"text":"marcheur ","color":"gray"},{"selector":"@a[tag=mg.lbw,scores={mg.lbp=$(p)}]","color":"yellow"},{"text":" — guide ","color":"gray"},{"selector":"@a[tag=mg.lbg,scores={mg.lbp=$(p)}]","color":"aqua"},{"text":". Le premier marcheur sur le bloc d'or fait gagner sa paire !","color":"gray"}]
