from PIL import Image
import Comb
def FusionFull(t0,base):
    return t0
def FusionCompact(t0,base,way):
    if way == "fill":
        tf = Image.new("RGBA",(base*8,base*8))
        f1 = t0.crop((0,0,base,base))
        f2 = t0.crop((base,0,base*2,base))
        f3 = t0.crop((base*2,0,base*3,base))
        f4 = t0.crop((base*3,0,base*4,base))
        f5 = t0.crop((base*4,0,base*5,base))
        t0.close()
        tf = Comb.Full(base,f1,f2,f4,f1,f1,f1,f3,f4,f1,f1,f4,f1,f1,f1,f4,f3,f3,f3,f2,f3,f3,f4,f3,f4,f1,f1,f4,f1,f4,f3,f4,f4,f5,f5,f5,f5,f5,f5,f5,f5,f5,f5,f5,f5,f5,f5,f5)
        f1.close()
        f2.close()
        f3.close()
        f4.close()
        f5.close()
        return tf
    else:
        tf = Comb.Comb(t0,base)
        t0.close()
        return tf
def FusionSimple(t0,base,way,t1=None):
    if not t1:
        t1 = Image.new("RGBA",(base,base))
    if way == "fill":
        t1.close()
        tf = Comb.Convert(t0,base,((0,0),(1,32),(1,33),(1,34),(1,35),(1,36),(1,37),(1,38),(1,39),(1,40),(1,41),(1,42),(1,43),(1,44),(1,45),(1,46),(2,8),(3,3),(8,2),(9,16),(10,1),(11,24),(16,6),(16,17),(16,20),(16,22),(17,7),(17,10),(17,21),(17,23),(18,4),(18,9),(19,5),(19,11),(24,14),(24,26),(24,28),(24,30),(25,15),(25,19),(25,29),(25,31)),8,8)
        t0.close()
        return tf
    else:
        tf = Comb.CombAdv(t0,t1,base)
        t0.close()
        t1.close()
        return tf
def FusionHorizontal(t0,base,way)
    if way == "fill":
        tf = Comb.Convert(t0,base,((0,0),(0,8),(0,16),(0,24),(1,1),(1,4),(1,6),(1,9),(1,12),(1,17),(1,20),(1,22),(1,25),(2,2),(2,7),(2,10),(2,14),(2,18),(2,21),(2,23),(2,26),(2,28),(2,30),(2,32),(2,33),(2,34),(2,35),(2,36),(2,37),(2,38),(2,39),(2,40),(2,41),(2,42),(2,43),(2,44),(2,45),(2,46),(3,3),(3,5),(3,11),(3,13),(3,15),(3,19),(3,27),(3,29),(3,31)),8,8)
        t0.close()
        return tf
    else:
        ti = Comb.Convert(t0,base,((0,0),(0,2),(0,9),(0,11),(1,10),(1,16),(1,18),(1,26),(2,1),(2,8),(2,17),(2,24),(3,3),(3,19),(3,25),(3,27)),4,4)
        t0.close()
        t1 = Image.new("RGBA",(base,base))
        tf = Comb.CombAdv(ti,t1,base)
        ti.close()
        t1.close()
        return tf
def FusionVertical(t0,base,way)
    if way == "fill":
        tf = Comb.Convert(t0,base,(),8,8)
        t0.close()
        return tf
    else:
        ti = Comb.Convert(t0,base,(),4,4)
        t0.close()
        t1 = Image.new("RGBA",(base,base))
        tf = Comb.CombAdv(ti,t1,base)
        ti.close()
        t1.close()
        return tf
def FusionJustHorizontalVertical(th,tv,base,way)
    if way == "fill":
        t0 = Image.new("RGBA",(base*4,base*4))
        t0.paste(tv,(0,0))
        tv.close()
        t0.paste(th,(0,0))
        th.close()
        ti = Comb.Convert(t0,base,(),4,4)
        t0.close()
        tf = Comb.Convert(ti,base,((0,0),(1,32),(1,33),(1,34),(1,35),(1,36),(1,37),(1,38),(1,39),(1,40),(1,41),(1,42),(1,43),(1,44),(1,45),(1,46),(2,8),(3,3),(8,2),(9,16),(10,1),(11,24),(16,6),(16,17),(16,20),(16,22),(17,7),(17,10),(17,21),(17,23),(18,4),(18,9),(19,5),(19,11),(24,14),(24,26),(24,28),(24,30),(25,15),(25,19),(25,29),(25,31)),8,8)
        ti.close()
        return tf
    else:
        t0 = Image.new("RGBA",(base*4,base*4))
        t0.paste(tv,(0,0))
        tv.close()
        t0.paste(th,(0,0))
        th.close()
        ti = Comb.Convert(t0,base,(),4,4)
        t0.close()
        t1 = Image.new("RGBA",(base,base))
        tf = Comb.CombAdv(ti,t1,base)
        ti.close()
        t1.close()
        return tf
def FusionJustVerticalHorizontal(tv,th,base,way)