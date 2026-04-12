## Cypress - JavaScript


### Installation and Setup
1. Open the terminal/VSCode CLI, and enter the command `npm install cypress --save-dev`. Following package managers are supported as of date:
- npm	>=10.1.0
- Yarn 1 (Classic)
- Yarn (Modern aka berry)
- pnpm	>=8.x

2. Once the installation is complete, run the command `npx cypress open` to open a GUI setup of Cypress app in the local environment.

3. Select either `E2E testing` or `Component testing` depending on the requirements (mine is `E2E`, so this step will be specific to that. Feel free to explore both, if required).

4. The configuration files will be created automatically by default (displayed on the second step after choosing the testing type).

5. Choose which browser you would like to execute the test suite on, and click Start.

6. Once the browser opens, the test spec creation screen will be visible, wherein the app will provide `Example spec scaffolding` or `New spec` options.

7. Once done, the Studio page will open, wherein the real-time actions of the test script can be seen and debugging of the script can be performed from.