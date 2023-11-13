<template>
    <div class="container pb-0">
        <router-view/>
    </div>
</template>

<script>

export default {
    name: 'app',
    computed: {
        user() {
            return this.$store.state.user;
        }
    },
}
</script>
<style lang="sass">
@import './assets/css/index.scss'
</style>
