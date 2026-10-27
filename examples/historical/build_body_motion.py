from pathlib import Path
exec(Path('work/face_motion_helpers.py').read_text().replace('JawSingle','FaceMotion'))
OLD=B;B=Path('outputs/BlueSailor_JerseyMaid_BodyMotion')
for d in ['parts','source']:shutil.copytree(OLD/d,B/d,dirs_exist_ok=True)
for d in ['editable','evidence','runtime']:(B/d).mkdir(parents=True,exist_ok=True)
before={k:E.tostring(n(m,'keyforms')) for k,m in meshes.items()}
changed=['Sleeve_Hand_R','Sleeve_Hand_L','Skirt_Base','Apron_Front','Chest_Bow']
for name in changed:
 m=meshes[name];grid=deref(n(m.find('.//ACParameterControllableSource'),'keyformGridSource'))
 spec=[(pids[n(deref(b),'parameterGuid').get('xs.ref')],[float(x.text) for x in n(deref(b),'keys')]) for b in n(grid,'keyformBindings')]
 base=next(vals(n(f,'positions')).copy()*canvas for f,v in forms(m) if all(x==0 for x in v.values()))
 spec=[(pid,[-10,-5,0,5,10] if 'BodyAngle' in pid else [-1,-.5,0,.5,1]) for pid,levels in spec]
 def form(f,v):
  q=base.copy();x=base[:,0];y=base[:,1]
  if name.startswith('Sleeve'):
   side=-1 if name.endswith('_R') else 1;s=v['ParamSleeveR' if side==-1 else 'ParamSleeveL'];roll=v['ParamBodyAngleZ']/10
   t=np.clip((y-350)/410,0,1);w=np.clip((y-735)/110,0,1);bend=t*t*(3-2*t)
   q[:,0]+=s*(6.5*bend+2*w)+roll*side*1.8*t
   q[:,1]+=s*side*2.2*bend+roll*side*2.2*np.exp(-((y-415)/130)**2)*np.clip((y-350)/65,0,1)
   q[:,0]+=(x-(330 if side==-1 else 640))*(-.015*s*side)*np.sin(np.pi*t)**2
  elif name=='Skirt_Base':
   t=np.clip((y-560)/295,0,1);s=v['ParamRibbonSway'];turn=v['ParamBodyAngleX']/10
   q[:,0]+=s*7.5*t*t
   q[:,1]+=s*(x-485)/210*2*t+turn*(x-485)/210*t+1.6*s*np.sin((x-330)/48)*t*t
  elif name=='Apron_Front':
   t=np.clip((y-568)/210,0,1);s=v['ParamApronSway'];pitch=v['ParamBodyAngleY']/10
   q[:,0]+=s*5*t*t
   q[:,1]+=s*(1.8*np.sin((x-485)/90)*t+1.1*np.sin((x-350)/34)*t*t)+pitch*1.2*t
  else:
   t=np.clip((y-350)/65,0,1);s=v['ParamBowSway'];q[:,0]+=s*3.1*t*t;q[:,1]+=s*(x-485)/50*1.5*t
  arr(n(f,'positions'),q/canvas)
 bindings(m,spec,form)
# Smooth yaw width response through the neutral pose; shared outer transform preserves attachments.
w=warps['JerseyBodyXY'][0]
xx,yy=np.meshgrid(np.linspace(0,W,10),np.linspace(0,H,10));base=np.c_[xx.ravel(),yy.ravel()]
def body(f,v):
 q=base.copy();upper=np.clip((1500-q[:,1])/970,0,1);turn=v['ParamBodyAngleX']/10;pitch=v['ParamBodyAngleY']/10
 q[:,0]+=turn*19*upper-(q[:,0]-485)*.035*turn*turn*upper
 q[:,1]+=(q[:,0]-485)*turn*.025*np.exp(-((q[:,1]-450)/350)**2)-pitch*5*upper
 arr(n(f,'positions'),q)
bindings(w,[('ParamBodyAngleX',[-10,-5,0,5,10]),('ParamBodyAngleY',[-10,-5,0,5,10])],body)
assert all(E.tostring(n(m,'keyforms'))==before[k] for k,m in meshes.items() if k not in changed)
checks=[]
for name in changed:
 m=meshes[name];tri=np.fromstring(deref(n(m,'indices')).text,sep=' ',dtype=int).reshape(-1,3);areas=[]
 for f,v in forms(m):
  q=vals(n(f,'positions'));t=q[tri];a=t[:,1]-t[:,0];b=t[:,2]-t[:,0];areas.append(a[:,0]*b[:,1]-a[:,1]*b[:,0])
 a=np.array(areas);assert np.all(a*a[0]>0),name;checks.append(dict(mesh=name,forms=len(a),minimum_area_ratio=float((a/a[0]).min())))
for f,v in forms(w):
 q=vals(n(f,'positions')).reshape(10,10,2);a=q[:-1,1:]-q[:-1,:-1];b=q[1:,:-1]-q[:-1,:-1];assert np.all(a[:,:,0]*b[:,:,1]-a[:,:,1]*b[:,:,0]>0)
for e in root.iter():e.attrib.pop('xs.idx',None)
entry['content']=(prefix+E.tostring(root,encoding='unicode')).encode();(B/'editable/BlueSailor_JerseyMaid_BodyMotion.cmo3').write_bytes(pack_caff(entries))
a=json.loads((OLD/'evidence/build_audit.json').read_text());a.update(incremental_base='BlueSailor_JerseyMaid_FaceMotion',changed_meshes=changed,changed_warps=['JerseyBodyXY'],preserved_meshes=sorted(set(meshes)-set(changed)));(B/'evidence/build_audit.json').write_text(json.dumps(a,indent=2))
(B/'evidence/body_geometry.json').write_text(json.dumps(dict(meshes=checks,unchanged_mesh_keyforms=len(meshes)-len(changed),body_warp_forms=25),indent=2));print('PASS',checks)
