<template>
    <template v-if="isPassed">
        <div class="testCard testCard-background testCard-point testCard-small d-flex justify-content-between"
             @click="next()">
            <p class="text-secondary fw-medium">Тест Название</p>
            <p class="text-primary testCard-arrow">14 попыток </p>
        </div>
    </template>
    <template v-else>
        <div class="testCard testCard-background testCard-boxshadow pb-2" @click="next()">
            <p class="testCard-title text-light mb-2 d-flex gap-2">
            <span>
                <img src="@/assets/img/icon/info.svg" alt=""/>
            </span>
                {{ title }}
            </p>
            <ul class="d-flex flex-column">
                <li
                    class="testCard-arrow px-4 py-1 text-secondary"
                    v-for="test in tests"
                    :key="'test-'+test.id">
                    {{ test.name }}
                </li>
            </ul>
        </div>
    </template>
</template>

<script>
export default {
    name: "TestCard",
    props: {
        title: {
            type: String,
            default() {
                return ''
            }
        },
        tests: {
            type: Array,
            default() {
                return [];
            }
        },
        isPassed: {
            type: Boolean,
            default() {
                return false;
            }
        },
        id: {
            type: String
        }
    },
    methods: {
        next() {
            this.$store.dispatch('addTestId', {test_id: this.id});
            this.$router.push({name: `test`});
        }
    }
}
</script>
