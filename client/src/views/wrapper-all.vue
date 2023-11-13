<template>
    <TopBar class="mb-4"/>
    <router-view class="pb-5"/>
</template>

<script>
import TopBar from "@/components/top-bar.vue";

export default {
    name: "wrapper-all",
    components: {TopBar}
}
</script>