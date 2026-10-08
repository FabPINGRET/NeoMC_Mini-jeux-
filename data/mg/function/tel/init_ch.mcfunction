execute if score $tk mg.st >= $tn mg.st run return 0
data modify storage mg:tel ch append value {s0:"",s2:"",s4:""}
scoreboard players add $tk mg.st 1
function mg:tel/init_ch
