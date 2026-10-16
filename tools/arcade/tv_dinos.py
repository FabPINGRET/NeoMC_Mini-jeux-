"""🦖 Terra Nova : espèces de dinosaures (données partagées par gen_terranova.py et tools/resourcepack/dino_rp.py).

Chaque espèce = un mob vanilla invisible (le « corps » qui marche, attaque, encaisse) + un modèle articulé :
- avec le resource pack ($rp = 1) : une item_display par os (corps, cou, tête, mâchoire, queue ×2, pattes…), modèles 3D
  mg:dino/<espèce>_<os>, animés (repos, marche, attaque, rugissement) par des poses précalculées ici ;
- sans le resource pack : les mêmes boîtes en block_display (blocs colorés, pose de repos, sans animation).

Repère : en blocs, pieds du mob à l'origine, +z = avant, +y = haut. Un os a une articulation (joint, coordonnées dans le repère
de son parent au repos), une rotation de repos, des boîtes (dans son propre repère) et un type d'animation.
"""
import math

FRAMES = 8                      # images par cycle
STATES = ('idle', 'walk', 'atk', 'roar')


# ---------------------------------------------------------------- quaternions (x, y, z, w)
def qmul(a, b):
    ax, ay, az, aw = a
    bx, by, bz, bw = b
    return (aw * bx + ax * bw + ay * bz - az * by,
            aw * by - ax * bz + ay * bw + az * bx,
            aw * bz + ax * by - ay * bx + az * bw,
            aw * bw - ax * bx - ay * by - az * bz)


def qaxis(ax, deg):
    h = math.radians(deg) / 2
    s = math.sin(h)
    return {'x': (s, 0, 0, math.cos(h)), 'y': (0, s, 0, math.cos(h)), 'z': (0, 0, s, math.cos(h))}[ax]


def qeuler(rx=0, ry=0, rz=0):
    """Rotation locale : lacet (y), puis tangage (x), puis roulis (z)."""
    return qmul(qmul(qaxis('y', ry), qaxis('x', rx)), qaxis('z', rz))


def qrot(q, v):
    x, y, z, w = q
    vx, vy, vz = v
    # v' = q v q*
    ix = w * vx + y * vz - z * vy
    iy = w * vy + z * vx - x * vz
    iz = w * vz + x * vy - y * vx
    iw = -x * vx - y * vy - z * vz
    return (ix * w + iw * -x + iy * -z - iz * -y,
            iy * w + iw * -y + iz * -x - ix * -z,
            iz * w + iw * -z + ix * -y - iy * -x)


def vadd(a, b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])


# ---------------------------------------------------------------- os et espèces
class Bone:
    def __init__(self, name, parent, joint, rest=(0, 0, 0), anim=None, boxes=None, amp=1.0, phase=0.0):
        self.name, self.parent, self.joint, self.rest = name.lower(), parent and parent.lower(), joint, rest
        self.anim, self.amp, self.phase = anim, amp, phase
        self.boxes = boxes or []          # (x1, y1, z1, x2, y2, z2, matière)

    def box(self, x1, y1, z1, x2, y2, z2, m):
        self.boxes.append((min(x1, x2), min(y1, y2), min(z1, z2), max(x1, x2), max(y1, y2), max(z1, z2), m))
        return self


class Species:
    def __init__(self, key, label, color, mats, bones, scale=1.0):
        self.key, self.label, self.color, self.mats = key, label, color, mats
        self.bones = bones
        self.scale = scale
        self.by = {b.name: b for b in bones}

    def bone(self, name):
        return self.by[name.lower()]


# ---------------------------------------------------------------- animations (rotation locale en degrés selon l'état et l'image)
def _s(f, ph=0.0, per=FRAMES):
    return math.sin(2 * math.pi * f / per + ph)


def anim_rot(b, st, f):
    """Rotation d'animation (rx, ry, rz) en degrés et décalage vertical (bob) de l'os b."""
    a, A, ph = b.anim, b.amp, b.phase
    if a is None:
        return (0, 0, 0), 0
    if a == 'body':
        if st == 'walk':
            return (0, 0, 0), 0.035 * A * abs(_s(f))
        if st == 'roar':
            return (-6 * A, 0, 0), 0.05 * A
        if st == 'atk':
            return (4 * A, 0, 0), -0.03 * A
        return (0, 0, 0), 0.012 * A * _s(f)
    if a in ('leg', 'arm'):
        if st == 'walk':
            return (30 * A * _s(f, ph), 0, 0), 0
        if st == 'atk' and a == 'arm':
            return (-45 * A, 0, 0), 0
        if st == 'roar' and a == 'arm':
            return (-25 * A, 0, 0), 0
        return (0, 0, 0), 0
    if a == 'knee':                               # suit le pas : pliée quand la patte revient vers l'avant
        if st == 'walk':
            return (-35 * A * max(0.0, _s(f, ph + math.pi / 2)), 0, 0), 0
        return (0, 0, 0), 0
    if a == 'tail':
        if st == 'walk':
            return (2 * A * _s(f, ph, FRAMES / 2), 12 * A * _s(f, ph), 0), 0
        if st == 'atk':
            return (-6 * A, 16 * A * _s(f, ph), 0), 0
        if st == 'roar':
            return (-10 * A, 6 * A * _s(f, ph), 0), 0
        return (-1.5 * A * _s(f, ph), 6 * A * _s(f, ph), 0), 0
    if a == 'neck':
        if st == 'walk':
            return (4 * A * _s(f, ph, FRAMES / 2), 3 * A * _s(f, ph), 0), 0
        if st == 'atk':
            return (14 * A + 6 * A * _s(f, 0, FRAMES / 2), 0, 0), 0
        if st == 'roar':
            return (-22 * A, 4 * A * _s(f), 0), 0
        return (2 * A * _s(f, ph), 5 * A * _s(f, ph + 1), 0), 0
    if a == 'head':
        if st == 'atk':
            return (10 * A, 0, 0), 0
        if st == 'roar':
            return (-14 * A, 0, 0), 0
        return (0, 0, 0), 0
    if a == 'jaw':
        if st == 'atk':
            return (34 * A * abs(_s(f, 0, FRAMES)), 0, 0), 0
        if st == 'roar':
            return (40 * A + 4 * A * _s(f), 0, 0), 0
        if st == 'idle':
            return (3 * A * max(0.0, _s(f)), 0, 0), 0
        return (0, 0, 0), 0
    if a in ('wingL', 'wingR'):
        sg = 1 if a == 'wingL' else -1
        if st in ('walk', 'atk'):
            return (0, 0, sg * 38 * A * _s(f, ph)), 0
        if st == 'roar':
            return (0, 0, sg * 25 * A), 0
        return (0, 0, sg * 12 * A * _s(f, ph)), 0
    if a in ('frillL', 'frillR'):
        sg = 1 if a == 'frillL' else -1
        if st in ('atk', 'roar'):
            return (0, sg * -8 * A, sg * -70 * A), 0     # collerette déployée
        return (0, 0, 0), 0
    raise ValueError(a)


def poses(sp, st, f):
    """Pose de chaque os : {nom: (position de l'articulation, quaternion)} dans le repère du mob."""
    out = {}
    for b in sp.bones:
        r, bob = anim_rot(b, st, f)
        local = qeuler(b.rest[0] + r[0], b.rest[1] + r[1], b.rest[2] + r[2])   # lacet, tangage, roulis cumulés (pas de roulis parasite)
        if b.parent is None:
            pos, q = vadd(b.joint, (0, bob, 0)), local
        else:
            ppos, pq = out[b.parent]
            pos, q = vadd(ppos, qrot(pq, b.joint)), qmul(pq, local)
        out[b.name] = (pos, q)
    return out


def bone_extent(b):
    e = 0.0
    for x1, y1, z1, x2, y2, z2, _ in b.boxes:
        e = max(e, abs(x1), abs(x2), abs(y1), abs(y2), abs(z1), abs(z2))
    return e


def bone_scale(b):
    """Échelle d'affichage de l'os : le modèle doit tenir dans ±1,5 bloc autour de l'articulation (limites -16..32 du format)."""
    return max(1.0, math.ceil(bone_extent(b) / 1.45 * 4) / 4)


# ---------------------------------------------------------------- gabarits
def theropod(key, label, color, mats, s=1.0, body=(0.5, 0.55, 1.1), hip=0.95, neck=(0.26, 0.5, 40), head=(0.34, 0.3, 0.62),
             tail=(0.3, 1.7), leg=0.2, arm=(0.08, 0.32), crest=None, horns=None, sail=None, spikes=False, frill=False,
             dome=False, beak=False, small_arms=False, long_snout=False, extra=None):
    """Bipède : raptor, carnotaure, dilophosaure, T-Rex, spinosaure, gallimimus, compsognathus, pachycéphalosaure."""
    bw, bh, bl = (v * s for v in body)
    nw, nl, nang = neck[0] * s, neck[1] * s, neck[2]
    hw, hh, hl = (v * s for v in head)
    tw, tl = tail[0] * s, tail[1] * s
    H = hip * s
    lw = leg * s
    aw, al = arm[0] * s, arm[1] * s
    B = []
    body_b = Bone('body', None, (0, H, 0), anim='body')
    body_b.box(-bw / 2, -bh * 0.42, -bl * 0.38, bw / 2, -bh * 0.05, bl * 0.62, 'belly')
    body_b.box(-bw / 2 - 0.004, -bh * 0.05, -bl * 0.4, bw / 2 + 0.004, bh * 0.55, bl * 0.6, 'skin')
    body_b.box(-bw * 0.22, bh * 0.55, -bl * 0.36, bw * 0.22, bh * 0.6, bl * 0.56, 'stripe')
    if spikes:
        for i in range(4):
            z = -bl * 0.3 + i * bl * 0.25
            body_b.box(-0.03 * s, bh * 0.6, z, 0.03 * s, bh * 0.6 + 0.14 * s, z + 0.1 * s, 'dark')
    if sail:
        sh = sail * s
        body_b.box(-0.035 * s, bh * 0.58, -bl * 0.3, 0.035 * s, bh * 0.58 + sh * 0.75, bl * 0.5, 'sail')
        body_b.box(-0.03 * s, bh * 0.58 + sh * 0.75, -bl * 0.15, 0.03 * s, bh * 0.58 + sh, bl * 0.35, 'sail')
        body_b.box(-0.04 * s, bh * 0.58 + sh * 0.95, -bl * 0.12, 0.04 * s, bh * 0.58 + sh * 1.02, bl * 0.32, 'dark')
    B.append(body_b)
    # cou + tête + mâchoire
    neck_b = Bone('neck', 'body', (0, bh * 0.32, bl * 0.52), rest=(-nang, 0, 0), anim='neck')
    neck_b.box(-nw / 2, -nw / 2, -nw * 0.3, nw / 2, nw / 2, nl, 'skin')
    neck_b.box(-nw * 0.38, -nw / 2 - 0.01, 0, nw * 0.38, -nw * 0.2, nl * 0.95, 'belly')
    if spikes:
        neck_b.box(-0.025 * s, nw / 2, nl * 0.2, 0.025 * s, nw / 2 + 0.12 * s, nl * 0.32, 'dark')
        neck_b.box(-0.025 * s, nw / 2, nl * 0.6, 0.025 * s, nw / 2 + 0.1 * s, nl * 0.72, 'dark')
    B.append(neck_b)
    head_b = Bone('head', 'neck', (0, 0, nl), rest=(nang * 0.95, 0, 0), anim='head')
    sn = 0.62 if not long_snout else 0.45
    head_b.box(-hw / 2, -hh * 0.25, -hh * 0.35, hw / 2, hh * 0.7, hl * sn, 'skin')
    head_b.box(-hw * 0.36, -hh * 0.25, hl * sn, hw * 0.36, hh * (0.42 if not beak else 0.3), hl, 'skin' if not beak else 'beak')
    head_b.box(-hw / 2 - 0.012, hh * 0.32, hl * (sn - 0.22), hw / 2 + 0.012, hh * 0.5, hl * (sn - 0.08), 'eye')
    if not beak:
        head_b.box(-hw * 0.33, -hh * 0.31, hl * 0.4, hw * 0.33, -hh * 0.24, hl * 0.97, 'teeth')
    head_b.box(-hw * 0.2, hh * 0.69, -hh * 0.2, hw * 0.2, hh * 0.74, hl * sn * 0.9, 'stripe')
    if crest:                                   # dilophosaure : deux crêtes
        for sx in (-1, 1):
            head_b.box(sx * hw * 0.12, hh * 0.7, -hh * 0.1, sx * hw * 0.2, hh * 0.7 + crest * s, hl * 0.75, 'crest')
    if horns:                                   # carnotaure : cornes au-dessus des yeux
        for sx in (-1, 1):
            head_b.box(sx * hw * 0.28, hh * 0.68, hl * 0.12, sx * hw * 0.5, hh * 0.68 + horns * s, hl * 0.3, 'horn')
    if dome:                                    # pachycéphalosaure : dôme osseux
        head_b.box(-hw * 0.55, hh * 0.55, -hh * 0.45, hw * 0.55, hh * 1.15, hl * 0.45, 'dome')
        head_b.box(-hw * 0.6, hh * 0.45, -hh * 0.55, hw * 0.6, hh * 0.65, hl * 0.25, 'dark')
    if spikes:
        head_b.box(-hw * 0.3, hh * 0.7, -hh * 0.3, -hw * 0.18, hh * 0.95, hl * 0.1, 'dark')
        head_b.box(hw * 0.18, hh * 0.7, -hh * 0.3, hw * 0.3, hh * 0.95, hl * 0.1, 'dark')
    B.append(head_b)
    jaw_b = Bone('jaw', 'head', (0, -hh * 0.25, -hh * 0.2), anim='jaw')
    jaw_b.box(-hw * 0.4, -hh * 0.32, 0, hw * 0.4, 0, hl * (0.95 if not beak else 0.85), 'belly' if not beak else 'beak')
    if not beak:
        jaw_b.box(-hw * 0.3, 0, hl * 0.45, hw * 0.3, 0.05 * s, hl * 0.9, 'teeth')
    B.append(jaw_b)
    if frill:                                   # dilophosaure : collerette repliée le long du cou
        for nm_, sx in (('frillL', 1), ('frillR', -1)):
            fb = Bone(nm_, 'neck', (sx * nw * 0.5, 0, nl * 0.8), anim=nm_)
            fb.box(0, -nw * 0.9, -nl * 0.35, sx * 0.03 * s, nw * 0.9, 0.0, 'frill')
            fb.box(0, -nw * 0.6, -nl * 0.3, sx * 0.04 * s, nw * 0.6, -nl * 0.05, 'stripe')
            B.append(fb)
    # queue
    tail_b = Bone('tail', 'body', (0, bh * 0.22, -bl * 0.38), rest=(4, 0, 0), anim='tail')
    tail_b.box(-tw / 2, -tw / 2, -tl * 0.52, tw / 2, tw / 2, 0.05, 'skin')
    tail_b.box(-tw * 0.3, tw / 2, -tl * 0.5, tw * 0.3, tw / 2 + 0.02, 0, 'stripe')
    if sail:
        tail_b.box(-0.03 * s, tw / 2, -tl * 0.4, 0.03 * s, tw / 2 + sail * s * 0.3, -0.02, 'sail')
    B.append(tail_b)
    tail2 = Bone('tail2', 'tail', (0, 0, -tl * 0.5), rest=(3, 0, 0), anim='tail', amp=1.5, phase=-0.9)
    tail2.box(-tw * 0.32, -tw * 0.32, -tl * 0.52, tw * 0.32, tw * 0.32, 0.03, 'skin')
    tail2.box(-tw * 0.2, -tw * 0.2, -tl * 0.62, tw * 0.2, tw * 0.2, -tl * 0.48, 'dark')
    tail2.box(-tw * 0.2, tw * 0.32, -tl * 0.45, tw * 0.2, tw * 0.34, 0, 'stripe')
    B.append(tail2)
    # pattes arrière (cuisse + jambe) et bras
    for side, sx, ph in (('L', 1, 0.0), ('R', -1, math.pi)):
        th = Bone('leg' + side, 'body', (sx * (bw / 2 - lw * 0.2), 0, bl * 0.05), rest=(-12, 0, 0), anim='leg', phase=ph)
        th.box(-lw / 2, -H * 0.5, -lw * 0.7, lw / 2, bh * 0.15, lw * 0.75, 'skin')
        B.append(th)
        sh = Bone('shin' + side, 'leg' + side, (0, -H * 0.46, 0), rest=(14, 0, 0), anim='knee', phase=ph)
        sh.box(-lw * 0.32, -H * 0.5, -lw * 0.32, lw * 0.32, 0.02, lw * 0.32, 'skin')
        sh.box(-lw * 0.48, -H * 0.56, -lw * 0.35, lw * 0.48, -H * 0.48, lw * 1.15, 'dark')
        sh.box(-lw * 0.42, -H * 0.56, lw * 1.15, lw * 0.42, -H * 0.5, lw * 1.35, 'claw')
        B.append(sh)
        if al > 0:
            ar = Bone('arm' + side, 'body', (sx * (bw / 2 - aw * 0.3), bh * 0.12, bl * 0.48), rest=(-35, 0, sx * 8), anim='arm',
                      amp=0.4 if small_arms else 0.8, phase=ph + math.pi)
            ar.box(-aw / 2, -al, -aw / 2, aw / 2, 0.02, aw / 2, 'skin')
            ar.box(-aw * 0.4, -al - 0.09 * s, -aw * 0.1, aw * 0.4, -al + 0.01, aw * 0.9, 'claw')
            B.append(ar)
    sp = Species(key, label, color, mats, B, s)
    if extra:
        extra(sp, s)
    return sp


def quadruped(key, label, color, mats, s=1.0, body=(1.2, 1.0, 2.4), hip=1.2, shoulder=1.1, neck=(0.5, 0.6, 15), head=(0.6, 0.55, 0.8),
              tail=(0.4, 1.8), leg=(0.32, 0.36), extra=None, jaw=True):
    """Quadrupède : tricératops, stégosaure, ankylosaure, brachiosaure."""
    bw, bh, bl = (v * s for v in body)
    nw, nl, nang = neck[0] * s, neck[1] * s, neck[2]
    hw, hh, hl = (v * s for v in head)
    tw, tl = tail[0] * s, tail[1] * s
    Hh, Hs = hip * s, shoulder * s
    lf, lh = leg[0] * s, leg[1] * s
    B = []
    body_b = Bone('body', None, (0, Hh, 0), anim='body', amp=1.6)
    body_b.box(-bw / 2, -bh * 0.4, -bl * 0.45, bw / 2, -bh * 0.08, bl * 0.5, 'belly')
    body_b.box(-bw / 2 - 0.005, -bh * 0.08, -bl * 0.47, bw / 2 + 0.005, bh * 0.55, bl * 0.52, 'skin')
    body_b.box(-bw * 0.42, bh * 0.55, -bl * 0.4, bw * 0.42, bh * 0.68, bl * 0.42, 'skin')
    body_b.box(-bw * 0.2, bh * 0.68, -bl * 0.35, bw * 0.2, bh * 0.72, bl * 0.38, 'stripe')
    B.append(body_b)
    neck_b = Bone('neck', 'body', (0, (Hs - Hh) + bh * 0.2, bl * 0.48), rest=(-nang, 0, 0), anim='neck', amp=0.6)
    neck_b.box(-nw / 2, -nw / 2, -nw * 0.3, nw / 2, nw / 2, nl, 'skin')
    neck_b.box(-nw * 0.4, -nw / 2 - 0.01, 0, nw * 0.4, -nw * 0.2, nl * 0.95, 'belly')
    B.append(neck_b)
    head_b = Bone('head', 'neck', (0, 0, nl), rest=(nang * 0.9, 0, 0), anim='head', amp=0.6)
    head_b.box(-hw / 2, -hh * 0.3, -hh * 0.3, hw / 2, hh * 0.7, hl * 0.6, 'skin')
    head_b.box(-hw * 0.35, -hh * 0.3, hl * 0.6, hw * 0.35, hh * 0.35, hl, 'beak')
    head_b.box(-hw / 2 - 0.012, hh * 0.3, hl * 0.3, hw / 2 + 0.012, hh * 0.47, hl * 0.42, 'eye')
    B.append(head_b)
    if jaw:
        jaw_b = Bone('jaw', 'head', (0, -hh * 0.3, 0), anim='jaw', amp=0.6)
        jaw_b.box(-hw * 0.32, -hh * 0.22, 0, hw * 0.32, 0, hl * 0.92, 'beak')
        B.append(jaw_b)
    tail_b = Bone('tail', 'body', (0, bh * 0.25, -bl * 0.45), rest=(8, 0, 0), anim='tail', amp=0.8)
    tail_b.box(-tw / 2, -tw / 2, -tl * 0.52, tw / 2, tw / 2, 0.05, 'skin')
    tail_b.box(-tw * 0.3, tw / 2, -tl * 0.5, tw * 0.3, tw / 2 + 0.02, 0, 'stripe')
    B.append(tail_b)
    tail2 = Bone('tail2', 'tail', (0, 0, -tl * 0.5), rest=(5, 0, 0), anim='tail', amp=1.2, phase=-0.9)
    tail2.box(-tw * 0.32, -tw * 0.32, -tl * 0.55, tw * 0.32, tw * 0.32, 0.03, 'skin')
    B.append(tail2)
    for nm_, sx, z, top, w_, ph in (('armL', 1, bl * 0.34, Hs - Hh, lf, 0.0), ('armR', -1, bl * 0.34, Hs - Hh, lf, math.pi),
                                     ('legL', 1, -bl * 0.3, 0, lh, math.pi), ('legR', -1, -bl * 0.3, 0, lh, 0.0)):
        L = Hs if nm_.startswith('arm') else Hh
        lg = Bone(nm_, 'body', (sx * (bw / 2 - w_ * 0.45), top, z), anim='leg', amp=0.7, phase=ph)
        lg.box(-w_ / 2, -L * 0.55, -w_ / 2, w_ / 2, bh * 0.1, w_ / 2, 'skin')
        B.append(lg)
        kn = Bone(('fore' if nm_.startswith('arm') else 'shin') + nm_[-1], nm_, (0, -L * 0.52, 0), anim='knee', amp=0.5, phase=ph)
        kn.box(-w_ * 0.42, -L * 0.48, -w_ * 0.42, w_ * 0.42, 0.02, w_ * 0.42, 'skin')
        kn.box(-w_ * 0.5, -L * 0.48, -w_ * 0.5, w_ * 0.5, -L * 0.4, w_ * 0.62, 'dark')
        B.append(kn)
    sp = Species(key, label, color, mats, B, s)
    if extra:
        extra(sp, s)
    return sp


def pterosaur(key, label, color, mats, s=1.0):
    B = []
    body_b = Bone('body', None, (0, 0.9 * s, 0), anim='body', amp=0.5)
    body_b.box(-0.22 * s, -0.18 * s, -0.45 * s, 0.22 * s, 0.2 * s, 0.4 * s, 'skin')
    body_b.box(-0.16 * s, -0.22 * s, -0.35 * s, 0.16 * s, -0.17 * s, 0.3 * s, 'belly')
    B.append(body_b)
    neck_b = Bone('neck', 'body', (0, 0.1 * s, 0.38 * s), rest=(-20, 0, 0), anim='neck', amp=0.5)
    neck_b.box(-0.09 * s, -0.09 * s, -0.05 * s, 0.09 * s, 0.09 * s, 0.4 * s, 'skin')
    B.append(neck_b)
    head_b = Bone('head', 'neck', (0, 0, 0.4 * s), rest=(20, 0, 0), anim='head')
    head_b.box(-0.12 * s, -0.08 * s, -0.12 * s, 0.12 * s, 0.14 * s, 0.22 * s, 'skin')
    head_b.box(-0.06 * s, -0.06 * s, 0.22 * s, 0.06 * s, 0.06 * s, 0.95 * s, 'beak')
    head_b.box(-0.03 * s, 0.1 * s, -0.75 * s, 0.03 * s, 0.32 * s, 0.05 * s, 'crest')
    head_b.box(-0.13 * s, 0.03 * s, 0.05 * s, 0.13 * s, 0.09 * s, 0.13 * s, 'eye')
    B.append(head_b)
    jaw_b = Bone('jaw', 'head', (0, -0.06 * s, 0.2 * s), anim='jaw')
    jaw_b.box(-0.05 * s, -0.06 * s, 0, 0.05 * s, 0, 0.72 * s, 'beak')
    B.append(jaw_b)
    for nm_, sx in (('wingL', 1), ('wingR', -1)):
        wb = Bone(nm_, 'body', (sx * 0.2 * s, 0.12 * s, 0.15 * s), anim=nm_)
        wb.box(0, -0.03 * s, -0.55 * s, sx * 1.15 * s, 0.03 * s, 0.25 * s, 'wing')
        wb.box(0, -0.06 * s, 0.15 * s, sx * 1.15 * s, 0.05 * s, 0.27 * s, 'skin')
        B.append(wb)
        wt = Bone(nm_ + 't', nm_, (sx * 1.15 * s, 0, 0), anim=nm_, amp=0.7, phase=-0.6)
        wt.box(0, -0.025 * s, -0.4 * s, sx * 1.05 * s, 0.025 * s, 0.25 * s, 'wing')
        wt.box(0, -0.05 * s, 0.15 * s, sx * 1.05 * s, 0.04 * s, 0.26 * s, 'skin')
        wt.box(sx * 1.0 * s, -0.04 * s, 0.1 * s, sx * 1.12 * s, 0.04 * s, 0.3 * s, 'claw')
        B.append(wt)
    tail_b = Bone('tail', 'body', (0, 0, -0.45 * s), anim='tail', amp=0.4)
    tail_b.box(-0.05 * s, -0.05 * s, -0.4 * s, 0.05 * s, 0.05 * s, 0, 'skin')
    B.append(tail_b)
    for side, sx in (('L', 1), ('R', -1)):
        lg = Bone('leg' + side, 'body', (sx * 0.12 * s, -0.15 * s, -0.25 * s), rest=(60, 0, 0), anim=None)
        lg.box(-0.04 * s, -0.4 * s, -0.04 * s, 0.04 * s, 0, 0.04 * s, 'dark')
        B.append(lg)
    return Species(key, label, color, mats, B, s)


# ---------------------------------------------------------------- détails propres à certaines espèces
def top_of(b, mat='skin'):
    return max(bx[4] for bx in b.boxes if bx[6] == mat)


def _trike(sp, s):
    h = sp.bone('head')
    h.box(-0.95 * s, 0.05 * s, -0.55 * s, 0.95 * s, 1.35 * s, -0.25 * s, 'frill')         # collerette
    h.box(-0.98 * s, 1.25 * s, -0.6 * s, 0.98 * s, 1.42 * s, -0.2 * s, 'dark')
    h.box(-0.6 * s, -0.02 * s, -0.56 * s, 0.6 * s, 1.1 * s, -0.5 * s, 'stripe')
    for sx in (-1, 1):                                                                      # deux grandes cornes
        h.box(sx * 0.22 * s, 0.42 * s, 0.1 * s, sx * 0.34 * s, 0.56 * s, 0.95 * s, 'horn')
        h.box(sx * 0.24 * s, 0.44 * s, 0.95 * s, sx * 0.32 * s, 0.53 * s, 1.15 * s, 'horn')
    h.box(-0.07 * s, 0.25 * s, 0.75 * s, 0.07 * s, 0.6 * s, 0.9 * s, 'horn')             # corne du nez


def _stego(sp, s):
    b = sp.bone('body')
    y0 = top_of(b) - 0.08 * s
    for i, (z, hgt) in enumerate([(-0.9, 0.55), (-0.5, 0.75), (-0.1, 0.85), (0.3, 0.7), (0.65, 0.5)]):
        for sx in (-1, 1):
            off = 0.12 * s * sx
            zz = z * s + (0.1 * s if sx > 0 else 0)
            b.box(off - 0.04 * s, y0, zz, off + 0.04 * s, y0 + hgt * s, zz + 0.38 * s, 'plate')
            b.box(off - 0.045 * s, y0 + hgt * s * 0.7, zz + 0.08 * s, off + 0.045 * s, y0 + hgt * s, zz + 0.3 * s, 'dark')
    t = sp.bone('tail')
    for z in (-0.35, -0.7):
        t.box(-0.035 * s, 0.15 * s, z * s, 0.035 * s, 0.5 * s, z * s + 0.28 * s, 'plate')
    t2 = sp.bone('tail2')
    for sx in (-1, 1):                                                                       # thagomizer
        t2.box(sx * 0.1 * s, 0.05 * s, -0.85 * s, sx * 0.55 * s, 0.13 * s, -0.75 * s, 'horn')
        t2.box(sx * 0.1 * s, 0.1 * s, -0.55 * s, sx * 0.5 * s, 0.18 * s, -0.45 * s, 'horn')


def _ankylo(sp, s):
    b = sp.bone('body')
    b.box(-0.95 * s, 0.25 * s, -1.05 * s, 0.95 * s, 0.62 * s, 1.0 * s, 'plate')            # carapace
    for i in range(5):
        z = -0.95 * s + i * 0.45 * s
        for sx in (-1, 1):
            b.box(sx * 0.95 * s, 0.2 * s, z, sx * 1.22 * s, 0.32 * s, z + 0.16 * s, 'horn')
        b.box(-0.6 * s, 0.62 * s, z + 0.1 * s, 0.6 * s, 0.7 * s, z + 0.22 * s, 'dark')
    h = sp.bone('head')
    for sx in (-1, 1):
        h.box(sx * 0.3 * s, 0.25 * s, -0.25 * s, sx * 0.5 * s, 0.4 * s, -0.05 * s, 'horn')
    t2 = sp.bone('tail2')
    t2.box(-0.38 * s, -0.25 * s, -1.25 * s, 0.38 * s, 0.25 * s, -0.75 * s, 'plate')          # massue
    t2.box(-0.3 * s, 0.25 * s, -1.2 * s, 0.3 * s, 0.32 * s, -0.8 * s, 'dark')


def _brachio(sp, s):
    h = sp.bone('head')
    h.box(-0.18 * s, 0.35 * s, -0.15 * s, 0.18 * s, 0.6 * s, 0.35 * s, 'skin')              # bosse nasale
    n = sp.bone('neck')
    n.box(-0.08 * s, 0.21 * s, 0.1 * s, 0.08 * s, 0.24 * s, 2.4 * s, 'stripe')


def _carno(sp, s):
    b = sp.bone('body')
    y0 = top_of(b)
    for i in range(6):                                                                       # rangées d'écailles
        z = -0.5 * s + i * 0.3 * s
        for sx in (-1, 1):
            b.box(sx * 0.2 * s, y0 - 0.02 * s, z, sx * 0.12 * s, y0 + 0.06 * s, z + 0.12 * s, 'dark')


def _rex(sp, s):
    h = sp.bone('head')
    for sx in (-1, 1):
        h.box(sx * 0.32 * s, 0.24 * s, 0.08 * s, sx * 0.4 * s, 0.32 * s, 0.25 * s, 'dark')  # arcades
    b = sp.bone('body')
    y0 = top_of(b)
    for i in range(5):
        z = -0.35 * s + i * 0.28 * s
        b.box(-0.12 * s, y0 - 0.01 * s, z, 0.12 * s, y0 + 0.04 * s, z + 0.14 * s, 'dark')


def _spino(sp, s):
    h = sp.bone('head')
    h.box(-0.1 * s, 0.2 * s, -0.05 * s, 0.1 * s, 0.32 * s, 0.4 * s, 'crest')


# ---------------------------------------------------------------- palettes : matière -> (couleur RVB, motif, bloc de secours)
def M(**kw):
    base = {'teeth': ((236, 230, 210), 'teeth', 'white_concrete'), 'claw': ((54, 46, 40), 'solid', 'black_terracotta'),
            'eye': ((250, 200, 40), 'eye', 'yellow_concrete'), 'dark': ((46, 40, 36), 'scales', 'black_terracotta')}
    base.update(kw)
    return base


SPECIES = {}


def reg(sp):
    SPECIES[sp.key] = sp
    return sp


reg(theropod('raptor', 'Slasher', 'green', M(
    skin=((84, 112, 52), 'scales', 'green_terracotta'), belly=((176, 168, 118), 'scales', 'white_terracotta'),
    stripe=((52, 66, 34), 'stripes', 'brown_terracotta'), dark=((40, 44, 30), 'scales', 'black_terracotta')),
    s=1.0, body=(0.46, 0.5, 1.0), hip=0.85, neck=(0.22, 0.42, 38), head=(0.32, 0.28, 0.6), tail=(0.26, 1.6), leg=0.19,
    arm=(0.07, 0.3), spikes=True))
reg(theropod('carno', 'Carnotaure', 'red', M(
    skin=((150, 52, 36), 'scales', 'red_terracotta'), belly=((210, 160, 110), 'scales', 'orange_terracotta'),
    stripe=((90, 30, 24), 'stripes', 'brown_terracotta'), horn=((60, 50, 44), 'solid', 'black_terracotta'),
    dark=((70, 26, 20), 'scales', 'black_terracotta')),
    s=2.1, body=(0.62, 0.62, 1.15), hip=0.95, neck=(0.34, 0.32, 22), head=(0.46, 0.4, 0.62), tail=(0.36, 1.55), leg=0.24,
    arm=(0.07, 0.14), horns=0.22, small_arms=True, extra=_carno))
reg(theropod('rex', 'Roi Tyran', 'dark_red', M(
    skin=((92, 74, 54), 'scales', 'brown_terracotta'), belly=((176, 150, 112), 'scales', 'white_terracotta'),
    stripe=((58, 44, 34), 'stripes', 'black_terracotta'), dark=((40, 30, 24), 'scales', 'black_terracotta'),
    eye=((255, 120, 20), 'eye', 'orange_concrete')),
    s=3.6, body=(0.62, 0.65, 1.25), hip=1.0, neck=(0.36, 0.3, 20), head=(0.56, 0.5, 0.95), tail=(0.36, 1.75), leg=0.26,
    arm=(0.05, 0.12), small_arms=True, extra=_rex))
reg(theropod('dilo', 'Dilophosaure', 'dark_green', M(
    skin=((70, 130, 96), 'scales', 'cyan_terracotta'), belly=((210, 196, 120), 'scales', 'yellow_terracotta'),
    stripe=((42, 80, 60), 'stripes', 'green_terracotta'), crest=((200, 60, 40), 'stripes', 'red_concrete'),
    frill=((236, 150, 40), 'frill', 'orange_concrete')),
    s=1.25, body=(0.42, 0.48, 1.0), hip=0.9, neck=(0.2, 0.55, 45), head=(0.28, 0.26, 0.55), tail=(0.24, 1.6), leg=0.18,
    arm=(0.07, 0.3), crest=0.14, frill=True))
reg(theropod('spino', 'Spinosaure', 'dark_aqua', M(
    skin=((70, 90, 92), 'scales', 'cyan_terracotta'), belly=((182, 176, 150), 'scales', 'white_terracotta'),
    stripe=((40, 56, 60), 'stripes', 'gray_terracotta'), sail=((178, 70, 46), 'stripes', 'red_terracotta'),
    crest=((178, 70, 46), 'solid', 'red_terracotta')),
    s=3.0, body=(0.5, 0.55, 1.35), hip=0.85, neck=(0.26, 0.5, 30), head=(0.3, 0.26, 0.95), tail=(0.3, 1.9), leg=0.22,
    arm=(0.09, 0.34), sail=0.75, long_snout=True, extra=_spino))
reg(theropod('compy', 'Compsognathus', 'yellow', M(
    skin=((140, 150, 70), 'scales', 'lime_terracotta'), belly=((210, 200, 150), 'scales', 'white_terracotta'),
    stripe=((80, 90, 40), 'stripes', 'green_terracotta')),
    s=0.42, body=(0.5, 0.55, 1.0), hip=0.95, neck=(0.24, 0.5, 45), head=(0.34, 0.3, 0.55), tail=(0.24, 1.8), leg=0.2,
    arm=(0.08, 0.3)))
reg(theropod('galli', 'Gallimimus', 'gold', M(
    skin=((176, 140, 92), 'scales', 'terracotta'), belly=((226, 214, 186), 'scales', 'white_terracotta'),
    stripe=((120, 90, 60), 'stripes', 'brown_terracotta'), beak=((90, 80, 70), 'solid', 'gray_terracotta')),
    s=1.0, body=(0.5, 0.55, 0.95), hip=1.25, neck=(0.16, 0.85, 62), head=(0.2, 0.2, 0.42), tail=(0.24, 1.35), leg=0.2,
    arm=(0.06, 0.3), beak=True))
reg(theropod('pachy', 'Pachycéphalosaure', 'gold', M(
    skin=((150, 110, 70), 'scales', 'brown_terracotta'), belly=((210, 180, 140), 'scales', 'white_terracotta'),
    stripe=((96, 70, 44), 'stripes', 'brown_terracotta'), dome=((226, 210, 180), 'solid', 'white_terracotta'),
    beak=((110, 90, 70), 'solid', 'brown_terracotta')),
    s=1.05, body=(0.6, 0.62, 1.05), hip=0.85, neck=(0.26, 0.32, 25), head=(0.36, 0.32, 0.42), tail=(0.28, 1.3), leg=0.22,
    arm=(0.07, 0.24), dome=True, beak=True))
reg(quadruped('trike', 'Tricératops', 'dark_green', M(
    skin=((96, 110, 72), 'scales', 'green_terracotta'), belly=((176, 166, 130), 'scales', 'white_terracotta'),
    stripe=((64, 74, 50), 'stripes', 'brown_terracotta'), beak=((70, 60, 50), 'solid', 'gray_terracotta'),
    frill=((176, 100, 54), 'frill', 'orange_terracotta'), horn=((236, 226, 200), 'solid', 'white_terracotta')),
    s=1.3, body=(1.25, 1.05, 2.4), hip=1.25, shoulder=1.05, neck=(0.6, 0.35, -5), head=(0.75, 0.62, 0.95), tail=(0.42, 1.6),
    leg=(0.36, 0.4), extra=_trike))
reg(quadruped('stego', 'Stégosaure', 'yellow', M(
    skin=((126, 120, 70), 'scales', 'yellow_terracotta'), belly=((196, 186, 140), 'scales', 'white_terracotta'),
    stripe=((80, 76, 46), 'stripes', 'brown_terracotta'), beak=((80, 70, 56), 'solid', 'gray_terracotta'),
    plate=((176, 76, 50), 'frill', 'red_terracotta'), horn=((226, 216, 190), 'solid', 'white_terracotta')),
    s=1.3, body=(1.05, 1.1, 2.3), hip=1.45, shoulder=0.95, neck=(0.4, 0.55, -18), head=(0.36, 0.34, 0.6), tail=(0.38, 2.0),
    leg=(0.3, 0.38), extra=_stego))
reg(quadruped('ankylo', 'Ankylosaure', 'gray', M(
    skin=((110, 98, 80), 'scales', 'brown_terracotta'), belly=((170, 160, 136), 'scales', 'white_terracotta'),
    stripe=((70, 62, 50), 'stripes', 'black_terracotta'), beak=((70, 64, 56), 'solid', 'gray_terracotta'),
    plate=((128, 118, 100), 'plates', 'gray_terracotta'), horn=((210, 200, 176), 'solid', 'white_terracotta')),
    s=1.2, body=(1.7, 0.8, 2.2), hip=0.85, shoulder=0.8, neck=(0.5, 0.3, -5), head=(0.62, 0.42, 0.55), tail=(0.36, 1.7),
    leg=(0.34, 0.38), extra=_ankylo))
reg(quadruped('brachio', 'Brachiosaure', 'gray', M(
    skin=((128, 136, 140), 'scales', 'light_gray_terracotta'), belly=((196, 196, 186), 'scales', 'white_terracotta'),
    stripe=((90, 96, 100), 'stripes', 'gray_terracotta'), beak=((100, 106, 110), 'solid', 'gray_terracotta')),
    s=2.0, body=(1.25, 1.1, 2.1), hip=1.25, shoulder=1.5, neck=(0.42, 2.6, 62), head=(0.42, 0.36, 0.62), tail=(0.38, 2.4),
    leg=(0.38, 0.38), extra=_brachio))
reg(pterosaur('ptera', 'Ptéranodon', 'aqua', M(
    skin=((150, 120, 96), 'scales', 'terracotta'), belly=((210, 200, 180), 'scales', 'white_terracotta'),
    wing=((120, 80, 64), 'wing', 'brown_terracotta'), beak=((210, 190, 140), 'solid', 'yellow_terracotta'),
    crest=((190, 60, 40), 'solid', 'red_terracotta')), s=1.6))
