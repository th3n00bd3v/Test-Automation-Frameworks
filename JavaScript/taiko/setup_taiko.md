## Taiko - JavaScript

Taiko is a lightweight Nodejs library with a simple API to automate browsers.

### Steps

1. In the CLI, enter the command `npm init -y` once inside of the project folder.

2. Once the command is initialized, install taiko using the command `npm install taiko`. Use the `-g` flag to install globally, if needed.

3. Once installed, there are two ways to run taiko:

a. REPL (Interactive mode): Typing `taiko` in the CLI will run it in the shell itself. You can keep typing the commands like a set of instructions:

![Alt text](assets/repl_taiko.gif)


b. Scripts can be run via the command `npx taiko {script name}.js` on saving inside the project folder.

### Advantages
- Works with the JavaScript and the Node.js eco-system.
- No installation/management of drivers required.
- Easy to use API with implicit waits.
- End to end or user journey testing of web application.
- CLI recorder for scripting tests
- Headless mode by default.
- Managed docker instances.
- Faster test runs.

### Disadvantages

- No browser/mobile testing support, only supports native Chromium browser for now.
- Only supports JavaScript.
- Test distribution not in scope (AFAIK).
- No GUI-based recorder available.
- No test organization, only simple tests.