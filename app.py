import asyncio
from typing import List
from pyppeteer import launch

async def get_article_titles(keywords: List[str]):
   # launch browser in headless mode
   browser = await launch({"headless": False, "args": ["--start-maximized"]},executablePath='/usr/bin/google-chrome')
   # create a new page
   page = await browser.newPage()
   # set page viewport to the largest size
   await page.setViewport({"width": 1600, "height": 900})
   # navigate to the page
   await page.goto("https://www.educative.io/edpresso")
   # locate the search box
   entry_box = await page.querySelector(
       "#__next > div.ed-grid > div.ed-grid-main > div > div.flex.flex-row.items-center.justify-around.bg-gray-50.dark\:bg-dark.lg\:py-0.lg\:px-6.lg\:top-24.lg\:sticky > div > div.w-full.p-0.m-0.flex.flex-col.lg\:w-1\/2.lg\:py-0.lg\:px-4.mx-2 > div.pt-6.px-4.pb-0.lg\:sticky.lg\:p-0.top-32.lg\:top-24 > div > div > div.w-full.dark\:bg-dark.h-12.flex-auto.text-sm.font-normal.rounded-sm.cursor-text.inline-flex.items-center.hover\:bg-alphas-black06.dark\:hover\:bg-gray-A900.border.border-solid.overflow-hidden.focus-within\:ring-1.border-gray-400.dark\:border-gray-900.focus-within\:border-primary.dark\:focus-within\:border-primary-light.focus-within\:ring-primary.dark\:focus-within\:ring-primary-light > input"
   )

   for keyword in keywords:
       print("====================== {} ======================".format(keyword))
       # type keyword in search box
       await entry_box.type(keyword)
       # wait for search results to load
       await page.waitFor(4000)
       # extract the article titles
       topics = await page.querySelectorAll("h2")
       for topic in topics:
           title = await topic.getProperty("textContent")
           # print the article titles
           print(await title.jsonValue())

       # clear the input box
       for _ in range(len(keyword)):
           await page.keyboard.press("Backspace")

print("Starting...")
asyncio.get_event_loop().run_until_complete(
   get_article_titles(["python", "opensource", "opencv"])
)
print("Finished extracting articles titles")
