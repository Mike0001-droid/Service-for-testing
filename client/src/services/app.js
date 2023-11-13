import {app as settings} from '@/settings';
import {REST, RESTError} from './rest';

export default class extends REST {
    static get settings() {
        return settings;
    }

    static obtainToken(params) {
        return this._post(`token/create`, {}, params).then((data) => {
            return data;
        }).catch((error) => {
            throw new RESTError(error, 'Не удалось авторизоваться');
        });
    }

    static getCategory(){
        return this._get(`category`,{},{}).then((data)=>{
            return data
        }).catch((error)=>{
            throw new RESTError(error, 'Не удалось получить категории');
        })
    }

    static getTestForId(id){
        return this._get(`test/${id}`,{},{}).then((data)=>{
            return data
        }).catch((error)=>{
            throw new RESTError(error, 'Не удалось получить тест');
        })
    }
    static getSubTest(id){
        return this._get(`subtest/${id}`,{},{}).then((data)=>{
            return data
        }).catch((error)=>{
            throw new RESTError(error, 'Не удалось получить сабтест');
        })
    }
}
