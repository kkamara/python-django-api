const contentContainer = document.getElementById('id-content-container');
const loginForm = document.getElementById('login-form');
const searchForm = document.getElementById('search-form');
const baseEndpoint = "http://localhost:8000/api";

if (loginForm) {
    loginForm.addEventListener('submit', handleLogin);
}
if (searchForm) {
    searchForm.addEventListener('submit', handleSearch);
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

function handleSearch(event) {
    event.preventDefault();
    let formData = new FormData(searchForm);
    let data = Object.fromEntries(formData);
    let searchParams = new URLSearchParams(data);    
    const endpoint = `${baseEndpoint}/search/?${searchParams}`;
    const headers = {
        "Content-Type": "application/json",
    }
    const authToken = localStorage.getItem("access");
    if (authToken) {
        headers.Authorization = `Bearer ${authToken}`;
    }
    const options = {
        method: "GET",
        headers: headers,
    };
    fetch(endpoint, options)
        .then(res => res.json())
        .then(data => {
            const validData = isTokenNotValid(data)
            if (validData && contentContainer) {
                contentContainer.innerHTML = ""
                if (data && data.hits) {
                    let htmlStr  = ""
                    for (let result of data.hits) {
                        htmlStr += "<li>"+ result.title + "</li>"
                    }
                    contentContainer.innerHTML = htmlStr
                    if (0 === data.hits.length) {
                        contentContainer.innerHTML = "<p>No results found</p>"
                    }
                } else {
                    contentContainer.innerHTML = "<p>No results found</p>"
                }
            }
        })
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

// getProductList();

const { liteClient: algoliasearch } = window["algoliasearch/lite"];

const appID = "ALGOLIA_APPLICATION_ID";
const apiKey = "ALGOLIA_SEARCH_API_KEY";
const indexName = "cfe_Product";

const searchClient = algoliasearch(appID, apiKey);

const search = instantsearch({
  indexName,
  searchClient,
});

search.addWidgets([
  instantsearch.widgets.searchBox({
    container: "#searchbox",
  }),

  instantsearch.widgets.clearRefinements({
    container: "#clear-refinements",
  }),

  instantsearch.widgets.refinementList({
    container: "#usernames-list",
    attribute: "username",
  }),

  instantsearch.widgets.refinementList({
    container: "#public-list",
    attribute: "public",
  }),

  instantsearch.widgets.hits({
    container: "#hits",
    templates: {
        item: `
            <div>
                <div>{{#helpers.highlight}}{ "attribute": "title" }{{/helpers.highlight}}</div>
                <div>{{#helpers.highlight}}{ "attribute": "body" }{{/helpers.highlight}}</div>
                <p>{{ username }}</p>
                <p>&#163;{{ price }}</p>
            </div>
        `,
    },
  }),
]);

search.start();
