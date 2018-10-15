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

class Logger{
    constructor(data){
        this.cfg = data.getConfig();
    }

    debug(msg){
        this._logMsg(0, msg);
    }

    log(msg){
        this._logMsg(1, msg);
    }

    info(msg){
        this._logMsg(2, msg);
    }

    warn(msg){
        this._logMsg(3, msg);
    }

    error(msg){
        this._logMsg(4, msg);
    }

    critical(msg){
        this._logMsg(5, msg);
    }

    _logMsg(level, message){
        if((level == 2 || level == 0) && this.cfg.debug){
            process.stdout.write(this._format(level, message, this.cfg.colour));
        }
        if(level != 2 && level != 0){
            process.stdout.write(this._format(level, message, this.cfg.colour));
        }
    }
                                     
    _format(level, msg, colour){
        
    }
}

module.exports = Logger
