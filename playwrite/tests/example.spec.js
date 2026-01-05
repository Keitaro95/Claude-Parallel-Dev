import { test, expect } from '@playwright/test';

test('homepage has title', async ({ page }) => {
  await page.goto('/');
  await expect(page.locator('h1')).toContainText('Cosmo Frontend');
});

test('backend health check', async ({ page }) => {
  await page.goto('/');
  await expect(page.locator('p')).toContainText('Backend status:');
});
