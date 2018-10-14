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

const Base = require('./Base.js')
const fs = require('fs')
const ini = require('ini')

class INI extends Base {
    get type(){
        return 'ini';
    }
    
    get typeCode(){
        return 1;
    }

    getData(path){
        return ini.parse(fs.readFileSync(path));
    }

    setData(path, data){
        return fs.writeFileSync(path, ini.stringify(data));
    }
}

module.exports = INI