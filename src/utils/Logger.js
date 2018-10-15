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

    var min  = date.getMinutes();
    min = (min < 10 ? "0" : "") + min;

    var sec  = date.getSeconds();
    sec = (sec < 10 ? "0" : "") + sec;

    return hour + ":" + min + ":" + sec;
}

const levels = ['debug','info','warn','error','critical'];

class Logger{
    constructor(data){
        this.cfg = data.getConfig();
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
        if(level <= 1 && this.cfg.debug){
            process.stdout.write(this._format(level, message, this.cfg.colour));
        }
        if(level > 1){
            process.stdout.write(this._format(level, message, this.cfg.colour));
        }
    }
                                     
    _format(level, msg, colour){
        let colour = ''
        switch(level){
            case 0:
                break;
            case 1:
                break;
            case 2:
                break;
            case 3:
                break;
            case 4:
                break;
        }
        return this.cfg.log_format.replace('{msg}',msg).replace('{level}', levels[level]).replace('{time}', getTime());
    }
}

module.exports = Logger
