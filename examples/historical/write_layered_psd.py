"""Preserve current failed-QA art as an editable draft, not a rig-ready deliverable."""
from pathlib import Path
import sys,struct,json,hashlib
sys.path.insert(0,str(Path('work/pydeps').resolve()))
import numpy as np
from PIL import Image
from psd_tools import PSDImage
P=Path('outputs/live2d_vtuber_clean'); D=P/'03_parts/parts_v006'
rows=json.loads((D/'manifest.json').read_text());src=Image.open(P/'00_source/original.png').convert('RGBA');w,h=src.size
u16=lambda v:struct.pack('>H',v)
i16=lambda v:struct.pack('>h',v)
u32=lambda v:struct.pack('>I',v)
records=[];channels=[]
for row in reversed(rows):
 im=Image.open(P/row['file']).convert('RGBA');box=im.getbbox()
 if not box:raise ValueError(row['name'])
 left,top,right,bottom=box;crop=im.crop(box);cw,ch=crop.size
 name=row['name'].encode('ascii');pn=bytes([len(name)])+name;pn+=b'\0'*(-len(pn)%4)
 extra=u32(0)+u32(0)+pn
 rec=struct.pack('>iiii',top,left,bottom,right)+u16(4)
 for cid in [0,1,2,-1]:rec+=i16(cid)+u32(2+cw*ch)
 rec+=b'8BIMnorm'+bytes([255,0,0 if row['neutral_visible'] else 2,0])+u32(len(extra))+extra
 records.append(rec);channels.append(b''.join(u16(0)+band.tobytes() for band in crop.split()))
ld=i16(-len(rows))+b''.join(records)+b''.join(channels);ld+=b'\0'*(len(ld)%2)
lm=u32(len(ld))+ld+u32(0)
merged=Image.open(P/'08_test/neutral_v006.png').convert('RGBA')
data=b'8BPS'+u16(1)+b'\0'*6+u16(4)+u32(h)+u32(w)+u16(8)+u16(3)+u32(0)+u32(0)+u32(len(lm))+lm+u16(0)+b''.join(b.tobytes() for b in merged.split())
out=P/'04_psd/character_parts_v006_QA_FAILED_DRAFT.psd';out.write_bytes(data)
psd=PSDImage.open(out);assert psd.size==(w,h);assert len(psd)==len(rows)
checks=[];rebuild=Image.new('RGBA',(w,h))
for layer,row in zip(reversed(list(psd)),rows):
 expected=Image.open(P/row['file']).convert('RGBA');actual=layer.topil().convert('RGBA')
 assert layer.name==row['name'];assert layer.visible==row['neutral_visible']
 restored=Image.new('RGBA',(w,h));restored.paste(actual,(layer.left,layer.top))
 ea=np.array(expected);ra=np.array(restored);mask=ea[:,:,3]>0
 assert np.array_equal(ea[:,:,3],ra[:,:,3])
 assert np.array_equal(ea[mask],ra[mask])
 if layer.visible:rebuild=Image.alpha_composite(rebuild,restored)
 checks.append({'name':layer.name,'visible':layer.visible,'pixel_roundtrip':'PASS'})
rebuild.save(P/'08_test/psd_v006_reconstructed.png')
a=np.array(rebuild);b=np.array(src);v=b[:,:,3]>0
assert np.array_equal(a[v],b[v]);assert np.array_equal(a[:,:,3],b[:,:,3])
report={'status':'DRAFT_ART_QA_FAILED','format_validation':'PASS','layer_count':len(psd),'canvas':[w,h],'neutral_visible_pixel_difference':0,'psd_layer_roundtrip':checks,'cubism_import':'NOT_TESTED','rigging':'NOT_STARTED','iphone_test':'NOT_TESTED','sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data)}
(P/'08_test/psd_v006_validation.json').write_text(json.dumps(report,indent=2),encoding='utf8')
print(json.dumps({k:v for k,v in report.items() if k!='psd_layer_roundtrip'}))
