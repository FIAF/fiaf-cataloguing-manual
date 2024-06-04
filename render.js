const puppeteer = require('puppeteer');
const fs = require('fs');
const path = require('path');

async function renderSVG(filepath) {
        
    const browser = await puppeteer.launch();

    const page = await browser.newPage();

    const indexPath = path.resolve(__dirname, filepath+'.html');
    // console.log(indexPath)
    await page.goto('file://' + indexPath);

    await page.waitForSelector('svg');

    const svgContent = await page.evaluate(() => {
        const svgElement = document.querySelector('svg');
        return svgElement.outerHTML;
    });

    const outPath = path.resolve(__dirname, filepath+'.svg');
    fs.writeFileSync(outPath, svgContent);

    await browser.close();

    // console.log('SVG graph saved successfully!');

}

diagrams = [
    'diagrams/0.2.1a/en',
    'diagrams/0.2.1b/en',
    'diagrams/0.2.1c/en',
    'diagrams/0.2.1d/en',
    'diagrams/1.1/en',
    'diagrams/A.2.5/en',
    'diagrams/E.5.1.1/en',
    'diagrams/E.5.1.2/en',
    'diagrams/E.5.1.3/en',
    'diagrams/E.5.2.1/en',
    'diagrams/title/en',
    'diagrams/colophon/en',
]

diagrams.forEach(d => renderSVG(d))
