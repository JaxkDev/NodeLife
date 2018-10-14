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

const fs = require('fs');
const Logger = require('./utils/Logger.js');
const Secure = require('./utils/Secure.js');

const savesExists = function(){

}

const setup = function(data){
    //load saves here
    data.firstBoot = savesExists();
    data.id = Math.round(Math.random*9999);
    data.logger = new Logger(data)
}

class NodeLife {
    constructor() {
      setup(this);
      
    }
    set name(name) {
      this._name = name.charAt(0).toUpperCase() + name.slice(1);
    }
    get name() {
      return this._name;
    }
    sayHello() {
      console.log('Hello, my name is ' + this.name + ', I have ID: ' + this.id);
    }
}

module.exports = NodeLife;