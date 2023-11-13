<template>
    <TopBar class="mb-4"/>
    <router-view class="pb-5"/>
</template>

<script>
import TopBar from "@/components/top-bar.vue";

export default {
    name: "wrapper-passed",
    components: {TopBar}
}
</script>