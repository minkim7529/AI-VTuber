from pathlib import Path
exec(Path('work/face_motion_helpers.py').read_text().replace('JawSingle','BodyMotion'))
OLD=B;B=Path('outputs/BlueSailor_JerseyMaid_TongueAlign')
for d in ['parts','source']:shutil.copytree(OLD/d,B/d,dirs_exist_ok=True)
for d in ['editable','evidence','runtime']:(B/d).mkdir(parents=True,exist_ok=True)
before={k:E.tostring(n(m,'keyforms')) for k,m in meshes.items()};m=meshes['tongue_out'];old={(v['ParamTongueOut'],v['ParamMouthOpenY']):(vals(n(f,'positions')).copy(),float(f.find('.//f[@xs.n="opacity"]').text)) for f,v in forms(m)}
def tongue(f,v):
 t=v['ParamTongueOut'];op=v['ParamMouthOpenY'];a,b=(0,.3) if op<=.3 else (.3,1);u=(op-a)/(b-a);q=old[t,a][0]*(1-u)+old[t,b][0]*u
 q[:,1]+=(7+14*op)/H
 arr(n(f,'positions'),q);f.find('.//f[@xs.n="opacity"]').text=str(old[t,a][1]*(1-u)+old[t,b][1]*u)
bindings(m,[('ParamTongueOut',[0,.25,.5,.75,1]),('ParamMouthOpenY',[0,.15,.3,.6,1])],tongue)
assert all(E.tostring(n(m,'keyforms'))==before[k] for k,m in meshes.items() if k!='tongue_out')
tri=np.fromstring(deref(n(m,'indices')).text,sep=' ',dtype=int).reshape(-1,3) if False else np.fromstring(deref(n(meshes['tongue_out'],'indices')).text,sep=' ',dtype=int).reshape(-1,3)
areas=[]
for f,v in forms(meshes['tongue_out']):
 q=vals(n(f,'positions'));p=q[tri];a=p[:,1]-p[:,0];b=p[:,2]-p[:,0];areas.append(a[:,0]*b[:,1]-a[:,1]*b[:,0])
a=np.array(areas);assert np.all(a*a[0]>0)
for e in root.iter():e.attrib.pop('xs.idx',None)
entry['content']=(prefix+E.tostring(root,encoding='unicode')).encode();(B/'editable/BlueSailor_JerseyMaid_TongueAlign.cmo3').write_bytes(pack_caff(entries))
a=json.loads((OLD/'evidence/build_audit.json').read_text());a.update(incremental_base='BodyMotion plus accepted MouthResponse calibration',changed_meshes=['tongue_out'],changed_warps=[],preserved_meshes=sorted(set(meshes)-{'tongue_out'}));(B/'evidence/build_audit.json').write_text(json.dumps(a,indent=2));print('PASS tongue forms 25; other 36 meshes unchanged')
