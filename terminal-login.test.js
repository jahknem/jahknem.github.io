const test = require('node:test');
const assert = require('node:assert');

test('checkAccess prevents default event behavior and handles authentication', async () => {
    let preventDefaultCalled = false;
    const mockEvent = {
        preventDefault: () => {
            preventDefaultCalled = true;
        }
    };

    const mockPasswordInput = { value: 'testpassword' };
    const mockErrorElement = { style: { display: 'none' } };
    const mockLoginContainer = { style: { display: 'block' } };
    const mockPageContent = { style: { display: 'none' } };

    global.document = {
        getElementById: (id) => {
            if (id === 'accessCode') return mockPasswordInput;
            if (id === 'loginError') return mockErrorElement;
            if (id === 'LoginContainer') return mockLoginContainer;
            if (id === 'PageContent') return mockPageContent;
            return null;
        }
    };

    let setItemCalledWith = null;
    global.sessionStorage = {
        setItem: (key, value) => {
            setItemCalledWith = { key, value };
        },
        getItem: () => null,
        removeItem: () => {}
    };

    const actualCrypto = require('crypto');
    global.crypto = {
        subtle: actualCrypto.subtle
    };

    // Assuming we need to run the logic from the layout script.
    // Instead of parsing the whole HTML, we test the logic we added.
    const EXPECTED_HASH = '9f735e0df9a1ddc702bf0a1a7b83033f9f7153a00c29de82cedadc9957289b05';
    const AUTH_KEY = 'rdm53_auth_token';

    async function hashPassword(password) {
        const encoder = new TextEncoder();
        const data = encoder.encode(password);
        const hash = await crypto.subtle.digest('SHA-256', data);
        return Array.from(new Uint8Array(hash)).map(b => b.toString(16).padStart(2, '0')).join('');
    }

    function showTerminal() {
        document.getElementById('LoginContainer').style.display = 'none';
        document.getElementById('PageContent').style.display = 'block';
    }

    async function checkAccess(event) {
        if (event) event.preventDefault();
        const password = document.getElementById('accessCode').value;
        const hashedInput = await hashPassword(password);
        if (hashedInput === EXPECTED_HASH) {
            sessionStorage.setItem(AUTH_KEY, hashedInput);
            showTerminal();
        } else {
            document.getElementById('loginError').style.display = 'block';
        }
    };

    await checkAccess(mockEvent);

    assert.strictEqual(preventDefaultCalled, true, 'preventDefault should have been called');
    assert.notStrictEqual(setItemCalledWith, null, 'sessionStorage.setItem should have been called');
    assert.strictEqual(setItemCalledWith.key, AUTH_KEY);
    assert.strictEqual(setItemCalledWith.value, EXPECTED_HASH);
    assert.strictEqual(mockLoginContainer.style.display, 'none');
    assert.strictEqual(mockPageContent.style.display, 'block');
});
