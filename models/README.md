# 리깅 모델 파일

작업한 두 모델의 Cubism 편집 원본과 VTube Studio 실행 파일을 함께 올렸습니다. 각 버전의 배포 폴더에 정리해 둔 파일을 기준으로 구성했습니다.

## 세일러복 — BlueSailor V2 refined

- [Cubism 편집 파일 (.cmo3)](sailor/editable/BlueSailor_V2_refined.cmo3)
- [VTube Studio 실행 폴더](sailor/runtime/BlueSailor_V2_Expressions)
- 버전: 2026-10-06 refined 배포본, 최종 r4로 정리한 편집 원본

## 메이드복 — JerseyMaid JawTurn R1

- [Cubism 편집 파일 (.cmo3)](jersey-maid/editable/BlueSailor_JerseyMaid_JawTurnR1.cmo3)
- [VTube Studio 실행 폴더](jersey-maid/runtime/BlueSailor_JerseyMaid_Detail)
- 버전: 2026-10-11 JawTurn 배포본

메이드복 Cubism 캡처는 별도 작업 폴더의 JawTurn R1 원본을 열어 촬영했습니다. 여기에는 실행 모델과 함께 정리해 둔 release 폴더의 편집본을 올렸습니다. 파일 이름과 버전 계열은 같지만 작업 폴더의 CMO3와 바이트 단위로 동일한 파일은 아닙니다.

## 내려받아 열기

1. 저장소 상단의 **Code → Download ZIP**으로 전체 파일을 내려받고 압축을 풉니다.
2. Cubism에서 수정하려면 각 `editable` 폴더의 `.cmo3` 파일을 엽니다. 원본은 보관하고 복사본으로 작업하는 것을 권장합니다.
3. VTube Studio에서는 `runtime` 안의 모델 폴더 전체를 사용합니다. `BlueSailor_V2_Expressions` 또는 `BlueSailor_JerseyMaid_Detail` 폴더를 VTube Studio의 `Live2DModels` 폴더에 넣고 모델 목록에서 선택합니다.

실행 폴더에는 MOC3, model3 JSON, 2048 텍스처, 물리 설정, 표정 5개, 혀 모션과 VTube Studio 설정을 포함했습니다. `.moc3`만 따로 옮기면 텍스처와 설정을 찾지 못하므로 폴더 구조를 유지해 주세요. 기존에 같은 이름의 모델을 설치했다면 먼저 백업해 두세요.

표정 파일은 놀람, 웃음, 경멸, 울음, 혀 내밀기로 구성했습니다. 실행 모델의 물리는 `.physics3.json`에 저장돼 있습니다. CMO3를 다시 내보낼 때는 프로젝트 내부 설정과 실행 폴더의 물리 설정이 같은지 확인해야 합니다.

## 파일 구성과 상태

편집 원본은 Cubism 5.3.00 FREE 작업 환경에서 사용한 버전입니다. 세일러복 실행본은 당시 설치된 VTube Studio와의 호환을 위해 SDK 4.2로 출력했습니다.

이 폴더에는 CMO3와 실행 파일을 포함했으며 PSD와 중간 작업 버전은 포함하지 않았습니다. 큰 회전의 원화 경계와 최종 보정 후 iPhone 실기 검증 등 남은 내용은 [작업 기록](../docs/production-notes.md)을 참고해 주세요.

[SHA-256 파일 목록](SHA256SUMS.txt)으로 내려받은 파일을 확인할 수 있습니다.
