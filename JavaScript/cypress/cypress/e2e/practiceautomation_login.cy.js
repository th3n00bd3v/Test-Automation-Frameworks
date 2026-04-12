describe('Practice Test Login', () => {

  beforeEach(() => {
    cy.visit('https://practicetestautomation.com/practice-test-login/');
  });

  function login() {

    cy.get('ul > :nth-child(2) > :nth-child(2)').invoke('text').then((username) => {
      cy.get('ul > :nth-child(2) > :nth-child(4)').invoke('text').then((password) => {
        cy.get('[name="username"]').type(username);
        cy.get('[name="password"]').type(password);
        cy.get('#submit').click();
      });
    });
  }

  it('Login successfully', () => {
    login();
    cy.url().should('include', '/logged-in-successfully/');
  });

  it('should show success message', () => {
    login();
    cy.get('h1').should('have.text', 'Logged In Successfully');
  });

  it('should logout successfully', () => {
    login();
    cy.get('.wp-block-button__link').click();
    cy.url().should('include', '/practice-test-login/');
  });

  it ('Invalid username', () => {
    cy.get('[name="username"]').type('invalidUser');
    cy.get('[name="password"]').type('invalidPass');
    cy.get('#submit').click();
    cy.get('#error').should('have.text', 'Your username is invalid!');
  });

  it ('Invalid password', () => {
    cy.get('[name="username"]').type('student');
    cy.get('[name="password"]').type('invalidPass');
    cy.get('#submit').click();
    cy.get('#error').should('have.text', 'Your password is invalid!');
  });

});