import asyncio

from opendart.utils import save_json_as_file
from opendart.async_apis import fetch_all_listed_corp, fetch_total_issued_stock_by_corp_code

async def print_all_issued_stocks():
    corps = await fetch_all_listed_corp()
    result = await asyncio.gather(
        *[fetch_total_issued_stock_by_corp_code(corp['corp_code']) for corp in corps]
    )
    for i, corp in enumerate(corps):
        corp['issued_stock'] = result[i]
        if corp['issued_stock']:
            print(corp)
    return corps

save_json_as_file(asyncio.run(print_all_issued_stocks()), 'issued')


from datetime import date
int(''.join(date.today().isoformat().split('-')))
