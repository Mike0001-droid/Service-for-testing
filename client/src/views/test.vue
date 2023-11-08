<template>
    <TopBar class="mb-4"/>
    <history-page class="mb-4" />
    <router-view/>
</template>

<script>
import TopBar from "@/components/top-bar.vue";
import HistoryPage from "@/components/history-page.vue";

export default {
    name: "TestPage",
    components: {HistoryPage,TopBar},
}
</script>
