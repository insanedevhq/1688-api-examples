# 1688 API examples (Python and Node.js)

Get product data from [1688.com](https://www.1688.com), Alibaba's Chinese wholesale marketplace, without a Chinese
business account or an 1688 Open Platform app: keyword search, every SKU with its price and stock, price tiers, MOQ,
delivery promise, dropshipping data and the supplier profile.

The examples call the Apify Actor [1688 Scraper](https://apify.com/insanedev/1688-scraper) through the official
`apify-client` package.

> Disclosure: I'm insanedev, the author of that Actor. It is paid per result ($4.49 per 1,000 products, the supplier
> profile $0.99 per 1,000 more; failed or empty results are not charged). New Apify accounts get $5 of free credit
> each month, which covers about 1,000 products.

## Why not the official 1688 API?

The 1688 Open Platform (开放平台) gives its product APIs to registered developers with an approved app, and the
application expects a Chinese business identity. Resellers of "1688 item_get" APIs exist, usually with monthly plans
and per-call quotas. If you just need product, SKU and
supplier data for sourcing, price monitoring or dropshipping research, running a scraper is the quicker path.

## Quick start (Python)

```bash
cd python
pip install -r requirements.txt
export APIFY_TOKEN=your_token   # https://console.apify.com/settings/integrations
python search_products.py 保温杯
```

Output for one phone case (手机壳), from a real run in November 2026:

```
Diagonal plug-in card rhombus leather European and American suitable for iPhone18Promax light luxury Apple 17 mobile phone case card bag
  https://detail.1688.com/offer/1074015425783.html
  MOQ 1 | 1+ pcs: ¥42.8, 300+ pcs: ¥41.8, 800+ pcs: ¥39.8 | stock 127552 | 128 SKUs
  supplier: 东莞市壳时顺电子有限公司
```

`offers_to_csv.py` takes product links or offer IDs you already follow and writes one CSV row per SKU (price, stock,
weight). Schedule it daily to see price and stock changes.

## Quick start (Node.js)

```bash
cd node
npm install
APIFY_TOKEN=your_token node search-products.js 手机壳
```

## Tips

- Chinese keywords find far more than English ones (手机壳 = phone case, 收纳盒 = storage box). Set
  `translateTitles: true` to get an English `titleEn` next to the Chinese title.
- `一件代发` (dropshipping) or `48小时发货` (ships in 48 hours) in the keyword narrow the search to offers with those
  terms.
- `includeDetails: false` returns only search rows (title, price, supplier scores, repurchase rate), cheaper at
  $1.49 per 1,000, when you only want to shortlist suppliers.
- All fields are listed on the [Actor page](https://apify.com/insanedev/1688-scraper).

## License

MIT
