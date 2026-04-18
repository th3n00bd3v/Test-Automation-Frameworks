const { openBrowser, goto, write, click, closeBrowser } = require('taiko');

(async () => {
    try {
        await openBrowser();
        await goto('https://duckduckgo.com');

        await write('Taiko automation');
        await click('Search');

    } catch (error) {
        console.error(error);
    } finally {
        await closeBrowser();
    }
})();