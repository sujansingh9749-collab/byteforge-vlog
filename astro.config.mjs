// astro.config.mjs
// AdSense এর জন্য Sitemap ও SEO অপ্টিমাইজড Config

import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

// https://astro.build/config
export default defineConfig({
  // ✅ তোমার আসল domain URL এখানে দাও (AdSense approval এর জন্য জরুরি)
  site: 'https://byteforgevlog.com',

  integrations: [
    // ✅ Sitemap - Google AdSense ও SEO এর জন্য প্রয়োজনীয়
    sitemap({
      changefreq: 'weekly',
      priority: 0.7,
      lastmod: new Date(),
    }),
  ],

  // ✅ Build settings
  build: {
    // Inline stylesheets for better performance
    inlineStylesheets: 'auto',
  },

  // ✅ Markdown settings for blog posts
  markdown: {
    shikiConfig: {
      theme: 'github-dark',
      wrap: true,
    },
  },
});
