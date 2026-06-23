import { test, expect } from '@playwright/test';

test('Garfield 영화 검색 테스트', async ({ page }) => {
  // 1. 영화 앱 페이지로 이동
  await page.goto('https://debs-obrien.github.io/playwright-movies-app');
  
  // 페이지가 완전히 로드될 때까지 대기
  await page.waitForLoadState('networkidle');
  
  // 2. 검색 입력란에 'Garfield' 입력
  await page.getByRole('textbox', { name: 'Search Input' }).fill('Garfield');
  
  // 3. 검색 버튼 클릭
  await page.getByRole('button', { name: 'Search for a movie' }).click();
  
  // 검색 결과 페이지로 이동하는지 확인
  await expect(page).toHaveURL(/.*search.*Garfield/);
  
  // 페이지 타이틀이 변경되었는지 확인
  await expect(page).toHaveTitle(/Garfield.*Search Results/);
  
  // 4. 검색 결과에서 'The Garfield Movie'가 표시되는지 확인
  await expect(page.getByRole('heading', { name: 'The Garfield Movie' })).toBeVisible();
  
  // 영화 포스터도 표시되는지 확인
  await expect(page.getByRole('img', { name: 'poster of The Garfield Movie' })).toBeVisible();
  
  // 검색 결과 목록이 표시되는지 확인
  await expect(page.getByRole('list', { name: 'movies' })).toBeVisible();
  
  // 검색어가 페이지 제목에 표시되는지 확인
  await expect(page.getByRole('heading', { name: 'Garfield' })).toBeVisible();
  await expect(page.getByRole('heading', { name: 'search results' })).toBeVisible();
});

test('Garfield 검색 결과 상세 검증', async ({ page }) => {
  // 영화 앱 페이지로 이동
  await page.goto('https://debs-obrien.github.io/playwright-movies-app');
  await page.waitForLoadState('networkidle');
  
  // 검색 수행
  await page.getByRole('textbox', { name: 'Search Input' }).fill('Garfield');
  await page.getByRole('button', { name: 'Search for a movie' }).click();
  
  // 검색 결과 페이지 확인
  await expect(page).toHaveURL(/.*search.*Garfield/);
  
  // 영화 카드 클릭 가능 여부 확인
  const movieLink = page.getByRole('link', { name: /poster of The Garfield Movie/ });
  await expect(movieLink).toBeVisible();
  
  // 영화 평점이 표시되는지 확인
  const movieCard = page.locator('[role="listitem"]').filter({ hasText: 'The Garfield Movie' });
  await expect(movieCard.locator('text=★')).toBeVisible();
  
  // 스크린샷 저장 (선택사항)
  await page.screenshot({ path: '/Users/judyda/Work/0613_Study/garfield-search-results.png' });
});
