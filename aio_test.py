import asyncio

from opendart.async_apis.public_notice import fetch_all_listed_corp
from opendart.async_apis.business_report import fetch_total_issued_stock_by_corp_code

async def print_all_issued_stocks():
    corps = await fetch_all_listed_corp()
    result = await asyncio.gather(
        *[fetch_total_issued_stock_by_corp_code(corp['corp_code']) for corp in corps]
    )
    for i in range(len(corps)):
        if result[i]:
            print(corps[i]['corp_name'], result[i])

asyncio.run(print_all_issued_stocks())
