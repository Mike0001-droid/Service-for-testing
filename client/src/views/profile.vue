<template>
    <TopBar/>
    <div class="row mt-4">
        <div :class="`user col-12 col-lg-4 col-xl-3 ${showMenu?'user__active':''}`" @click="hadlerShowMenu">
            <div class="user__toggle">
                <p class="text-white fw-bold">Меню</p>
            </div>
            <b-form :class="`tab tab__drop tab-radius-small p-4 form ${showMenu?'tab__drop--active':''}`" @click="e=>{e.stopPropagation()}">
                <button class="tab__exit" @click="hadlerShowMenu"></button>
                <div class="d-flex gap-3 align-items-center mb-4">
                    <div class="user__cover">
                        <img class="w-100" src="@/assets/img/icon/profile-user.svg" alt=""/>
                    </div>
                    <p class="d-flex flex-column h6 text-primary fw-bolder">
                        Фамилия <br/> Имя
                        <span class="h6 text-success">
                            {{ 'name@mail.ru' }}
                        </span>
                    </p>
                </div>
                <b-form-group class="mb-4" label="Мои данные">
                    <div class="form__input mb-3 d-flex align-items-center">
                        <b-form-input
                            class="form__input"
                            placeholder="Имя"
                        />
                        <button>
                            <img src="@/assets/img/icon/edit-fill.svg" alt="">
                        </button>
                    </div>
                    <div class="form__input mb-3 d-flex align-items-center">
                        <b-form-input
                            class="form__input"
                            placeholder="Фамилия"
                        />
                        <button>
                            <img src="@/assets/img/icon/edit-fill.svg" alt="">
                        </button>
                    </div>
                    <div class="form__input mb-3 d-flex align-items-center">
                        <b-form-input
                            class="form__input"
                            placeholder="Пол"
                        />
                        <button>
                            <img src="@/assets/img/icon/edit-fill.svg" alt="">
                        </button>
                    </div>
                    <div class="form__input mb-3 d-flex align-items-center">
                        <b-form-input
                            class="form__input"
                            placeholder="Дата рождения"
                        />

                        <button>
                            <img src="@/assets/img/icon/edit-fill.svg" alt="">
                        </button>
                    </div>
                    <div class="form__input mb-3 d-flex align-items-center">
                        <b-form-input
                            class="form__input"
                            placeholder="Email"
                        />
                        <button>
                            <img src="@/assets/img/icon/edit-fill.svg" alt="">
                        </button>
                    </div>
                </b-form-group>
                <b-form-group class="mb-3" label="Впишите старый пароль">
                    <b-form-input class="form__input" placeholder="****************"/>
                </b-form-group>
                <b-form-group class="mb-4" label="Придумайте новый пароль">
                    <b-form-input class="form__input" placeholder="****************"/>
                </b-form-group>
                <b-button variant="primary" class="p-2">Сохранить</b-button>
            </b-form>
        </div>
        <div class="col-12 col-lg-8 col-xl-9 d-flex flex-column">
            <HistoryPage class="mx-5 mx-md-0"/>
            <div class="d-flex flex-column flex-grow-1 gap-3 justify-content-center py-5 py-md-0">
                <test-card :isPassed="true"/>
                <test-card :isPassed="true"/>
                <test-card :isPassed="true"/>
                <test-card :isPassed="true"/>
                <test-card :isPassed="true"/>
                <test-card :isPassed="true"/>
                <test-card :isPassed="true"/>
                <test-card :isPassed="true"/>
                <div class="d-flex justify-content-end mt-3">
                    <b-button variant="primary" class="w-auto px-4" @click="next('tests')">ВСЕ ТЕСТЫ</b-button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import TopBar from "@/components/top-bar.vue";
import TestCard from "@/components/test-card.vue";
import HistoryPage from "@/components/history-page.vue";

export default {
    name: "profile",
    components: {HistoryPage, TestCard,TopBar},
    data() {
        return {
            passedTests: [1, 2, 3, 4, 5, 6, 7],
            showMenu: false,
        }
    },
    methods: {
        next(params) {
            this.$router.push(params)
        },
        hadlerShowMenu() {
            this.showMenu = !this.showMenu;
        }
    }
}
</script>