<template>
    <template v-if="longDescription">
        <div class="row flex-sm-column flex-md-row align-items-start">
            <table class="attempts col-8 col-md-4 col-lg-3 mb-4">
                <thead>
                <tr>
                    <td>
                        Попытка
                    </td>
                    <td>
                        Дата
                    </td>
                </tr>
                </thead>
                <tbody>
                <tr v-for="(attempt,index) in attempts" :key="attempt+Date.now()">
                    <td>
                        {{ index + 1 }} Попытка
                    </td>
                    <td>
                        {{ attempt }}
                    </td>
                </tr>
                </tbody>
            </table>
            <div class="col-12 col-md-8 col-lg-9 text-secondary">
                <div class="testCard testCard-point mb-4">
                    Авторы: Арнольд Басс, Энн Дарки (1957)<br/>
                    Адаптация: А. К. Осницкий (1998); А. А. Хван и др. (2005)<br/>
                    смотрите замечания по методике<br/>
                </div>
                <div class="testCard testCard-point  mb-4">
                    Шкала тревоги Спилбергера-Ханина (State-Trait Anxiety Inventory, STAI) является информативным
                    способом
                    самооценки как уровня тревожности в данный момент (реактивная тревожность, как состояние), так и
                    личностной
                    тревожности (как устойчивая характеристика человека).
                    <br/>
                    <br/>
                    Шкала тревоги Спилбергера-Ханина (State-Trait Anxiety Inventory, STAI) является информативным
                    способом
                    самооценки как уровня тревожности в данный момент (реактивная тревожность, как состояние), так и
                    личностной
                    тревожности (как устойчивая характеристика человека).
                    <br/>
                    <br/>
                    Шкала тревоги Спилбергера-Ханина (State-Trait Anxiety Inventory, STAI) является информативным
                    способом
                    самооценки как уровня тревожности в данный момент (реактивная тревожность, как состояние), так и
                    личностной
                    тревожности (как устойчивая характеристика человека).
                    <br/>
                    <br/>
                    Шкала тревоги Спилбергера-Ханина (State-Trait Anxiety Inventory, STAI) является информативным
                    способом
                    самооценки как уровня тревожности в данный момент (реактивная тревожность, как состояние), так и
                    личностной
                    тревожности (как устойчивая характеристика человека).
                    <br/>
                    <br/>
                    Шкала тревоги Спилбергера-Ханина (State-Trait Anxiety Inventory, STAI) является информативным
                    способом
                    самооценки как уровня тревожности в данный момент (реактивная тревожность, как состояние), так и
                    личностной
                    тревожности (как устойчивая характеристика человека).
                    <br/>
                    <br/>
                    Шкала тревоги Спилбергера-Ханина (State-Trait Anxiety Inventory, STAI) является информативным
                    способом
                    самооценки как уровня тревожности в данный момент (реактивная тревожность, как состояние), так и
                    личностной
                    тревожности (как устойчивая характеристика человека).
                    <br/>
                    <br/>
                    Шкала тревоги Спилбергера-Ханина (State-Trait Anxiety Inventory, STAI) является информативным
                    способом
                    самооценки как уровня тревожности в данный момент (реактивная тревожность, как состояние), так и
                    личностной
                    тревожности (как устойчивая характеристика человека).
                </div>
                <div class="d-flex justify-content-between">
                    <b-button variant="secondary" class="text-primary fw-bold">75 вопросов</b-button>
                    <b-button variant="primary" class="px-4" @click="next('finale')">Пройти тест</b-button>
                </div>
            </div>
        </div>
    </template>
    <template v-else>
        <div class="d-flex justify-content-between align-items-center">
            <b-button variant="primary" class="px-4" @click="next('finale')">Пройти тест</b-button>
        </div>
        <div class="testCard testCard-point  mb-4">
            Авторы: Арнольд Басс, Энн Дарки (1957)<br/>
            Адаптация: А. К. Осницкий (1998); А. А. Хван и др. (2005)<br/>
            смотрите замечания по методике<br/>
        </div>
        <div class="testCard testCard-point  mb-4">
            Шкала тревоги Спилбергера-Ханина (State-Trait Anxiety Inventory, STAI) является информативным способом
            самооценки как уровня тревожности в данный момент (реактивная тревожность, как состояние), так и
            личностной
            тревожности (как устойчивая характеристика человека).
            <br/>
            <br/>
            Шкала тревоги Спилбергера-Ханина (State-Trait Anxiety Inventory, STAI) является информативным способом
            самооценки как уровня тревожности в данный момент (реактивная тревожность, как состояние), так и
            личностной
            тревожности (как устойчивая характеристика человека).
        </div>
        <div class="d-flex flex-column align-items-end w-25">
            <table class="attempts mb-4 w-100">
                <thead>
                <tr>
                    <td>
                        Попытка
                    </td>
                    <td>
                        Дата
                    </td>
                </tr>
                </thead>
                <tbody>
                <tr v-for="(attempt,index) in attempts" :key="attempt+Date.now()">
                    <td>
                        {{ index + 1 }} Попытка
                    </td>
                    <td>
                        {{ attempt }}
                    </td>
                </tr>
                </tbody>
            </table>
            <b-button variant="primary">Все результаты</b-button>
        </div>
    </template>
</template>

<script>
export default {
    name: "test-description",
    data() {
        return {
            test: null,
            attempts: ['24.07.2023', '24.07.2023', '24.07.2023', '24.07.2023', '24.07.2023'],
            longDescription: true,
        }
    },
    created() {
        this.test = this.$store.state.test;
    },
    methods: {
        next() {
            this.$router.push(this.$route.path.replace('description', 'response'));
        }
    }
}
</script>