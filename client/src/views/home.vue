<template>
    <div class="d-flex flex-column min-vh-100">
        <TopBar/>
        <div class="row  flex-md-row align-items-center justify-content-center h-75 flex-grow-1">
            <div class="col-sm-12 col-lg-7 col-xl-6">
                <h1 class="mb-4 h1 fw-bold text-primary">Выбери и пройди тестирование</h1>
                <p class="mb-5 h3 text-secondary">Авторизируйтесь на платформе,<br/> чтобы проходить
                    тесты </p>
                <div class="d-flex flex-column align-items-center col-7 col-md-5">
                    <b-button variant="primary" class="w-100 p-3 mb-3 text-uppercase" @click="next('tests')">Выбрать тест</b-button>
                    <b-button variant="secondary" class="btn  w-100 mb-3 h3 text-secondary " @click="next()">
                        Зарегистрироваться
                    </b-button>
                </div>
            </div>
            <div class="col-sm-8 col-lg-5 col-xl-6">
                <img src="@/assets/img/temp/sign_up.png" alt="">
            </div>
        </div>
    </div>
</template>

<script>

import TopBar from "@/components/top-bar.vue";

export default {
    name: "NamePage",
    components: {TopBar},
    methods: {
        next(params) {
            this.$router.push(params || 'auth');
        }
    }

}
</script>