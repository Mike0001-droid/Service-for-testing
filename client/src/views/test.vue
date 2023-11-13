<template>
    <b-overlay
        :show="showLoaderTest"
        rounded
        spinner-big
        spinner-variant="primary"
    >
        <HistoryPage class="mb-4"/>
        <router-view/>
    </b-overlay>
</template>

<script>

import HistoryPage from "@/components/history-page.vue";
import app from "@/services/app";

export default {
    name: "test",
    components: {HistoryPage},
    data() {
        return {
            test: null,
            showLoaderTest: true,
        }
    },
    created() {
        this.test = this.$store.state.test;
        this.getTest();
    },
    methods:{
        getTest() {
            this.showLoaderTest = true;
            app.getTestForId(this.test.test_id).then(data => {
                this.$store.dispatch('updateTest', {...this.test, ...data});
                this.test = this.$store.state.test;
                this.showLoaderTest = false;
            }).catch(err => {
                this.$store.dispatch('showError', err);
                this.showLoaderTest = false;
            });
        },
    }
}
</script>
