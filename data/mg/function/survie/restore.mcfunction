# Retour en survie de @s (macro id) : position, XP, point de réapparition
data modify storage mg:survie g set value {d:"mg:survie",ya:0f,pi:0f}
$data modify storage mg:survie g.x set from storage mg:survie p.k$(id).pos[0]
$data modify storage mg:survie g.y set from storage mg:survie p.k$(id).pos[1]
$data modify storage mg:survie g.z set from storage mg:survie p.k$(id).pos[2]
$data modify storage mg:survie g.ya set from storage mg:survie p.k$(id).rot[0]
$data modify storage mg:survie g.pi set from storage mg:survie p.k$(id).rot[1]
$data modify storage mg:survie g.d set from storage mg:survie p.k$(id).dim
function mg:survie/goto with storage mg:survie g
data modify storage mg:survie xp set value {l:0,p:0}
$data modify storage mg:survie xp.l set from storage mg:survie p.k$(id).xpl
$data modify storage mg:survie xp.p set from storage mg:survie p.k$(id).xpp
function mg:survie/xp_set with storage mg:survie xp
$function mg:survie/resp_restore {id:$(id)}
