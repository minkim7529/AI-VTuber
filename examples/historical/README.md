# 과거 제작 코드 예제

이 폴더는 당시 작업 폴더 `work/`의 코드 세 개를 내용 변경 없이 보관한 자료입니다. 전체 모델을 재생성하는 독립 실행 도구가 아니며, 이번 공개 과정에서는 실행하지 않고 코드를 읽어 작업 방식을 확인했습니다.

- [write_layered_psd.py](write_layered_psd.py): v006 파츠로 PSD 초안을 저장하고 레이어 위치·알파·픽셀을 다시 읽어 검사합니다. 코드에 명시된 결과물은 그림 품질 검수 실패 초안입니다.
- [build_body_motion.py](build_body_motion.py): FaceMotion을 바탕으로 몸통과 의상 키폼을 변경하고 변경하지 않은 메시와 삼각형 방향을 검사합니다.
- [build_tongue_align.py](build_tongue_align.py): BodyMotion을 바탕으로 혀 위치와 입 벌림 연결을 수정하고 다른 메시의 키폼 보존을 확인합니다.

원본 코드는 프로젝트 루트를 현재 디렉터리로 가정합니다. `work/face_motion_helpers.py`, 로컬 Python 의존성, `outputs/` 아래 이전 버전·파츠·원화 등이 필요하며 이 폴더에 모두 포함하지 않았습니다. 코드에는 파일을 생성하거나 복사하는 동작이 있습니다. 의존성과 경로를 갖추지 않은 채 실행하는 용도로 제공하지 않습니다.

작업 설명은 [상세 제작 과정](../../docs/detailed-workflow.md)에 정리했습니다.
