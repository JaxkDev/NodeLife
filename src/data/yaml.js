const Base = require('./Base.js')
const fs = require('fs')
const yaml = require('yaml')

class YAML extends Base {
    get type(){
        return 'yaml';
    }
    
    get typeCode(){
        return 2;
    }

    getData(path){
        return yaml.parse(fs.readFileSync(path));
    }

    setData(path, data){
        return fs.writeFileSync(path, yaml.stringify(data));
    }
}

module.exports = YAML