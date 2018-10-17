/*
*  __    __                  __            __        __   ______           
* |  \  |  \                |  \          |  \      |  \ /      \          
* | $$\ | $$  ______    ____| $$  ______  | $$       \$$|  $$$$$$\ ______  
* | $$$\| $$ /      \  /      $$ /      \ | $$      |  \| $$_  \$$/      \ 
* | $$$$\ $$|  $$$$$$\|  $$$$$$$|  $$$$$$\| $$      | $$| $$ \   |  $$$$$$\
* | $$\$$ $$| $$  | $$| $$  | $$| $$    $$| $$      | $$| $$$$   | $$    $$
* | $$ \$$$$| $$__/ $$| $$__| $$| $$$$$$$$| $$_____ | $$| $$     | $$$$$$$$
* | $$  \$$$ \$$    $$ \$$    $$ \$$     \| $$     \| $$| $$      \$$     \
*  \$$   \$$  \$$$$$$   \$$$$$$$  \$$$$$$$ \$$$$$$$$ \$$ \$$       \$$$$$$$
*   
* @author Jackthehack21                                                                    
*
*/

const colours = require('./Colour.js');

const getTime = function() {
    var date = new Date();

    var hour = date.getHours();
    hour = (hour < 10 ? "0" : "") + hour;

    var min = date.getMinutes();
    min = (min < 10 ? "0" : "") + min;

    var sec = date.getSeconds();
    sec = (sec < 10 ? "0" : "") + sec;

    return hour + ":" + min + ":" + sec;
}

const levels = ['debug','info','warn','error','critical'];

class Logger{
    constructor(data){
        this._cfg = data.config;
    }

    debug(msg){
        this._logMsg(0, msg);
    }

    info(msg){
        this._logMsg(1, msg);
    }

    warn(msg){
        this._logMsg(2, msg);
    }

    error(msg){
        this._logMsg(3, msg);
    }

    critical(msg){
        this._logMsg(4, msg);
    }

    _logMsg(level, message){
        if(level == 0 && this._cfg.debug){
            process.stdout.write(this._applyColour(level, message)+'\n');
        }
        if(level == 0 && !this._cfg.debug){
            // this._saveLog(this._format(level, message))
        }
        if(level > 0){
            process.stdout.write(this._applyColour(level, message)+'\n');
        }
    }

    _applyColour(level, msg){
        const c = require('./Colour.js');
        switch(level){
            case 0:
                // green
                return c.green.open+msg+c.green.close;
            case 1:
                // white
                return c.bold.open+msg+c.bold.close;
            case 2:
                // yellow
                return c.yellow.open+msg+c.yellow.close;
            case 3:
                // red
                return c.red.open+msg+c.red.close;
            case 4:
                // bold red
                return c.bold.open+c.red.open+msg+c.red.close+c.bold.close;
        }
    }
                                     
    _format(level, msg){
        return this._cfg.log_format.replace('{msg}',msg).replace('{level}', levels[level]).replace('{time}', getTime());
    }
}

module.exports = Logger
