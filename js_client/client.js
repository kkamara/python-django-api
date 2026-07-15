const contentContainer = document.getElementById('id-content-container');
const loginForm = document.getElementById('login-form');
const baseEndpoint = "http://localhost:8000/api";

if (loginForm) {
    loginForm.addEventListener('submit', handleLogin);
}

function handleLogin(event) {
    event.preventDefault();
    const loginEndpoint = `${baseEndpoint}/token/`;
    let loginFormData = new FormData(loginForm);
    let loginObjectData = Object.fromEntries(loginFormData);
    const options = {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(loginObjectData),
    };
    fetch(loginEndpoint, options)
        .then(res => res.json())
        .then(authData => handleAuthData(authData, getProductList))
        .catch(err => alert(err));
}

function handleAuthData(authData, callback) {
    localStorage.setItem("access", authData.access);
    localStorage.setItem("refresh", authData.refresh);
    if (callback) {
        callback();
    }
}

function writeToContainer(data) {
    if (contentContainer) {
        contentContainer.innerHTML = "<pre>" + JSON.stringify(data, null, 4) + "</pre>";
    }
}

function getFetchOptions(method, body) {
    return {
        method: null === method ? "GET" : method,
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${localStorage.getItem("access")}`,
        },
        body: body ? body : null,
    };
}

function isTokenNotValid(jsonData) {
    if (jsonData.code && "token_not_valid" === jsonData.code) {
        alert("Please login again")
        return false
    }
    return true
}

function getProductList() {
    const endpoint = `${baseEndpoint}/products/`;
    const options = getFetchOptions();
    fetch(endpoint, options)
        .then(res => res.json())
        .then(data => {
            const validData = isTokenNotValid(data);
            if (validData) {
                writeToContainer(data);
            }
        })
        .catch(err => alert(err));
}

getProductList();
