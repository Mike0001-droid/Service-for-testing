import {createRouter, createWebHistory} from 'vue-router';
import home from '@/views/home.vue';
import auth from "@/views/auth.vue";
import profile from "@/views/profile.vue";

import WrapperAll from "@/views/wrapper-all.vue";
import WrapperPassed from "@/views/wrapper-passed.vue";
import AllTests from "@/views/tests-all.vue";
import PassedTests from "@/views/tests-passed.vue";

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
            }
        },
        props: true,
    },
    {
        path: '/all_tests',
        name: 'all_tests',
        component: WrapperAll,
        redirect: {name: 'allTests'},
        meta: {
            title: 'Все тесты',
            requiresAuth: false,
            breadcrumb: false
        },
        props: true,
        children: [
            {
                path: '',
                name: 'allTests',
                component: AllTests,
                meta: {
                    title: 'ProTest',
                    requiresAuth: false,
                    current: false,
                    breadcrumb() {
                        return {
                            label: 'Все тесты',
                            link: `tests`,
                            current: false,
                        }
                    }
                },
                props: true,
            },
            {
                path: '',
                name: 'AllTest',
                component: Test,
                meta: {
                    title: 'ProTest',
                    requiresAuth: false,
                    current: false,
                    breadcrumb: false
                },
                props: true,
                redirect: {name: 'allDescription'},
                children: [
                    {
                        path: 'description',
                        name: 'allDescription',
                        component: testDescription,
                        meta: {
                            title: 'Описание', step: 1, requiresAuth: false,
                            breadcrumb() {
                                return {
                                    label: 'Тест',
                                    link: `test`,
                                    current: false,
                                    _path: ''
                                }
                            }
                        },
                        props: true
                    },
                    {
                        path: 'response',
                        name: 'allResponse',
                        component: testResponse,
                        meta: {
                            title: 'Тест',
                            step: 2,
                            requiresAuth: false,
                            breadcrumb() {
                                return {
                                    label: 'Тест',
                                    link: `test`,
                                    current: false,
                                }
                            }
                        },
                        props: true
                    },
                    {
                        path: 'finale',
                        name: 'allFinale',
                        component: testFinale,
                        meta: {
                            title: 'Описание теста',
                            step: 3,
                            requiresAuth: false,
                            breadcrumb() {
                                return {
                                    label: 'тест заключение',
                                    link: `test`,
                                    current: false,
                                    _path: '/finale'
                                }
                            }
                        },
                        props: true
                    }
                ]
            }
        ]
    },
    {
        path: '/passed_tests',
        name: 'passed_tests',
        component: WrapperPassed,
        redirect: {name: 'PassedTests'},
        meta: {
            title: 'Пройденные тесты',
            requiresAuth: true,
            breadcrumb: false
        },
        props: true,
        children: [
            {
                path: '',
                name: 'PassedTests',
                component: PassedTests,
                meta: {
                    title: 'ProTest',
                    requiresAuth: false,
                    current: false,
                    breadcrumb() {
                        return {
                            label: 'Пройденные тесты',
                            link: `tests`,
                            current: false,
                        }
                    }
                },
                props: true,
            },
            {
                path: '',
                name: 'PassedTest',
                component: Test,
                meta: {
                    title: 'ProTest',
                    requiresAuth: false,
                    current: false,
                    breadcrumb: false
                },
                props: true,
                redirect: {name: 'passedDescription'},
                children: [
                    {
                        path: 'description',
                        name: 'passedDescription',
                        component: testDescription,
                        meta: {
                            title: 'Описание', step: 1, requiresAuth: false,
                            breadcrumb() {
                                return {
                                    label: 'Тест',
                                    link: `test`,
                                    current: false,
                                    _path: ''
                                }
                            }
                        },
                        props: true
                    },
                    {
                        path: 'response',
                        name: 'passedResponse',
                        component: testResponse,
                        meta: {
                            title: 'Тест',
                            step: 2,
                            requiresAuth: false,
                            breadcrumb() {
                                return {
                                    label: 'Тест',
                                    link: `test`,
                                    current: false,
                                }
                            }
                        },
                        props: true
                    },
                    {
                        path: 'finale',
                        name: 'passedFinale',
                        component: testFinale,
                        meta: {
                            title: 'Описание теста',
                            step: 3,
                            requiresAuth: false,
                            breadcrumb() {
                                return {
                                    label: 'тест заключение',
                                    link: `test`,
                                    current: false,
                                    _path: '/finale'
                                }
                            }
                        },
                        props: true
                    }
                ]
            }
        ]
    }
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
            next({name: 'auth'});
        }
    } else {
        next();
    }
});

export default router;
