"""Search 1688.com by keyword and print each product's price tiers, MOQ, stock and supplier.

    pip install -r requirements.txt
    export APIFY_TOKEN=...   # https://console.apify.com/settings/integrations
    python search_products.py 保温杯
"""

import os
import sys

from apify_client import ApifyClient

keyword = sys.argv[1] if len(sys.argv) > 1 else "保温杯"  # 保温杯 = insulated cup

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("insanedev/1688-scraper").call(
    run_input={
        "searchKeywords": [keyword],
        "maxItemsPerKeyword": 20,
        "translateTitles": True,
    }
)

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    tiers = ", ".join(f"{t['minQuantity']}+ pcs: ¥{t['price']}" for t in item.get("priceTiers") or [])
    supplier = (item.get("supplierProfile") or {}).get("companyName") or (item.get("seller") or {}).get("company")
    print(item.get("titleEn") or item.get("title"))
    print(f"  {item.get('url')}")
    print(f"  MOQ {item.get('minOrderQuantity')} | {tiers} | stock {item.get('totalStock')} | {item.get('skuCount')} SKUs")
    print(f"  supplier: {supplier}")
