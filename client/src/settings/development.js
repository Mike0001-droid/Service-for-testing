const ajax = {
    timeout: 75000,
    responseType: 'json',
    responseEncoding: 'utf8'
};
const serviceUrl = {
    url: '//tests.flexidev.ru',
    localPath: '//localhost',
    protocol: 'http',
    port: '8000',
    api: '/api',
    onLocal: false
}
let urlPath = `${serviceUrl.url}${serviceUrl.api}`;

const app = {
    url: `${urlPath}`,
    token: 'c7d63a2e58d186ae3760a5f7c690293e973c08c4'
};
const accountMenu = {
    authorized:[
        {
            link: '/all_tests',
            name: 'allTests',
            title: 'Все тесты'
        },
        {
            link: '/passed_tests',
            name: 'passedTests',
            title: 'Пройденные тесты'
        }
    ],
    notAuthorized:[
        {
            link: '/all_tests',
            name: 'allTests',
            title: 'Все тесты'
        }
    ]
}
export {
    ajax,
    app,
    accountMenu
}