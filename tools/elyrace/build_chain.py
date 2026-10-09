"""Construction des parcours en tranches (chargees de force une a une, remplies, puis liberees) : fonctions
mg:elyrace/c<N>/{build, build_start, build_wait, build_<i>, loaded_<i>} propres a chaque parcours (plus clear_<i> si le
parcours declare CLEAR_Y : nettoyage de la tranche par passes avant de la construire), et mg:elyrace/{build, build_next,
build_abort} communes. Les parcours se construisent l'un apres l'autre : la derniere
tranche de chacun pose son drapeau (spec.FLAG, stockage mg:elyrace), puis appelle build_next.
Python stdlib uniquement (compatible 3.8).
"""
import course_common as CC
import terrain as T

SLICE = 96                          # largeur d'une tranche de construction (6 chunks)
SLICE_BUDGET = 20000                # commandes par tranche (limite de la chaine de commandes : 65 536)
CLEAR_STEP = 16                     # hauteur d'une passe de nettoyage (blocs) : une tranche de 96 x 16 x ~300 = ~0,5 M blocs par tick
PROBE_Y = 310                       # au-dessus de tout decor : jamais de bedrock a cette altitude
IN_GAME = 'execute if score $game mg.st matches 66 unless score $state mg.st matches 0 run '    # une course tourne : sa zone de depart est chargee par fl_add
BUSY = 'execute unless score $state mg.st matches 0 run '      # une partie quelconque tourne (course, autre jeu) : la construction attend
SOLO_BUSY = 'execute if entity @a[tag=mg.xso] run '            # un contre-la-montre solo tourne (il ne passe pas par $state) : la construction attend aussi
SOLO_REFUSAL = SOLO_BUSY + 'return run tellraw @a[tag=mg.admin] [{"text":"[Mini-Jeux] Course d\'élytres : construction impossible pendant un contre-la-montre solo.","color":"red"}]'


def wait_lines(ret):
    """Les deux gardes d'attente (partie en cours, solo en cours) : chacune renvoie `ret` (une commande a faire a la place de construire)."""
    return [BUSY + 'return run ' + ret, SOLO_BUSY + 'return run ' + ret]


def n_slices(spec):
    return (spec.X1 - spec.X0) // SLICE


def slice_box(spec, k):
    xa = spec.X0 + SLICE * (k - 1)
    return xa, xa + SLICE - 1


def slice_commands(c, k):
    """Commandes de la tranche k : relief puis decors, restreints a la tranche, fills decoupes a 32 768 blocs."""
    xa, xb = slice_box(c.spec, k)
    out = []
    for cmd in [('fill',) + tuple(r) for r in c.rects] + list(c.world.cmds):
        cl = T.clip_cmd(cmd, xa, xb)
        if cl is None:
            continue
        for part in (T.split_fill(cl) if cl[0] == 'fill' else [cl]):
            out.append(T.cmd_text(part))
    return out


def clear_passes(spec):
    """Passes de nettoyage d'un parcours qui declare CLEAR_Y : [(y bas, y haut)] de CLEAR_STEP blocs."""
    lo, hi = spec.CLEAR_Y
    return [(y, min(y + CLEAR_STEP - 1, hi)) for y in range(lo, hi + 1, CLEAR_STEP)]


def forceload(op, spec, k):
    xa, xb = slice_box(spec, k)
    return 'forceload %s %d %d %d %d' % (op, xa, spec.Z0, xb, spec.Z1 - 1)


def loaded_lines(spec, k):
    xa, xb = slice_box(spec, k)
    out = ['# Tranche %d : tous les chunks sont chargés ? Même motif que mg:dropadv/loaded_all : « unless block … bedrock » ne réussit' % k,
           '# que si le chunk est chargé (il n\'y a jamais de bedrock à y %d) ; sinon le score reste à 0 et la fonction échoue' % PROBE_Y]
    for x in range(xa + 8, xb + 1, 16):
        for z in range(spec.Z0 + 8, spec.Z1, 16):
            out.append('execute store success score $xbl mg.st unless block %d %d %d minecraft:bedrock' % (x, PROBE_Y, z))
            out.append('execute if score $xbl mg.st matches 0 run return fail')
    out.append('return 1')
    return out


def clear_lines(spec, k):
    """c<N>/clear_<k> : nettoie la tranche k (fill air strict sur toute la bande z) par passes, une par tick ($xcp = numero de la
    passe, 0 = pas commence) ; la derniere passe appelle build_<k>. Un parcours reconstruit sur une ancienne version n'en garde
    aucun reste. Une partie qui demarre suspend le nettoyage (comme build_wait) ; la chaine s'arrete avec build_abort / uninstall."""
    xa, xb = slice_box(spec, k)
    me, passes = CC.fn(spec, 'clear_%d' % k), clear_passes(spec)
    out = ['# Tranche %d du parcours %d : nettoyage en %d passes de %d blocs de haut (y %d à %d), une par tick, puis construction (build_%d)'
           % (k, spec.NUM, len(passes), CLEAR_STEP, spec.CLEAR_Y[0], spec.CLEAR_Y[1], k),
           '# $xcp = passe en cours (0 = pas commencée) ; build_abort remet $xcp à 0 et arrête la suite (schedule clear), uninstall arrête la suite',
           '# « strict » : pas de mise à jour des voisins, les rails ne tombent pas en objets ; les objets éventuels sont tués avant la construction',
           '# une partie démarre (ou un solo) : on suspend le nettoyage (et la construction qui suit) jusqu\'à ce que $state revienne à 0 et que les solos finissent']
    out += wait_lines('schedule function %s 20t' % me)
    out += ['execute if score $xcp mg.st matches 0 run scoreboard players set $xcp mg.st 1']
    for p, (ya, yb) in enumerate(passes, 1):
        for part in T.split_fill(('fill', xa, ya, spec.Z0, xb, yb, spec.Z1 - 1, 'air strict')):
            out.append('execute if score $xcp mg.st matches %d run %s' % (p, T.cmd_text(part)))
    lo, hi = spec.CLEAR_Y
    out += ['scoreboard players add $xcp mg.st 1',
            'execute if score $xcp mg.st matches ..%d run return run schedule function %s 1t' % (len(passes), me),
            'scoreboard players set $xcp mg.st 0',
            'kill @e[type=item,x=%d,y=%d,z=%d,dx=%d,dy=%d,dz=%d]' % (xa, lo, spec.Z0, xb - xa, hi - lo, spec.Z1 - 1 - spec.Z0),
            'function ' + CC.fn(spec, 'build_%d' % k)]
    return out


def course_build_lines(spec):
    """c<N>/build (OP) : reconstruit ce parcours seul."""
    return ['# (OP) Reconstruit le parcours %d (%s) seul, en %d tranches de %d blocs (chargées de force une à une)' % (spec.NUM, spec.NAME, n_slices(spec), SLICE),
            '# pas pendant une partie de la course : build_abort libérerait la zone de départ chargée par fl_add',
            IN_GAME + 'return run tellraw @a[tag=mg.admin] [{"text":"[Mini-Jeux] Course d\'élytres : construction impossible pendant une partie.","color":"red"}]',
            '# ni pendant un contre-la-montre solo (il se joue sur ce parcours et ne passe pas par $state)',
            SOLO_REFUSAL,
            'function mg:elyrace/build_abort',
            'data remove storage mg:elyrace ' + spec.FLAG,
            'function ' + CC.fn(spec, 'build_start')]


def build_start_lines(spec):
    out = ['# Démarre la construction du parcours %d : tranche 1 chargée de force, la suite est enchaînée par build_wait' % spec.NUM,
           'scoreboard players set $xbk mg.st 1',
           'scoreboard players set $xbw mg.st 0']
    if hasattr(spec, 'CLEAR_Y'):
        out.append('scoreboard players set $xcp mg.st 0')
    return out + [forceload('add', spec, 1), 'schedule function %s 20t' % CC.fn(spec, 'build_wait')]


def build_wait_lines(spec):
    me = CC.fn(spec, 'build_wait')
    out = ['# Attend le chargement de la tranche $xbk puis la construit (parcours %d)' % spec.NUM,
           '# $xbk à 0 = aucune construction en cours (arrêtée par build_abort, build_fail ou core/load) : un schedule resté en attente s\'éteint ici',
           'execute if score $xbk mg.st matches 0 run return 0',
           '# une partie démarre pendant la construction (course, solo ou autre jeu) : on ne construit pas (les remplissages sont lourds) et $xbw',
           '# n\'avance pas (pas de faux build_fail). Choix assumé : la tranche en cours reste chargée de force pendant la pause (la relâcher puis',
           '# la recharger ferait ré-attendre le chargement) ; la pause dure autant que la partie, jusqu\'à ce que $state revienne à 0',
           '# et que les solos soient finis (un solo ne passe pas par $state : garde propre, SOLO_BUSY)']
    out += wait_lines('schedule function %s 20t' % me)
    first = 'clear_%d' if hasattr(spec, 'CLEAR_Y') else 'build_%d'           # nettoyage d'abord, s'il y en a un
    for k in range(1, n_slices(spec) + 1):
        out.append('execute if score $xbk mg.st matches %d if function %s run return run function %s'
                   % (k, CC.fn(spec, 'loaded_%d' % k), CC.fn(spec, first % k)))
    out += ['scoreboard players add $xbw mg.st 1',
            '# 2 minutes sans chargement : message, puis on libère les chargements forcés des tranches et on s\'arrête',
            'execute if score $xbw mg.st matches 120.. run tellraw @a[tag=mg.admin] [{"text":"[Mini-Jeux] Course d\'élytres : zone pas chargée (parcours %d, tranche ","color":"red"},{"score":{"name":"$xbk","objective":"mg.st"},"color":"red"},{"text":"). Relance /function mg:elyrace/c%d/build.","color":"red"}]'
            % (spec.NUM, spec.NUM),
            'execute if score $xbw mg.st matches 120.. run return run function ' + CC.fn(spec, 'build_fail'),
            'schedule function %s 20t' % me]
    return out


def build_fail_lines(spec):
    """c<N>/build_fail : abandon d'une construction (délai de chargement dépassé). Ne libère que les tranches de CE parcours :
    build_abort (global) libérerait aussi la zone chargée par le fl_add d'une partie en cours."""
    out = ['# Abandon de la construction du parcours %d : libère les chargements forcés de ses tranches seulement, puis rétablit ceux du jeu' % spec.NUM]
    out += [forceload('remove', spec, k) for k in range(1, n_slices(spec) + 1)]
    out += ['# $xbk revient à 0 : build_next peut de nouveau construire (le drapeau du parcours n\'est pas posé)',
            'scoreboard players set $xbk mg.st 0',
            'function mg:core/forceloads',
            '# la tranche 1 recouvre la zone de départ : si une partie se joue sur ce parcours, son fl_add est rétabli',
            IN_GAME + 'execute if score $xc mg.st matches %d run function %s' % (spec.NUM, CC.fn(spec, 'fl_add')),
            '# nouvel essai dans 5 minutes (build_next : premier parcours sans drapeau ; reporté tant qu\'une partie se joue)',
            'schedule function mg:elyrace/build_next 300s']
    return out


def slice_lines(c, k):
    spec, n = c.spec, n_slices(c.spec)
    out = ['# Course d\'élytres : parcours %d, tranche %d / %d (x %d à %d)' % ((spec.NUM, k, n) + slice_box(spec, k))] + slice_commands(c, k)
    out.append(forceload('remove', spec, k))
    if k < n:
        out += ['scoreboard players set $xbk mg.st %d' % (k + 1), 'scoreboard players set $xbw mg.st 0',
                forceload('add', spec, k + 1), 'schedule function %s 20t' % CC.fn(spec, 'build_wait')]
    else:
        out += ['function mg:core/forceloads', 'data modify storage mg:elyrace %s set value 1b' % spec.FLAG,
                'tellraw @a[tag=mg.admin] [{"text":"[Mini-Jeux] ","color":"gold"},{"text":"Course d\'élytres : %s construit.","color":"green"}]' % spec.NAME,
                '# construction terminée : $xbk à 0 (sinon build_next se croirait encore en construction), puis parcours suivant s\'il en reste un',
                'scoreboard players set $xbk mg.st 0',
                'function mg:elyrace/build_next']
    return out


def course_files(c):
    """Fonctions de construction d'un parcours : {nom relatif a c<N>/: lignes}."""
    spec = c.spec
    fns = {'build': course_build_lines(spec), 'build_start': build_start_lines(spec), 'build_wait': build_wait_lines(spec),
           'build_fail': build_fail_lines(spec)}
    for k in range(1, n_slices(spec) + 1):
        fns['build_%d' % k] = slice_lines(c, k)
        if hasattr(spec, 'CLEAR_Y'):
            fns['clear_%d' % k] = clear_lines(spec, k)
        fns['loaded_%d' % k] = loaded_lines(spec, k)
    return fns


def common_files(specs):
    """build (OP, tout reconstruire), build_next, build_abort."""
    flags = ' '.join('if data storage mg:elyrace %s' % s.FLAG for s in specs)
    next_ = ['# Lance la construction du premier parcours pas encore construit (drapeau absent) ; rien à faire quand tous le sont',
             'execute %s run return 0' % flags,
             '# une construction tourne déjà ($xbk = tranche en cours, 0 sinon : posé par build_start, remis à 0 par la dernière tranche,',
             '# build_fail et build_abort ; core/load le remet à 0 au chargement) : la dernière tranche rappellera build_next',
             'execute if score $xbk mg.st matches 1.. run return 0',
             '# pas pendant une partie ni un solo : on réessaie dans une minute (build_abort libérerait la zone de départ chargée par fl_add)']
    next_ += wait_lines('schedule function mg:elyrace/build_next 60s')
    next_ +=['execute unless data storage mg:elyrace %s run return run function %s' % (s.FLAG, CC.fn(s, 'build_start')) for s in specs]
    abort = ['# Arrête la construction : libère les chargements forcés des tranches de tous les parcours puis rétablit ceux du jeu',
             'schedule clear mg:elyrace/build', 'schedule clear mg:elyrace/build_next']
    abort += ['schedule clear ' + CC.fn(s, 'build_wait') for s in specs]
    abort += ['schedule clear ' + CC.fn(s, 'clear_%d' % k) for s in specs if hasattr(s, 'CLEAR_Y') for k in range(1, n_slices(s) + 1)]
    if any(hasattr(s, 'CLEAR_Y') for s in specs):
        abort.append('scoreboard players set $xcp mg.st 0')
    abort += [forceload('remove', s, k) for s in specs for k in range(1, n_slices(s) + 1)]
    abort += ['scoreboard players set $xbk mg.st 0', 'function mg:core/forceloads']
    build = ['# (OP) Reconstruit tous les parcours, l\'un après l\'autre (chacun en tranches chargées de force)',
             '# pas pendant une partie de la course : build_abort libérerait la zone de départ chargée par fl_add',
             IN_GAME + 'return run tellraw @a[tag=mg.admin] [{"text":"[Mini-Jeux] Course d\'élytres : construction impossible pendant une partie.","color":"red"}]',
             '# ni pendant un contre-la-montre solo (il ne passe pas par $state)',
             SOLO_REFUSAL,
             'function mg:elyrace/build_abort', 'function mg:elyrace/forget', 'function mg:elyrace/build_next']
    return {'build': build, 'build_next': next_, 'build_abort': abort}
