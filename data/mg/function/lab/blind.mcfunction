# Écran noir du marcheur (glyphe du resource pack, renvoyé en titre toutes les secondes ; sans pack : aveuglement seul)
execute unless score $rp mg.st matches 1 run return 0
title @a[tag=mg.lbw,tag=mg.play] times 0 30 0
title @a[tag=mg.lbw,tag=mg.play] title {"text":"\ue300","font":"mg:lab"}
