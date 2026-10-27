# 작업·검증 기록

이 문서는 로컬 프로젝트의 당시 보고서와 배포 기록을 바탕으로 정리했습니다. 과거 검사 기록과 2026-10-27에 새로 확인한 내용을 구분합니다.

## 2026-09-27~28: 초기 세일러복 실행 검증본

근거 문서: `live2d_vtuber_clean/09_docs/clean_start.md`, `capability_report.md`, `final_report.md`.

- 원본 복사 및 SHA-256 확인. 초기 폴더에서 삭제한 파일은 0개.
- 이미지·PSD 생성 및 재개방, 숨은 뒷머리 보완, Cubism 5.3.00 FREE에서 프로젝트 열기와 SDK 4.2 출력.
- v009: ArtMesh 33개, Parameter 17개, Deformer 11개, 텍스처 2048×2048 한 장으로 보고됨. 이후 버전의 수치와 혼합하지 않음.
- VTube Studio 1.35.10에서 모의 얼굴 입력과 22장 화면 증빙을 통한 검사.
- 고개·시선·눈 개폐·입 형태·복합 극단 검사, 12초 주기 입력과 12초 중립 복귀 물리 시험.
- 보고서는 실행 체크포인트로 판정했으며, 원화 수준의 최종 품질 달성을 선언하지 않음.

## 2026-10-06: BlueSailor V2 refined

근거 문서: `BlueSailor_V2_refined_release/README.md`, `evidence/detail_validation.json`.

- 배포 README에서 CMO3를 최종 r4, PSD를 갱신된 37레이어로 명시.
- 검사 JSON에는 37 ArtMesh, 19 Parameter, 18 Warp, 텍스처 한 장(2048), 물리 파일 존재가 기록됨. 해당 JSON이 모든 최종 r4 변경을 재검사했다는 뜻은 아님.
- 반감기 눈 선 겹침·눈꼬리 알파 경계·턱과 뒷머리 깊이·혀와 닫힌 입 선을 보정.
- 5개 표정과 일회성 혀 모션 유지.
- 배포 기록상 눈/회전 화면 검사는 r3, 기본 입과 혀는 r4로 확인. r4는 혀 파라미터가 0일 때 기존 상태를 유지하는 변경으로 설명됨.
- 최종 수정 후 iPhone 실기 검증 미수행. 큰 회전의 경계, 표정 중복 방지 등은 개선 후보.

## 2026-10-11: JerseyMaid JawTurn R1

근거 문서: `BlueSailor_JerseyMaid_JawTurn_release/README.md`, `evidence/runtime_validation.json`.

- FaceCleanup R5 기반으로 턱 끝 추가 수평 이동을 약 15px에서 7px로 조정하고 볼·턱 비대칭 변형과 목 윗부분 추종을 보정.
- 회전 윤곽 35개 키폼과 목 25개 키폼에서 격자 뒤집힘 없음으로 보고됨.
- VTube Studio XY 35조합 API 응답·유한 값 및 5개 표정 호출 확인.
- 설치 MOC3와 내보낸 파일의 SHA-256 일치 기록.
- 좌우 회전, 대각선 입 벌림·눈 감기 화면 확인. iPhone 실기 검증 미수행.

## 2026-10-27: 공개용 화면 캡처

실제로 연 파일:

- `BlueSailor_V2_refined_release/editable/BlueSailor_V2_refined.cmo3`
- `BlueSailor_JerseyMaid_JawTurnR1/editable/BlueSailor_JerseyMaid_JawTurnR1.cmo3`

Cubism Editor 5.3.00 FREE에서 두 모델의 외형을 사용자 제공 이미지와 대조하고, 파츠·디포머·파라미터를 표시해 총 4장을 캡처했습니다. 이 날 VTube Studio나 iPhone 동작 검사를 새로 수행한 것은 아닙니다.

## 프롬프트와 결과의 관계

공개한 프롬프트는 사용자가 실제 제작에 사용했다고 제공한 원문입니다. 최초 대상은 세일러복 상반신 모델이며, 메이드복 전신 의상과 후속 세부 수정까지 이 프롬프트 한 번으로 모두 생성됐다고 해석해서는 안 됩니다. 저장된 후속 버전과 보정 기록을 함께 소개했습니다.

원문의 “CLEAN START”, 삭제, 실행 등의 문구는 당시 제작 지시를 인용한 것입니다. 이 문서화 작업에서는 해당 지시를 재실행하지 않았습니다.
