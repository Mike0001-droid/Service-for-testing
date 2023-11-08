<template>
    <TopBar class="mb-4"/>
    <HistoryPage class="mb-4"/>
    <div class="d-flex flex-column flex-grow-1 gap-3 justify-content-center">
        <test-card :isPassed="true"/>
    </div>
</template>

<script>
import TopBar from "@/components/top-bar.vue";
import HistoryPage from "@/components/history-page.vue";
import TestCard from "@/components/test-card.vue";

export default {
    name: "PassedTests",
    components: {TestCard, HistoryPage, TopBar},
    data() {
        return {
            passedTests: [1, 2, 3, 4, 5, 6, 7]
        }
    },
    methods: {
        next(params) {
            this.$router.push(params)
        }
    }

}
</script>
