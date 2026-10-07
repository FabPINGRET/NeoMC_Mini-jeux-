# @s (pilote du spawn) garde son kart et sa caméra (pas orphelins)
function mg:kart/kk
tag @e[tag=mg.kk] remove mg.lko
tag @e[tag=mg.kcamc] remove mg.lko
tag @e[tag=mg.kk] remove mg.kk
tag @e[tag=mg.kcamc] remove mg.kcamc
