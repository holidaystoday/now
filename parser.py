#-*- coding: utf-8 -*-

import asyncio
import json
from selectolax.parser import HTMLParser
from patchright.async_api import async_playwright

URL = "https://kakoysegodnyaprazdnik.ru/zavtra"

async def get_holidays() -> list[str]:
    async with async_playwright() as p:
        browser = await p.chromium.launch(channel='chrome', headless=False) 
        page = await browser.new_page()

        await page.goto(URL, wait_until="domcontentloaded")

        try:
            btn = await page.query_selector("#cont")
            if btn:
                await btn.click()
                try:
                    await page.wait_for_selector(".listing_wr", timeout=60000)
                except Exception:
                    await asyncio.sleep(1)
        except Exception:
            pass

        try:
            await page.wait_for_load_state("networkidle", timeout=60000)
        except Exception:
            pass

        html = await page.content()
        await browser.close()

    doc = HTMLParser(html)
    container = doc.css_first(".listing_wr")
    nodes = container.css("span[itemprop='text']") if container else doc.css("span[itemprop='text']")
    return [n.text(strip=True) for n in nodes if n.text(strip=True)]

if __name__ == "__main__":
    res = asyncio.run(get_holidays())
    
    data = {"holidays": res}
    
    with open("holidays.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
