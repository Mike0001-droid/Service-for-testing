<template>
    <div>
        <ol
            v-if="$breadcrumbs.value && $breadcrumbs.value.length > 1"
            class="breadcrumb mb-0"
        >
            <li
                v-for="(item, index) in $breadcrumbs.value"
                :key="`breadcrumbs-${index}`"
                class="breadcrumb-item text-success"

            >
                <span
                    v-if="!item.current"
                >
                    {{ item.label }}
                </span>
                <span
                    v-else
                >
                {{ item.label }}
            </span>
            </li>
        </ol>
        <div class="h3 text-primary fw-bold">{{$breadcrumbs.value[this.$breadcrumbs.value.length - 1].label}}</div>
    </div>
</template>

<script>
export default {
    name: "history-page",
    props: {
        breadcrumbs: {
            type: Array,
            default() {
                return []
            }
        },
        breadcrumbsActive: {
            type: String,
            default() {
                return ''
            }
        }
    },
    data() {
    },
    watch: {
        "$route": {
            immediate: true,
            handler() {
                this.initBreadcrumbs();
            }
        },
        "$store.state.test": {
            immediate: true,
            handler() {
                this.initBreadcrumbs();
            }
        },
    },
    methods: {
        next(params) {
            this.$router.push({name: params || 'tests'});
        },
        initBreadcrumbs(){
            this.$nextTick(()=>{
                if (this.$breadcrumbs.value[this.$breadcrumbs.value.length - 1].link === 'test') {
                    this.$breadcrumbs.value[this.$breadcrumbs.value.length - 1].label = this.$store.state.test.name;
                }
            })
        }
    }
}
</script>
