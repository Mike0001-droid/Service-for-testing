<template>
    <div class="auth d-flex justify-content-center align-items-center">
        <div class="tab tab__restrictions h-75">
            <b-card no-body>
                <b-tabs card>
                    <b-tab title="Вход" active class="w-75">
                        <b-form @submit="onSubmit" class="mt-4">
                            <div class="form__input mb-4 d-flex align-items-center">
                                <b-form-input class="form__input" v-model="user.email"
                                              placeholder="turkish.sweetshop@gmail.com"/>
                                <div>
                                    <img src="@/assets/img/icon/user.svg" alt="">
                                </div>
                            </div>
                            <div class="form__input mb-2 d-flex align-items-center">
                                <b-form-input class="form__input" v-model="user.password" placeholder="password"/>
                                <div>
                                    <img src="@/assets/img/icon/password.svg" alt="">
                                </div>
                            </div>
                            <b-form-checkbox v-model="user.isRemember">Запомнить меня</b-form-checkbox>
                            <b-button
                                type="submit"
                                variant="primary"
                                class="btn btn-fill w-100 p-2 mt-4 mb-2"
                            >
                                войти
                            </b-button>
                            <b-button variant="secondary" class="border-bottom w-100 p-2 mb-3">Забыли пароль?</b-button>
                            <b-button
                                variant="outline-primary"
                                class="btn btn-fill w-100 p-2 mb-3"
                                @click="next('all_tests')"
                            >
                                Войти без регистрации
                            </b-button>
                        </b-form>
                    </b-tab>
                    <b-tab title="Регистрация" class="w-75">
                        <b-form
                            @submit="onSubmit"
                        >
                            <b-form-input v-model="user.name" class="form__input mb-4" placeholder="Имя"/>
                            <b-form-input v-model="user.surname" class="form__input mb-4" placeholder="Фамилия"/>
                            <b-form-input v-model="user.gender" class="form__input mb-4" placeholder="Пол"/>
                            <b-form-input v-model="user.birthday" class="form__input mb-4" placeholder="Дата рождения"/>
                            <b-form-input v-model="user.email" class="form__input mb-4" placeholder="Email"/>
                            <div class="form__input mb-4 d-flex align-items-center">
                                <b-form-input class="form__input" v-model="user.password" placeholder="password"/>
                                <div>
                                    <img src="@/assets/img/icon/password.svg" alt="">
                                </div>
                            </div>
                            <b-button
                                type="submit"
                                class="w-100 p-2 mb-4"
                                variant="primary"
                            >Регистрация
                            </b-button>
                            <p class="h6 text-md-center text-secondary">Регистрируясь, вы соглашаетесь с
                                <span class="text-primary">пользовательским соглашением</span>
                                и даете
                                согласие на обработку <span class="text-primary">персональных данных</span>
                            </p>
                        </b-form>
                    </b-tab>
                </b-tabs>
            </b-card>
        </div>
    </div>
</template>

<script>
export default {
    name: "auth-page",
    data() {
        return {
            selectType: "",
            user: {
                name: '',
                surname: '',
                gender: '',
                birthday: '',
                email: '',
                password: '',
                isRemember: false
            }
        }
    },
    created() {
        this.selectType = this.$route.params.type;
    },
    methods: {
        onSubmit() {
            this.next();
        },
        next(params){
            this.$router.push({name:params||'profile'});
        }
    }
}
</script>
