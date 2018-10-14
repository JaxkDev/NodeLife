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
    return false
}

const setup = function(data){
    // load saves here
    data.firstBoot = savesExists() === false;
    data.secure = new Secure();
    if(data.firstBoot){
		data.id = Math.round(Math.random()*8998)+1000;
		data._key = data.secure.genKey(10);
    }
	data.logger = new Logger(data)
	console.log(data)
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
    getConfig() {
		console.log('hi');
    }
}

module.exports = NodeLife;