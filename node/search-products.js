// Search 1688.com by keyword: price tiers, MOQ, stock and supplier for each product.
//   npm install
//   APIFY_TOKEN=... node search-products.js 手机壳
import { ApifyClient } from 'apify-client';

const keyword = process.argv[2] ?? '手机壳'; // 手机壳 = phone case
const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const run = await client.actor('insanedev/1688-scraper').call({
    searchKeywords: [keyword],
    maxItemsPerKeyword: 20,
    translateTitles: true,
});
const { items } = await client.dataset(run.defaultDatasetId).listItems();

for (const item of items) {
    const tiers = (item.priceTiers ?? []).map((t) => `${t.minQuantity}+: ¥${t.price}`).join(', ');
    console.log(item.titleEn ?? item.title);
    console.log(`  ${item.url}`);
    console.log(`  MOQ ${item.minOrderQuantity} | ${tiers} | stock ${item.totalStock}`);
    console.log(`  supplier: ${item.supplierProfile?.companyName ?? item.seller?.company ?? '-'}`);
}
