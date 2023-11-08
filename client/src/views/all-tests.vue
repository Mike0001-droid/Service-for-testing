<template>
    <top-bar class="mb-4"/>
    <HistoryPage class="mb-4" :breadcrumbs="breadcrumb.breadcrumbs" :breadcrumbs-active="breadcrumb.active"/>
    <div class="testCard testCard-point text-secondary mb-4">
        Быстрая навигация по популярным тестам и тематикам. Всего на сайте более тысячи тестов, найти нужный можно
        при помощи подробного <span class="text-primary">тематического указателя</span>, по каталогу
        <span class="text-primary">авторов</span>, или <span
        class="text-primary">поиском</span> по названию. Можно посмотреть <span
        class="text-primary">полный список</span>.
    </div>
    <div class="d-flex gap-3 mb-3 flex-wrap">
        <b-button
            v-for="testFilter in testFilters"
            :key="testFilter.type"
            :variant="currentFilter.type===testFilter.type?'primary':'outline-primary'"
            @click="changeCurrentType(testFilter.type)"
            class="px-5"
        >
            {{ testFilter.name }}
        </b-button>
    </div>
    <div class="mb-3 text-success">
        Сортировать по:
        <b-button
            v-for="testFilterAds in testFiltersAds"
            :key="testFilterAds.type"
            :variant="currentFilter.sorted===testFilterAds.type?'secondary active':'secondary'"
            @click="changeCurrentSorted(testFilterAds.type)"
            class="p-0 mx-1"
        >
            {{ testFilterAds.name }}
        </b-button>

    </div>
    <div class="mb-5 d-flex align-items-center form__inside px-2 col-6 col-md-4 col-lg-3">
        <b-form-input
            class="form__input"
            placeholder="Поиск"
            v-model="currentFilter.searchValue"
        />
        <b-button pill variant="light">
            <img src="@/assets/img/icon/search.svg" alt="">
        </b-button>
    </div>
    <b-overlay
        :show="showLoaderTests"
        class="row gx-2"
        rounded
        spinner-big
        spinner-variant="primary"
    >
        <TestCard
            v-for="testCategory in filteredTestsCategory"
            :title="testCategory.name"
            :id="testCategory.id"
            :key="'TestCard'+testCategory.id"
            :isPassed="false"
            :tests="testCategory.test"
            class="col-sm-6 col-md-4 col-lg-3"
        />
    </b-overlay>
</template>

<script>
import {app} from "@/services";
import TopBar from "@/components/top-bar.vue";
import HistoryPage from "@/components/history-page.vue";
import TestCard from "@/components/test-card.vue";

export default {
    name: "AllTest",
    components: {TestCard, HistoryPage, TopBar},
    data() {
        return {
            testFilters: [
                {
                    name: 'Тесты',
                    type: 'test'
                },
                {
                    name: 'Темы',
                    type: 'topics'
                },
                {
                    name: 'Авторы',
                    type: 'authors'
                }
            ],
            testFiltersAds: [
                {
                    name: 'Сложности',
                    type: 'difficulties'
                },
                {
                    name: 'Популярности',
                    type: 'popularity'
                }
            ],
            currentFilter: {type: 'test', sorted: 'difficulties', searchValue: ''},
            testsCategory: [],
            showLoaderTests: true,
            breadcrumb:{
                breadcrumbs:[],
                active:'Все тесты'
            }
        }
    },
    created() {
        this.showLoaderTests = true;
        app.getCategory().then((res) => {
            this.testsCategory = res;
            this.showLoaderTests = false;
        }).catch((error) => {
            this.$store.dispatch('showError', error);
            this.showLoaderTests = false;
        })
    },
    computed: {
        filteredTestsCategory() {
            return this.testsCategory.filter(item => item.test.some(test => test.name.toLowerCase().includes(this.currentFilter.searchValue.toLowerCase())))
        }
    },
    methods: {
        changeCurrentType(type) {
            this.currentFilter = {...this.currentFilter, type};
        },
        changeCurrentSorted(sorted) {
            this.currentFilter = {...this.currentFilter, sorted};
        }
    }
}
</script>
