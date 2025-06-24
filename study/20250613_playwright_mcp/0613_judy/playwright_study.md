# 웹 테스트 자동화의 혁신: Playwright MCP를 활용한 AI 기반 E2E 테스트

## 📋 발표 개요
- **목적**: 웹 기능과 성능 테스트 자동화의 완전 자동화 실현
- **핵심 아이디어**: 자연어 → AI → 테스트 코드 → 실행까지 전 과정 자동화

---

## 🚨 현재 E2E 테스트의 문제점

### 기존 방식의 한계
- **높은 진입장벽**: QA 담당자가 프로젝트 코드를 깊이 이해해야 함
- **수동 작업 의존도**: 셀렉터 파악, 테스트 시나리오 구현 등 반복적인 수작업
- **유지보수 비용**: 코드 변경 시마다 테스트 코드 수정 필요
- **시간 소모**: 매번 수동으로 테스트 시나리오를 작성하고 실행

### 해결 방안
```
자연어 시나리오 → LLM → Playwright MCP → 테스트 실행 + 스크립트 생성
```

---

## ⚙️ 환경 설정 (macOS 기준)

### 1. MCP 서버 설정
```bash
# MCP 서버 등록
code --add-mcp '{"name":"playwright","command":"npx","args":["@playwright/mcp@latest"]}'

# MCP 서버 실행
npx @playwright/mcp@latest --port 8931
```

### 2. VS Code Agent 모드 활용 예시
```
# 한국어 자연어 입력 예시
"https://www.expedia.co.kr/?locale=ko_KR"에 접속해서, 발리 호텔을 검색해줘. 
그리고 나서 검색 결과를 캡쳐해서 보여줘.

# 영어 프롬프트 예시
Generate a Playwright test for the following scenario:
- Navigate to https://debs-obrien.github.io/playwright-movies-app
- Search for 'Garfield'
- Verify the movie is in the list
```

---

## 🎯 Playwright MCP의 핵심 장점

### 자동화 테스트의 새로운 패러다임
- ✅ **자연어 기반**: 비개발자도 테스트 시나리오 작성 가능
- ✅ **코드 자동 생성**: AI가 실행 가능한 테스트 스크립트 생성
- ✅ **통합 테스트**: UI + API 테스트를 하나의 시나리오로 통합
- ✅ **성능 테스트 연동**: K6와 결합하여 기능+성능 테스트 동시 수행

---

## 🔧 Playwright 기술적 특징

### 다중 브라우저 지원
- **지원 브라우저**: Chrome, Firefox, Safari(WebKit), Microsoft Edge
- **언어 지원**: JavaScript, TypeScript, Python, Java, .NET

### 핵심 기능
- **자동 대기**: 요소 준비 상태까지 자동 대기
- **시각적 테스팅**: 스크린샷 비교를 통한 UI 회귀 테스트
- **네트워크 제어**: API 요청 가로채기 및 조작
- **모바일 에뮬레이션**: 반응형 디자인 테스트
- **병렬 실행**: 테스트 시간 대폭 단축

---

## 🎬 실제 데모: 영화 검색 테스트

### 시나리오
1. 영화 앱 페이지 접속
2. 'Garfield' 검색
3. 검색 결과 검증

### 생성된 테스트 과정
```typescript
// AI가 자동 생성한 테스트 코드 예시
test('Garfield 영화 검색 테스트', async ({ page }) => {
  await page.goto('https://debs-obrien.github.io/playwright-movies-app');
  await page.click('[data-testid="search-area"]');
  await page.fill('input[placeholder="Search for a movie"]', 'Garfield');
  await page.click('button[type="submit"]');
  await expect(page).toHaveURL(/.*search.*Garfield/);
  await expect(page.locator('text=The Garfield Movie')).toBeVisible();
});
```

---

## 🚀 실행 방법

### 기능 테스트
```bash
cd /Users/judyda/Work/playwright_test && npx playwright test garfield-search.spec.ts
```

### 성능 테스트 (K6 연동)
```bash
cd /Users/judyda/Work/playwright_test && k6 run k6-tests/garfield-search-performance.js
```

---

## 🏗️ 플랫폼화 아키텍처

### 시스템 구성요소
```
사용자 → 어드민 서버 → SQS → 테스트 러너 → S3 결과 저장
```

### 주요 컴포넌트
- **어드민 서버**: 테스트 실행 요청 및 결과 조회
- **SQS**: 테스트 실행 요청량 제어 및 큐 관리
- **테스트 러너**: 실제 테스트 코드 수행
- **S3**: 테스트 결과 및 리포트 저장

### 확장성 고려사항
- ⚠️ **컴퓨팅 리소스**: 수평 확장 가능한 구조 필요
- ⚠️ **메모리 관리**: 청크 단위 처리로 OOM 방지
- ⚠️ **결과 처리**: 대용량 테스트 결과 효율적 저장

---

## 💡 기대 효과 및 ROI

### 생산성 향상
- **시간 절약**: 테스트 작성 시간 80% 단축
- **인력 효율성**: 비개발자도 테스트 시나리오 작성 가능
- **품질 향상**: 일관된 테스트 품질 보장

### 운영 효율성
- **위기 대응**: 자동화된 회귀 테스트로 빠른 버그 발견
- **가시성**: 실시간 테스트 결과 모니터링
- **유지보수**: 하드코딩 문제 해결

---

## 🔮 향후 발전 방향

### 단기 목표
- 더 복잡한 시나리오 자동 생성
- 다양한 테스트 프레임워크 연동

### 장기 비전
- 완전 자율적 테스트 시스템
- AI 기반 테스트 최적화
- 예측적 품질 관리

---

## 📚 참고 자료
- [Microsoft Playwright MCP](https://github.com/microsoft/playwright-mcp)
- [Playwright 공식 문서](https://playwright.dev/)
- [데모 프로젝트](https://github.com/debs-obrien/generate-test-with-copilot)
- [플랫폼화 사례](https://www.youtube.com/watch?v=cGks5f2f0YE)
