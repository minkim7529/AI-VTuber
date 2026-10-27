# 실제 리깅 구조 — v009

BodyXY → BreathAndBodyZ
- HeadXY → HeadZ → FaceTurn / HairFront / HairSide / HairBack
- NeckXY → NeckZ → neck
- Ribbon → 리본 날개와 꼬리
- 몸통, 소매, 세일러 칼라, 리본 매듭, 배지

face_base는 HeadZ 아래, 눈·코·입은 FaceTurn 아래에 있습니다. FaceTurn은 얼굴 내부의 상대 이동과 폭 변화를 추가하지만 현재 X/Y 회전의 입체감은 약합니다. 파라미터 ±30은 실제 시각적 30도 회전을 의미하지 않습니다.

NeckXY/NeckZ는 9×9 로컬 Warp 두 개로 분리했습니다. 목 위쪽은 머리를 따라가고 아래쪽은 옷깃 위치에 고정되도록 감쇠합니다. 복합 극단 두 방향에서 검은 틈이 사라진 것을 실제 VTS 화면으로 확인했습니다.

눈 흰자와 속눈썹은 각 눈의 Open 파라미터에 연결하며, 감은 눈 선은 별도 레이어입니다. iris_L/R은 각각 sclera_L/R로 clipping합니다. 눈동자 자체는 EyeBall X/Y 두 축에만 직접 연결됩니다. 반쯤 감은 눈의 앞머리 경계에는 작은 선 조각이 남아 있습니다.

입 내부/혀는 MouthOpenY×MouthForm 2축 키폼입니다. 닫힌 입 선은 열릴 때 사라집니다. E/I 계열은 모서리가 올라가고 위쪽 곡선이 평평해지며, O/U 계열은 폭과 곡선을 좁힙니다. tongue는 mouth_inside로 clipping합니다. 원본에 없는 입 내부는 보완 원화이며 자연스러움의 추가 개선이 필요합니다.

Physics는 runtime의 BlueSailor.physics3.json에 별도로 저장됩니다. CMO3 안에 Cubism Physics 설정이 저장되어 있다는 의미는 아닙니다. 4개 그룹은 Front hair, Side hair, Back hair, Ribbon이며 각 출력은 서로 다른 파라미터에 연결됩니다. Fps=60, 출력 Scale은 0.25 / 0.30 / 0.32 / 0.30입니다.
