import {createRouter, createWebHistory} from 'vue-router';
import home from '@/views/home.vue';
import auth from "@/views/auth.vue";
import profile from "@/views/profile.vue";
import AllTests from "@/views/all-tests.vue";
import PassedTests from "@/views/passed-tests.vue";
import Test from "@/views/test.vue";
import testDescription from "@/views/test-description.vue";
import testFinale from "@/views/test-finale.vue";
import testResponse from "@/views/test-response.vue";
import {helpers} from "@/utils/helpers";
import store from "@/store/store";


const routes = [
    {
        path: '/',
        name: 'home',
        component: home,
        meta: {
            title: 'Приветствие',
            requiresAuth: false,
            breadcrumb: false
        },
        props: true
    },
    {
        path: '/auth',
        name: 'auth',
        component: auth,
        meta: {
            title: 'Авторизация',
            requiresAuth: false,
            breadcrumb: false
        },
        props: true,
    },
    {
        path: '/profile',
        name: 'profile',
        component: profile,
        meta: {
            title: 'Личный кабинет',
            requiresAuth: true,
            breadcrumb: {
                label: 'Публичные счета',
                link: '1'
            }
        },
        props: true,
    },
    {
        path: '/tests',
        name: 'tests',
        component: AllTests,
        meta: {
            title: 'Все тесты',
            requiresAuth: false,
            breadcrumb() {
                return {
                    label: 'Публичные счета222',
                    link: `tests`,
                    current: false,
                    _path:'/tests'
                }
            }
        },
        props: true,
    },
    {
        path: '/passed_tests',
        name: 'passed_tests',
        component: PassedTests,
        meta: {
            title: 'Пройденные тесты',
            requiresAuth: true,
            breadcrumb: {
                label: 'Публичные счета',
                link: `passed_tests`
            }
        },
        props: true,
    },
    {
        path: '/test',
        name: 'test',
        component: Test,
        meta: {
            title: 'ProTest',
            requiresAuth: false,
            current: false,
            breadcrumb() {
                return {
                    label: 'Публичные счета321',
                    link: `test2`,
                    current: false,
                    _path:'/'
                }
            }
        },
        props: true,
        redirect: {name: 'description'},
        children: [
            {
                path: 'description',
                name: 'description',
                component: testDescription,
                meta: {
                    title: 'Описание теста', step: 1, requiresAuth: false,
                    breadcrumb() {
                        return {
                            label: 'Публичные счета3221',
                            link: `test`,
                            current: false,
                            _path:''
                        }
                    }
                },
                props: true
            },
            {
                path: 'response',
                name: 'response',
                component: testResponse,
                meta: {
                    title: 'Описание теста',
                    step: 2,
                    requiresAuth: false,
                    breadcrumb() {
                        return {
                            label: 'Публичные счета31',
                            link: `response`,
                            current: false,
                            _path:'/response'
                        }
                    }
                },
                props: true
            },
            {
                path: 'finale',
                name: 'finale',
                component: testFinale,
                meta: {
                    title: 'Описание теста',
                    step: 3,
                    requiresAuth: false,
                    breadcrumb() {
                        return {
                            label: 'Публичные счета123',
                            link: `finale`,
                            current: false,
                            _path:'/finale'
                        }
                    }
                },
                props: true
            }
        ]
    },
];

const router = createRouter({
    history: createWebHistory(),
    linkActiveClass: 'is-subactive',
    linkExactActiveClass: 'is-active',
    routes: routes
});

router.beforeEach((to, from, next) => {
    document.title = to.meta.title + ' - ProTest' || 'ProTest';
    if (to.matched.some(record => record.meta.requiresAuth)) {
        if (store.state.user && store.state.user.id) {
            let jwt = helpers.parseJwt(store.state.access);
            let expDate = new Date(jwt.exp * 1000);
            if (expDate < new Date()) {
                next({name: 'tests'});
            } else {
                next();
            }
        } else {
            next({name: 'tests'});
        }
    } else {
        next();
    }
});

export default router;
