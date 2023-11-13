<template>
    <div class="topBar">
        <div class="topBar__content p-4 align-items-center row">
            <b-button class="topBar__title col-2" @click="next(user?'profile':null)">Pro<span>Test</span>
            </b-button>
            <div :class="`topBar__nav ${showMainMenu?'topBar__nav--active':''} col-md-6 col-lg-7`"
                 @click="handlerShowMainMenu">
                <div
                    :class="`${showMainMenu?'topBar__menu--show':''} topBar__menu d-flex flex-column flex-md-row  gap-3`"
                    @click="(e)=>e.stopPropagation()">
                    <button @click="handlerShowMainMenu"
                            :class="`topBar__burger topBar__burger ${showMainMenu?'topBar__burger--active':''}`">
                        <span/>
                    </button>
                    <router-link class="topBar__link text-uppercase fw-bold d-block d-md-none" to="/profile" v-if="user">Личный кабинет</router-link>
                    <router-link
                        v-for="item in accountMenu"
                        :key="item.name"
                        class="topBar__link text-uppercase fw-bold"
                        :to="item.link"
                        :title="item.title"
                    >
                        {{ item.title }}
                    </router-link>
                    <a class="topBar__link topBar__menu--item text-uppercase fw-bold p-0 d-block d-md-none" v-if="user">Выход
                    </a>
                    <b-button class="topBar__link topBar__menu--item text-uppercase fw-bold p-0 d-flex d-md-none" v-else @click="next()">
                        вход / регистрация
                    </b-button>
                </div>
            </div>
            <div v-if="user" class="d-none d-md-flex col-md-4 col-lg-3">
                <div class="topBar__info d-flex align-items-center h5 text-primary gap-2" @click="handlerShowMenu">
                    {{ 'name@mail.ru' }}
                    <div class="topBar__user">
                        <img src="@/assets/img/icon/profile-user.svg" alt=""/>
                    </div>
                </div>
            </div>
            <b-button v-else variant="outline-primary" class="col-2 py-2 px-3 col-4  col-lg-3  d-none d-md-block"
                      @click="next()">вход / регистрация
            </b-button>
            <button @click="handlerShowMainMenu"
                    :class="`${showMainMenu?'topBar__burger topBar__burger--active':'topBar__burger'}`">
                <span/>
            </button>
        </div>
        <ul :class="showDropMenu? 'topBar__dropdown dropdown-menu show':'dropdown-menu'">
            <li class="mx-2">
                <b-button class="text-primary fw-bold">{{ 'Имя Фамилия' }}</b-button>
            </li>
            <li class="mx-2">
                <b-button class="text-primary">Личный кабинет</b-button>
            </li>
            <li class="mx-2 border-top">
                <b-button class="text-primary">Выход</b-button>
            </li>
        </ul>
    </div>
</template>

<script>
import {accountMenu} from '@/settings';

export default {
    name: "top-bar",
    data() {
        return {
            accountMenu: [],
            showDropMenu: false,
            user: null,
            showMainMenu: false
        }
    },
    created() {
        this.user = this.$store.state.user;
        if (this.user) {
            this.accountMenu = accountMenu.authorized;
        } else {
            this.accountMenu = accountMenu.notAuthorized;
        }
    },
    methods: {
        next(params) {
            this.$router.push({name: params || 'auth'});
        },
        handlerShowMenu() {
            this.showDropMenu = !this.showDropMenu;
        },
        handlerShowMainMenu() {
            this.showMainMenu = !this.showMainMenu;
        }
    }
}
</script>
