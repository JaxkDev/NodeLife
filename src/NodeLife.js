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
const lang = require('./lang/get.js');
const Logger = require('./utils/Logger.js');
const Secure = require('./utils/Secure.js');
const checkSystem = require('./functions/checkSystem.js');

const defaultConfig = function(data){
	let dataD = fs.readFileSync('./src/resources/config.yml')
	fs.writeFileSync(data.dataPath+'\\config.yml', dataD)
	let yml = require('./data/yaml.js')
	data.config = new yml().getData('./src/resources/config.yml');
}

const loadConfig = function(data){
	let yml = require('./data/yaml.js')
	data.config = new yml().getData(data.dataPath+'\\config.yml');
}

const savesExists = function(data){
    return fs.existsSync(data.dataPath+'\\config.yml')
}

const setup = function(data){
	data.dataPath = process.env.APPDATA+'\\NodeLife';
	data.firstBoot = savesExists(data) === false;
    data.secure = new Secure();
    if(data.firstBoot){
		fs.mkdirSync(data.dataPath);
		data.id = Math.round(Math.random()*8998)+1000;
		data._key = data.secure.genKey(10);
		defaultConfig(data);
    } else {
		loadConfig(data);
	}
	data.logger = new Logger(data)
	data.messages = lang.get(data.config.lang)
	if(!checkSystem.execute(this)){
		data.logger.info(data.messages.shutdown)
		process.exit(1);
	}
	data.logger.info(data.messages.startup)
	// boot
	// console.log(data)
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
