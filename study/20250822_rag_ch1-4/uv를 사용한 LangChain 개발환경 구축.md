# uv를 사용한 LangChain 개발환경 구축

# 전제조건

- 이미 VSCode, homebrew, git, python이 설치되었다고 가정.

# uv를 사용한 LangChain 개발환경 구축

- LangChain 프로젝트를 진행하다 보면 다양한 파이썬 라이브러리가 필요합니다. 하지만 서로 다른 패키지들이 요구하는 의존성이 충돌하면서 "dependency hell"에 빠지기 쉽습니다.
- **uv**는 이런 문제를 해결해주는 차세대 파이썬 패키지 매니저로, 기존 도구들보다 압도적으로 빠른 속도와 안정적인 의존성 관리를 제공합니다.

## Poetry vs uv: 어떤 도구를 선택할까?

| 특징 | Poetry | uv |
| --- | --- | --- |
| **설치 속도** | 표준 | 10-100배 빠름 (병렬 처리) |
| **메모리 사용량** | 높음 | 낮음 (효율적 캐싱) |
| **명령어 친숙도** | 고유 명령어 체계 | pip과 유사한 구조 |
| **생태계 호환성** | 제한적 (자체 lock 형식) | 완벽 (pip, requirements.txt 지원) |
| **프로젝트 관리** | 통합 기능 풍부 | 패키지 관리 특화 |
| **개발 언어** | Python | Rust |

**선택 가이드:**

- 빠른 설치와 기존 프로젝트 호환성을 원한다면 → **uv**
- 프로젝트 스캐폴딩, 배포 등 통합 관리를 원한다면 → **Poetry**

## 01 uv 설치하기

터미널에서 uv를 설치합니다:

```bash
pip3 install uv
```

## 02 프로젝트 디렉토리로 이동

작업할 LangChain 프로젝트 폴더로 이동합니다:

```bash
cd ~/Documents/langchain-kr
```

## 03 격리된 개발환경 생성

uv를 사용해 독립적인 파이썬 환경을 만들고 진입합니다:

```bash
# Python 3.11 기반의 가상환경 생성
uv venv --python 3.11

# 생성된 환경 활성화 (macOS/Linux)
source .venv/bin/activate
```

## 04 가상환경 활성화 확인

성공적으로 가상환경이 활성화되면 터미널 프롬프트가 변경됩니다:

```
(langchain-kr) username@MacBook-Air langchain-kr %
```

이제 시스템의 다른 파이썬 프로젝트와 완전히 분리된 깨끗한 작업공간이 준비되었습니다.

## 05 필요한 라이브러리 일괄 설치

프로젝트에 필요한 모든 패키지를 한 번에 설치합니다:

```bash
uv pip install -r requirements.txt
```

## 06 설치 검증

설치가 완료되면 현재 환경에 설치된 패키지들을 확인해보세요:

```bash
pip list
```