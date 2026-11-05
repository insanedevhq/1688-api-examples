"""Read known 1688 offers (links or IDs) and save one CSV row per SKU: price, stock, weight.

Run it daily (cron, GitHub Actions) to track price and stock changes of your suppliers.

    export APIFY_TOKEN=...
    python offers_to_csv.py 1050877556974 https://detail.1688.com/offer/944759232751.html
"""

import csv
import os
import sys

from apify_client import ApifyClient

offers = sys.argv[1:] or ["1050877556974"]

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("insanedev/1688-scraper").call(run_input={"offers": offers})

with open("skus.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["offerId", "title", "skuId", "variant", "priceCny", "stock", "weightKg"])
    for item in client.dataset(run["defaultDatasetId"]).iterate_items():
        for sku in item.get("skus") or []:
            w.writerow([
                item.get("offerId"),
                item.get("titleEn") or item.get("title"),
                sku.get("skuId"),
                sku.get("attributes"),
                sku.get("price"),
                sku.get("stock"),
                sku.get("weightKg"),
            ])
print("Saved skus.csv")
