const Base = require('./Base.js')
const fs = require('fs')

class JSON extends Base {
    get type(){
        return 'json';
    }
    
    get typeCode(){
        return 0;
    }

    getData(path){
        return JSON.parse(fs.readFileSync(path));
    }

    setData(path, data){
        return fs.writeFileSync(path, JSON.stringify(data));
    }
}

module.exports = JSON