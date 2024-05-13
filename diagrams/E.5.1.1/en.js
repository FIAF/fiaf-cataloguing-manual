const puppeteer = require('puppeteer');
const fs = require('fs');
const path = require('path');

(async () => {
    const browser = await puppeteer.launch();

    const page = await browser.newPage();

    const indexPath = path.resolve(__dirname, 'en.html');
    await page.goto('file://' + indexPath);

    await page.waitForSelector('svg');

    const svgContent = await page.evaluate(() => {
        const svgElement = document.querySelector('svg');
        return svgElement.outerHTML;
    });

    const outPath = path.resolve(__dirname, 'en.svg');
    fs.writeFileSync(outPath, svgContent);

    await browser.close();

    console.log('SVG graph saved successfully!');
})();
