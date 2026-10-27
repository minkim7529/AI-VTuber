# 구버전 측정 자료

아래 JSON은 이전 작업 결과에서 내용 변경 없이 복사했습니다. 이번에는 파일을 읽고 입 벌림 출력의 범위를 재집계했으며, 추적 실험을 새로 실행하지 않았습니다.

- [입 매핑 변경](calibration/mouth_mapping_change.json), [보정 전](calibration/iphone_mouth_before.json), [보정 후](calibration/iphone_mouth_after.json): `BlueSailor_JerseyMaid_MouthResponse_release/evidence/` 원본. 당시 보고서에 iPhone 실기 측정으로 기록된 모델 출력입니다. 전후 샘플 수와 수행 동작이 같다고 가정하지 않습니다.
- [몸통 기하 검사](geometry/body_geometry.json): `BlueSailor_JerseyMaid_BodyMotion_release/evidence/` 원본. 변경 메시의 키폼과 삼각형 면적 비율을 기록합니다.
- [머리 물리 검사](geometry/hair_dynamics_final.json), [정지 구간 출력](geometry/idle_motion_check.json): `BlueSailor_JerseyMaid_HairBreeze_release/evidence/` 원본. 모의 입력 검사이며 iPhone 실기 검사가 아닙니다.

수치 검사는 모든 중간 프레임의 시각적 완성도를 보장하지 않습니다. 해석과 버전별 범위는 [상세 제작 과정](../docs/detailed-workflow.md)에 정리했습니다.
