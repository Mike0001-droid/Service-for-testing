import {createStore} from 'vuex';
import VuexPersist from 'vuex-persist'

const vuexPersist = new VuexPersist({
    key: 'test-system',
    storage: window.localStorage
});
const testTemplate = () => {
    return {
        test_id: null,
        subtest: [],
        select_subtest:{},
        active_subtest: 0,
        name: null,
        sdescription: null,
        answer:[]
    }
};

const store = createStore({
    state: {
        user: false,
        error:null
    },
    plugins: [vuexPersist.plugin],
    mutations: {
        ADD_TEST(state) {
            state.test = testTemplate();
        },
        ADD_TEST_ID(state, test) {
            state.test = testTemplate();
            state.test.test_id = test.test_id
        },
        UPDATE_TEST(state, test) {
            state.test = test
        },
        UPDATE_ANSWER(state, answer){
            state.test.answer.push(answer)
        },
        ERROR(state, error) {
            state.error = error;
        },
    },
    actions: {
        addTest(context) {
            context.commit('ADD_TEST');
        },
        addTestId(context, params) {
            context.commit('ADD_TEST_ID', params);
        },
        updateTest(context, params) {
            context.commit('UPDATE_TEST', params);
        },
        updateAnswer(context, params) {
            context.commit('UPDATE_ANSWER', params);
        },
        showError(context, error) {
            context.commit('ERROR', error);
        },
    }
});

export default store;


