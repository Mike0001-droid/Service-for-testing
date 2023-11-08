import { logger as settings } from '@/settings';
import { REST, RESTError } from './rest';

export default class extends REST {
    static get settings() {
        return settings;
    }
    static get serviceName() {
        return 'logger';
    }
    static get level() {
        return settings.level;
    }
    static get levels() {
        return ['debug', 'info', 'warning', 'error', 'critical'];
    }
    static log(level, message) {
        if (this._levelIdx(level) !== -1) {
            return this._log(level, message);
        } else {
            throw new Error(`Неверный уровень логирования: ${level}`);
        }
    }
    static report(error) {
        return this.error(this._getReport(error.err));
    }
    static debug(message) {
        return this._log('debug', message);
    }
    static info(message) {
        return this._log('info', message);
    }
    static warning(message) {
        return this._log('warning', message);
    }
    static error(message) {
        return this._log('error', message);
    }
    static critical(message) {
        return this._log('critical', message);
    }
    static _log(level, message) {
        if (this._isEnabled(level)) {
            return this._send(level, message);
        } else {
            return Promise.resolve();
        }
    }
    static _send(level, message) {
        const data = {
            level: level,
            message: message
        };
        return this._post('log/send', {}, data).catch((error) => {
            throw new RESTError(error, `Ошибка при отправке ${level} лога`, { request: { data } });
        });
    }
    static _isEnabled(level) {
        return this._levelIdx(level) >= this._levelIdx(this.level);
    }
    static _levelIdx(level) {
        return this.levels.indexOf(level);
    }
    static _getReport(err) {
        let text = `${ err.name }: ${ err.message } at ${ err.fileName }:${ err.lineNumber }:${ err.columnNumber }`;
        if (err.request) {
            text += "\nRequest: " + JSON.stringify(err.request);
        }
        if (err.response) {
            text += "\nResponse: " + JSON.stringify(err.response);
        }
        if (err.parent) {
            text += "\n" + this._getReport(err.parent);
        }
        return text;
    }
}
